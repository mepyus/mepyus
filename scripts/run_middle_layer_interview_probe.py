#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = REPO_ROOT / "app" / "work" / "archive_review" / "interview_support" / "middle_layer_experiments" / "generated"

ROLE_DISPLAY = {
    "problem_or_constraint_role": "문제/제약 역할",
    "mechanism_role": "핵심 메커니즘 역할",
    "verification_or_evaluation_role": "검증/평가 역할",
    "control_or_deployment_role": "운영/배치 역할",
    "reflection_or_gap_role": "반성/갭 역할",
    "observer_or_transition_role": "전환/관찰 역할",
}

TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9_+-]{2,}|[가-힣]{2,}")
TIMESTAMP_RE = re.compile(r"\b\d{1,2}:\d{2}(?::\d{2})?\b")
CHAPTER_RE = re.compile(r"^\s*(?:chapter|챕터)\s*\d+[:.]?\s*", re.IGNORECASE)
SPEAKER_RE = re.compile(r"^\s*[A-Za-z가-힣][A-Za-z가-힣 ._-]{0,30}:\s+")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+|(?<=다\.)\s+|(?<=요\.)\s+")

GENERIC_DISCOURSE_TERMS = {
    "우리가",
    "우리는",
    "있습니다",
    "겁니다",
    "그래서",
    "그러니까",
    "사실은",
    "사실",
    "어떻게",
    "말이죠",
    "합니다",
    "합니다만",
    "그렇죠",
    "그런데",
    "하지만",
    "그리고",
    "이렇게",
    "저는",
    "당신이",
    "정말",
    "여전히",
    "아마",
    "뭔가",
    "같은",
    "거대한",
    "있는",
    "제가",
    "우리",
    "이미",
    "다른",
    "아주",
    "이게",
    "이건",
    "그런",
    "모든",
    "결국",
    "거죠",
    "이제",
    "지금",
    "여기서",
    "이런",
    "저런",
    "되죠",
    "되는",
    "보면",
    "하죠",
    "그거",
    "것이",
    "이것",
    "그것",
}

DOMAIN_SIGNAL_TERMS = {
    "scaling",
    "verification",
    "verifiable",
    "compute",
    "automation",
    "coding",
    "software",
    "model",
    "models",
    "learning",
    "reflection",
    "process",
    "signal",
    "rl",
    "deployment",
    "control",
    "security",
    "operator",
    "operators",
    "training",
    "evaluation",
    "reliability",
    "generation",
    "causal",
    "mask",
    "autoregressive",
    "ontology",
    "agent",
    "agents",
    "constraint",
    "constraints",
    "verification",
    "scaling",
    "학습",
    "검증",
    "자동화",
    "연산",
    "반사",
    "반성",
    "강화학습",
    "배포",
    "통제",
    "보안",
    "운영자",
    "훈련",
    "생성",
    "평가",
    "신호",
}

PROBLEM_HINTS = {
    "문제",
    "한계",
    "제약",
    "병목",
    "위험",
    "부족",
    "어렵",
    "verification",
    "trust",
    "security",
    "rl",
    "reflection",
    "deployment",
    "constraint",
    "limits",
}
STRUCTURE_HINTS = {
    "model",
    "models",
    "architecture",
    "transformer",
    "software",
    "layer",
    "layers",
    "system",
    "systems",
    "control",
    "agent",
    "decoder",
    "encoder",
    "attention",
    "ontology",
}
MECHANISM_HINTS = {
    "training",
    "evaluation",
    "signal",
    "signals",
    "process",
    "generation",
    "generation",
    "scaling",
    "verification",
    "operator",
    "mask",
    "autoregressive",
    "qkv",
    "self",
    "attention",
    "coding",
}

ROLE_HINTS: Dict[str, Sequence[str]] = {
    "problem_or_constraint_role": (
        "문제", "한계", "제약", "병목", "어렵", "부족", "limits", "constraint", "constraints", "bottleneck",
    ),
    "mechanism_role": (
        "architecture", "model", "models", "mechanism", "attention", "decoder", "encoder", "software", "layer",
        "layers", "ontology", "signal", "process", "reflection", "autoregressive", "causal", "mask", "qkv",
        "자기회귀", "구조", "메커니즘", "학습", "반성", "신호", "통제",
    ),
    "verification_or_evaluation_role": (
        "verification", "verifiable", "evaluation", "metric", "metrics", "benchmark", "reliability",
        "검증", "평가", "벤치마크", "신뢰성", "measure", "compute", "scaling", "훈련", "데이터", "확장성",
    ),
    "control_or_deployment_role": (
        "deployment", "deploy", "control", "operator", "operators", "security", "clearance", "regulated",
        "enterprise", "production", "field", "전장", "배포", "통제", "운영자", "보안", "기관", "현장", "실전", "전개",
    ),
    "reflection_or_gap_role": (
        "reflection", "gap", "critique", "limits", "rl", "learning", "animal", "ghost", "supervision",
        "반성", "갭", "한계", "강화학습", "학습", "비판", "인간", "동물", "DNA",
    ),
    "observer_or_transition_role": (
        "그러니까", "하지만", "그리고", "사실", "이제", "말이죠", "그렇죠", "뭔가", "chapter", "챕터",
    ),
}


