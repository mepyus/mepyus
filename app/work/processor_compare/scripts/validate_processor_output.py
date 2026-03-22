#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path


SCENE_VALUES = {
    "discovery",
    "explanation",
    "comparison",
    "evidence",
    "question",
    "reflection",
    "instruction",
    "transition",
    "unknown",
}

ROLE_VALUES = {
    "thesis",
    "support",
    "bridge",
    "example",
    "contrast",
    "definition",
    "expansion",
    "problem",
    "meta",
    "unknown",
}

ANCHOR_TYPES = {"semantic", "structural", "object", "process"}
ANCHOR_SCOPES = {"local", "cross_source", "provisional"}
FLOAT_FIELDS = ["direction", "intensity", "stability", "confidence", "ambiguity"]
STRING_FIELDS = [
    "input_doc_id",
    "input_bundle_id",
    "fragment_id",
    "fragment_text",
    "source_type",
    "fragment_version",
    "scene",
    "role",
    "why_short",
]
ARRAY_FIELDS = ["anchors", "semantic_tags", "structural_tags", "evidence_text", "processor_notes"]


def parse_args():
    parser = argparse.ArgumentParser(description="Validate processor raw JSON/JSONL output.")
    parser.add_argument("input_path", help="File or directory containing JSON/JSONL outputs")
    parser.add_argument("--processor", help="Processor id for reporting", default=None)
    return parser.parse_args()


def iter_input_files(input_path: Path):
    if input_path.is_file():
        yield input_path
        return
    if not input_path.exists():
        raise FileNotFoundError(f"input path does not exist: {input_path}")
    for path in sorted(input_path.rglob("*")):
        if path.is_file() and path.suffix.lower() in {".json", ".jsonl"}:
            yield path


def load_records(path: Path):
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return [], [f"{path}: empty file"]
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        payload = None

    if payload is not None:
        if isinstance(payload, list):
            return [(index + 1, item) for index, item in enumerate(payload)], []
        else:
            return [(1, payload)], []

    errors = []
    records = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        if not line.strip():
            continue
        try:
            records.append((line_no, json.loads(line)))
        except json.JSONDecodeError as exc:
            errors.append(f"{path}:{line_no}: invalid JSON: {exc.msg}")
    return records, errors


def validate_anchor(anchor, prefix):
    errors = []
    if not isinstance(anchor, dict):
        return [f"{prefix}: anchor must be an object"]
    for field in ("anchor_id", "anchor_label", "anchor_type", "anchor_scope"):
        if field not in anchor:
            errors.append(f"{prefix}: missing anchor field '{field}'")
    if "anchor_id" in anchor and not isinstance(anchor["anchor_id"], str):
        errors.append(f"{prefix}: anchor_id must be a string")
    if "anchor_label" in anchor and not isinstance(anchor["anchor_label"], str):
        errors.append(f"{prefix}: anchor_label must be a string")
    if "anchor_type" in anchor and anchor["anchor_type"] not in ANCHOR_TYPES:
        errors.append(f"{prefix}: invalid anchor_type '{anchor.get('anchor_type')}'")
    if "anchor_scope" in anchor and anchor["anchor_scope"] not in ANCHOR_SCOPES:
        errors.append(f"{prefix}: invalid anchor_scope '{anchor.get('anchor_scope')}'")
    return errors


def validate_record(record, prefix):
    errors = []
    if not isinstance(record, dict):
        return [f"{prefix}: record must be an object"]
    required_fields = set(STRING_FIELDS + ARRAY_FIELDS + FLOAT_FIELDS)
    for field in required_fields:
        if field not in record:
            errors.append(f"{prefix}: missing field '{field}'")

    for field in STRING_FIELDS:
        if field in record and not isinstance(record[field], str):
            errors.append(f"{prefix}: field '{field}' must be a string")

    for field in FLOAT_FIELDS:
        if field not in record:
            continue
        value = record[field]
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            errors.append(f"{prefix}: field '{field}' must be a float in 0..1")
            continue
        if value < 0 or value > 1:
            errors.append(f"{prefix}: field '{field}' out of range: {value}")

    for field in ARRAY_FIELDS:
        if field in record and not isinstance(record[field], list):
            errors.append(f"{prefix}: field '{field}' must be an array")

    if isinstance(record.get("anchors"), list):
        for index, anchor in enumerate(record["anchors"]):
            errors.extend(validate_anchor(anchor, f"{prefix}: anchors[{index}]"))

    for field in ("semantic_tags", "structural_tags", "evidence_text", "processor_notes"):
        if isinstance(record.get(field), list):
            for index, item in enumerate(record[field]):
                if not isinstance(item, str):
                    errors.append(f"{prefix}: {field}[{index}] must be a string")

    if record.get("scene") not in SCENE_VALUES:
        errors.append(f"{prefix}: invalid scene '{record.get('scene')}'")
    if record.get("role") not in ROLE_VALUES:
        errors.append(f"{prefix}: invalid role '{record.get('role')}'")

    if isinstance(record.get("processor_notes"), list) and len(record["processor_notes"]) > 2:
        errors.append(f"{prefix}: processor_notes exceeds max length 2")
    if isinstance(record.get("semantic_tags"), list) and len(record["semantic_tags"]) > 5:
        errors.append(f"{prefix}: semantic_tags exceeds max length 5")
    if isinstance(record.get("structural_tags"), list) and len(record["structural_tags"]) > 5:
        errors.append(f"{prefix}: structural_tags exceeds max length 5")
    if isinstance(record.get("why_short"), str) and "\n" in record["why_short"]:
        errors.append(f"{prefix}: why_short must be a single sentence")
    if isinstance(record.get("evidence_text"), list) and len(record["evidence_text"]) == 0:
        errors.append(f"{prefix}: evidence_text must contain at least one item")
    return errors


def main():
    args = parse_args()
    input_path = Path(args.input_path)
    processor = args.processor or input_path.name
    try:
        files = list(iter_input_files(input_path))
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if not files:
        print(f"[{processor}] no JSON/JSONL files found in {input_path}", file=sys.stderr)
        return 2

    total_records = 0
    failed_records = 0
    all_errors = []

    for path in files:
        records, file_errors = load_records(path)
        all_errors.extend(file_errors)
        for line_no, record in records:
            total_records += 1
            record_errors = validate_record(record, f"{path}:{line_no}")
            if record_errors:
                failed_records += 1
                all_errors.extend(record_errors)

    valid_records = total_records - failed_records
    print(f"[{processor}] files={len(files)} records={total_records} valid={valid_records} failed={failed_records}")
    for message in all_errors:
        print(f"ERROR: {message}")
    return 1 if all_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
