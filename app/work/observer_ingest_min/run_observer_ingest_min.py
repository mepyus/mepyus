from __future__ import annotations

import argparse
from datetime import datetime
import json
import re
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.runtime.lower_support_layers import (
    build_camera_support_bundles_for_split_units,
    build_content_role_tags_for_split_units,
    build_line_seed_bundles_for_split_units,
)
OUTPUT_ROOT = REPO_ROOT / "app" / "work" / "observer_ingest_min" / "generated"

TIMESTAMP_LINE_RE = re.compile(
    r"^\s*(?:\[\d{1,2}:\d{2}(?::\d{2})?\]|\d{1,2}:\d{2}(?::\d{2})?)\b"
)
TIMESTAMP_ANY_RE = re.compile(r"(?:\[\d{1,2}:\d{2}(?::\d{2})?\]|\b\d{1,2}:\d{2}(?::\d{2})?\b)")


def slugify(value: str) -> str:
    lowered = value.strip().lower()
    cleaned = re.sub(r"[^a-z0-9_-]+", "_", lowered)
    return cleaned.strip("_") or "input"


def load_single_input(path: str, label: str | None) -> dict:
    source_path = Path(path)
    if not source_path.is_absolute():
        source_path = (REPO_ROOT / source_path).resolve()
    if not source_path.exists():
        raise FileNotFoundError(f"input not found: {source_path}")
    return {
        "input_id": slugify(label or source_path.stem),
        "source_path": str(source_path),
        "label": label or source_path.stem,
        "input_kind": "mixed",
        "split_mode": "auto",
        "note": "direct mode input",
    }


def load_registry(path: str) -> list[dict]:
    registry_path = Path(path)
    if not registry_path.is_absolute():
        registry_path = (REPO_ROOT / registry_path).resolve()
    rows = json.loads(registry_path.read_text(encoding="utf-8"))
    normalized = []
    for row in rows:
        source_path = Path(row["source_path"])
        if not source_path.is_absolute():
            source_path = (registry_path.parent / source_path).resolve()
            if not source_path.exists():
                source_path = (REPO_ROOT / row["source_path"]).resolve()
        normalized_row = dict(row)
        normalized_row["source_path"] = str(source_path)
        normalized.append(normalized_row)
    return normalized


def detect_profile(text: str, input_kind: str | None) -> str:
    if input_kind and input_kind != "mixed":
        return input_kind
    if TIMESTAMP_ANY_RE.search(text):
        return "transcript"
    if re.search(r"^\s*#{1,3}\s+", text, re.MULTILINE):
        return "note"
    if len(text.splitlines()) > 40:
        return "article"
    return "mixed"


def detect_split_mode(text: str, requested: str, detected_profile: str) -> str:
    if requested != "auto":
        return requested
    if TIMESTAMP_ANY_RE.search(text):
        return "timestamp"
    if re.search(r"^\s*#{1,3}\s+", text, re.MULTILINE):
        return "heading"
    return "paragraph"


def split_by_timestamp(lines: list[str]) -> list[dict]:
    segments: list[dict] = []
    current_lines: list[str] = []
    current_refs: list[int] = []
    current_marker = ""
    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not stripped:
            continue
        has_timestamp = bool(TIMESTAMP_LINE_RE.match(stripped)) or (bool(TIMESTAMP_ANY_RE.search(stripped)) and len(stripped) < 20)
        if has_timestamp and current_lines:
            segments.append(
                {
                    "segment_id": f"seg_{len(segments)+1:03d}",
                    "start_ref": current_marker or f"line_{current_refs[0]}",
                    "end_ref": current_marker or f"line_{current_refs[-1]}",
                    "unit_type": "timestamp_segment",
                    "text": " ".join(current_lines).strip(),
                    "line_refs": current_refs[:],
                }
            )
            current_lines = []
            current_refs = []
        if has_timestamp:
            current_marker = stripped
        current_lines.append(stripped)
        current_refs.append(idx)
    if current_lines:
        segments.append(
            {
                "segment_id": f"seg_{len(segments)+1:03d}",
                "start_ref": current_marker or f"line_{current_refs[0]}",
                "end_ref": current_marker or f"line_{current_refs[-1]}",
                "unit_type": "timestamp_segment",
                "text": " ".join(current_lines).strip(),
                "line_refs": current_refs[:],
            }
        )
    return merge_short_segments(segments, target_size=3)


