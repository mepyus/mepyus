from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List
import hashlib
import json

from app.work.input_layer.axis_input_parser import parse_axis_material_drafts


MAX_ADMISSION_CANDIDATES = 4
MIN_FRAGMENT_LENGTH = 12


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def normalize_text(text: str) -> str:
    lines = [line.rstrip() for line in text.replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    return "\n".join(lines).strip()


def compute_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def split_fragments_minimal(text: str) -> List[str]:
    raw_chunks = [chunk.strip() for chunk in text.split("\n\n")]
    raw_chunks = [chunk for chunk in raw_chunks if chunk]

    if not raw_chunks:
        return [text]

    merged: List[str] = []
    for chunk in raw_chunks:
        if len(chunk) < MIN_FRAGMENT_LENGTH:
            if merged:
                merged[-1] = merged[-1] + "\n\n" + chunk
            else:
                merged.append(chunk)
        else:
            merged.append(chunk)

    return merged or [text]


def parse_axis_fragments(text: str) -> List[dict]:
    drafts = parse_axis_material_drafts(text)
    if not drafts:
        return [
            {
                "text": fragment,
                "block_label": "plain",
                "axes": {
                    "direction": "descriptive_forward",
                    "intensity": "medium",
                    "stability": "transitional",
                    "time": "unspecified",
                },
                "connectivity_keys": [],
            }
            for fragment in split_fragments_minimal(text)
        ]

    return [
        {
            "text": draft.source_text,
            "block_label": draft.block_label,
            "axes": {
                "direction": draft.axes.direction,
                "intensity": draft.axes.intensity,
                "stability": draft.axes.stability,
                "time": draft.axes.time,
            },
            "connectivity_keys": list(draft.connectivity_keys),
        }
        for draft in drafts
    ]


def has_giant_collapse_risk(text: str, fragment_rows: List[dict]) -> bool:
    non_empty_lines = [line.strip() for line in text.split("\n") if line.strip()]
    return len(non_empty_lines) >= 2 and len(fragment_rows) == 1


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def build_event(run_id: str, note_path: Path, source_hash: str, normalized: str) -> dict:
    return {
        "id": f"evt_{run_id}",
        "type": "event",
        "run_id": run_id,
        "source_note_path": str(note_path),
        "source_content_hash": source_hash,
        "parent_ids": [],
        "body": normalized,
        "created_at": now_iso(),
    }


def build_fragments(
    run_id: str,
    note_path: Path,
    source_hash: str,
    fragments: List[dict],
    event_id: str,
) -> List[dict]:
    rows: List[dict] = []
    for idx, fragment in enumerate(fragments, start=1):
        rows.append(
            {
                "id": f"frag_{run_id}_{idx:03d}",
                "type": "fragment",
                "run_id": run_id,
                "source_note_path": str(note_path),
                "source_content_hash": source_hash,
                "parent_ids": [event_id],
                "fragment_index": idx,
                "text": fragment["text"],
                "block_label": fragment.get("block_label", "plain"),
                "axes": dict(fragment.get("axes", {})),
                "connectivity_keys": list(fragment.get("connectivity_keys", [])),
                "created_at": now_iso(),
            }
        )
    return rows


def build_candidates(
    run_id: str,
    note_path: Path,
    source_hash: str,
    event_id: str,
    fragment_rows: List[dict],
) -> List[dict]:
    candidates: List[dict] = []
    for idx, fragment in enumerate(fragment_rows, start=1):
        text = fragment.get("text", "").strip()
        if len(text) < MIN_FRAGMENT_LENGTH:
            continue
        candidates.append(
            {
                "id": f"cand_{run_id}_{idx:03d}",
                "type": "candidate",
                "run_id": run_id,
                "source_note_path": str(note_path),
                "source_content_hash": source_hash,
                "parent_ids": [event_id, fragment["id"]],
                "fragment_id": fragment["id"],
                "text": fragment["text"],
                "block_label": fragment.get("block_label", "plain"),
                "axes": dict(fragment.get("axes", {})),
                "connectivity_keys": list(fragment.get("connectivity_keys", [])),
                "created_at": now_iso(),
            }
        )
        if len(candidates) >= MAX_ADMISSION_CANDIDATES:
            break
    return candidates


def build_bridges(
    run_id: str,
    note_path: Path,
    source_hash: str,
    event: dict,
    fragment_rows: List[dict],
    candidate_rows: List[dict],
    giant_collapse: bool,
) -> List[dict]:
    source_refs = [
        {
            "kind": "note",
            "path": str(note_path),
            "source_content_hash": source_hash,
        }
    ]

    if giant_collapse:
        fragment_id = fragment_rows[0]["id"] if fragment_rows else None
        bridge = {
            "bridge_id": f"bridge_{run_id}_001",
            "type": "bridge",
            "run_id": run_id,
            "status": "HOLD",
            "status_reason": "giant_collapse_risk",
            "ready_checks": {
                "has_event": bool(event.get("id")),
                "has_fragment": bool(fragment_rows),
                "has_candidate": bool(candidate_rows),
                "has_source_hash": bool(source_hash),
                "has_source_refs": True,
                "has_parent_refs": bool(event.get("id")),
            },
            "source_note_path": str(note_path),
            "source_content_hash": source_hash,
            "event_id": event["id"],
            "fragment_id": fragment_id,
            "candidate_id": candidate_rows[0]["id"] if candidate_rows else None,
            "source_refs": source_refs,
            "parent_refs": [event["id"]] + ([fragment_id] if fragment_id else []),
            "created_at": now_iso(),
        }
        return [bridge]

    if not candidate_rows:
        bridge = {
            "bridge_id": f"bridge_{run_id}_001",
            "type": "bridge",
            "run_id": run_id,
            "status": "HOLD",
            "status_reason": "candidate_missing",
            "ready_checks": {
                "has_event": bool(event.get("id")),
                "has_fragment": bool(fragment_rows),
                "has_candidate": False,
                "has_source_hash": bool(source_hash),
                "has_source_refs": True,
                "has_parent_refs": bool(event.get("id")),
            },
            "source_note_path": str(note_path),
            "source_content_hash": source_hash,
            "event_id": event["id"],
            "fragment_id": None,
            "candidate_id": None,
            "source_refs": source_refs,
            "parent_refs": [event["id"]],
            "created_at": now_iso(),
        }
        return [bridge]

    bridges: List[dict] = []
    for idx, candidate in enumerate(candidate_rows[:MAX_ADMISSION_CANDIDATES], start=1):
        fragment_id = candidate.get("fragment_id")
        fragment = next((row for row in fragment_rows if row["id"] == fragment_id), None)

        if fragment is None:
            bridge = {
                "bridge_id": f"bridge_{run_id}_{idx:03d}",
                "type": "bridge",
                "run_id": run_id,
                "status": "HOLD",
                "status_reason": "fragment_missing_for_candidate",
                "ready_checks": {
                    "has_event": bool(event.get("id")),
                    "has_fragment": False,
                    "has_candidate": bool(candidate.get("id")),
                    "has_source_hash": bool(source_hash),
                    "has_source_refs": True,
                    "has_parent_refs": True,
                },
                "source_note_path": str(note_path),
                "source_content_hash": source_hash,
                "event_id": event["id"],
                "fragment_id": fragment_id,
                "candidate_id": candidate["id"],
                "source_refs": source_refs,
                "parent_refs": [event["id"], candidate["id"]],
                "created_at": now_iso(),
            }
            bridges.append(bridge)
            continue

        bridge = {
            "bridge_id": f"bridge_{run_id}_{idx:03d}",
            "type": "bridge",
            "run_id": run_id,
            "status": "BRIDGE_READY",
            "status_reason": "minimum_handoff_contract_satisfied",
            "ready_checks": {
                "has_event": bool(event.get("id")),
                "has_fragment": bool(fragment.get("id")),
                "has_candidate": bool(candidate.get("id")),
                "has_source_hash": bool(source_hash),
                "has_source_refs": True,
                "has_parent_refs": True,
            },
            "source_note_path": str(note_path),
            "source_content_hash": source_hash,
            "event_id": event["id"],
            "fragment_id": fragment["id"],
            "candidate_id": candidate["id"],
            "candidate_text": candidate.get("text"),
            "block_label": candidate.get("block_label", "plain"),
            "axes": dict(candidate.get("axes", {})),
            "connectivity_keys": list(candidate.get("connectivity_keys", [])),
            "source_refs": source_refs,
            "parent_refs": [event["id"], fragment["id"], candidate["id"]],
            "created_at": now_iso(),
        }
        bridges.append(bridge)

    return bridges


def run_stage0_handoff(runtime_root: Path, payload: Dict[str, str]) -> Dict[str, object]:
    raw_payload = str(payload.get("raw_payload", "")).strip()
    if not raw_payload:
        raise ValueError("raw_payload is required")

    source_type = str(payload.get("source_type", "memo")).strip().lower() or "memo"
    source_ref = str(payload.get("source_ref", "")).strip() or _default_source_ref(source_type)

    normalized = normalize_text(raw_payload)
    if not normalized:
        raise ValueError("raw_payload is required")

    source_hash = compute_hash(normalized)
    run_id = f"probe_run_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"

    source_docs_dir = runtime_root / "source_documents"
    stage0_root = runtime_root / "stage0_handoff"
    runs_dir = stage0_root / "runs"
    ledger_dir = stage0_root / "ledger"
    source_docs_dir.mkdir(parents=True, exist_ok=True)
    runs_dir.mkdir(parents=True, exist_ok=True)
    ledger_dir.mkdir(parents=True, exist_ok=True)

    note_path = source_docs_dir / f"{source_ref}.note.txt"
    note_path.write_text(normalized + "\n", encoding="utf-8")

    run_dir = runs_dir / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    fragments = parse_axis_fragments(normalized)
    event = build_event(run_id, note_path, source_hash, normalized)
    fragment_rows = build_fragments(run_id, note_path, source_hash, fragments, event["id"])
    candidate_rows = build_candidates(run_id, note_path, source_hash, event["id"], fragment_rows)
    giant_collapse = has_giant_collapse_risk(normalized, fragment_rows)
    bridge_rows = build_bridges(
        run_id=run_id,
        note_path=note_path,
        source_hash=source_hash,
        event=event,
        fragment_rows=fragment_rows,
        candidate_rows=candidate_rows,
        giant_collapse=giant_collapse,
    )

    manifest = {
        "run_id": run_id,
        "source_note_path": str(note_path),
        "source_content_hash": source_hash,
        "status": "EVENT_FRAGMENT_CANDIDATE_BRIDGE_WRITTEN",
        "bridge_status": bridge_rows[0].get("status") if bridge_rows else "",
        "bridge_status_reason": bridge_rows[0].get("status_reason") if bridge_rows else "",
        "counts": {
            "event": 1,
            "fragment": len(fragment_rows),
            "candidate": len(candidate_rows),
            "bridge": len(bridge_rows),
        },
        "decomposition_kind": "axis_stage0_bridge_handoff",
        "created_at": now_iso(),
    }

    write_json(run_dir / "event.json", event)
    write_json(run_dir / "fragments.json", fragment_rows)
    write_json(run_dir / "candidates.json", candidate_rows)
    write_json(run_dir / "bridges.json", bridge_rows)
    write_json(run_dir / "manifest.json", manifest)

    ledger_row = {
        "source_content_hash": source_hash,
        "source_note_path": str(note_path),
        "run_id": run_id,
        "recorded_at": now_iso(),
    }
    with (ledger_dir / "processed_hashes_multi_candidate_probe.jsonl").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(ledger_row, ensure_ascii=False) + "\n")

    return {
        "run_dir": run_dir,
        "run_id": run_id,
        "source_ref": source_ref,
        "source_type": source_type,
        "source_note_path": str(note_path),
        "source_content_hash": source_hash,
        "event": event,
        "fragments": fragment_rows,
        "candidates": candidate_rows,
        "bridges": bridge_rows,
        "manifest": manifest,
    }


