#!/usr/bin/env python3
import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


NUMERIC_FIELDS = ["direction", "intensity", "stability", "confidence", "ambiguity"]
PROCESSORS = ["codex", "chatgpt", "gemini"]
ROLE_NAMES = {"thesis", "support", "bridge", "example", "contrast", "definition", "expansion", "problem", "meta"}


def parse_args():
    parser = argparse.ArgumentParser(description="Compare normalized processor outputs.")
    parser.add_argument("--codex", required=True, help="Normalized codex JSONL file")
    parser.add_argument("--chatgpt", required=True, help="Normalized chatgpt JSONL file")
    parser.add_argument("--gemini", required=True, help="Normalized gemini JSONL file")
    parser.add_argument("--reports-dir", required=True, help="Output directory for reports")
    return parser.parse_args()


def load_jsonl(path: Path):
    records = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        records.append(record)
    return records


def list_overlap(values):
    sets = [set(value) for value in values]
    union = set().union(*sets)
    if not union:
        return 1.0
    return round(len(set.intersection(*sets)) / len(union), 4)


def anchor_overlap(records):
    anchor_sets = [set(anchor["anchor_label"] for anchor in record["anchors"]) for record in records]
    union = set().union(*anchor_sets)
    if not union:
        return 1.0
    return round(len(set.intersection(*anchor_sets)) / len(union), 4)


def evidence_overlap(records):
    return list_overlap([record["evidence_text"] for record in records])


def tokenize(text):
    return {token for token in re.findall(r"\w+", text.lower()) if len(token) > 1}


def text_similarity(left, right):
    left_tokens = tokenize(left)
    right_tokens = tokenize(right)
    if not left_tokens and not right_tokens:
        return 1.0
    union = left_tokens | right_tokens
    if not union:
        return 0.0
    return round(len(left_tokens & right_tokens) / len(union), 4)


def match_records(reference_records, candidate_records, threshold=0.2):
    unmatched_candidates = set(range(len(candidate_records)))
    matches = {}
    for ref_index, reference in enumerate(reference_records):
        best_index = None
        best_score = -1.0
        for candidate_index in unmatched_candidates:
            score = text_similarity(reference["fragment_text"], candidate_records[candidate_index]["fragment_text"])
            if score > best_score:
                best_score = score
                best_index = candidate_index
        if best_index is not None and best_score >= threshold:
            matches[ref_index] = {
                "record": candidate_records[best_index],
                "score": best_score,
            }
            unmatched_candidates.remove(best_index)
        else:
            matches[ref_index] = {
                "record": None,
                "score": 0.0,
            }
    return matches, [candidate_records[index] for index in sorted(unmatched_candidates)]


def contains_any(text, patterns):
    lowered = text.lower()
    return any(pattern in lowered for pattern in patterns)


def infer_calibration_signals(base_record, records_by_processor, doc_counts, match_scores):
    text = base_record["fragment_text"]
    roles = {processor: records_by_processor[processor]["role"] for processor in PROCESSORS if records_by_processor[processor]}
    scenes = {processor: records_by_processor[processor]["scene"] for processor in PROCESSORS if records_by_processor[processor]}
    signals = []

    if contains_any(text, ["들어가며", "결론부터", "요약", "란?", "정의"]) and {"thesis", "definition"} & set(roles.values()):
        signals.append("summary_definition_boundary_candidate")

    problem_markers = ["문제", "한계", "부담", "어렵", "사일로", "끊어진", "제약"]
    solution_markers = ["해결", "보완", "가능", "활용", "개선", "이를 통해", "대안", "보완한 것이"]
    if contains_any(text, problem_markers) and contains_any(text, solution_markers):
        signals.append("problem_solution_boundary_candidate")

    mechanism_markers = ["구축", "단계", "정의", "생성", "탐색", "변환", "적재", "구조", "방식", "메커니즘"]
    value_markers = ["중요", "가치", "활용", "추론", "신뢰성", "정확성", "효과", "이점", "가능성"]
    if contains_any(text, mechanism_markers) and contains_any(text, value_markers):
        signals.append("mechanism_value_boundary_candidate")

    if any(scene not in {"discovery", "explanation", "comparison", "evidence", "question", "reflection", "instruction", "transition", "unknown"} for scene in scenes.values()):
        signals.append("scene_schema_violation")

    if "chatgpt" in scenes and scenes["chatgpt"] in ROLE_NAMES:
        signals.append("scene_schema_violation")
    if "gemini" in scenes and scenes["gemini"] in ROLE_NAMES.union({"process"}):
        signals.append("scene_schema_violation")

    if any(records_by_processor[processor] and (
        records_by_processor[processor]["scene"] == "reflection" or records_by_processor[processor]["role"] == "meta"
    ) for processor in PROCESSORS) and base_record["scene"] == "explanation":
        signals.append("meta_overreach_candidate")

    if doc_counts["chatgpt"] > doc_counts["codex"] and match_scores.get("chatgpt", 0.0) < 0.75:
        signals.append("oversegmentation_candidate")

    if doc_counts["gemini"] < doc_counts["codex"] and match_scores.get("gemini", 0.0) < 0.75:
        signals.append("overmerged_candidate")

    if doc_counts["codex"] >= doc_counts["gemini"] and doc_counts["codex"] <= doc_counts["chatgpt"]:
        signals.append("mid_granularity_candidate")

    return sorted(dict.fromkeys(signals))