def split_by_heading(text: str) -> list[dict]:
    units: list[dict] = []
    current_title = "preamble"
    current_lines: list[str] = []
    for line in text.splitlines():
        if re.match(r"^\s*#{1,3}\s+", line):
            if current_lines:
                units.append(
                    {
                        "segment_id": f"seg_{len(units)+1:03d}",
                        "start_ref": current_title,
                        "end_ref": current_title,
                        "unit_type": "heading_block",
                        "text": " ".join(current_lines).strip(),
                        "line_refs": [],
                    }
                )
            current_title = re.sub(r"^\s*#{1,3}\s+", "", line).strip()
            current_lines = [line.strip()]
        elif line.strip():
            current_lines.append(line.strip())
    if current_lines:
        units.append(
            {
                "segment_id": f"seg_{len(units)+1:03d}",
                "start_ref": current_title,
                "end_ref": current_title,
                "unit_type": "heading_block",
                "text": " ".join(current_lines).strip(),
                "line_refs": [],
            }
        )
    return units


def split_by_paragraph(text: str) -> list[dict]:
    paragraphs = [chunk.strip() for chunk in re.split(r"\n\s*\n", text) if chunk.strip()]
    units = []
    for idx, paragraph in enumerate(paragraphs, start=1):
        units.append(
            {
                "segment_id": f"seg_{idx:03d}",
                "start_ref": f"para_{idx:03d}",
                "end_ref": f"para_{idx:03d}",
                "unit_type": "paragraph",
                "text": paragraph,
                "line_refs": [],
            }
        )
    return merge_short_segments(units, target_size=2)


def merge_short_segments(segments: list[dict], target_size: int) -> list[dict]:
    merged: list[dict] = []
    bucket: list[dict] = []
    for segment in segments:
        bucket.append(segment)
        total_chars = sum(len(row["text"]) for row in bucket)
        if len(bucket) >= target_size or total_chars >= 700:
            merged.append(merge_bucket(bucket, len(merged) + 1))
            bucket = []
    if bucket:
        if merged and sum(len(row["text"]) for row in bucket) < 220:
            merged[-1] = merge_bucket([split_to_segment(merged[-1])] + bucket, len(merged))
        else:
            merged.append(merge_bucket(bucket, len(merged) + 1))
    return merged


def split_to_segment(unit: dict) -> dict:
    return {
        "segment_id": unit["segment_id"],
        "start_ref": unit["start_ref"],
        "end_ref": unit["end_ref"],
        "unit_type": unit["unit_type"],
        "text": unit["text"],
        "line_refs": unit.get("line_refs", []),
    }


def merge_bucket(bucket: list[dict], index: int) -> dict:
    return {
        "segment_id": f"unit_{index:03d}",
        "start_ref": bucket[0]["start_ref"],
        "end_ref": bucket[-1]["end_ref"],
        "unit_type": bucket[0]["unit_type"],
        "text": " ".join(row["text"] for row in bucket).strip(),
        "source_segment_ids": [row["segment_id"] for row in bucket],
        "line_refs": [ref for row in bucket for ref in row.get("line_refs", [])],
    }


def split_input(text: str, split_mode: str, detected_profile: str) -> list[dict]:
    if split_mode == "timestamp":
        return split_by_timestamp(text.splitlines())
    if split_mode == "heading":
        return split_by_heading(text)
    return split_by_paragraph(text)


