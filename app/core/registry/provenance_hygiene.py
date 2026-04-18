from __future__ import annotations

import json
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from app.core.registry.atomic_io import atomic_write_json, atomic_write_text


SAFE_REPEAT_RELATIONSHIPS = {
    "generated_core_label_packet",
    "registered_in_structured_doc_registry",
    "generated_origin_map_seed",
}


@dataclass
class CandidateGroup:
    group_key: str
    classification: str
    safety: str
    source_doc_ref: str
    relationship: str
    derived_target_ref: str
    row_count: int
    unique_run_ids: list[str]
    unique_idempotency_keys: list[str]
    sample_ticket_refs: list[str]
    row_indices: list[int]
    reason: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "group_key": self.group_key,
            "classification": self.classification,
            "safety": self.safety,
            "source_doc_ref": self.source_doc_ref,
            "relationship": self.relationship,
            "derived_target_ref": self.derived_target_ref,
            "row_count": self.row_count,
            "unique_run_ids": self.unique_run_ids,
            "unique_idempotency_keys": self.unique_idempotency_keys,
            "sample_ticket_refs": self.sample_ticket_refs,
            "row_indices": self.row_indices,
            "reason": self.reason,
        }


def load_provenance_links(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload.get("links", [])


def scan_provenance_accumulation(links: list[dict[str, Any]]) -> dict[str, Any]:
    relationship_counter = Counter(link.get("relationship", "") for link in links)
    source_counter = Counter(link.get("source_doc_ref", "") for link in links)
    run_id_presence = Counter("has_run_id" if link.get("run_id") else "legacy_or_missing_run_id" for link in links)
    idempotency_presence = Counter(
        "has_idempotency_key" if link.get("idempotency_key") else "legacy_or_missing_idempotency_key" for link in links
    )
    return {
        "total_rows": len(links),
        "relationship_counts": dict(relationship_counter.most_common()),
        "source_doc_counts": dict(source_counter.most_common()),
        "run_id_presence": dict(run_id_presence),
        "idempotency_key_presence": dict(idempotency_presence),
    }


def group_duplicate_candidates(links: list[dict[str, Any]]) -> list[CandidateGroup]:
    exact_counter: Counter[tuple[tuple[str, Any], ...]] = Counter()
    exact_rows: dict[tuple[tuple[str, Any], ...], list[int]] = defaultdict(list)
    for idx, row in enumerate(links):
        frozen = tuple(sorted(row.items()))
        exact_counter[frozen] += 1
        exact_rows[frozen].append(idx)

    candidates: list[CandidateGroup] = []
    for frozen, count in exact_counter.items():
        if count <= 1:
            continue
        row = dict(frozen)
        candidates.append(
            CandidateGroup(
                group_key=f"exact::{row.get('source_doc_ref','')}::{row.get('derived_target_ref','')}::{row.get('relationship','')}",
                classification="exact_duplicate",
                safety="safe",
                source_doc_ref=row.get("source_doc_ref", ""),
                relationship=row.get("relationship", ""),
                derived_target_ref=row.get("derived_target_ref", ""),
                row_count=count,
                unique_run_ids=sorted({row.get("run_id", "")}),
                unique_idempotency_keys=sorted({row.get("idempotency_key", "")}),
                sample_ticket_refs=sorted({row.get("ticket_ref", "")}),
                row_indices=exact_rows[frozen],
                reason="All stored fields are equal.",
            )
        )

    grouped: dict[tuple[str, str, str], list[tuple[int, dict[str, Any]]]] = defaultdict(list)
    for idx, row in enumerate(links):
        key = (row.get("source_doc_ref", ""), row.get("derived_target_ref", ""), row.get("relationship", ""))
        grouped[key].append((idx, row))

    for (source_doc_ref, derived_target_ref, relationship), rows in grouped.items():
        if len(rows) <= 1:
            continue
        unique_run_ids = sorted({row.get("run_id", "") for _, row in rows})
        unique_idempotency_keys = sorted({row.get("idempotency_key", "") for _, row in rows})
        sample_ticket_refs = sorted({row.get("ticket_ref", "") for _, row in rows})
        row_indices = [idx for idx, _ in rows]

        if relationship in SAFE_REPEAT_RELATIONSHIPS:
            classification = "same_idempotency_context_repeated_append"
            safety = "safe"
            reason = "Stable registry/provenance relation repeated across re-ingest runs for the same logical target."
        elif "receipt_seed_origin_map" in derived_target_ref:
            classification = "same_receipt_seed_lineage_duplicate"
            safety = "safe"
            reason = "Receipt-seed origin map lineage points to the same logical target repeatedly."
        else:
            classification = "same_source_same_target_different_run_duplicate"
            safety = "manual_review"
            reason = "Same source/target/relation repeated, but relation may represent meaningful repeated operation history."

        candidates.append(
            CandidateGroup(
                group_key=f"group::{source_doc_ref}::{derived_target_ref}::{relationship}",
                classification=classification,
                safety=safety,
                source_doc_ref=source_doc_ref,
                relationship=relationship,
                derived_target_ref=derived_target_ref,
                row_count=len(rows),
                unique_run_ids=unique_run_ids,
                unique_idempotency_keys=unique_idempotency_keys,
                sample_ticket_refs=sample_ticket_refs,
                row_indices=row_indices,
                reason=reason,
            )
        )

    per_doc_rows: dict[str, list[tuple[int, dict[str, Any]]]] = defaultdict(list)
    for idx, row in enumerate(links):
        per_doc_rows[row.get("source_doc_ref", "")].append((idx, row))
    for source_doc_ref, rows in per_doc_rows.items():
        if len(rows) <= 6:
            continue
        run_ids = sorted({row.get("run_id", "") for _, row in rows})
        if len(run_ids) <= 1:
            continue
        candidates.append(
            CandidateGroup(
                group_key=f"reingest::{source_doc_ref}",
                classification="same_document_reingest_accumulation",
                safety="manual_review",
                source_doc_ref=source_doc_ref,
                relationship="*",
                derived_target_ref="*",
                row_count=len(rows),
                unique_run_ids=run_ids,
                unique_idempotency_keys=sorted({row.get("idempotency_key", "") for _, row in rows}),
                sample_ticket_refs=sorted({row.get("ticket_ref", "") for _, row in rows}),
                row_indices=[idx for idx, _ in rows],
                reason="The same document has multiple re-ingest runs; compactable reading is useful, but raw rows remain audit-relevant.",
            )
        )
    return sorted(candidates, key=lambda row: (-row.row_count, row.classification, row.group_key))


def classify_compaction_safety(candidates: list[CandidateGroup]) -> dict[str, Any]:
    by_safety = Counter(candidate.safety for candidate in candidates)
    by_classification = Counter(candidate.classification for candidate in candidates)
    return {
        "safe_group_count": by_safety.get("safe", 0),
        "manual_review_group_count": by_safety.get("manual_review", 0),
        "unsafe_group_count": by_safety.get("unsafe", 0),
        "classification_counts": dict(by_classification),
    }


def build_compaction_preview(links: list[dict[str, Any]]) -> dict[str, Any]:
    scan = scan_provenance_accumulation(links)
    candidates = group_duplicate_candidates(links)
    safety = classify_compaction_safety(candidates)
    safe_rows = sum(candidate.row_count for candidate in candidates if candidate.safety == "safe")
    manual_rows = sum(candidate.row_count for candidate in candidates if candidate.safety == "manual_review")
    return {
        "preview_name": "provenance_compaction_preview_v1",
        "scan_summary": scan,
        "candidate_summary": {
            **safety,
            "safe_candidate_rows": safe_rows,
            "manual_review_candidate_rows": manual_rows,
        },
        "candidate_groups": [candidate.as_dict() for candidate in candidates],
    }


def write_compaction_preview(preview: dict[str, Any], json_path: Path, md_path: Path, source_path: Path) -> None:
    atomic_write_json(json_path, preview)
    lines = [
        "# provenance_compacted_latest",
        "",
        "## 1. Source",
        f"- raw_provenance_path: `{source_path}`",
        f"- preview_manifest: `{json_path}`",
        "",
        "## 2. Totals",
        f"- total_rows: `{preview['scan_summary']['total_rows']}`",
        f"- safe_group_count: `{preview['candidate_summary']['safe_group_count']}`",
        f"- manual_review_group_count: `{preview['candidate_summary']['manual_review_group_count']}`",
        f"- safe_candidate_rows: `{preview['candidate_summary']['safe_candidate_rows']}`",
        f"- manual_review_candidate_rows: `{preview['candidate_summary']['manual_review_candidate_rows']}`",
        "",
        "## 3. Classification Counts",
    ]
    for key, value in preview["candidate_summary"]["classification_counts"].items():
        lines.append(f"- `{key}`: `{value}`")
    lines.extend([
        "",
        "## 4. Representative Groups",
    ])
    for group in preview["candidate_groups"][:10]:
        lines.append(
            f"- `{group['classification']}` / `{group['safety']}` / `{group['source_doc_ref']}` / "
            f"`{group['relationship']}` / rows=`{group['row_count']}` / runs=`{len(group['unique_run_ids'])}`"
        )
    lines.extend([
        "",
        "## 5. Raw Preservation Rule",
        "- This compacted surface does not replace the raw provenance index.",
        "- Any later apply step must preserve backup/snapshot and emit a summary.",
    ])
    atomic_write_text(md_path, "\n".join(lines) + "\n")


def apply_bounded_compaction(preview: dict[str, Any], source_path: Path, output_root: Path) -> dict[str, Any]:
    output_root.mkdir(parents=True, exist_ok=True)
    raw_payload = json.loads(source_path.read_text(encoding="utf-8"))
    raw_links = raw_payload.get("links", [])
    keep_indices = set(range(len(raw_links)))
    compacted_groups = []
    for group in preview["candidate_groups"]:
        if group["safety"] != "safe":
            continue
        row_indices = group["row_indices"]
        if len(row_indices) <= 1:
            continue
        representative_index = max(row_indices)
        for idx in row_indices:
            if idx != representative_index:
                keep_indices.discard(idx)
        compacted_groups.append(
            {
                "group_key": group["group_key"],
                "classification": group["classification"],
                "preserved_index": representative_index,
                "compacted_indices": sorted(idx for idx in row_indices if idx != representative_index),
            }
        )
    compacted_links = [row for idx, row in enumerate(raw_links) if idx in keep_indices]
    result = {
        "compaction_name": "provenance_bounded_compaction_v1",
        "source_path": str(source_path),
        "raw_row_count": len(raw_links),
        "compacted_row_count": len(compacted_links),
        "compacted_groups": compacted_groups,
    }
    atomic_write_json(output_root / "provenance_compaction_apply_latest.json", result)
    atomic_write_json(output_root / "provenance_link_index_compacted_v1.json", {"index_name": "provenance_link_index_compacted_v1", "links": compacted_links})
    return result