def build_comparison(doc_key, base_record, records_by_processor, match_scores, doc_counts):
    records = [records_by_processor[name] for name in PROCESSORS]
    available_records = [record for record in records if record is not None]
    numeric_deltas = {}
    max_numeric_delta = 0.0
    for field in NUMERIC_FIELDS:
        values = [record[field] for record in available_records]
        delta = round(max(values) - min(values), 4) if values else 0.0
        numeric_deltas[field] = delta
        max_numeric_delta = max(max_numeric_delta, delta)

    semantic_overlap = list_overlap([record["semantic_tags"] for record in available_records]) if available_records else 0.0
    structural_overlap = list_overlap([record["structural_tags"] for record in available_records]) if available_records else 0.0
    anchor_score = anchor_overlap(available_records) if available_records else 0.0
    evidence_score = evidence_overlap(available_records) if available_records else 0.0
    unique_anchor_owners = defaultdict(set)
    for processor in PROCESSORS:
        if not records_by_processor[processor]:
            continue
        for anchor in records_by_processor[processor]["anchors"]:
            unique_anchor_owners[anchor["anchor_label"]].add(processor)
    unique_semantic_owners = defaultdict(set)
    for processor in PROCESSORS:
        if not records_by_processor[processor]:
            continue
        for tag in records_by_processor[processor]["semantic_tags"]:
            unique_semantic_owners[tag].add(processor)

    hidden_items = sorted(
        [
            {"type": "anchor", "value": value, "processor": next(iter(owners))}
            for value, owners in unique_anchor_owners.items()
            if len(owners) == 1
        ]
        + [
            {"type": "semantic_tag", "value": value, "processor": next(iter(owners))}
            for value, owners in unique_semantic_owners.items()
            if len(owners) == 1
        ],
        key=lambda item: (item["type"], item["value"], item["processor"]),
    )

    has_missing_processor = any(record is None for record in records)
    has_anchorless_processor = any(record is not None and len(record["anchors"]) == 0 for record in records)
    has_anchored_processor = any(record is not None and len(record["anchors"]) > 0 for record in records)
    category = "stable"
    is_split = False
    if len(available_records) >= 2:
        is_split = (
            len(set(record["scene"] for record in available_records)) > 1
            or len(set(record["role"] for record in available_records)) > 1
            or semantic_overlap < 0.5
            or structural_overlap < 0.5
            or anchor_score < 0.5
            or max_numeric_delta >= 0.35
        )
    if has_missing_processor or (has_anchorless_processor and has_anchored_processor):
        category = "broken_link"
    elif is_split:
        category = "split"
    elif hidden_items:
        category = "hidden_candidate"

    calibration_signals = infer_calibration_signals(base_record, records_by_processor, doc_counts, match_scores)

    return {
        "doc_key": doc_key,
        "reference_fragment_id": base_record["fragment_id"],
        "reference_source_file_id": base_record.get("source_file_id", ""),
        "input_doc_id": base_record["input_doc_id"],
        "input_bundle_id": base_record["input_bundle_id"],
        "fragment_text": base_record["fragment_text"],
        "category": category,
        "numeric_deltas": numeric_deltas,
        "max_numeric_delta": round(max_numeric_delta, 4),
        "scene_values": {
            processor: (records_by_processor[processor]["scene"] if records_by_processor[processor] else "missing")
            for processor in PROCESSORS
        },
        "role_values": {
            processor: (records_by_processor[processor]["role"] if records_by_processor[processor] else "missing")
            for processor in PROCESSORS
        },
        "semantic_overlap": semantic_overlap,
        "structural_overlap": structural_overlap,
        "anchor_overlap": anchor_score,
        "evidence_overlap": evidence_score,
        "match_scores": match_scores,
        "calibration_signals": calibration_signals,
        "hidden_items": hidden_items,
        "anchors": {
            processor: ([anchor["anchor_label"] for anchor in records_by_processor[processor]["anchors"]] if records_by_processor[processor] else [])
            for processor in PROCESSORS
        },
        "matched_fragment_ids": {
            processor: (records_by_processor[processor]["fragment_id"] if records_by_processor[processor] else None)
            for processor in PROCESSORS
        },
        "why_short": {
            processor: (records_by_processor[processor]["why_short"] if records_by_processor[processor] else "")
            for processor in PROCESSORS
        },
    }


