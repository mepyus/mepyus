from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List


REPO_ROOT = Path(__file__).resolve().parent.parent
HANDOFF_PATH = REPO_ROOT / "runtime" / "manifests" / "vectorfl_paper_codex_handoff_latest_v0.json"
RETURN_PATH = REPO_ROOT / "runtime" / "manifests" / "vectorfl_paper_codex_return_latest_v0.json"
BRIDGE_TIMEOUT_SECONDS = 45


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _load_handoff() -> Dict[str, Any]:
    if not HANDOFF_PATH.exists():
        raise FileNotFoundError(f"latest handoff not found: {HANDOFF_PATH}")
    payload = json.loads(HANDOFF_PATH.read_text(encoding="utf-8"))
    required = [
        "task",
        "goal",
        "selected_context_summary",
        "relevant_files",
        "constraints",
        "requested_action",
        "expected_output",
        "forbidden_scope",
    ]
    missing = [key for key in required if key not in payload]
    if missing:
        raise ValueError(f"latest handoff malformed; missing keys: {', '.join(missing)}")
    return payload


def _output_schema() -> Dict[str, Any]:
    return {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "summary": {"type": "string"},
            "changed_files": {
                "type": "array",
                "items": {"type": "string"},
            },
            "blockers": {
                "type": "array",
                "items": {"type": "string"},
            },
            "next_recommendation": {"type": "string"},
            "needs_supervisor_decision": {"type": "boolean"},
        },
        "required": [
            "summary",
            "changed_files",
            "blockers",
            "next_recommendation",
            "needs_supervisor_decision",
        ],
    }


def _build_prompt(handoff: Dict[str, Any]) -> str:
    return f"""You are Codex running in a read-only bridge adapter for VectorFL Paper.

Use the handoff below as the only required task context. Do not change any files. Do not broaden scope. Return only structured output matching the provided JSON schema.

Task:
{handoff["task"]}

Goal:
{handoff["goal"]}

Selected context summary:
{json.dumps(handoff["selected_context_summary"], ensure_ascii=False, indent=2)}

Relevant files:
{json.dumps(handoff["relevant_files"], ensure_ascii=False, indent=2)}

Codex top files:
{json.dumps(handoff.get("codex_top_files", handoff["relevant_files"]), ensure_ascii=False, indent=2)}

External record anchor:
{json.dumps(handoff.get("external_record_anchor", {}), ensure_ascii=False, indent=2)}

Constraints:
{json.dumps(handoff["constraints"], ensure_ascii=False, indent=2)}

Requested action:
{handoff["requested_action"]}

Expected output:
{json.dumps(handoff["expected_output"], ensure_ascii=False, indent=2)}

Forbidden scope:
{json.dumps(handoff["forbidden_scope"], ensure_ascii=False, indent=2)}

Your job:
1. Read the handoff as the actual latest worker input from VectorFL Paper.
2. Produce a concise work result for the current requested action.
3. If no file changes are appropriate in read-only mode, return an empty changed_files list and explain the blocker or next recommendation clearly.
4. Keep the answer compact and supervisor-readable.
"""


def _write_return(payload: Dict[str, Any]) -> None:
    RETURN_PATH.parent.mkdir(parents=True, exist_ok=True)
    RETURN_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _failure_return(*, message: str, exit_code: int, raw_command: List[str]) -> Dict[str, Any]:
    return {
        "schema_version": "vectorfl_paper_codex_return_latest_v0",
        "source_handoff_artifact": str(HANDOFF_PATH.relative_to(REPO_ROOT)),
        "worker": "codex",
        "status": "failed",
        "summary": "Codex bridge execution failed before a usable worker result could be reflected.",
        "changed_files": [],
        "blockers": [message],
        "next_recommendation": "Inspect the bridge command and Codex CLI environment, then rerun the same latest handoff path.",
        "needs_supervisor_decision": True,
        "returned_at": _now_iso(),
        "raw_command": raw_command,
        "execution_mode": "codex_exec_read_only",
        "exit_code": exit_code,
    }


def main() -> None:
    print(f"[vectorfl-paper-codex-bridge] reading handoff: {HANDOFF_PATH.relative_to(REPO_ROOT)}")
    try:
        handoff = _load_handoff()
    except Exception as error:
        print(f"[vectorfl-paper-codex-bridge] error: {error}", file=sys.stderr)
        raise

    prompt = _build_prompt(handoff)

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_root = Path(temp_dir)
        schema_path = temp_root / "codex_bridge_output_schema.json"
        output_path = temp_root / "codex_bridge_last_message.json"
        schema_path.write_text(json.dumps(_output_schema(), ensure_ascii=False, indent=2), encoding="utf-8")

        command = [
            "codex",
            "exec",
            "--skip-git-repo-check",
            "--sandbox",
            "read-only",
            "--cd",
            str(REPO_ROOT),
            "--output-schema",
            str(schema_path),
            "--output-last-message",
            str(output_path),
            "-",
        ]
        print(f"[vectorfl-paper-codex-bridge] running codex command: {' '.join(command)}")

        try:
            completed = subprocess.run(
                command,
                input=prompt,
                text=True,
                capture_output=True,
                cwd=str(REPO_ROOT),
                timeout=BRIDGE_TIMEOUT_SECONDS,
            )
        except subprocess.TimeoutExpired:
            failure = _failure_return(
                message=f"codex exec timed out after {BRIDGE_TIMEOUT_SECONDS} seconds",
                exit_code=124,
                raw_command=command,
            )
            _write_return(failure)
            print(f"[vectorfl-paper-codex-bridge] wrote failed return: {RETURN_PATH.relative_to(REPO_ROOT)}")
            raise SystemExit(124)

        if completed.stdout.strip():
            print(completed.stdout.strip())
        if completed.stderr.strip():
            print(completed.stderr.strip(), file=sys.stderr)

        if completed.returncode != 0:
            failure = _failure_return(
                message=f"codex exec failed with exit_code={completed.returncode}",
                exit_code=completed.returncode,
                raw_command=command,
            )
            _write_return(failure)
            print(f"[vectorfl-paper-codex-bridge] wrote failed return: {RETURN_PATH.relative_to(REPO_ROOT)}")
            raise SystemExit(completed.returncode)

        if not output_path.exists():
            failure = _failure_return(
                message="codex exec completed without writing output-last-message",
                exit_code=completed.returncode,
                raw_command=command,
            )
            _write_return(failure)
            print(f"[vectorfl-paper-codex-bridge] wrote failed return: {RETURN_PATH.relative_to(REPO_ROOT)}")
            raise SystemExit(1)

        result = json.loads(output_path.read_text(encoding="utf-8"))
        latest_return = {
            "schema_version": "vectorfl_paper_codex_return_latest_v0",
            "source_handoff_artifact": str(HANDOFF_PATH.relative_to(REPO_ROOT)),
            "worker": "codex",
            "status": "completed",
            "summary": result["summary"],
            "changed_files": list(result.get("changed_files", [])),
            "blockers": list(result.get("blockers", [])),
            "next_recommendation": result["next_recommendation"],
            "needs_supervisor_decision": bool(result["needs_supervisor_decision"]),
            "returned_at": _now_iso(),
            "raw_command": command,
            "execution_mode": "codex_exec_read_only",
            "exit_code": completed.returncode,
        }
        _write_return(latest_return)
        print(f"[vectorfl-paper-codex-bridge] wrote latest return: {RETURN_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