@dataclass
class ProbeResult:
    input_path: str
    source_ref: str
    raw_paragraph_count: int
    normalized_block_count: int
    dominant_topic_anchors: List[Dict[str, object]]
    suppressed_discourse_anchors: List[Dict[str, object]]
    case_blocks: List[Dict[str, object]]
    provisional_frame_sketch: List[str]
    dominant_roles: List[str]
    dominant_role_gloss: List[str]
    secondary_roles: List[str]
    secondary_role_gloss: List[str]
    observer_only_roles: List[str]
    observer_role_gloss: List[str]
    role_evidence_terms: Dict[str, List[str]]
    case_specific_signals: List[str]
    anchor_bucket_counts: Dict[str, int]
    user_layer_hint_signals: List[str]
    user_facing_summary: str
    caution_notes: List[str]


def _now_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _relative(path: Path) -> str:
    try:
        rel = path.resolve().relative_to(REPO_ROOT)
    except ValueError:
        rel = path.resolve()
    return str(rel).replace("\\", "/")


def _normalize_line(line: str) -> str:
    line = TIMESTAMP_RE.sub(" ", line)
    line = CHAPTER_RE.sub("", line)
    line = SPEAKER_RE.sub("", line)
    line = re.sub(r"\s+", " ", line).strip()
    return line


def _pre_normalize(text: str) -> List[str]:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = TIMESTAMP_RE.sub("\n", text)
    chunks = [chunk.strip() for chunk in re.split(r"\n\s*\n+|\n+", text) if chunk.strip()]
    normalized: List[str] = []
    for chunk in chunks:
        lines = [_normalize_line(line) for line in chunk.splitlines()]
        lines = [line for line in lines if line]
        if not lines:
            continue
        merged = " ".join(lines)
        sentences = [part.strip() for part in SENTENCE_SPLIT_RE.split(merged) if part.strip()]
        normalized.extend(sentences or [merged])
    return normalized


def _tokenize(text: str) -> List[str]:
    return [tok for tok in TOKEN_RE.findall(text) if len(tok) >= 2]


def _score_tokens(tokens: Sequence[str]) -> Dict[str, float]:
    counts = Counter(tokens)
    scored: Dict[str, float] = {}
    for token, count in counts.items():
        lowered = token.lower()
        if len(token) < 3 and not token.isupper():
            continue
        if lowered in GENERIC_DISCOURSE_TERMS or token in GENERIC_DISCOURSE_TERMS:
            scored[token] = count * 0.08
        else:
            bonus = 1.0
            if re.search(r"[A-Z]", token):
                bonus += 0.25
            if len(token) >= 5:
                bonus += 0.15
            if lowered in DOMAIN_SIGNAL_TERMS or token in DOMAIN_SIGNAL_TERMS:
                bonus += 0.9
            scored[token] = count * bonus
    return scored


def _top_scored_tokens(scored: Dict[str, float], limit: int = 12) -> List[Dict[str, object]]:
    rows = sorted(scored.items(), key=lambda item: item[1], reverse=True)[:limit]
    return [{"value": key, "score": round(value, 3)} for key, value in rows]


def _anchor_bucket(value: str) -> str:
    lowered = value.lower()
    if lowered in GENERIC_DISCOURSE_TERMS or value in GENERIC_DISCOURSE_TERMS:
        return "discourse_residue_anchor"
    if re.fullmatch(r"[A-Z][a-z]+|[A-Z]{2,}", value) or value in {"Dario", "Andrej", "Alex"}:
        return "speaker_or_source_residue_anchor"
    if any(hint.lower() == lowered or hint == value for hints in ROLE_HINTS.values() for hint in hints):
        return "user_layer_hint_anchor"
    return "core_topic_anchor"


def _anchor_bucket_counts(anchors: Sequence[Dict[str, object]], suppressed: Sequence[Dict[str, object]]) -> Dict[str, int]:
    counts: Counter[str] = Counter()
    for row in anchors:
        counts[_anchor_bucket(str(row["value"]))] += 1
    for row in suppressed:
        counts["discourse_residue_anchor"] += int(row["count"])
    return dict(counts)


def _role_gloss(roles: Sequence[str]) -> List[str]:
    return [ROLE_DISPLAY.get(role, role) for role in roles]