def build_source_manifest(run_id: str, input_row: dict, detected_profile: str, split_mode_used: str, raw_line_count: int, units: list[dict]) -> dict:
    return {
        "input_id": input_row["input_id"],
        "source_path": input_row["source_path"],
        "label": input_row["label"],
        "input_kind": input_row.get("input_kind", "mixed"),
        "detected_profile": detected_profile,
        "split_mode_used": split_mode_used,
        "raw_line_count": raw_line_count,
        "unit_count": len(units),
        "run_id": run_id,
    }


def build_split_units(units: list[dict]) -> list[dict]:
    rows = []
    for idx, unit in enumerate(units, start=1):
        rows.append(
            {
                "unit_id": f"unit_{idx:03d}",
                "start_ref": unit["start_ref"],
                "end_ref": unit["end_ref"],
                "unit_type": unit["unit_type"],
                "text_excerpt": unit["text"][:220],
                "char_count": len(unit["text"]),
                "source_segment_ids": unit.get("source_segment_ids", [unit["segment_id"]]),
            }
        )
    return rows


def build_processing_trace(run_id: str, input_id: str, detected_profile: str, split_mode_used: str, source_unit_count: int, merged_unit_count: int) -> dict:
    return {
        "run_id": run_id,
        "input_id": input_id,
        "detected_profile": detected_profile,
        "split_mode_used": split_mode_used,
        "source_unit_count": source_unit_count,
        "merged_unit_count": merged_unit_count,
        "engine_stage": "summary_written",
        "notes": "minimal observer ingest path: load -> detect -> split -> summary",
    }


def infer_flow_note(units: list[dict]) -> str:
    if not units:
        return "no readable flow detected"
    excerpts = [unit["text_excerpt"] for unit in units[:3]]
    joined = " ".join(excerpts)
    if "## " in joined or "제품" in joined or "소개" in joined:
        return "앞쪽은 소개/문제제기, 중간은 설명 확장, 뒤로 갈수록 주제 전환이 생기는 흐름으로 읽힌다."
    if TIMESTAMP_ANY_RE.search(joined):
        return "시계열형 transcript 흐름으로 읽히고, 초반/중반/후반의 주제 이동을 따라가기 쉬운 분해다."
    return "입력은 중간 단위 block으로 나뉘었고, 앞/중간/뒤 흐름을 빠르게 재확인하기 좋은 분해다."


def write_readable_input_board(manifest: dict, split_units: list[dict]) -> str:
    lines = [
        f"# readable input board / {manifest['run_id']}",
        "",
        "## 1. 입력 정보",
        f"- input_id: `{manifest['input_id']}`",
        f"- label: `{manifest['label']}`",
        f"- source_path: `{manifest['source_path']}`",
        f"- input_kind: `{manifest['input_kind']}`",
        f"- detected_profile: `{manifest['detected_profile']}`",
        "",
        "## 2. split 결과",
        f"- split_mode_used: `{manifest['split_mode_used']}`",
        f"- raw_line_count: `{manifest['raw_line_count']}`",
        f"- unit_count: `{manifest['unit_count']}`",
        "",
        "## 3. unit 목록 요약",
    ]
    for unit in split_units:
        lines.append(
            f"- {unit['unit_id']} — {unit['unit_type']} / {unit['start_ref']} ~ {unit['end_ref']} — \"{unit['text_excerpt'][:120]}...\""
        )
    lines.extend(
        [
            "",
            "## 4. 당장 읽히는 흐름",
            f"- {infer_flow_note(split_units)}",
            "",
        ]
    )
    return "\n".join(lines)


