from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from uuid import uuid4


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.input_layer.source_locator.origin_map_minimum_v1 import build_origin_map
from app.core.events.event_append_guard import append_jsonl_locked, load_jsonl_with_tail_recovery, recover_jsonl_tail
from app.core.registry.atomic_io import atomic_write_json, atomic_write_text, file_lock, locked_load_json, make_idempotency_key
from app.core.registry.folder_status_sync import sync_folder_status
from app.core.runtime.line_thickening import RereadObservation, record_reread_observation
from app.core.runtime.multi_lens_runtime_flow import (
    build_multi_lens_observation_payload,
    build_multi_lens_supervisor_surface,
)
from app.input_layer.labeler.labeler import (
    build_core_intake_labels,
    build_label_packet,
    normalize_external_labels,
)
from app.input_layer.gmd_native_read import build_gmd_native_read


ALIAS_MAP_PATH = REPO_ROOT / "runtime" / "manifests" / "document_routing_alias_map_v1.json"
DOC_REGISTRY_PATH = REPO_ROOT / "runtime" / "manifests" / "structured_internal_docs_registry_v1.json"
TICKET_REGISTRY_PATH = REPO_ROOT / "runtime" / "manifests" / "ticket_registry_v1.json"
PROVENANCE_INDEX_PATH = REPO_ROOT / "runtime" / "manifests" / "provenance_link_index_v1.json"
ORIGIN_MAPS_ROOT = REPO_ROOT / "runtime" / "manifests" / "origin_maps"
LABEL_PACKET_ROOT = REPO_ROOT / "runtime" / "manifests" / "label_packets"
ENGINE_LEDGER = REPO_ROOT / "runtime" / "events" / "engine_event_ledger.jsonl"
FOLDER_ACTIVITY_ROOT = REPO_ROOT / "runtime" / "events" / "folder_activity"
RECEIPTS_ROOT = REPO_ROOT / "runtime" / "receipts"
VIEWS_ROOT = REPO_ROOT / "runtime" / "views"
COMMANDS_ROOT = REPO_ROOT / "runtime" / "commands"
MULTI_LENS_VIEW_ROOT = VIEWS_ROOT / "multi_lens_document_reading"
OBSERVER_SCRIPT = REPO_ROOT / "app" / "work" / "observer_ingest_min" / "run_observer_ingest_min.py"
OBSERVER_OUTPUT_ROOT = REPO_ROOT / "app" / "work" / "observer_ingest_min" / "generated"
MARKER_BLOCK_RE = re.compile(r"\[\[(DOCROLE|RUNMODE|PRIORITY):(.+?)\]\]")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Process a structured doc with routing markers.")
    parser.add_argument("--doc", required=True, help="Path to the structured document")
    parser.add_argument("--actor", default="codex")
    parser.add_argument("--source-session", default="local_codex_session")
    parser.add_argument(
        "--record-line-thickening",
        action="store_true",
        help="append a bounded line_thickening observation from the structured-doc routing path",
    )
    return parser.parse_args()


def slugify(value: str) -> str:
    lowered = value.strip().lower()
    cleaned = re.sub(r"[^a-z0-9_-]+", "_", lowered)
    return cleaned.strip("_") or "doc"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    atomic_write_json(path, payload)


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def make_event_id() -> str:
    return f"evt_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid4().hex[:8]}"


def append_jsonl(path: Path, row: dict) -> None:
    append_jsonl_locked(path, row)


def append_event(
    *,
    event_type: str,
    target_ref: str,
    source_doc_ref: str,
    ticket_ref: str,
    actor: str,
    status: str = "recorded",
    notes: str = "",
    folder_ref: str = "",
    output_ref: str = "",
    derived_from: str = "",
) -> dict:
    event = {
        "event_id": make_event_id(),
        "event_type": event_type,
        "timestamp": now_iso(),
        "actor": actor,
        "target_ref": target_ref,
        "source_doc_ref": source_doc_ref,
        "ticket_ref": ticket_ref,
        "status": status,
        "notes": notes,
    }
    if folder_ref:
        event["folder_ref"] = folder_ref
    if output_ref:
        event["output_ref"] = output_ref
    if derived_from:
        event["derived_from"] = derived_from
    append_jsonl(ENGINE_LEDGER, event)
    if folder_ref:
        append_jsonl(FOLDER_ACTIVITY_ROOT / f"{folder_ref}.folder_activity_log.jsonl", event)
    return event


def resolve_doc_path(doc: str) -> Path:
    path = Path(doc)
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    if not path.exists():
        raise FileNotFoundError(f"document not found: {path}")
    return path


def parse_markers(text: str) -> dict[str, str]:
    markers: dict[str, str] = {}
    for line in text.splitlines()[:8]:
        for key, value in MARKER_BLOCK_RE.findall(line):
            markers[key] = value.strip()
    return markers


