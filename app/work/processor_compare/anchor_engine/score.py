from __future__ import annotations

from collections import Counter, defaultdict
from typing import Dict, Iterable, List, Tuple
import math


TYPE_WEIGHT = {
    "semantic": 0.90,
    "object": 0.85,
    "process": 0.82,
    "structural": 0.72,
}

TYPE_PRIORITY = {
    "semantic": 0.95,
    "object": 0.88,
    "process": 0.80,
    "structural": 0.70,
}

POSITION_WEIGHT = {
    "title": 1.00,
    "heading": 0.90,
    "bullet_lead": 0.80,
    "first_paragraph": 0.75,
    "body": 0.50,
    "tail": 0.35,
}


def build_anchor_statistics(items: List[Dict[str, object]]) -> Dict[str, object]:
    in_doc = Counter((str(item["doc_id"]), str(item["canonical_key"])) for item in items)
    docs_by_key = defaultdict(set)
    sections_by_key = defaultdict(set)
    position_by_key = defaultdict(list)
    coanchor = defaultdict(Counter)

    by_doc_section = defaultdict(list)
    for item in items:
        key = str(item["canonical_key"])
        doc_id = str(item["doc_id"])
        section_id = str(item.get("section_id", "body"))
        docs_by_key[key].add(doc_id)
        sections_by_key[(doc_id, key)].add(section_id)
        position_by_key[(doc_id, key)].append(str(item.get("source_position", "body")))
        by_doc_section[(doc_id, section_id)].append(key)

    for _bucket, keys in by_doc_section.items():
        unique = list(dict.fromkeys(keys))
        for left in unique:
            for right in unique:
                if left == right:
                    continue
                coanchor[left][right] += 1

    return {
        "in_doc": in_doc,
        "docs_by_key": docs_by_key,
        "sections_by_key": sections_by_key,
        "position_by_key": position_by_key,
        "coanchor": coanchor,
    }


def enrich_with_statistics(item: Dict[str, object], stats: Dict[str, object], doc_count: int) -> Dict[str, object]:
    key = str(item["canonical_key"])
    doc_id = str(item["doc_id"])
    in_doc_repeat = _repeat_to_unit(int(stats["in_doc"][(doc_id, key)]))
    cross_doc_repeat = _doc_repeat_to_unit(len(stats["docs_by_key"][key]))
    position_weight = max(POSITION_WEIGHT.get(value, 0.50) for value in stats["position_by_key"][(doc_id, key)] or ["body"])
    coanchor_connectivity = _coanchor_to_unit(sum(stats["coanchor"][key].values()))
    distinctiveness = _distinctiveness(len(stats["docs_by_key"][key]), doc_count)

    item["in_doc_repeat"] = in_doc_repeat
    item["cross_doc_repeat"] = cross_doc_repeat
    item["position_weight"] = round(position_weight, 3)
    item["coanchor_connectivity"] = coanchor_connectivity
    item["distinctiveness_hint"] = distinctiveness
    item["specificity_score"] = compute_specificity_score(item, distinctiveness)
    item["type_weight"] = TYPE_WEIGHT.get(str(item.get("anchor_type", "semantic")), 0.72)
    item["strong_score"] = compute_strong_score(item)
    item["promoted"] = should_promote(item)
    return item


def compute_specificity_score(item: Dict[str, object], distinctiveness_hint: float) -> float:
    label = str(item.get("display_label", ""))
    key = str(item.get("canonical_key", ""))
    phrase_len = int(item.get("phrase_len", 1))
    score = 0.25 + distinctiveness_hint * 0.35
    if bool(item.get("alias_matched")):
        score += 0.18
    if "_" in key or " " in label:
        score += 0.18
    if any(ch.isupper() for ch in label):
        score += 0.10
    if phrase_len >= 2:
        score += 0.12
    if str(item.get("source_position", "body")) in {"title", "heading"}:
        score += 0.10
    return _clamp(score)


def compute_strong_score(item: Dict[str, object]) -> float:
    score = (
        0.20 * float(item.get("in_doc_repeat", 0.0))
        + 0.25 * float(item.get("cross_doc_repeat", 0.0))
        + 0.15 * float(item.get("position_weight", 0.0))
        + 0.15 * float(item.get("specificity_score", 0.0))
        + 0.15 * float(item.get("type_weight", 0.0))
        + 0.10 * float(item.get("coanchor_connectivity", 0.0))
        - 0.20 * float(item.get("weakness_penalty", 0.0))
    )
    return _clamp(score)