def write_operator_summary(manifest: dict, split_units: list[dict], processing_trace: dict) -> str:
    front = split_units[0]["text_excerpt"][:100] if split_units else ""
    middle = split_units[len(split_units) // 2]["text_excerpt"][:100] if split_units else ""
    end = split_units[-1]["text_excerpt"][:100] if split_units else ""
    lines = [
        f"# operator summary / {manifest['run_id']}",
        "",
        "## A. 입력 인식 결과",
        f"- `{manifest['label']}` 는 `{manifest['detected_profile']}` 성격 입력으로 읽혔다.",
        "",
        "## B. 분해 결과",
        f"- split mode: `{manifest['split_mode_used']}`",
        f"- 총 `{manifest['unit_count']}` 개 unit 으로 나뉘었다.",
        "",
        "## C. 흐름 요약",
        f"- 앞: `{front}`",
        f"- 중간: `{middle}`",
        f"- 뒤: `{end}`",
        "",
        "## D. 처리 상태",
        f"- engine_stage: `{processing_trace['engine_stage']}`",
        "",
        "## E. 다음 확장 가능 포인트",
        "- 이 입력은 이후 transcript probe / corridor probe의 source-side 분해 입력으로 확장 가능하다.",
        "",
    ]
    return "\n".join(lines)


def write_outputs(run_id: str, manifest: dict, split_units: list[dict], processing_trace: dict, readable_board: str, operator_summary: str) -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    source_ref = manifest["source_path"]
    content_role_tags = build_content_role_tags_for_split_units(source_ref, split_units)
    line_seed_bundles = build_line_seed_bundles_for_split_units(source_ref, split_units, content_role_tags)
    camera_support_bundles = build_camera_support_bundles_for_split_units(
        source_ref,
        split_units,
        content_role_tags,
        line_seed_bundles,
    )
    (OUTPUT_ROOT / f"source_manifest_{run_id}.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUTPUT_ROOT / f"split_units_{run_id}.json").write_text(json.dumps(split_units, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUTPUT_ROOT / f"processing_trace_{run_id}.json").write_text(json.dumps(processing_trace, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUTPUT_ROOT / f"readable_input_board_{run_id}.md").write_text(readable_board + "\n", encoding="utf-8")
    (OUTPUT_ROOT / f"operator_summary_{run_id}.md").write_text(operator_summary + "\n", encoding="utf-8")
    (OUTPUT_ROOT / f"content_role_tags_{run_id}.json").write_text(json.dumps(content_role_tags, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUTPUT_ROOT / f"line_seed_bundles_{run_id}.json").write_text(json.dumps(line_seed_bundles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUTPUT_ROOT / f"camera_support_bundles_{run_id}.json").write_text(json.dumps(camera_support_bundles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def run_single(input_row: dict, requested_profile: str) -> str:
    source_path = Path(input_row["source_path"])
    text = source_path.read_text(encoding="utf-8")
    detected_profile = detect_profile(text, None if requested_profile == "auto" else requested_profile)
    split_mode_used = detect_split_mode(text, input_row.get("split_mode", "auto"), detected_profile)
    raw_line_count = len(text.splitlines())
    units = split_input(text, split_mode_used, detected_profile)
    run_id = f"{input_row['input_id']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    manifest = build_source_manifest(run_id, input_row, detected_profile, split_mode_used, raw_line_count, units)
    split_units = build_split_units(units)
    processing_trace = build_processing_trace(run_id, input_row["input_id"], detected_profile, split_mode_used, len(units), len(split_units))
    readable_board = write_readable_input_board(manifest, split_units)
    operator_summary = write_operator_summary(manifest, split_units, processing_trace)
    write_outputs(run_id, manifest, split_units, processing_trace, readable_board, operator_summary)
    return run_id


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input")
    parser.add_argument("--label")
    parser.add_argument("--profile", default="auto")
    parser.add_argument("--registry")
    args = parser.parse_args()

    if not args.input and not args.registry:
        raise SystemExit("use --input or --registry")

    run_ids: list[str] = []
    if args.input:
        input_row = load_single_input(args.input, args.label)
        run_ids.append(run_single(input_row, args.profile))
    if args.registry:
        for row in load_registry(args.registry):
            run_ids.append(run_single(row, args.profile))

    print("\n".join(run_ids))


if __name__ == "__main__":
    main()