def ensure_doc_registry_entry(
    *,
    doc_id: str,
    doc_ref: str,
    core_labels: dict[str, object],
    idempotency_key: str,
    run_id: str,
) -> None:
    lock_path = DOC_REGISTRY_PATH.with_suffix(DOC_REGISTRY_PATH.suffix + ".lock")
    with file_lock(lock_path):
        payload = locked_load_json(DOC_REGISTRY_PATH)
        entries = payload.setdefault("entries", [])
        existing = next((row for row in entries if row["doc_id"] == doc_id), None)
        record = {
            "doc_id": doc_id,
            "doc_ref": doc_ref,
            "input_class": core_labels["input_class"],
            "processing_profile": core_labels["processing_profile"],
            "material_grade": core_labels["material_grade"],
            "role": core_labels["role"],
            "source_session": core_labels["source_session"],
            "derived_from": None,
            "execution_linkable": core_labels["execution_linkable"],
            "last_run_id": run_id,
            "idempotency_key": idempotency_key,
        }
        if existing:
            existing.update(record)
        else:
            entries.append(record)
        atomic_write_json(DOC_REGISTRY_PATH, payload)


def ensure_ticket_entry(
    *,
    ticket_id: str,
    title: str,
    source_doc_ref: str,
    target_refs: list[str],
    notes: str,
    run_id: str,
    idempotency_key: str,
) -> None:
    lock_path = TICKET_REGISTRY_PATH.with_suffix(TICKET_REGISTRY_PATH.suffix + ".lock")
    with file_lock(lock_path):
        payload = locked_load_json(TICKET_REGISTRY_PATH)
        entries = payload.setdefault("entries", [])
        existing = next((row for row in entries if row["ticket_id"] == ticket_id), None)
        record = {
            "ticket_id": ticket_id,
            "title": title,
            "status": "completed",
            "source_doc_ref": source_doc_ref,
            "ticket_class": "structured_doc_routing",
            "target_refs": target_refs,
            "notes": notes,
            "last_run_id": run_id,
            "idempotency_key": idempotency_key,
        }
        if existing:
            existing.update(record)
        else:
            entries.append(record)
        atomic_write_json(TICKET_REGISTRY_PATH, payload)


def append_provenance_link(
    source_doc_ref: str,
    derived_target_ref: str,
    ticket_ref: str,
    relationship: str,
    *,
    run_id: str,
    idempotency_key: str,
) -> None:
    lock_path = PROVENANCE_INDEX_PATH.with_suffix(PROVENANCE_INDEX_PATH.suffix + ".lock")
    with file_lock(lock_path):
        payload = locked_load_json(PROVENANCE_INDEX_PATH)
        links = payload.setdefault("links", [])
        row = {
            "source_doc_ref": source_doc_ref,
            "derived_target_ref": derived_target_ref,
            "ticket_ref": ticket_ref,
            "relationship": relationship,
            "run_id": run_id,
            "idempotency_key": idempotency_key,
        }
        if not any(
            existing.get("idempotency_key") == idempotency_key and existing.get("derived_target_ref") == derived_target_ref
            for existing in links
        ):
            links.append(row)
            atomic_write_json(PROVENANCE_INDEX_PATH, payload)


def run_observer_ingest(doc_path: Path, label: str) -> tuple[str, list[str], list[str], list[str]]:
    cmd = [sys.executable, str(OBSERVER_SCRIPT), "--input", str(doc_path), "--label", label, "--profile", "auto"]
    proc = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True, check=True)
    run_id = proc.stdout.strip().splitlines()[-1].strip()
    generated = [
        f"app/work/observer_ingest_min/generated/source_manifest_{run_id}.json",
        f"app/work/observer_ingest_min/generated/split_units_{run_id}.json",
        f"app/work/observer_ingest_min/generated/processing_trace_{run_id}.json",
        f"app/work/observer_ingest_min/generated/readable_input_board_{run_id}.md",
        f"app/work/observer_ingest_min/generated/operator_summary_{run_id}.md",
        f"app/work/observer_ingest_min/generated/content_role_tags_{run_id}.json",
        f"app/work/observer_ingest_min/generated/line_seed_bundles_{run_id}.json",
        f"app/work/observer_ingest_min/generated/camera_support_bundles_{run_id}.json",
    ]
    commands = [" ".join(cmd)]
    return run_id, generated, commands, proc.stdout.strip().splitlines()


