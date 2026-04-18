from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.registry.atomic_io import atomic_write_json, atomic_write_text, make_idempotency_key


RUNTIME_ROOT = REPO_ROOT / "runtime"
RECEIPTS_ROOT = RUNTIME_ROOT / "receipts"
VIEWS_ROOT = RUNTIME_ROOT / "views"
RECONSTRUCTION_ROOT = VIEWS_ROOT / "reconstruction_supervisor"
EXPLORATION_ROOT = RUNTIME_ROOT / "observer" / "exploration" / "json"
MULTI_LENS_ROOT = VIEWS_ROOT / "multi_lens_document_reading"
ENGINE_STATE_LATEST_ROOT = VIEWS_ROOT / "engine_state_latest"
ENGINE_STATE_EVENT_ROOT = VIEWS_ROOT / "engine_state_update_events"

SECTION_RE = re.compile(r"^##\s+(.+?)\s*$")
BULLET_RE = re.compile(r"^- ([^:]+): `?(.*?)`?$")
PATH_BULLET_RE = re.compile(r"^- `(.+?)`$")
TOKEN_RE = re.compile(r"[a-z0-9]+")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a bounded reconstruction supervisor surface.")
    parser.add_argument("--scope-ref", help="Bounded scope ref such as a source doc path or asset id")
    parser.add_argument("--receipt", help="Relative path to a receipt markdown file")
    parser.add_argument("--operation-board", help="Relative path to an operation board markdown file")
    parser.add_argument("--supervisor-view", help="Relative path to a supervisor-facing runtime view json")
    parser.add_argument("--sidecar", help="Relative path to an exploration sidecar json")
    parser.add_argument("--engine-state", help="Relative path to an engine state latest json")
    parser.add_argument("--engine-event", help="Relative path to an engine state update event json")
    parser.add_argument("--reconstruction-id", help="Explicit reconstruction id")
    parser.add_argument("--actor", default="codex")
    return parser.parse_args()


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def as_repo_rel(path: Path) -> str:
    return str(path.resolve().relative_to(REPO_ROOT))


def resolve_rel_path(value: Optional[str]) -> Optional[Path]:
    if not value:
        return None
    path = Path(value)
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    return path


def slugify(value: str) -> str:
    cleaned = re.sub(r"[^a-z0-9_-]+", "_", value.strip().lower())
    return cleaned.strip("_") or "surface"


def tokenize(value: str) -> List[str]:
    return TOKEN_RE.findall(value.lower())


def parse_operation_board(board_path: Path) -> Dict[str, str]:
    data: Dict[str, str] = {}
    for line in load_text(board_path).splitlines():
        match = BULLET_RE.match(line.strip())
        if not match:
            continue
        key = slugify(match.group(1))
        data[key] = match.group(2)
    return data


def parse_receipt(receipt_path: Path) -> Dict[str, Any]:
    lines = load_text(receipt_path).splitlines()
    data: Dict[str, Any] = {
        "sections": {},
        "generated_files": [],
    }
    current_section = ""
    for line in lines:
        section_match = SECTION_RE.match(line)
        if section_match:
            current_section = section_match.group(1)
            data["sections"][current_section] = []
            continue
        if current_section:
            data["sections"][current_section].append(line)

    for line in data["sections"].get("1. Source", []):
        match = BULLET_RE.match(line.strip())
        if match:
            data[slugify(match.group(1))] = match.group(2)
    for line in data["sections"].get("3. Normalized Routing", []):
        match = BULLET_RE.match(line.strip())
        if match:
            data[slugify(match.group(1))] = match.group(2)
    for line in data["sections"].get("5A. Run Identity", []):
        match = BULLET_RE.match(line.strip())
        if match:
            data[slugify(match.group(1))] = match.group(2)
    for line in data["sections"].get("7. Generated / Updated Files", []):
        match = PATH_BULLET_RE.match(line.strip())
        if match:
            data["generated_files"].append(match.group(1))
    for line in data["sections"].get("9. Final Status", []):
        match = BULLET_RE.match(line.strip())
        if match:
            data[slugify(match.group(1))] = match.group(2)
    return data


def score_overlap(base_tokens: Sequence[str], candidate_tokens: Sequence[str]) -> int:
    if not base_tokens or not candidate_tokens:
        return 0
    base = set(base_tokens)
    candidate = set(candidate_tokens)
    return len(base & candidate)


def build_scope_tokens(scope_ref: Optional[str], receipt_data: Dict[str, Any]) -> List[str]:
    values = [
        scope_ref,
        str(receipt_data.get("doc_id", "")),
        str(receipt_data.get("source_path", "")),
        Path(str(receipt_data.get("source_path", "") or "unknown")).stem,
    ]
    tokens: List[str] = []
    for value in values:
        tokens.extend(tokenize(str(value)))
    return tokens