def build_handoff_materials(runtime_root: Path, payload: Dict[str, str]) -> Dict[str, object]:
    stage0_output = run_stage0_handoff(runtime_root, payload)
    handoff_materials: List[Dict[str, object]] = []
    for bridge in stage0_output["bridges"]:
        if bridge.get("status") != "BRIDGE_READY":
            continue
        handoff_materials.append(
            {
                "source_type": stage0_output["source_type"],
                "source_ref": stage0_output["source_ref"],
                "source_note_path": stage0_output["source_note_path"],
                "source_content_hash": stage0_output["source_content_hash"],
                "run_id": stage0_output["run_id"],
                "bridge_id": bridge["bridge_id"],
                "bridge_status": bridge.get("status"),
                "bridge_status_reason": bridge.get("status_reason"),
                "event_id": bridge.get("event_id"),
                "fragment_id": bridge.get("fragment_id"),
                "candidate_id": bridge.get("candidate_id"),
                "candidate_text": bridge.get("candidate_text", ""),
                "block_label": bridge.get("block_label", "plain"),
                "axes": dict(bridge.get("axes", {})),
                "connectivity_keys": list(bridge.get("connectivity_keys", [])),
                "source_refs": list(bridge.get("source_refs", [])),
                "parent_refs": list(bridge.get("parent_refs", [])),
                "fragment_count": stage0_output["manifest"]["counts"]["fragment"],
                "candidate_count": stage0_output["manifest"]["counts"]["candidate"],
                "bridge_count": stage0_output["manifest"]["counts"]["bridge"],
                "source_document_id": stage0_output["source_content_hash"],
                "decomposition_kind": str(
                    stage0_output["manifest"].get("decomposition_kind", "axis_stage0_bridge_handoff")
                ),
            }
        )

    return {
        "stage0_output": stage0_output,
        "handoff_materials": handoff_materials,
    }


def _default_source_ref(source_type: str) -> str:
    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    return "%s-%s" % (source_type, timestamp)