def _record_structured_doc_line_thickening(runtime_root: Path, observer_run_id: str) -> dict:
    source_manifest_path = OBSERVER_OUTPUT_ROOT / f"source_manifest_{observer_run_id}.json"
    split_units_path = OBSERVER_OUTPUT_ROOT / f"split_units_{observer_run_id}.json"
    readable_board_path = OBSERVER_OUTPUT_ROOT / f"readable_input_board_{observer_run_id}.md"
    operator_summary_path = OBSERVER_OUTPUT_ROOT / f"operator_summary_{observer_run_id}.md"
    processing_trace_path = OBSERVER_OUTPUT_ROOT / f"processing_trace_{observer_run_id}.json"

    source_manifest = load_json(source_manifest_path)
    split_units = load_json(split_units_path)
    processing_trace = load_json(processing_trace_path)
    unit = split_units[min(1, len(split_units) - 1)] if split_units else {}
    source_pointer = (
        f"app/work/observer_ingest_min/generated/split_units_{observer_run_id}.json"
        f"#unit_id={unit.get('unit_id', 'unit_001')};start_ref={unit.get('start_ref', '')};end_ref={unit.get('end_ref', '')}"
    )
    evidence = (
        f"structured doc routing produced {source_manifest.get('unit_count', len(split_units))} split units "
        f"for {source_manifest.get('label')}; board={readable_board_path.relative_to(REPO_ROOT)}; "
        f"summary={operator_summary_path.relative_to(REPO_ROOT)}"
    )
    observation = RereadObservation(
        run_id=observer_run_id,
        asset_or_surface=str(operator_summary_path.relative_to(REPO_ROOT)),
        view_type="structured_doc_routing",
        line_name="transition_over_surface",
        evidence=evidence,
        grounding_type="direct",
        support_points=[
            f"split unit {unit.get('unit_id', 'unit_001')}",
            f"split_mode={processing_trace.get('split_mode_used', '')}",
            f"run_id={observer_run_id}",
        ],
        weakness_points=["single grounded structured-doc route only"],
        contradiction_points=[],
        caution_points=["broader validation requires another route"],
        next_probe_surface=str(readable_board_path.relative_to(REPO_ROOT)),
        thickness_before="thin",
        thickness_after="thin",
        observed_at=now_iso(),
        source_kind="trace_log",
        source_path_or_ref=str(source_manifest_path.relative_to(REPO_ROOT)),
        source_run_id_or_event_id=observer_run_id,
        source_pointer=source_pointer,
        evidence_mode="direct_span",
        validation_path_id="structured_doc_routing",
        evidence_origin_kind="derived_report",
        independence_class="self_referential_derived",
    )
    return record_reread_observation(runtime_root, observation)


def write_gmd_native_read(observer_run_id: str, doc_rel: str) -> tuple[Path, dict[str, object]]:
    source_manifest_path = OBSERVER_OUTPUT_ROOT / f"source_manifest_{observer_run_id}.json"
    split_units_path = OBSERVER_OUTPUT_ROOT / f"split_units_{observer_run_id}.json"
    processing_trace_path = OBSERVER_OUTPUT_ROOT / f"processing_trace_{observer_run_id}.json"

    source_manifest = load_json(source_manifest_path)
    split_units = load_json(split_units_path)
    processing_trace = load_json(processing_trace_path)
    payload = build_gmd_native_read(
        doc_ref=doc_rel,
        source_manifest=source_manifest,
        split_units=split_units,
        processing_trace=processing_trace,
    )
    output_path = OBSERVER_OUTPUT_ROOT / f"gmd_native_read_{observer_run_id}.json"
    write_json(output_path, payload)
    return output_path, payload