def _user_layer_hint_signals(dominant_roles: Sequence[str], secondary_roles: Sequence[str], case_specific_signals: Sequence[str]) -> List[str]:
    hints: List[str] = []
    role_to_hint = {
        "problem_or_constraint_role": "현재 문제/병목",
        "mechanism_role": "구조/작동 원리",
        "verification_or_evaluation_role": "검증/신뢰",
        "control_or_deployment_role": "운영/배치",
        "reflection_or_gap_role": "반성/갭",
    }
    for role in list(dominant_roles) + list(secondary_roles):
        mapped = role_to_hint.get(role)
        if mapped and mapped not in hints:
            hints.append(mapped)
    for signal in case_specific_signals[:3]:
        if signal not in hints:
            hints.append(signal)
    return hints[:6]


def _user_facing_summary(dominant_roles: Sequence[str], secondary_roles: Sequence[str], case_specific_signals: Sequence[str]) -> str:
    gloss = _role_gloss(dominant_roles)
    secondary = _role_gloss(secondary_roles)
    lead = ", ".join(gloss) if gloss else "주요 역할 불명확"
    tail = ", ".join(secondary) if secondary else "보조 역할 약함"
    signals = ", ".join(case_specific_signals[:4]) if case_specific_signals else "신호 약함"
    return f"{lead} 중심으로 읽히고, {tail}가 보조로 붙으며, case-specific signal은 {signals}"


def _suppressed_terms(tokens: Sequence[str], limit: int = 10) -> List[Dict[str, object]]:
    counts = Counter(token for token in tokens if token.lower() in GENERIC_DISCOURSE_TERMS or token in GENERIC_DISCOURSE_TERMS)
    return [{"value": key, "count": value} for key, value in counts.most_common(limit)]


def _aggregate_blocks(blocks: Sequence[str]) -> List[str]:
    aggregated: List[str] = []
    current = ""
    current_sentences = 0
    for block in blocks:
        candidate = block if not current else current + " " + block
        if len(candidate) < 420 and current_sentences < 5:
            current = candidate
            current_sentences += 1
        else:
            if current:
                aggregated.append(current.strip())
            current = block
            current_sentences = 1
    if current.strip():
        aggregated.append(current.strip())
    return aggregated


def _role_scores(text: str, topic_terms: Sequence[str]) -> Dict[str, float]:
    lowered = text.lower()
    scores: Dict[str, float] = {}
    for role, hints in ROLE_HINTS.items():
        score = 0.0
        for hint in hints:
            if hint.lower() in lowered or hint in text:
                score += 1.0
        for token in topic_terms:
            if token.lower() in {hint.lower() for hint in hints}:
                score += 1.25
        scores[role] = score
    return scores


def _infer_block_roles(text: str, top_terms: Sequence[str]) -> Tuple[str, List[str]]:
    scores = _role_scores(text, top_terms)
    ordered = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    primary = ordered[0][0] if ordered and ordered[0][1] > 0 else "problem_or_constraint_role"
    secondary = [role for role, score in ordered[1:3] if score > 0]
    return primary, secondary


def _build_case_blocks(blocks: Sequence[str]) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    for index, block in enumerate(blocks, start=1):
        tokens = _tokenize(block)
        scored = _score_tokens(tokens)
        top_terms = [row["value"] for row in _top_scored_tokens(scored, limit=6)]
        primary_role, secondary_roles = _infer_block_roles(block, top_terms)
        rows.append(
            {
                "block_id": f"block_{index:02d}",
                "role": primary_role,
                "secondary_roles": secondary_roles,
                "top_topic_terms": [{"value": term, "score": next(row["score"] for row in _top_scored_tokens(scored, limit=6) if row["value"] == term)} for term in top_terms],
                "preview": block[:220] + ("..." if len(block) > 220 else ""),
            }
        )
    return rows[:8]


def _role_mix(case_blocks: Sequence[Dict[str, object]], dominant_topic_anchors: Sequence[Dict[str, object]]) -> Tuple[List[str], List[str], List[str], Dict[str, List[str]], List[str], List[str]]:
    role_counts: Counter[str] = Counter()
    evidence: Dict[str, List[str]] = {key: [] for key in ROLE_HINTS}
    signal_terms = [str(row["value"]) for row in dominant_topic_anchors[:8]]

    for block in case_blocks:
        primary = str(block.get("role", "problem_or_constraint_role"))
        role_counts[primary] += 2
        for role in block.get("secondary_roles", []):
            role_counts[str(role)] += 1
        for role in [primary] + [str(role) for role in block.get("secondary_roles", [])]:
            for row in block.get("top_topic_terms", [])[:3]:
                value = str(row.get("value", ""))
                if value and value not in evidence[role]:
                    evidence[role].append(value)

    observer_count = role_counts.get("observer_or_transition_role", 0)
    if observer_count:
        role_counts.pop("observer_or_transition_role", None)
    dominant_roles = [role for role, _ in role_counts.most_common(2)]
    secondary_roles = [role for role, _ in role_counts.most_common(4) if role not in dominant_roles][:2]
    observer_roles = ["observer_or_transition_role"] if observer_count > 0 else []
    frame = dominant_roles + [role for role in secondary_roles if role not in dominant_roles]
    case_specific = [term for term in signal_terms if term.lower() not in GENERIC_DISCOURSE_TERMS][:6]
    trimmed_evidence = {role: terms[:4] for role, terms in evidence.items() if terms}
    return dominant_roles, secondary_roles, observer_roles, trimmed_evidence, case_specific, frame[:4]