def summarize_selection(
    *,
    selected_path: Optional[Path],
    selected_score: int,
    strategy: str,
    reason: str,
) -> Dict[str, Any]:
    return {
        "selected_ref": as_repo_rel(selected_path) if selected_path else None,
        "selected_score": selected_score if selected_score >= 0 else None,
        "strategy": strategy,
        "reason": reason,
    }


def choose_best_receipt(
    explicit_receipt: Optional[Path],
    explicit_board: Optional[Path],
    *,
    scope_ref: Optional[str],
) -> Tuple[Path, Optional[Path], Dict[str, Any]]:
    if explicit_receipt:
        return explicit_receipt, explicit_board, summarize_selection(
            selected_path=explicit_receipt,
            selected_score=-1,
            strategy="explicit",
            reason="explicit receipt path provided",
        )

    base_tokens = tokenize(scope_ref or "")
    if scope_ref and base_tokens:
        scored: List[Tuple[int, Path]] = []
        for path in sorted(RECEIPTS_ROOT.glob("*.md")):
            receipt_data = parse_receipt(path)
            candidate_tokens = tokenize(str(receipt_data.get("doc_id", ""))) + tokenize(str(receipt_data.get("source_path", "")))
            score = score_overlap(base_tokens, candidate_tokens)
            if score > 0:
                scored.append((score, path))
        scored.sort(key=lambda item: (item[0], item[1].stat().st_mtime), reverse=True)
        if scored:
            score, path = scored[0]
            return path, explicit_board, summarize_selection(
                selected_path=path,
                selected_score=score,
                strategy="scope_token_overlap",
                reason="selected receipt with positive overlap against scope tokens",
            )
        raise ValueError(
            "no positive-overlap receipt found for scope_ref; "
            "provide --receipt explicitly or use a scope that resolves to a bounded receipt"
        )

    board_path = explicit_board or (VIEWS_ROOT / "operation_board_latest.md")
    board_data = parse_operation_board(board_path)
    receipt_ref = board_data.get("receipt")
    if not receipt_ref:
        raise ValueError(f"no receipt pointer found in board={board_path}")
    receipt_path = (REPO_ROOT / receipt_ref).resolve()
    return receipt_path, board_path, summarize_selection(
        selected_path=receipt_path,
        selected_score=-1,
        strategy="latest_board_pointer",
        reason="fell back to operation_board_latest pointer because no explicit or scope receipt matched",
    )


def choose_best_supervisor_view(
    explicit_view: Optional[Path],
    *,
    scope_ref: Optional[str],
    receipt_data: Dict[str, Any],
    allow_scope_search: bool,
) -> Tuple[Optional[Path], Dict[str, Any]]:
    if explicit_view:
        return explicit_view, summarize_selection(
            selected_path=explicit_view,
            selected_score=-1,
            strategy="explicit",
            reason="explicit supervisor view path provided",
        )

    for rel in receipt_data.get("generated_files", []):
        if rel.endswith(".json") and "_supervisor_surface_" in rel:
            path = (REPO_ROOT / rel).resolve()
            return path, summarize_selection(
                selected_path=path,
                selected_score=-1,
                strategy="receipt_generated_file",
                reason="selected supervisor view directly from receipt generated files",
            )

    if not allow_scope_search:
        return None, summarize_selection(
            selected_path=None,
            selected_score=0,
            strategy="disabled_without_scope",
            reason="global supervisor view search disabled because no scope_ref or explicit receipt bounded the selection",
        )

    base_tokens = build_scope_tokens(scope_ref, receipt_data)
    scored: List[Tuple[int, Path]] = []
    for path in sorted(MULTI_LENS_ROOT.glob("*_supervisor_surface_*.json")):
        score = score_overlap(base_tokens, tokenize(path.name))
        if score > 0:
            scored.append((score, path))
    scored.sort(key=lambda item: (item[0], item[1].stat().st_mtime), reverse=True)
    if scored:
        score, path = scored[0]
        return path, summarize_selection(
            selected_path=path,
            selected_score=score,
            strategy="scope_token_overlap",
            reason="selected supervisor view with positive overlap against scope/doc/source tokens",
        )

    return None, summarize_selection(
        selected_path=None,
        selected_score=0,
        strategy="scope_token_overlap",
        reason="no positive-overlap supervisor view found; linked views rely on board only",
    )