def write_receipt(
    *,
    receipt_path: Path,
    doc_id: str,
    doc_path: Path,
    raw_markers: dict[str, str],
    normalized: dict[str, str],
    core_labels: dict[str, object],
    label_packet_ref: str,
    ticket_id: str,
    run_id: str,
    idempotency_key: str,
    events: list[dict],
    generated_files: list[str],
    command_lines: list[str],
    gmd_payload: dict[str, object] | None = None,
) -> None:
    lines = [
        f"# operation receipt / {doc_id}",
        "",
        "## 1. Source",
        f"- doc_id: `{doc_id}`",
        f"- source_path: `{doc_path}`",
        "",
        "## 2. Raw Routing Markers",
        f"- DOCROLE: `{raw_markers.get('DOCROLE', '')}`",
        f"- RUNMODE: `{raw_markers.get('RUNMODE', '')}`",
        f"- PRIORITY: `{raw_markers.get('PRIORITY', '')}`",
        "",
        "## 3. Normalized Routing",
        f"- docrole: `{normalized['docrole']}`",
        f"- runmode: `{normalized['runmode']}`",
        f"- priority: `{normalized['priority']}`",
        "",
        "## 4. Registration",
        f"- input_class: `{core_labels['input_class']}`",
        f"- processing_profile: `{core_labels['processing_profile']}`",
        f"- material_grade: `{core_labels['material_grade']}`",
        f"- role: `{core_labels['role']}`",
        f"- execution_linkable: `{str(core_labels['execution_linkable']).lower()}`",
        f"- label_packet: `{label_packet_ref}`",
        "",
        "## 5. Ticket",
        f"- ticket_id: `{ticket_id or 'not_created'}`",
        f"- ticket_created: `{'yes' if ticket_id else 'no'}`",
        "",
        "## 5A. Run Identity",
        f"- run_id: `{run_id}`",
        f"- idempotency_key: `{idempotency_key}`",
        "",
        "## 6. Events",
    ]
    for event in events:
        lines.append(f"- `{event['event_type']}` -> `{event['target_ref']}` [{event['event_id']}]")
    lines.extend([
        "",
        "## 7. Generated / Updated Files",
    ])
    for path in generated_files:
        lines.append(f"- `{path}`")
    if gmd_payload:
        native = gmd_payload.get("gmd_native_read", {})
        commentary = gmd_payload.get("semantic_commentary", {})
        material = gmd_payload.get("translation_ready_material", {})
        lines.extend([
            "",
            "## 7A. GMD Native Read",
            f"- segmentation_basis: `{json.dumps(native.get('segmentation_basis', {}), ensure_ascii=False)}`",
            f"- ordering_basis: `{native.get('ordering_basis', 'unknown')}`",
            f"- grouping_logic: `{native.get('grouping_logic', 'unknown')}`",
            f"- role_hint_count: `{len(native.get('unit_role_hints', []))}`",
            f"- relation_clue_count: `{len(native.get('relation_clues', []))}`",
            f"- unresolved_count: `{len(native.get('unresolved_structure', []))}`",
            "",
            "## 7B. Semantic Commentary",
            f"- source_summary: `{commentary.get('source_summary', '')}`",
            f"- structure_summary: `{commentary.get('structure_summary', '')}`",
            f"- why_this_structure_matters: `{commentary.get('why_this_structure_matters', '')}`",
            "",
            "## 7C. Translation-Ready Material",
            f"- source_block: `{json.dumps(material.get('source_block', {}), ensure_ascii=False)}`",
            f"- provisional_line_block_count: `{len(material.get('provisional_line_block', []))}`",
            f"- uncertainty_block_count: `{len(material.get('uncertainty_block', []))}`",
        ])
    lines.extend([
        "",
        "## 8. Commands",
    ])
    for command in command_lines:
        lines.append(f"- `{command}`")
    lines.extend([
        "",
        "## 9. Final Status",
        f"- processed_at: `{now_iso()}`",
        f"- summary: `document routed, registered, recorded, and receipt written`",
    ])
    atomic_write_text(receipt_path, "\n".join(lines) + "\n")


def update_operation_board(
    doc_id: str,
    receipt_ref: str,
    ticket_id: str,
    generated_files: list[str],
    commands_ref: str,
    run_id: str,
    *,
    processed_at: str,
    routing_summary: dict[str, str],
    execution_note: str,
) -> tuple[Path, Path]:
    recent_events = []
    if ENGINE_LEDGER.exists():
        rows, _recovered = load_jsonl_with_tail_recovery(ENGINE_LEDGER)
        recent_events = rows[-12:]
    per_run_board_ref = f"runtime/views/operation_board_{run_id}.md"
    per_run_commands_ref = f"runtime/commands/structured_doc_routing_commands_{run_id}.md"
    provenance_compacted_ref = "runtime/views/provenance_compacted_latest.md"
    latest_lines = [
        "# operation_board_latest",
        "",
        "## latest run",
        f"- run_id: `{run_id}`",
        f"- timestamp: `{processed_at}`",
        "",
        "## pointers",
        f"- receipt: `{receipt_ref}`",
        f"- board (per-run): `{per_run_board_ref}`",
        f"- commands (per-run): `{per_run_commands_ref}`",
        f"- latest commands pointer: `{commands_ref}`",
        f"- provenance compacted: `{provenance_compacted_ref}`",
        "",
        "## summary",
        f"- doc_id: `{doc_id}`",
        f"- ticket: `{ticket_id or 'not_created'}`",
        f"- routing_mode: `{routing_summary['docrole']} / {routing_summary['runmode']} / {routing_summary['priority']}`",
        f"- execution: `{execution_note}`",
        "",
        "## note",
        "- This is a pointer surface. See per-run artifacts for full details.",
    ]
    per_run_lines = [
        f"# operation_board / {run_id}",
        "",
        "## 1. Latest Structured Docs",
        f"- `{doc_id}`",
        "",
        "## 2. Latest Tickets",
        f"- `{ticket_id or 'not_created'}`",
        "",
        "## 3. Latest Outputs",
    ]
    for path in generated_files:
        per_run_lines.append(f"- `{path}`")
    per_run_lines.extend([
        "",
        "## 4. Latest Events",
    ])
    for event in reversed(recent_events[-8:]):
        per_run_lines.append(f"- `{event['event_type']}` / `{event['target_ref']}` / `{event['timestamp']}`")
    per_run_lines.extend([
        "",
        "## 5. Latest Receipts",
        f"- `{receipt_ref}`",
        "",
        "## 6. Latest Commands",
        f"- `{commands_ref}`",
        "",
        "## 6A. Latest Run",
        f"- `{run_id}`",
        "",
        "## 7. Current Note / Caution",
        "- `RUNMODE` missing documents should still default to `ingest_only`.",
        "- This board is a seed surface, not a live dashboard.",
    ])
    board_path = VIEWS_ROOT / "operation_board_latest.md"
    per_run_board_path = VIEWS_ROOT / f"operation_board_{run_id}.md"
    board_path.parent.mkdir(parents=True, exist_ok=True)
    latest_board_text = "\n".join(latest_lines) + "\n"
    per_run_board_text = "\n".join(per_run_lines) + "\n"
    atomic_write_text(board_path, latest_board_text)
    atomic_write_text(per_run_board_path, per_run_board_text)
    return board_path, per_run_board_path


