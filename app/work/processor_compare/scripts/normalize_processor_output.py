#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description="Normalize processor raw JSON/JSONL output to JSONL.")
    parser.add_argument("input_path", help="File or directory containing raw JSON/JSONL outputs")
    parser.add_argument("output_path", help="Output JSONL file")
    parser.add_argument("--processor", help="Processor id; inferred from input path when omitted", default=None)
    return parser.parse_args()


def iter_input_files(input_path: Path):
    if input_path.is_file():
        yield input_path
        return
    for path in sorted(input_path.rglob("*")):
        if path.is_file() and path.suffix.lower() in {".json", ".jsonl"}:
            yield path


def load_records(path: Path):
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return []
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        payload = None
    if payload is None:
        return [json.loads(line) for line in text.splitlines() if line.strip()]
    if isinstance(payload, list):
        return payload
    return [payload]


def normalize_space(value: str) -> str:
    return " ".join(value.strip().split())


def to_snake_case(value: str) -> str:
    value = normalize_space(value).lower()
    value = value.replace("-", "_").replace("/", "_")
    value = re.sub(r"[^a-z0-9_ ]+", "", value)
    value = re.sub(r"\s+", "_", value)
    value = re.sub(r"_+", "_", value)
    return value.strip("_")


def normalize_anchor_label(value: str) -> str:
    return to_snake_case(value)


def normalize_string_list(items):
    cleaned = [to_snake_case(item) for item in items if isinstance(item, str) and normalize_space(item)]
    return sorted(dict.fromkeys(cleaned))


def normalize_evidence(items):
    cleaned = [normalize_space(item) for item in items if isinstance(item, str) and normalize_space(item)]
    return sorted(dict.fromkeys(cleaned))


def normalize_anchors(items):
    anchors = []
    for anchor in items:
        normalized = {
            "anchor_id": normalize_space(anchor.get("anchor_id", "")),
            "anchor_label": normalize_anchor_label(anchor.get("anchor_label", "")),
            "anchor_type": normalize_space(anchor.get("anchor_type", "")),
            "anchor_scope": normalize_space(anchor.get("anchor_scope", "")),
        }
        anchors.append(normalized)
    anchors.sort(key=lambda item: (item["anchor_label"], item["anchor_type"], item["anchor_scope"], item["anchor_id"]))
    return anchors


def normalize_record(record, processor_id, source_file_id):
    normalized = {
        "input_doc_id": normalize_space(record["input_doc_id"]),
        "input_bundle_id": normalize_space(record["input_bundle_id"]),
        "fragment_id": normalize_space(record["fragment_id"]),
        "fragment_text": normalize_space(record["fragment_text"]),
        "source_type": normalize_space(record["source_type"]),
        "fragment_version": normalize_space(record["fragment_version"]),
        "anchors": normalize_anchors(record["anchors"]),
        "direction": float(record["direction"]),
        "intensity": float(record["intensity"]),
        "stability": float(record["stability"]),
        "scene": normalize_space(record["scene"]).lower(),
        "role": normalize_space(record["role"]).lower(),
        "semantic_tags": normalize_string_list(record["semantic_tags"]),
        "structural_tags": normalize_string_list(record["structural_tags"]),
        "confidence": float(record["confidence"]),
        "ambiguity": float(record["ambiguity"]),
        "evidence_text": normalize_evidence(record["evidence_text"]),
        "why_short": normalize_space(record["why_short"]),
        "processor_notes": normalize_evidence(record["processor_notes"]),
        "processor_id": processor_id,
        "source_file_id": source_file_id,
    }
    return normalized


def main():
    args = parse_args()
    input_path = Path(args.input_path)
    output_path = Path(args.output_path)
    processor_id = args.processor or input_path.name
    records = []
    normalized_records = []
    for path in iter_input_files(input_path):
        source_file_id = path.stem
        for record in load_records(path):
            normalized_records.append(normalize_record(record, processor_id, source_file_id))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(record, ensure_ascii=False) for record in normalized_records]
    output_path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
    print(f"[{processor_id}] normalized {len(normalized_records)} records -> {output_path}")


if __name__ == "__main__":
    raise SystemExit(main())