def should_promote(item: Dict[str, object]) -> bool:
    if not bool(item.get("canonical_key")):
        return False
    if float(item.get("weakness_penalty", 0.0)) >= 0.40:
        return False
    if float(item.get("specificity_score", 0.0)) < 0.50:
        return False
    score = float(item.get("strong_score", 0.0))
    if score >= 0.60:
        return True
    if (
        bool(item.get("alias_matched"))
        and score >= 0.56
        and float(item.get("specificity_score", 0.0)) >= 0.72
    ):
        return True
    return (
        score >= 0.58
        and float(item.get("specificity_score", 0.0)) >= 0.60
        and str(item.get("anchor_type", "semantic")) in {"semantic", "object", "process"}
    )


def score_region_representatives(items: Iterable[Dict[str, object]]) -> List[Dict[str, object]]:
    rows = list(items)
    if not rows:
        return []
    region_freq = Counter(str(item["canonical_key"]) for item in rows)
    total = sum(region_freq.values()) or 1
    scored = []
    for item in rows:
        key = str(item["canonical_key"])
        score = (
            0.25 * (region_freq[key] / total)
            + 0.20 * 1.0
            + 0.20 * float(item.get("distinctiveness_hint", 0.0))
            + 0.15 * float(item.get("strong_score", 0.0))
            + 0.10 * float(item.get("coanchor_connectivity", 0.0))
            + 0.10 * float(item.get("position_weight", 0.0))
        )
        record = dict(item)
        record["region_anchor_score"] = _clamp(score)
        scored.append(record)
    scored.sort(key=lambda row: row["region_anchor_score"], reverse=True)
    return _enforce_type_balance(scored, limit=5)


def score_bridge_anchors(left_items: Iterable[Dict[str, object]], right_items: Iterable[Dict[str, object]]) -> List[Dict[str, object]]:
    left_map = {str(item["canonical_key"]): item for item in left_items}
    right_map = {str(item["canonical_key"]): item for item in right_items}
    overlap = set(left_map) & set(right_map)
    results = []
    for key in overlap:
        left = left_map[key]
        right = right_map[key]
        weakness = max(float(left.get("weakness_penalty", 0.0)), float(right.get("weakness_penalty", 0.0)))
        contextual_stability = 1.0 - abs(float(left.get("specificity_score", 0.0)) - float(right.get("specificity_score", 0.0)))
        score = (
            0.30 * 1.0
            + 0.20 * max(float(left.get("distinctiveness_hint", 0.0)), float(right.get("distinctiveness_hint", 0.0)))
            + 0.20 * max(float(left.get("strong_score", 0.0)), float(right.get("strong_score", 0.0)))
            + 0.15 * TYPE_PRIORITY.get(str(left.get("anchor_type", "semantic")), 0.70)
            + 0.15 * contextual_stability
            - 0.25 * weakness
        )
        if weakness >= 0.40:
            continue
        record = dict(left)
        record["bridge_score"] = _clamp(score)
        if record["bridge_score"] >= 0.60:
            results.append(record)
    results.sort(key=lambda row: row["bridge_score"], reverse=True)
    return results


def _repeat_to_unit(count: int) -> float:
    if count <= 1:
        return 0.20
    if count == 2:
        return 0.45
    if count == 3:
        return 0.65
    return min(1.0, 0.85 + (count - 4) * 0.05)


def _doc_repeat_to_unit(count: int) -> float:
    if count <= 1:
        return 0.10
    if count == 2:
        return 0.40
    if count == 3:
        return 0.65
    return 0.85


def _coanchor_to_unit(count: int) -> float:
    return _clamp(min(1.0, math.log1p(count) / 2.2))


def _distinctiveness(doc_presence: int, doc_count: int) -> float:
    if doc_count <= 1:
        return 1.0
    ratio = doc_presence / doc_count
    return _clamp(max(0.05, 1.0 - ratio))


def _enforce_type_balance(rows: List[Dict[str, object]], limit: int) -> List[Dict[str, object]]:
    quotas = {"semantic": 2, "object": 1, "process": 1, "structural": 1}
    selected = []
    seen = set()
    for row in rows:
        key = str(row["canonical_key"])
        anchor_type = str(row.get("anchor_type", "semantic"))
        if key in seen:
            continue
        if quotas.get(anchor_type, 0) <= 0:
            continue
        quotas[anchor_type] -= 1
        seen.add(key)
        selected.append(row)
        if len(selected) >= limit:
            break
    return selected


def _clamp(value: float) -> float:
    return max(0.0, min(1.0, round(value, 3)))