def ensure_commands_doc(latest_command: str, run_id: str, *, receipt_ref: str, processed_at: str) -> tuple[Path, Path]:
    per_run_ref = f"runtime/commands/structured_doc_routing_commands_{run_id}.md"
    latest_lines = [
        "# structured_doc_routing_commands_v1",
        "",
        "## latest run",
        f"- run_id: `{run_id}`",
        f"- timestamp: `{processed_at}`",
        "",
        "## command",
        f"- process_doc: `{latest_command}`",
        "",
        "## pointers",
        f"- receipt: `{receipt_ref}`",
        "- latest board: `runtime/views/operation_board_latest.md`",
        f"- per-run board: `runtime/views/operation_board_{run_id}.md`",
        f"- per-run commands: `{per_run_ref}`",
        "",
        "## note",
        "- This is a pointer surface. See the per-run commands artifact for detailed command context.",
    ]
    per_run_lines = [
        "# structured_doc_routing_commands_v1",
        "",
        "## 1. Document Processing Command",
        f"- `{latest_command}`",
        "",
        "## 1A. Run Identity",
        f"- `{run_id}`",
        "",
        "## 2. Receipt Check",
        "- `ls runtime/receipts`",
        "- `cat runtime/receipts/<doc_id>_operation_receipt.md`",
        "",
        "## 3. Board Check",
        "- `cat runtime/views/operation_board_latest.md`",
        "",
        "## 4. Recent Events",
        "- `tail -n 20 runtime/events/engine_event_ledger.jsonl`",
        "",
        "## 5. Manifest Checks",
        "- `cat runtime/manifests/structured_internal_docs_registry_v1.json`",
        "- `cat runtime/manifests/ticket_registry_v1.json`",
        "- `cat runtime/manifests/provenance_link_index_v1.json`",
    ]
    path = COMMANDS_ROOT / "structured_doc_routing_commands_v1.md"
    per_run_path = COMMANDS_ROOT / f"structured_doc_routing_commands_{run_id}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    atomic_write_text(path, "\n".join(latest_lines) + "\n")
    atomic_write_text(per_run_path, "\n".join(per_run_lines) + "\n")
    return path, per_run_path


def build_run_id(doc_rel: str, text: str) -> str:
    doc_hash = hashlib.sha256(f"{doc_rel}::{text}".encode("utf-8")).hexdigest()[:8]
    unique_suffix = uuid4().hex[:6]
    return f"run_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}_{doc_hash}_{unique_suffix}"


def recover_runtime_ledgers_if_needed(actor: str) -> list[dict]:
    recovery_events: list[dict] = []
    recovery_targets = [
        (ENGINE_LEDGER, "runtime"),
        (FOLDER_ACTIVITY_ROOT / "runtime.folder_activity_log.jsonl", "runtime"),
        (FOLDER_ACTIVITY_ROOT / "app.folder_activity_log.jsonl", "app"),
    ]
    for path, folder_ref in recovery_targets:
        recovered = recover_jsonl_tail(path)
        if recovered:
            recovery_events.append(
                append_event(
                    event_type="malformed_tail_recovered",
                    target_ref=str(path.relative_to(REPO_ROOT)),
                    source_doc_ref="",
                    ticket_ref="",
                    actor=actor,
                    status="recovered",
                    notes="Recovered valid JSONL rows after malformed tail detection.",
                    folder_ref=folder_ref,
                )
            )
    return recovery_events