def choose_sidecar(explicit_sidecar: Optional[Path], receipt_data: Dict[str, Any]) -> Optional[Path]:
    if explicit_sidecar:
        return explicit_sidecar

    doc_tokens = tokenize(str(receipt_data.get("doc_id", "")))
    source_tokens = tokenize(str(receipt_data.get("source_path", "")))
    base_tokens = doc_tokens + source_tokens
    best_score = -1
    best_path: Optional[Path] = None

    for path in sorted(EXPLORATION_ROOT.glob("*.json")):
        payload = load_json(path)
        candidate_tokens = tokenize(str(payload.get("exploration_id", ""))) + tokenize(str(payload.get("source_ref", "")))
        score = score_overlap(base_tokens, candidate_tokens)
        if score > best_score:
            best_score = score
            best_path = path

    if best_path:
        return best_path
    candidates = sorted(EXPLORATION_ROOT.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    return candidates[0] if candidates else None


def choose_best_sidecar(
    explicit_sidecar: Optional[Path],
    *,
    scope_ref: Optional[str],
    receipt_data: Dict[str, Any],
    allow_scope_search: bool,
) -> Tuple[Optional[Path], Dict[str, Any]]:
    if explicit_sidecar:
        return explicit_sidecar, summarize_selection(
            selected_path=explicit_sidecar,
            selected_score=-1,
            strategy="explicit",
            reason="explicit sidecar path provided",
        )

    if not allow_scope_search:
        return None, summarize_selection(
            selected_path=None,
            selected_score=0,
            strategy="disabled_without_scope",
            reason="auto sidecar search disabled because no scope_ref or explicit receipt bounded the selection",
        )

    base_tokens = build_scope_tokens(scope_ref, receipt_data)
    scored: List[Tuple[int, Path]] = []
    for path in sorted(EXPLORATION_ROOT.glob("*.json")):
        payload = load_json(path)
        candidate_tokens = tokenize(str(payload.get("exploration_id", ""))) + tokenize(str(payload.get("source_ref", "")))
        score = score_overlap(base_tokens, candidate_tokens)
        if score > 0:
            scored.append((score, path))
    scored.sort(key=lambda item: (item[0], item[1].stat().st_mtime), reverse=True)
    if scored:
        score, path = scored[0]
        return path, summarize_selection(
            selected_path=path,
            selected_score=score,
            strategy="scope_token_overlap",
            reason="selected sidecar with positive overlap against scope/doc/source tokens",
        )
    return None, summarize_selection(
        selected_path=None,
        selected_score=0,
        strategy="scope_token_overlap",
        reason="no positive-overlap sidecar found; builder leaves sidecar empty instead of falling back loosely",
    )


def choose_engine_state(
    explicit_state: Optional[Path],
    explicit_event: Optional[Path],
    receipt_data: Dict[str, Any],
) -> Tuple[Optional[Path], Optional[Path]]:
    if explicit_state or explicit_event:
        return explicit_state, explicit_event

    doc_id = str(receipt_data.get("doc_id", ""))
    source_path = str(receipt_data.get("source_path", ""))
    candidates = []
    source_stem = Path(source_path).stem if source_path else ""
    if doc_id.startswith("doc_"):
        candidates.append(doc_id[len("doc_"):])
    if source_stem:
        candidates.append(source_stem)

    for candidate in candidates:
        state_path = ENGINE_STATE_LATEST_ROOT / f"{candidate}.json"
        event_path = ENGINE_STATE_EVENT_ROOT / f"{candidate}.json"
        if state_path.exists() or event_path.exists():
            return (state_path if state_path.exists() else None, event_path if event_path.exists() else None)
    return None, None


def choose_best_engine_state(
    explicit_state: Optional[Path],
    explicit_event: Optional[Path],
    *,
    scope_ref: Optional[str],
    receipt_data: Dict[str, Any],
    allow_scope_search: bool,
) -> Tuple[Optional[Path], Optional[Path], Dict[str, Any]]:
    if explicit_state or explicit_event:
        return explicit_state, explicit_event, {
            "selected_state_ref": as_repo_rel(explicit_state) if explicit_state else None,
            "selected_event_ref": as_repo_rel(explicit_event) if explicit_event else None,
            "selected_score": None,
            "strategy": "explicit",
            "reason": "explicit engine state/event path provided",
        }

    if not allow_scope_search:
        return None, None, {
            "selected_state_ref": None,
            "selected_event_ref": None,
            "selected_score": 0,
            "strategy": "disabled_without_scope",
            "reason": "auto engine state search disabled because no scope_ref or explicit receipt bounded the selection",
        }

    base_tokens = build_scope_tokens(scope_ref, receipt_data)
    best_score = 0
    best_candidate: Optional[str] = None
    for path in sorted(ENGINE_STATE_LATEST_ROOT.glob("*.json")):
        if path.name == "index.json":
            continue
        candidate = path.stem
        score = score_overlap(base_tokens, tokenize(candidate))
        if score > best_score:
            best_score = score
            best_candidate = candidate

    if best_candidate:
        state_path = ENGINE_STATE_LATEST_ROOT / f"{best_candidate}.json"
        event_path = ENGINE_STATE_EVENT_ROOT / f"{best_candidate}.json"
        return (
            state_path if state_path.exists() else None,
            event_path if event_path.exists() else None,
            {
                "selected_state_ref": as_repo_rel(state_path) if state_path.exists() else None,
                "selected_event_ref": as_repo_rel(event_path) if event_path.exists() else None,
                "selected_score": best_score,
                "strategy": "scope_token_overlap",
                "reason": "selected engine state/event with positive overlap against scope/doc/source tokens",
            },
        )

    return None, None, {
        "selected_state_ref": None,
        "selected_event_ref": None,
        "selected_score": 0,
        "strategy": "scope_token_overlap",
        "reason": "no positive-overlap engine state found; state context remains empty",
    }


def summarize_generated_files(files: Sequence[str]) -> Dict[str, Any]:
    view_refs = [path for path in files if path.startswith("runtime/views/")]
    command_refs = [path for path in files if path.startswith("runtime/commands/")]
    manifest_refs = [path for path in files if path.startswith("runtime/manifests/")]
    app_refs = [path for path in files if path.startswith("app/")]
    return {
        "generated_file_count": len(files),
        "view_refs": view_refs[:6],
        "command_refs": command_refs[:4],
        "manifest_refs": manifest_refs[:4],
        "app_refs": app_refs[:4],
    }


def compress_sidecar(sidecar_payload: Optional[Dict[str, Any]], sidecar_ref: Optional[str]) -> Dict[str, Any]:
    if not sidecar_payload or not sidecar_ref:
        return {
            "selected_sidecar_ref": None,
            "observation_type": None,
            "core_candidate_count": 0,
            "outer_candidate_count": 0,
            "deferred_count": 0,
            "next_action_hint": None,
        }
    return {
        "selected_sidecar_ref": sidecar_ref,
        "observation_type": sidecar_payload.get("observation_type"),
        "core_candidate_count": len(sidecar_payload.get("kept_as_core_candidate", [])),
        "outer_candidate_count": len(sidecar_payload.get("kept_as_outer_candidate", [])),
        "deferred_count": len(sidecar_payload.get("deferred_items", [])),
        "next_action_hint": sidecar_payload.get("next_action_hint"),
    }


def build_primary_readout(
    receipt_data: Dict[str, Any],
    supervisor_view_payload: Optional[Dict[str, Any]],
    sidecar_payload: Optional[Dict[str, Any]],
    state_payload: Optional[Dict[str, Any]],
) -> Dict[str, str]:
    scope_ref = str(receipt_data.get("source_path") or receipt_data.get("doc_id") or "unknown_scope")
    view_kind = supervisor_view_payload.get("kind") if supervisor_view_payload else "no_supervisor_view_found"
    state_ref = state_payload.get("asset_id") if state_payload else "none"
    sidecar_obs = sidecar_payload.get("observation_type") if sidecar_payload else "none"
    stable_now = [
        "receipt-backed lineage spine available",
        f"supervisor view={view_kind}",
    ]
    if state_payload:
        stable_now.append(f"engine_state_latest={state_ref}")
    observed_only = "no exploration sidecar selected"
    if sidecar_payload:
        observed_only = (
            f"exploration sidecar selected with observation_type={sidecar_obs}; "
            "kept/outer/defer remains bounded observation supplement only"
        )
    next_attention = "review linked pointers if deeper artifact reread is needed"
    if sidecar_payload and sidecar_payload.get("next_action_hint"):
        next_attention = str(sidecar_payload["next_action_hint"])
    return {
        "current_surface_summary": (
            f"bounded reconstruction packet for {scope_ref}; "
            "receipt supplies lineage, views supply surfaced state, sidecar stays supplemental"
        ),
        "what_is_stable_now": "; ".join(stable_now),
        "what_is_only_observed": observed_only,
        "what_needs_next_attention": next_attention,
    }


def build_markdown(packet: Dict[str, Any]) -> str:
    lines = [
        f"# {packet['reconstruction_id']}",
        "",
        "## context",
        f"- reconstruction_id: `{packet['reconstruction_id']}`",
        f"- constructed_at: `{packet['constructed_at']}`",
        f"- scope_ref: `{packet['scope_ref']}`",
        f"- receipt_ref: `{packet['lineage']['receipt_ref']}`",
        f"- routing_run_id: `{packet['lineage'].get('routing_run_id') or 'not_found'}`",
        f"- observer_run_id: `{packet['lineage'].get('observer_run_id') or 'not_found'}`",
        f"- related_asset_id: `{packet['lineage'].get('related_asset_id') or 'not_found'}`",
        "",
        "## primary readout",
        f"- current_surface_summary: {packet['primary_readout']['current_surface_summary']}",
        f"- what_is_stable_now: {packet['primary_readout']['what_is_stable_now']}",
        f"- what_is_only_observed: {packet['primary_readout']['what_is_only_observed']}",
        f"- what_needs_next_attention: {packet['primary_readout']['what_needs_next_attention']}",
        "",
        "## linked surfaces",
    ]
    for ref in packet["linked_receipts"]:
        lines.append(f"- receipt: `{ref}`")
    for ref in packet["linked_views"]:
        lines.append(f"- view: `{ref}`")
    for ref in packet["linked_sidecars"]:
        lines.append(f"- sidecar: `{ref}`")
    lines.extend([
        "",
        "## handoff boundary",
        f"- summary: {packet['handoff_boundary']['summary']}",
        f"- authority_note: {packet['handoff_boundary']['authority_note']}",
        "",
        "## next attention",
        f"- bounded_next_attention: {packet['bounded_next_attention']}",
        f"- latest_pointer_note: latest pointer is surfaced convenience only; per-reconstruction packet remains the authoritative reconstruction artifact",
    ])
    return "\n".join(lines) + "\n"


def build_latest_json(
    *,
    packet_ref_json: str,
    packet_ref_md: str,
    packet: Dict[str, Any],
) -> Dict[str, Any]:
    return {
        "kind": "bounded_reconstruction_supervisor_latest_pointer_v1",
        "updated_at": packet["constructed_at"],
        "latest_reconstruction_id": packet["reconstruction_id"],
        "latest_json_ref": packet_ref_json,
        "latest_md_ref": packet_ref_md,
        "index_json_ref": "runtime/views/reconstruction_supervisor/index.json",
        "index_md_ref": "runtime/views/reconstruction_supervisor/index.md",
        "scope_ref": packet["scope_ref"],
        "surface_summary": build_latest_surface_summary(packet),
        "linked_receipts": packet["linked_receipts"],
        "linked_views": packet["linked_views"],
        "linked_sidecars": packet["linked_sidecars"],
        "authoritative_note": "latest is a surfaced pointer, not the authoritative source",
        "authoritative_reconstruction_ref": packet_ref_json,
    }


def build_latest_markdown(latest_payload: Dict[str, Any]) -> str:
    lines = [
        "# reconstruction_supervisor_latest",
        "",
        "## latest pointer",
        f"- latest_reconstruction_id: `{latest_payload['latest_reconstruction_id']}`",
        f"- updated_at: `{latest_payload['updated_at']}`",
        f"- latest_json_ref: `{latest_payload['latest_json_ref']}`",
        f"- latest_md_ref: `{latest_payload['latest_md_ref']}`",
        f"- index_json_ref: `{latest_payload['index_json_ref']}`",
        f"- index_md_ref: `{latest_payload['index_md_ref']}`",
        f"- scope_ref: `{latest_payload['scope_ref']}`",
        f"- surface_summary: `sidecar={str(latest_payload['surface_summary']['has_sidecar']).lower()} / state={str(latest_payload['surface_summary']['has_state_context']).lower()} / views={latest_payload['surface_summary']['linked_view_count']} / mode={latest_payload['surface_summary']['selection_mode']}`",
        "",
        "## note",
        f"- authoritative_note: {latest_payload['authoritative_note']}",
    ]
    return "\n".join(lines) + "\n"


def build_reconstruction_index_items() -> List[Dict[str, str]]:
    items: List[Dict[str, Any]] = []
    for path in sorted(RECONSTRUCTION_ROOT.glob("*.json")):
        if path.name in {"index.json"}:
            continue
        payload = load_json(path)
        reconstruction_id = payload.get("reconstruction_id")
        if not reconstruction_id:
            continue
        items.append(
            {
                "reconstruction_id": reconstruction_id,
                "scope_ref": str(payload.get("scope_ref", "")),
                "json_ref": as_repo_rel(path),
                "md_ref": as_repo_rel(path.with_suffix(".md")),
                "surface_summary": {
                    "has_sidecar": bool(payload.get("linked_sidecars")),
                    "has_state_context": bool(payload.get("state_context", {}).get("engine_state_latest_ref")),
                    "linked_view_count": len(payload.get("linked_views", [])),
                    "selection_mode": (
                        "explicit_or_scope_bounded"
                        if any(
                            strategy not in {"disabled_without_scope", "latest_board_pointer", None}
                            for strategy in [
                                payload.get("selection_trace", {}).get("receipt_selection", {}).get("strategy"),
                                payload.get("selection_trace", {}).get("view_selection", {}).get("strategy"),
                                payload.get("selection_trace", {}).get("sidecar_selection", {}).get("strategy"),
                                payload.get("selection_trace", {}).get("state_selection", {}).get("strategy"),
                            ]
                        )
                        else "latest_pointer_minimal"
                    ),
                    "read_mode": payload.get("supervisor_surface_kind"),
                },
            }
        )
    items.sort(key=lambda item: item["reconstruction_id"])
    return items


def build_reconstruction_index_json(updated_at: str) -> Dict[str, Any]:
    return {
        "kind": "bounded_reconstruction_supervisor_index_v1",
        "updated_at": updated_at,
        "latest_pointer_refs": {
            "json": "runtime/views/reconstruction_supervisor_latest.json",
            "md": "runtime/views/reconstruction_supervisor_latest.md",
        },
        "items": build_reconstruction_index_items(),
        "read_order": [
            "runtime/views/reconstruction_supervisor_latest.json",
            "runtime/views/reconstruction_supervisor/<reconstruction_id>.json",
            "runtime/views/reconstruction_supervisor/<reconstruction_id>.md",
        ],
        "note": "index is a surfaced navigation aid, not an authoritative source",
    }


def build_reconstruction_index_markdown(index_payload: Dict[str, Any]) -> str:
    lines = [
        "# reconstruction_supervisor_index",
        "",
        "## latest pointer",
        "",
        "- json: `runtime/views/reconstruction_supervisor_latest.json`",
        "- md: `runtime/views/reconstruction_supervisor_latest.md`",
        "",
        "## packets",
        "",
    ]
    for item in index_payload.get("items", []):
        lines.extend(
            [
                f"- `{item['reconstruction_id']}`",
                f"  - json: `{item['json_ref']}`",
                f"  - md: `{item['md_ref']}`",
                f"  - summary: `sidecar={str(item['surface_summary']['has_sidecar']).lower()} / state={str(item['surface_summary']['has_state_context']).lower()} / views={item['surface_summary']['linked_view_count']} / mode={item['surface_summary']['selection_mode']}`",
            ]
        )
    lines.extend(
        [
            "",
            "## read order",
            "",
            "- latest pointer부터 읽는다.",
            "- 그 다음 per-reconstruction json을 읽는다.",
            "- 사람이 다시 읽을 때만 md를 본다.",
            "",
            "## note",
            "",
            "- 이 index는 surfaced navigation aid다.",
            "- authoritative source는 per-reconstruction artifact다.",
        ]
    )
    return "\n".join(lines) + "\n"


def build_latest_surface_summary(packet: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "has_sidecar": bool(packet.get("linked_sidecars")),
        "has_state_context": bool(packet.get("state_context", {}).get("engine_state_latest_ref")),
        "linked_view_count": len(packet.get("linked_views", [])),
        "selection_mode": (
            "explicit_or_scope_bounded"
            if any(
                strategy not in {"disabled_without_scope", "latest_board_pointer", None}
                for strategy in [
                    packet.get("selection_trace", {}).get("receipt_selection", {}).get("strategy"),
                    packet.get("selection_trace", {}).get("view_selection", {}).get("strategy"),
                    packet.get("selection_trace", {}).get("sidecar_selection", {}).get("strategy"),
                    packet.get("selection_trace", {}).get("state_selection", {}).get("strategy"),
                ]
            )
            else "latest_pointer_minimal"
        ),
        "read_mode": packet.get("supervisor_surface_kind"),
    }


def build_reconstruction_folder_status(updated_at: str) -> str:
    items = build_reconstruction_index_items()
    json_count = len(list(RECONSTRUCTION_ROOT.glob("*.json")))
    md_count = len(list(RECONSTRUCTION_ROOT.glob("*.md")))
    lines = [
        "# folder_status / runtime/views/reconstruction_supervisor",
        "",
        "## 1. Folder Identity",
        "- path: `runtime/views/reconstruction_supervisor`",
        "- role_guess: Supervisor-facing bounded reconstruction packet surfaces and their lightweight navigation aids.",
        "- status_mode: `builder_generated_surface_summary`",
        "",
        "## 2. Snapshot",
        "- immediate_child_dirs: `0`",
        f"- immediate_child_files: `{json_count + md_count}`",
        f"- file_types: `.json` x {json_count}, `.md` x {md_count}",
        "",
        "## 3. Child Folders",
        "- none",
        "",
        "## 4. Core Files",
        "- `index.json`",
        "  summary: machine-readable navigation index for current reconstruction packet set",
        "- `index.md`",
        "  summary: human-readable navigation index and read order note",
    ]
    for item in items:
        json_name = Path(item["json_ref"]).name
        md_name = Path(item["md_ref"]).name
        lines.extend(
            [
                f"- `{json_name}`",
                f"  summary: reconstruction packet for `{item['scope_ref']}`",
                f"- `{md_name}`",
                f"  summary: human-readable companion for `{item['scope_ref']}`",
            ]
        )
    lines.extend(
        [
            "",
            "## 5. Current Use Hint",
            "- `runtime/views/reconstruction_supervisor_latest.*` 는 latest surfaced pointer다.",
            "- `index.*` 는 navigation surface다.",
            "- per-reconstruction `json`이 authoritative reconstruction artifact다.",
            "- `md`는 operator/supervisor reread companion이다.",
            "- 이 폴더는 decision surface가 아니라 read-only reconstruction surface다.",
            "",
            "## 6. Read Order",
            "- 먼저 `runtime/views/reconstruction_supervisor_latest.json` 또는 `.md`를 본다.",
            "- 필요하면 `runtime/views/reconstruction_supervisor/index.json` 또는 `.md`로 이동한다.",
            "- 다음으로 target reconstruction packet `json`을 본다.",
            "- 사람이 다시 읽을 때만 companion `md`를 본다.",
            "",
            "## 7. Guard Note",
            "- no decision logic",
            "- no governing behavior",
            "- no state mutation",
            "- latest is not authoritative",
            "- sidecar / receipt / views role separation must remain visible",
            "",
            "## 8. Updated At",
            f"- updated_at: `{updated_at}`",
        ]
    )
    return "\n".join(lines) + "\n"


def validate_packet(packet: Dict[str, Any], latest_payload: Dict[str, Any]) -> None:
    guard_values = packet.get("guards", {})
    required_true = [
        "not_decision_surface",
        "not_maturity_surface",
        "not_promotion_signal",
        "not_session_authority_surface",
        "read_only_reconstruction_only",
        "pointer_backed_surface",
    ]
    for key in required_true:
        if guard_values.get(key) is not True:
            raise ValueError(f"guard failed: {key}")
    if packet["lineage"].get("receipt_ref") not in packet["linked_receipts"]:
        raise ValueError("receipt lineage spine is not present in linked_receipts")
    if not packet["linked_views"]:
        raise ValueError("at least one linked view is required")
    if latest_payload.get("authoritative_note") == "latest is authoritative":
        raise ValueError("latest pointer must not be authoritative")


def first_non_empty(values: Iterable[Optional[str]]) -> Optional[str]:
    for value in values:
        if value:
            return value
    return None


def main() -> None:
    args = parse_args()

    scope_ref_arg = args.scope_ref
    explicit_receipt = resolve_rel_path(args.receipt)
    explicit_board = resolve_rel_path(args.operation_board)
    explicit_view = resolve_rel_path(args.supervisor_view)
    explicit_sidecar = resolve_rel_path(args.sidecar)
    explicit_state = resolve_rel_path(args.engine_state)
    explicit_event = resolve_rel_path(args.engine_event)
    allow_scope_search = bool(scope_ref_arg or explicit_receipt)

    receipt_path, board_path, receipt_selection = choose_best_receipt(
        explicit_receipt,
        explicit_board,
        scope_ref=scope_ref_arg,
    )
    receipt_data = parse_receipt(receipt_path)
    supervisor_view_path, view_selection = choose_best_supervisor_view(
        explicit_view,
        scope_ref=scope_ref_arg,
        receipt_data=receipt_data,
        allow_scope_search=allow_scope_search,
    )
    sidecar_path, sidecar_selection = choose_best_sidecar(
        explicit_sidecar,
        scope_ref=scope_ref_arg,
        receipt_data=receipt_data,
        allow_scope_search=allow_scope_search,
    )
    state_path, event_path, state_selection = choose_best_engine_state(
        explicit_state,
        explicit_event,
        scope_ref=scope_ref_arg,
        receipt_data=receipt_data,
        allow_scope_search=allow_scope_search,
    )

    supervisor_view_payload = load_json(supervisor_view_path) if supervisor_view_path else None
    sidecar_payload = load_json(sidecar_path) if sidecar_path else None
    state_payload = load_json(state_path) if state_path else None
    event_payload = load_json(event_path) if event_path else None

    scope_ref = first_non_empty(
        [
            scope_ref_arg,
            str(receipt_data.get("source_path")),
            str(receipt_data.get("doc_id")),
        ]
    ) or "unknown_scope"
    routing_run_id = str(receipt_data.get("run_id") or "")
    reconstruction_id = args.reconstruction_id or f"reconstruction_{slugify(Path(scope_ref).stem)}_{slugify(routing_run_id or make_idempotency_key(scope_ref))}"

    linked_views: List[str] = []
    if board_path:
        linked_views.append(as_repo_rel(board_path))
    if supervisor_view_path:
        linked_views.append(as_repo_rel(supervisor_view_path))
    if state_path:
        linked_views.append(as_repo_rel(state_path))
    if event_path:
        linked_views.append(as_repo_rel(event_path))

    linked_sidecars = [as_repo_rel(sidecar_path)] if sidecar_path else []
    linked_receipts = [as_repo_rel(receipt_path)]
    constructed_at = now_iso()

    packet = {
        "kind": "bounded_reconstruction_supervisor_surface_v1",
        "reconstruction_id": reconstruction_id,
        "constructed_at": constructed_at,
        "scope_ref": scope_ref,
        "supervisor_surface_kind": "surfaced_first_pointer_backed_reconstruction",
        "lineage": {
            "receipt_ref": as_repo_rel(receipt_path),
            "operation_board_ref": as_repo_rel(board_path) if board_path else None,
            "source_doc_ref": first_non_empty([str(receipt_data.get("source_path")), str(receipt_data.get("doc_id"))]),
            "routing_run_id": routing_run_id or None,
            "observer_run_id": supervisor_view_payload.get("observer_run_id") if supervisor_view_payload else None,
            "related_asset_id": state_payload.get("asset_id") if state_payload else None,
            "constructed_from_families": [
                "receipt_lineage_spine",
                "supervisor_surface_views",
                "bounded_observation_sidecar",
            ],
        },
        "routing_context": {
            "latest_receipt_ref": as_repo_rel(receipt_path),
            "operation_board_ref": as_repo_rel(board_path) if board_path else None,
            "routing_mode_summary": {
                "docrole": receipt_data.get("docrole"),
                "runmode": receipt_data.get("runmode"),
                "priority": receipt_data.get("priority"),
            },
            "generated_artifact_summary": summarize_generated_files(receipt_data.get("generated_files", [])),
        },
        "observer_context": compress_sidecar(sidecar_payload, linked_sidecars[0] if linked_sidecars else None),
        "state_context": {
            "engine_state_latest_ref": as_repo_rel(state_path) if state_path else None,
            "engine_state_update_event_ref": as_repo_rel(event_path) if event_path else None,
            "changed_canonical_fields": event_payload.get("changed_canonical_fields", []) if event_payload else [],
            "latest_maturation_state": event_payload.get("latest_maturation_state") if event_payload else None,
            "latest_traceability_status": event_payload.get("latest_traceability_status") if event_payload else None,
        },
        "primary_readout": build_primary_readout(receipt_data, supervisor_view_payload, sidecar_payload, state_payload),
        "linked_receipts": linked_receipts,
        "linked_views": linked_views,
        "linked_sidecars": linked_sidecars,
        "handoff_boundary": {
            "summary": (
                "this surface stops at surfaced reconstruction and linked pointers; "
                "it does not open governance, promotion, or mutation behavior"
            ),
            "authority_note": "observation handoff only; not a decision surface",
        },
        "bounded_next_attention": (
            sidecar_payload.get("next_action_hint")
            if sidecar_payload and sidecar_payload.get("next_action_hint")
            else "follow linked receipt/view/sidecar pointers for any deeper reread"
        ),
        "guards": {
            "not_decision_surface": True,
            "not_maturity_surface": True,
            "not_promotion_signal": True,
            "not_session_authority_surface": True,
            "read_only_reconstruction_only": True,
            "pointer_backed_surface": True,
            "state_mutation_performed": False,
            "governing_behavior_present": False,
        },
        "selection_trace": {
            "receipt_selection": receipt_selection,
            "view_selection": view_selection,
            "sidecar_selection": sidecar_selection,
            "state_selection": state_selection,
            "actor": args.actor,
        },
    }

    output_json_path = RECONSTRUCTION_ROOT / f"{reconstruction_id}.json"
    output_md_path = RECONSTRUCTION_ROOT / f"{reconstruction_id}.md"
    packet_md = build_markdown(packet)
    packet_json_ref = as_repo_rel(output_json_path)
    packet_md_ref = as_repo_rel(output_md_path)
    latest_payload = build_latest_json(packet_ref_json=packet_json_ref, packet_ref_md=packet_md_ref, packet=packet)
    validate_packet(packet, latest_payload)

    atomic_write_json(output_json_path, packet)
    atomic_write_text(output_md_path, packet_md)
    atomic_write_json(VIEWS_ROOT / "reconstruction_supervisor_latest.json", latest_payload)
    atomic_write_text(VIEWS_ROOT / "reconstruction_supervisor_latest.md", build_latest_markdown(latest_payload))
    index_payload = build_reconstruction_index_json(packet["constructed_at"])
    atomic_write_json(RECONSTRUCTION_ROOT / "index.json", index_payload)
    atomic_write_text(RECONSTRUCTION_ROOT / "index.md", build_reconstruction_index_markdown(index_payload))
    atomic_write_text(RECONSTRUCTION_ROOT / "folder_status.md", build_reconstruction_folder_status(packet["constructed_at"]))

    print(json.dumps(
        {
            "reconstruction_id": reconstruction_id,
            "json_ref": packet_json_ref,
            "md_ref": packet_md_ref,
            "latest_json_ref": "runtime/views/reconstruction_supervisor_latest.json",
            "latest_md_ref": "runtime/views/reconstruction_supervisor_latest.md",
            "sidecar_ref": linked_sidecars[0] if linked_sidecars else None,
            "state_ref": as_repo_rel(state_path) if state_path else None,
        },
        ensure_ascii=False,
        indent=2,
    ))


if __name__ == "__main__":
    main()