def probe_one(input_path: Path) -> ProbeResult:
    raw_text = input_path.read_text(encoding="utf-8")
    raw_paragraph_count = len([chunk for chunk in re.split(r"\n\s*\n+", raw_text.replace("\r\n", "\n").replace("\r", "\n")) if chunk.strip()])
    normalized_blocks = _pre_normalize(raw_text)
    aggregated_blocks = _aggregate_blocks(normalized_blocks)
    all_tokens = [tok for block in aggregated_blocks for tok in _tokenize(block)]
    scored = _score_tokens(all_tokens)
    case_blocks = _build_case_blocks(aggregated_blocks)
    dominant_topic_anchors = _top_scored_tokens(scored)
    dominant_roles, secondary_roles, observer_roles, role_evidence_terms, case_specific_signals, frame = _role_mix(
        case_blocks, dominant_topic_anchors
    )
    suppressed = _suppressed_terms(all_tokens)
    anchor_bucket_counts = _anchor_bucket_counts(dominant_topic_anchors, suppressed)
    user_layer_hint_signals = _user_layer_hint_signals(dominant_roles, secondary_roles, case_specific_signals)
    cautions = [
        "still experimental and read-only",
        "not promotion-ready",
        "speaker-style noise may remain",
    ]
    return ProbeResult(
        input_path=_relative(input_path),
        source_ref=f"{_relative(input_path)}#middle_layer_probe_v0",
        raw_paragraph_count=raw_paragraph_count,
        normalized_block_count=len(aggregated_blocks),
        dominant_topic_anchors=dominant_topic_anchors,
        suppressed_discourse_anchors=suppressed,
        case_blocks=case_blocks,
        provisional_frame_sketch=frame,
        dominant_roles=dominant_roles,
        dominant_role_gloss=_role_gloss(dominant_roles),
        secondary_roles=secondary_roles,
        secondary_role_gloss=_role_gloss(secondary_roles),
        observer_only_roles=observer_roles,
        observer_role_gloss=_role_gloss(observer_roles),
        role_evidence_terms=role_evidence_terms,
        case_specific_signals=case_specific_signals,
        anchor_bucket_counts=anchor_bucket_counts,
        user_layer_hint_signals=user_layer_hint_signals,
        user_facing_summary=_user_facing_summary(dominant_roles, secondary_roles, case_specific_signals),
        caution_notes=cautions,
    )


def main(argv: List[str]) -> int:
    if len(argv) < 2:
        print("usage: run_middle_layer_interview_probe.py <input_a> <input_b> [<input_c> ...]", file=sys.stderr)
        return 1

    input_paths = [Path(arg).resolve() for arg in argv[1:]]
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = _now_compact()
    results = [probe_one(path) for path in input_paths]

    payload = {
        "probe_name": "middle_layer_interview_probe_v1",
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "inputs": [
            {
                "input_path": row.input_path,
                "source_ref": row.source_ref,
                "raw_paragraph_count": row.raw_paragraph_count,
                "normalized_block_count": row.normalized_block_count,
                "dominant_topic_anchors": row.dominant_topic_anchors,
                "suppressed_discourse_anchors": row.suppressed_discourse_anchors,
                "case_blocks": row.case_blocks,
                "provisional_frame_sketch": row.provisional_frame_sketch,
                "dominant_roles": row.dominant_roles,
                "dominant_role_gloss": row.dominant_role_gloss,
                "secondary_roles": row.secondary_roles,
                "secondary_role_gloss": row.secondary_role_gloss,
                "observer_only_roles": row.observer_only_roles,
                "observer_role_gloss": row.observer_role_gloss,
                "role_evidence_terms": row.role_evidence_terms,
                "case_specific_signals": row.case_specific_signals,
                "anchor_bucket_counts": row.anchor_bucket_counts,
                "user_layer_hint_signals": row.user_layer_hint_signals,
                "user_facing_summary": row.user_facing_summary,
                "caution_notes": row.caution_notes,
            }
            for row in results
        ],
    }
    output_path = OUTPUT_DIR / f"middle_layer_interview_probe_{stamp}.json"
    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"output_path": _relative(output_path), "case_count": len(results)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