def write_origin_map_seed(doc_id: str, doc_text: str) -> tuple[Path, dict[str, object]]:
    payload = build_origin_map(doc_id, doc_text, "receipt_seed")
    path = ORIGIN_MAPS_ROOT / f"{doc_id}_receipt_seed_origin_map.json"
    write_json(path, payload)
    return path, payload


def sync_folder_status_surfaces(doc_rel: str, generated_files: list[str]) -> list[str]:
    sync_inputs = [doc_rel, *generated_files]
    result = sync_folder_status(
        REPO_ROOT,
        sync_inputs,
        include_ancestors=True,
        child_depth=0,
        actor="codex",
        source="structured_doc_routing",
    )
    return [path for path in [*result["inventory_files"], *result["status_files"]] if path not in generated_files]


def main() -> None:
    args = parse_args()
    doc_path = resolve_doc_path(args.doc)
    doc_rel = str(doc_path.relative_to(REPO_ROOT))
    text = doc_path.read_text(encoding="utf-8")
    recovery_events = recover_runtime_ledgers_if_needed(args.actor)
    raw_markers = parse_markers(text)
    alias_map = load_json(ALIAS_MAP_PATH)
    normalized = normalize_external_labels(raw_markers, alias_map)

    doc_id = f"doc_{slugify(doc_path.stem)}"
    ticket_id = ""
    events: list[dict] = list(recovery_events)
    generated_files: list[str] = []
    doc_text = text
    routing_run_id = build_run_id(doc_rel, doc_text)
    idempotency_key = make_idempotency_key(doc_rel, normalized["runmode"], hashlib.sha256(doc_text.encode("utf-8")).hexdigest())
    core_labels = build_core_intake_labels(normalized, source_session=args.source_session)
    label_packet = build_label_packet(
        doc_id=doc_id,
        doc_ref=doc_rel,
        external_labels=normalized,
        core_labels=core_labels,
    )
    label_packet_path = LABEL_PACKET_ROOT / f"{doc_id}_label_packet.json"
    write_json(label_packet_path, label_packet)
    label_packet_rel = str(label_packet_path.relative_to(REPO_ROOT))
    generated_files.append(label_packet_rel)

    ensure_doc_registry_entry(
        doc_id=doc_id,
        doc_ref=doc_rel,
        core_labels=core_labels,
        idempotency_key=idempotency_key,
        run_id=routing_run_id,
    )
    append_provenance_link(doc_rel, label_packet_rel, "", "generated_core_label_packet", run_id=routing_run_id, idempotency_key=make_idempotency_key(idempotency_key, label_packet_rel))
    append_provenance_link(
        doc_rel,
        str(DOC_REGISTRY_PATH.relative_to(REPO_ROOT)),
        "",
        "registered_in_structured_doc_registry",
        run_id=routing_run_id,
        idempotency_key=make_idempotency_key(idempotency_key, str(DOC_REGISTRY_PATH.relative_to(REPO_ROOT))),
    )
    events.append(
        append_event(
            event_type="file_created",
            target_ref=label_packet_rel,
            source_doc_ref=doc_rel,
            ticket_ref="",
            actor=args.actor,
            status="recorded",
            notes="Generated core input-layer label packet.",
            folder_ref="runtime",
            derived_from=doc_rel,
        )
    )
    events.append(
        append_event(
            event_type="doc_registered",
            target_ref=doc_rel,
            source_doc_ref=doc_rel,
            ticket_ref="",
            actor=args.actor,
            status="recorded",
            notes="Registered routed document as structured internal material.",
            folder_ref="runtime",
        )
    )
    events.append(
        append_event(
            event_type="routing_normalized",
            target_ref=doc_rel,
            source_doc_ref=doc_rel,
            ticket_ref="",
            actor=args.actor,
            status="recorded",
            notes=f"Normalized DOCROLE={normalized['docrole']}, RUNMODE={normalized['runmode']}, PRIORITY={normalized['priority']}.",
            folder_ref="runtime",
        )
    )

    if normalized["runmode"] in {"ingest_then_execute", "execute_only"}:
        ticket_id = f"tkt_process_{slugify(doc_path.stem)}"
        ensure_ticket_entry(
            ticket_id=ticket_id,
            title=f"process structured doc {doc_path.stem}",
            source_doc_ref=doc_rel,
            target_refs=[doc_rel],
            notes="Generated by structured doc routing wrapper.",
            run_id=routing_run_id,
            idempotency_key=idempotency_key,
        )
        events.append(
            append_event(
                event_type="ticket_created",
                target_ref=str(TICKET_REGISTRY_PATH.relative_to(REPO_ROOT)),
                source_doc_ref=doc_rel,
                ticket_ref=ticket_id,
                actor=args.actor,
                status="completed",
                notes="Created structured document processing ticket.",
                folder_ref="runtime",
            )
        )
        events.append(
            append_event(
                event_type="execution_started",
                target_ref=doc_rel,
                source_doc_ref=doc_rel,
                ticket_ref=ticket_id,
                actor=args.actor,
                status="started",
                notes="Started execution-coupled structured document processing.",
                folder_ref="app",
            )
        )

    commands_used = [f"{sys.executable} scripts/process_structured_doc_with_routing.py --doc {doc_rel}"]
    gmd_native_read_payload: dict[str, object] | None = None
    if args.record_line_thickening:
        commands_used[0] += " --record-line-thickening"
    if normalized["runmode"] != "reference_only":
        observer_run_id, ingest_outputs, ingest_commands, _stdout_lines = run_observer_ingest(doc_path, doc_path.stem)
        generated_files.extend(ingest_outputs)
        commands_used.extend(ingest_commands)
        gmd_native_read_path, gmd_native_read_payload = write_gmd_native_read(observer_run_id, doc_rel)
        gmd_native_read_rel = str(gmd_native_read_path.relative_to(REPO_ROOT))
        generated_files.append(gmd_native_read_rel)
        for output in ingest_outputs:
            append_provenance_link(
                doc_rel,
                output,
                ticket_id,
                "generated_by_structured_doc_routing",
                run_id=routing_run_id,
                idempotency_key=make_idempotency_key(idempotency_key, output),
            )
        append_provenance_link(
            doc_rel,
            gmd_native_read_rel,
            ticket_id,
            "derived_gmd_native_read",
            run_id=routing_run_id,
            idempotency_key=make_idempotency_key(idempotency_key, gmd_native_read_rel),
        )
        events.append(
            append_event(
                event_type="output_generated",
                target_ref=f"app/work/observer_ingest_min/generated/operator_summary_{observer_run_id}.md",
                source_doc_ref=doc_rel,
                ticket_ref=ticket_id,
                actor=args.actor,
                status="recorded",
                notes="Generated observer ingest outputs through structured document routing.",
                folder_ref="app",
                output_ref=f"app/work/observer_ingest_min/generated/source_manifest_{observer_run_id}.json",
            )
        )
        events.append(
            append_event(
                event_type="gmd_native_read_written",
                target_ref=gmd_native_read_rel,
                source_doc_ref=doc_rel,
                ticket_ref=ticket_id,
                actor=args.actor,
                status="recorded",
                notes="Preserved segmentation basis, ordering basis, role hints, relation clues, and uncertainty for later line translation and internal recall.",
                folder_ref="app",
                output_ref=gmd_native_read_rel,
                derived_from=f"app/work/observer_ingest_min/generated/split_units_{observer_run_id}.json",
            )
        )
        split_units_path = OBSERVER_OUTPUT_ROOT / f"split_units_{observer_run_id}.json"
        multi_lens_view_path = MULTI_LENS_VIEW_ROOT / f"{doc_id}_multi_lens_readout_{observer_run_id}.json"
        multi_lens_supervisor_view_path = MULTI_LENS_VIEW_ROOT / f"{doc_id}_multi_lens_supervisor_surface_{observer_run_id}.json"
        multi_lens_payload = build_multi_lens_observation_payload(
            split_units_path=split_units_path,
            source_id=doc_rel,
            registry_path=REPO_ROOT / "runtime" / "manifests" / "line_registry.json",
            observer_run_id=observer_run_id,
        )
        write_json(multi_lens_view_path, multi_lens_payload)
        multi_lens_view_rel = str(multi_lens_view_path.relative_to(REPO_ROOT))
        generated_files.append(multi_lens_view_rel)
        multi_lens_supervisor_payload = build_multi_lens_supervisor_surface(
            multi_lens_payload,
            observation_artifact_ref=multi_lens_view_rel,
        )
        write_json(multi_lens_supervisor_view_path, multi_lens_supervisor_payload)
        multi_lens_supervisor_view_rel = str(multi_lens_supervisor_view_path.relative_to(REPO_ROOT))
        generated_files.append(multi_lens_supervisor_view_rel)
        append_provenance_link(
            doc_rel,
            multi_lens_view_rel,
            ticket_id,
            "generated_multi_lens_observation_readout",
            run_id=routing_run_id,
            idempotency_key=make_idempotency_key(idempotency_key, multi_lens_view_rel),
        )
        append_provenance_link(
            doc_rel,
            multi_lens_supervisor_view_rel,
            ticket_id,
            "generated_multi_lens_supervisor_surface",
            run_id=routing_run_id,
            idempotency_key=make_idempotency_key(idempotency_key, multi_lens_supervisor_view_rel),
        )
        events.append(
            append_event(
                event_type="output_generated",
                target_ref=multi_lens_view_rel,
                source_doc_ref=doc_rel,
                ticket_ref=ticket_id,
                actor=args.actor,
                status="recorded",
                notes="Generated multi-lens observation readout after context-linked segmentation; runtime stops at readout handoff boundary.",
                folder_ref="runtime",
                output_ref=multi_lens_view_rel,
            )
        )
        events.append(
            append_event(
                event_type="output_generated",
                target_ref=multi_lens_supervisor_view_rel,
                source_doc_ref=doc_rel,
                ticket_ref=ticket_id,
                actor=args.actor,
                status="recorded",
                notes="Generated supervisor-facing multi-lens surfaced view; raw output remains secondary reference only.",
                folder_ref="runtime",
                output_ref=multi_lens_supervisor_view_rel,
            )
        )
        if args.record_line_thickening:
            _record_structured_doc_line_thickening(REPO_ROOT / "runtime", observer_run_id)

    origin_map_path, _origin_payload = write_origin_map_seed(doc_id, doc_text)
    origin_map_rel = str(origin_map_path.relative_to(REPO_ROOT))
    generated_files.append(origin_map_rel)
    append_provenance_link(
        doc_rel,
        origin_map_rel,
        ticket_id,
        "generated_origin_map_seed",
        run_id=routing_run_id,
        idempotency_key=make_idempotency_key(idempotency_key, origin_map_rel),
    )
    events.append(
        append_event(
            event_type="file_created",
            target_ref=origin_map_rel,
            source_doc_ref=doc_rel,
            ticket_ref=ticket_id,
            actor=args.actor,
            status="recorded",
            notes="Generated minimal origin map seed for source return.",
            folder_ref="runtime",
            derived_from=doc_rel,
        )
    )

    processed_at = now_iso()
    commands_path, per_run_commands_path = ensure_commands_doc(
        commands_used[0],
        routing_run_id,
        receipt_ref=str(RECEIPTS_ROOT / f"{doc_id}_operation_receipt.md").replace(str(REPO_ROOT) + "/", ""),
        processed_at=processed_at,
    )
    generated_files.append(str(commands_path.relative_to(REPO_ROOT)))
    generated_files.append(str(per_run_commands_path.relative_to(REPO_ROOT)))

    receipt_path = RECEIPTS_ROOT / f"{doc_id}_operation_receipt.md"
    write_receipt(
        receipt_path=receipt_path,
        doc_id=doc_id,
        doc_path=doc_path,
        raw_markers=raw_markers,
        normalized=normalized,
        core_labels=core_labels,
        label_packet_ref=label_packet_rel,
        ticket_id=ticket_id,
        run_id=routing_run_id,
        idempotency_key=idempotency_key,
        events=events,
        generated_files=generated_files,
        command_lines=commands_used,
        gmd_payload=gmd_native_read_payload,
    )
    generated_files.append(str(receipt_path.relative_to(REPO_ROOT)))
    events.append(
        append_event(
            event_type="receipt_written",
            target_ref=str(receipt_path.relative_to(REPO_ROOT)),
            source_doc_ref=doc_rel,
            ticket_ref=ticket_id,
            actor=args.actor,
            status="recorded",
            notes="Wrote single operation receipt for structured document processing.",
            folder_ref="runtime",
        )
    )

    execution_note = "action linked" if normalized["runmode"] in {"ingest_then_execute", "execute_only"} else "none (baseline asset)"
    board_path, per_run_board_path = update_operation_board(
        doc_id=doc_id,
        receipt_ref=str(receipt_path.relative_to(REPO_ROOT)),
        ticket_id=ticket_id,
        generated_files=generated_files,
        commands_ref=str(commands_path.relative_to(REPO_ROOT)),
        run_id=routing_run_id,
        processed_at=processed_at,
        routing_summary=normalized,
        execution_note=execution_note,
    )
    generated_files.append(str(board_path.relative_to(REPO_ROOT)))
    generated_files.append(str(per_run_board_path.relative_to(REPO_ROOT)))
    events.append(
        append_event(
            event_type="board_updated",
            target_ref=str(board_path.relative_to(REPO_ROOT)),
            source_doc_ref=doc_rel,
            ticket_ref=ticket_id,
            actor=args.actor,
            status="recorded",
            notes="Updated latest operation board for structured document routing.",
            folder_ref="runtime",
        )
    )

    synced_status_files = sync_folder_status_surfaces(doc_rel, generated_files)
    generated_files.extend(path for path in synced_status_files if path not in generated_files)

    print(
        json.dumps(
            {
                "doc_id": doc_id,
                "doc_ref": doc_rel,
                "normalized": normalized,
                "core_labels": core_labels,
                "label_packet_ref": label_packet_rel,
                "ticket_id": ticket_id or None,
                "run_id": routing_run_id,
                "idempotency_key": idempotency_key,
                "generated_files": generated_files,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