def write_jsonl(path: Path, records):
    lines = [json.dumps(record, ensure_ascii=False) for record in records]
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def main():
    args = parse_args()
    reports_dir = Path(args.reports_dir)
    reports_dir.mkdir(parents=True, exist_ok=True)

    normalized = {
        "codex": load_jsonl(Path(args.codex)),
        "chatgpt": load_jsonl(Path(args.chatgpt)),
        "gemini": load_jsonl(Path(args.gemini)),
    }
    grouped = {processor: defaultdict(list) for processor in PROCESSORS}
    for processor, records in normalized.items():
        for record in records:
            doc_key = record.get("source_file_id") or record["input_doc_id"]
            grouped[processor][doc_key].append(record)
    all_doc_keys = sorted(set().union(*(records.keys() for records in grouped.values())))

    comparisons = []
    unmatched_fragment_counts = {processor: 0 for processor in PROCESSORS}
    valid_counts = {processor: len(records) for processor, records in normalized.items()}
    doc_fragment_counts = {}
    for doc_key in all_doc_keys:
        base_records = grouped["codex"].get(doc_key, [])
        chatgpt_records = grouped["chatgpt"].get(doc_key, [])
        gemini_records = grouped["gemini"].get(doc_key, [])
        doc_counts = {
            "codex": len(base_records),
            "chatgpt": len(chatgpt_records),
            "gemini": len(gemini_records),
        }
        doc_fragment_counts[doc_key] = doc_counts
        if not base_records:
            unmatched_fragment_counts["chatgpt"] += len(chatgpt_records)
            unmatched_fragment_counts["gemini"] += len(gemini_records)
            continue
        chatgpt_matches, unmatched_chatgpt = match_records(base_records, chatgpt_records)
        gemini_matches, unmatched_gemini = match_records(base_records, gemini_records)
        unmatched_fragment_counts["chatgpt"] += len(unmatched_chatgpt)
        unmatched_fragment_counts["gemini"] += len(unmatched_gemini)
        for index, base_record in enumerate(base_records):
            records_by_processor = {
                "codex": base_record,
                "chatgpt": chatgpt_matches[index]["record"],
                "gemini": gemini_matches[index]["record"],
            }
            match_scores = {
                "codex": 1.0,
                "chatgpt": chatgpt_matches[index]["score"],
                "gemini": gemini_matches[index]["score"],
            }
            comparisons.append(build_comparison(doc_key, base_record, records_by_processor, match_scores, doc_counts))

    by_category = defaultdict(list)
    anchor_divergence = Counter()
    scene_disagreements = Counter()
    role_disagreements = Counter()
    calibration_signal_counts = Counter()
    tag_mismatch_examples = []
    for comparison in comparisons:
        by_category[comparison["category"]].append(comparison)
        for signal in comparison["calibration_signals"]:
            calibration_signal_counts[signal] += 1
        if comparison["anchor_overlap"] < 1.0:
            for processor, anchors in comparison["anchors"].items():
                for anchor in anchors:
                    anchor_divergence[(anchor, processor)] += 1
        if len(set(comparison["scene_values"].values())) > 1:
            scene_disagreements[tuple(sorted(comparison["scene_values"].values()))] += 1
        if len(set(comparison["role_values"].values())) > 1:
            role_disagreements[tuple(sorted(comparison["role_values"].values()))] += 1
        if comparison["semantic_overlap"] < 1.0 or comparison["structural_overlap"] < 1.0:
            tag_mismatch_examples.append(
                {
                    "reference_fragment_id": comparison["reference_fragment_id"],
                    "semantic_overlap": comparison["semantic_overlap"],
                    "structural_overlap": comparison["structural_overlap"],
                    "anchors": comparison["anchors"],
                    "match_scores": comparison["match_scores"],
                }
            )

    summary = {
        "total_docs_seen": len(all_doc_keys),
        "total_fragments_seen": sum(len(records) for records in normalized.values()),
        "total_fragments_compared": len(comparisons),
        "valid_outputs_by_processor": valid_counts,
        "unmatched_fragments_by_processor": unmatched_fragment_counts,
        "doc_fragment_counts": doc_fragment_counts,
        "category_counts": {category: len(by_category[category]) for category in ["stable", "split", "hidden_candidate", "broken_link"]},
        "calibration_signal_counts": dict(calibration_signal_counts),
        "top_anchor_divergence": [
            {"anchor_label": anchor, "processor": processor, "count": count}
            for (anchor, processor), count in anchor_divergence.most_common(10)
        ],
        "scene_disagreement_top": [
            {"scene_values": list(values), "count": count}
            for values, count in scene_disagreements.most_common(10)
        ],
        "role_disagreement_top": [
            {"role_values": list(values), "count": count}
            for values, count in role_disagreements.most_common(10)
        ],
        "tag_mismatch_examples": tag_mismatch_examples[:10],
        "input_adjustment_candidates": [
            "split fragments with repeated scene or role disagreement",
            "review fragments where anchor overlap stays low across all processors",
            "review summary_definition_boundary, problem_solution_boundary, and mechanism_value_boundary patterns",
        ],
        "label_adjustment_candidates": [
            "tighten scene and role boundary guidance for repeated disagreement clusters",
            "review semantic tag vocabulary when hidden_candidate tags repeat",
            "report scene_schema_violation and meta_overreach explicitly during calibration review",
        ],
    }

    Path(reports_dir / "comparison_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    markdown_lines = [
        "# Comparison Summary",
        "",
        f"- 총 문서 수: {summary['total_docs_seen']}",
        f"- 총 raw fragment 수: {summary['total_fragments_seen']}",
        f"- 실제 비교 기준 fragment 수: {summary['total_fragments_compared']}",
        f"- processor별 유효 출력 수: codex={valid_counts['codex']}, chatgpt={valid_counts['chatgpt']}, gemini={valid_counts['gemini']}",
        (
            "- processor별 후매칭 실패 fragment 수: "
            f"chatgpt={unmatched_fragment_counts['chatgpt']}, gemini={unmatched_fragment_counts['gemini']}"
        ),
        (
            "- stable / split / hidden_candidate / broken_link 개수: "
            f"{summary['category_counts']['stable']} / {summary['category_counts']['split']} / "
            f"{summary['category_counts']['hidden_candidate']} / {summary['category_counts']['broken_link']}"
        ),
        "",
        "## Divergence Anchors",
    ]
    if summary["top_anchor_divergence"]:
        markdown_lines.extend(
            [f"- {item['anchor_label']} ({item['processor']}): {item['count']}" for item in summary["top_anchor_divergence"]]
        )
    else:
        markdown_lines.append("- 없음")
    markdown_lines.append("")
    markdown_lines.append("## Calibration Signals")
    if summary["calibration_signal_counts"]:
        markdown_lines.extend(
            [f"- {signal}: {count}" for signal, count in sorted(summary["calibration_signal_counts"].items())]
        )
    else:
        markdown_lines.append("- 없음")
    markdown_lines.append("")
    markdown_lines.append("## Scene Disagreement Top")
    if summary["scene_disagreement_top"]:
        markdown_lines.extend(
            [f"- {', '.join(item['scene_values'])}: {item['count']}" for item in summary["scene_disagreement_top"]]
        )
    else:
        markdown_lines.append("- 없음")
    markdown_lines.append("")
    markdown_lines.append("## Role Disagreement Top")
    if summary["role_disagreement_top"]:
        markdown_lines.extend(
            [f"- {', '.join(item['role_values'])}: {item['count']}" for item in summary["role_disagreement_top"]]
        )
    else:
        markdown_lines.append("- 없음")
    markdown_lines.append("")
    markdown_lines.append("## Tag Mismatch Examples")
    if summary["tag_mismatch_examples"]:
        markdown_lines.extend(
            [
                (
                    f"- {item['reference_fragment_id']}: semantic_overlap={item['semantic_overlap']}, "
                    f"structural_overlap={item['structural_overlap']}"
                )
                for item in summary["tag_mismatch_examples"]
            ]
        )
    else:
        markdown_lines.append("- 없음")
    markdown_lines.append("")
    markdown_lines.append("## 입력기 조정 후보 포인트")
    markdown_lines.extend(f"- {item}" for item in summary["input_adjustment_candidates"])
    markdown_lines.append("")
    markdown_lines.append("## 라벨기 조정 후보 포인트")
    markdown_lines.extend(f"- {item}" for item in summary["label_adjustment_candidates"])
    (reports_dir / "comparison_summary.md").write_text("\n".join(markdown_lines) + "\n", encoding="utf-8")

    for category in ["stable", "split", "hidden_candidate", "broken_link"]:
        write_jsonl(reports_dir / f"{category}.jsonl", by_category[category])

    print(f"compared {len(comparisons)} fragments -> {reports_dir}")


if __name__ == "__main__":
    raise SystemExit(main())
