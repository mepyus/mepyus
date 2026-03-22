from __future__ import annotations

from collections import defaultdict
from typing import Dict, Iterable, List
import re

from .dictionaries import alias_entries, discourse_stopwords, particle_suffixes, weak_generic_nouns
from .normalize import normalize_record
from .score import build_anchor_statistics, enrich_with_statistics, score_bridge_anchors, score_region_representatives
from .typing import assign_anchor_type
from .weak_filter import compute_weakness_penalty, promotable_after_weak_filter, should_drop_weak_anchor


ASCII_TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9.+#/_-]*")
MIXED_TECH_RE = re.compile(r"[A-Za-z0-9.+#/_-]+(?:\s+[A-Za-z0-9.+#/_-]+){0,2}")
WORD_RE = re.compile(r"[A-Za-z0-9.+#/_-]+|[가-힣]+")
SENTENCE_SPLIT_RE = re.compile(r"[.!?\n]+")
SKIP_PHRASES = {
    "있게 된다",
    "있게 한다",
    "에서 부터",
    "할 수 있다",
    "할 수 있는",
}
BAD_TAILS = ("다", "고", "게", "며", "자", "죠", "요")
BAD_PARTS = {
    "있습니다",
    "있다",
    "있고",
    "있을",
    "있게",
    "된다",
    "되다",
    "이다",
    "입니다",
    "것이다",
    "됩니다",
    "활용할",
    "생각해",
    "대하여",
    "통하여",
    "위한",
    "위해",
    "때문에",
    "그러니까",
    "a",
    "b",
    "c",
}
COMPOUND_HEADS = {
    "엔지니어링",
    "타입",
    "레이어",
    "엔진",
    "파이프라인",
    "프로토콜",
    "모델",
    "시스템",
    "인터페이스",
    "전이",
    "추출",
    "정규화",
    "승격",
    "문학",
    "우화",
}
STOPWORDS = {value.lower() for value in discourse_stopwords()}
GENERIC_NOUNS = {value.lower() for value in weak_generic_nouns()}
PARTICLE_TOKENS = set(particle_suffixes())


def run_anchor_pipeline(documents: Iterable[Dict[str, object]]) -> Dict[str, object]:
    docs = list(documents)
    candidates = []
    for doc in docs:
        candidates.extend(extract_candidates(doc))

    normalized = [normalize_record(candidate) for candidate in candidates]
    typed = [assign_anchor_type(record) for record in normalized]
    stats = build_anchor_statistics(typed)

    enriched = []
    dropped_weak = []
    for item in typed:
        working = dict(item)
        working["weakness_penalty"] = compute_weakness_penalty(working)
        if should_drop_weak_anchor(working):
            dropped_weak.append(working)
            continue
        enriched.append(enrich_with_statistics(working, stats, len(docs)))

    promoted = [row for row in enriched if row.get("promoted")]

    by_doc = defaultdict(list)
    for row in promoted:
        by_doc[str(row["doc_id"])].append(row)

    region_summary = []
    for doc in docs:
        doc_id = str(doc["doc_id"])
        reps = score_region_representatives(by_doc.get(doc_id, []))
        region_summary.append(
            {
                "region_id": doc_id,
                "representative_anchors": [
                    {
                        "canonical_key": row["canonical_key"],
                        "display_label": row["display_label"],
                        "anchor_type": row["anchor_type"],
                        "region_anchor_score": row["region_anchor_score"],
                    }
                    for row in reps
                ],
                "supporting_anchors": [
                    row["display_label"]
                    for row in sorted(by_doc.get(doc_id, []), key=lambda item: item.get("strong_score", 0.0), reverse=True)[5:10]
                ],
                "dropped_weak_anchors": [
                    row["candidate_text"]
                    for row in dropped_weak
                    if str(row["doc_id"]) == doc_id
                ][:10],
            }
        )

    bridge_summary = []
    for index, left in enumerate(docs):
        for right in docs[index + 1 :]:
            left_rows = by_doc.get(str(left["doc_id"]), [])
            right_rows = by_doc.get(str(right["doc_id"]), [])
            shared = score_bridge_anchors(left_rows, right_rows)
            if not shared:
                continue
            bridge_summary.append(
                {
                    "bridge_id": f"bridge_{left['doc_id']}_{right['doc_id']}",
                    "left_region_id": left["doc_id"],
                    "right_region_id": right["doc_id"],
                    "shared_anchors": [
                        {
                            "canonical_key": row["canonical_key"],
                            "display_label": row["display_label"],
                            "anchor_type": row["anchor_type"],
                            "bridge_score": row["bridge_score"],
                        }
                        for row in shared[:5]
                    ],
                    "rejected_overlap_anchors": _rejected_overlap(left_rows, right_rows),
                }
            )

    return {
        "candidates": candidates,
        "normalized": enriched,
        "dropped_weak": dropped_weak,
        "promoted": promoted,
        "region_summary": region_summary,
        "bridge_summary": bridge_summary,
    }


def extract_promoted_anchors_for_text(
    text: str,
    *,
    doc_id: str = "inline_doc",
    title: str = "",
    source_type: str = "inline",
) -> List[Dict[str, object]]:
    payload = run_anchor_pipeline(
        [
            {
                "doc_id": doc_id,
                "title": title,
                "text": text,
                "sections": [{"section_id": "body", "heading": "", "text": text}],
                "metadata": {"source_type": source_type},
            }
        ]
    )
    rows = [row for row in payload["promoted"] if str(row["doc_id"]) == doc_id]
    if not rows:
        fallback_rows = [row for row in payload["normalized"] if str(row["doc_id"]) == doc_id]
        fallback_rows = [
            row
            for row in fallback_rows
            if bool(row.get("alias_matched"))
            and float(row.get("weakness_penalty", 0.0)) < 0.40
            and float(row.get("specificity_score", 0.0)) >= 0.72
            and str(row.get("anchor_type", "semantic")) in {"semantic", "object", "process", "structural"}
        ]
        rows = fallback_rows
    rows.sort(key=lambda row: (float(row.get("strong_score", 0.0)), float(row.get("specificity_score", 0.0))), reverse=True)
    return rows


def extract_candidates(doc: Dict[str, object]) -> List[Dict[str, object]]:
    candidates: List[Dict[str, object]] = []
    doc_id = str(doc["doc_id"])
    title = str(doc.get("title", "")).strip()
    if title:
        candidates.extend(_extract_from_unit(doc_id, "title", title, "title"))
    sections = list(doc.get("sections", []))
    if sections:
        for section in sections:
            section_id = str(section.get("section_id", "body"))
            heading = str(section.get("heading", "")).strip()
            if heading:
                candidates.extend(_extract_from_unit(doc_id, section_id, heading, "heading"))
            candidates.extend(_extract_from_unit(doc_id, section_id, str(section.get("text", "")), "body"))
    else:
        candidates.extend(_extract_from_unit(doc_id, "body", str(doc.get("text", "")), "body"))
    return candidates


def _extract_from_unit(doc_id: str, section_id: str, text: str, position: str) -> List[Dict[str, object]]:
    rows = []
    seen = set()
    for phrase, start, end in _extract_alias_phrases(text):
        _append_candidate(rows, seen, doc_id, section_id, text, position, phrase, start, end)
    for match in MIXED_TECH_RE.finditer(text):
        phrase = " ".join(match.group(0).split())
        if not _is_candidate_phrase(phrase):
            continue
        _append_candidate(rows, seen, doc_id, section_id, text, position, phrase, match.start(), match.end())
    for sentence in _iter_sentences(text):
        tokens = _tokenize_sentence(sentence["text"])
        for phrase, rel_start, rel_end in _extract_ngram_candidates(tokens, position):
            _append_candidate(
                rows,
                seen,
                doc_id,
                section_id,
                text,
                position,
                phrase,
                sentence["start"] + rel_start,
                sentence["start"] + rel_end,
            )
    return rows


def _is_candidate_phrase(phrase: str) -> bool:
    if len(phrase.strip()) < 2:
        return False
    parts = phrase.split()
    if len(parts) > 3:
        return False
    if any(part in BAD_PARTS for part in parts):
        return False
    if _contains_ascii_signal(phrase):
        return True
    if len(parts) == 1:
        token = parts[0]
        if token.endswith(BAD_TAILS):
            return False
        return len(token) >= 2
    for part in parts:
        if part.endswith(BAD_TAILS):
            return False
    return True


def _contains_ascii_signal(phrase: str) -> bool:
    return any(ch.isascii() and ch.isalpha() for ch in phrase)


def _rejected_overlap(left_rows: List[Dict[str, object]], right_rows: List[Dict[str, object]]) -> List[str]:
    left_keys = {str(row["canonical_key"]): row for row in left_rows}
    right_keys = {str(row["canonical_key"]): row for row in right_rows}
    rejected = []
    for key in sorted(set(left_keys) & set(right_keys)):
        if not promotable_after_weak_filter(left_keys[key]) or not promotable_after_weak_filter(right_keys[key]):
            rejected.append(left_keys[key]["display_label"])
    return rejected[:8]


def _append_candidate(
    rows: List[Dict[str, object]],
    seen: set[str],
    doc_id: str,
    section_id: str,
    text: str,
    position: str,
    phrase: str,
    start: int,
    end: int,
) -> None:
    phrase = " ".join(phrase.split()).strip()
    if not phrase or phrase in SKIP_PHRASES:
        return
    lowered = phrase.lower()
    if lowered in seen:
        return
    seen.add(lowered)
    rows.append(
        {
            "doc_id": doc_id,
            "section_id": section_id,
            "candidate_text": phrase,
            "span_start": start,
            "span_end": end,
            "context_window": text[max(0, start - 40) : min(len(text), end + 40)],
            "source_position": position,
            "phrase_len": len(phrase.split()),
            "language_mode": "ko",
        }
    )


def _extract_alias_phrases(text: str) -> List[tuple[str, int, int]]:
    hits: List[tuple[str, int, int]] = []
    lowered = text.lower()
    for entry in alias_entries():
        for alias in sorted((str(a) for a in entry.get("aliases", [])), key=len, reverse=True):
            alias_lower = alias.lower()
            if _alias_is_ascii(alias):
                pattern = re.compile(rf"(?<![A-Za-z0-9_]){re.escape(alias_lower)}(?![A-Za-z0-9_])")
                for match in pattern.finditer(lowered):
                    hits.append((text[match.start() : match.end()], match.start(), match.end()))
                continue
            start = 0
            while True:
                index = lowered.find(alias_lower, start)
                if index < 0:
                    break
                hits.append((text[index : index + len(alias)], index, index + len(alias)))
                start = index + len(alias_lower)
    hits.sort(key=lambda row: (row[1], -(row[2] - row[1])))
    return hits


def _iter_sentences(text: str) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    start = 0
    for piece in SENTENCE_SPLIT_RE.split(text):
        if not piece.strip():
            start += len(piece) + 1
            continue
        index = text.find(piece, start)
        if index < 0:
            index = start
        rows.append({"text": piece, "start": index})
        start = index + len(piece)
    return rows


def _alias_is_ascii(alias: str) -> bool:
    return any(ch.isascii() and ch.isalpha() for ch in alias)


def _tokenize_sentence(text: str) -> List[Dict[str, object]]:
    return [{"text": m.group(0), "start": m.start(), "end": m.end()} for m in WORD_RE.finditer(text)]


def _extract_ngram_candidates(tokens: List[Dict[str, object]], position: str) -> List[tuple[str, int, int]]:
    results: List[tuple[str, int, int]] = []
    for index, token in enumerate(tokens):
        word = str(token["text"])
        if _is_single_token_candidate(word, position):
            results.append((word, int(token["start"]), int(token["end"])))
        if index + 1 < len(tokens):
            phrase = f"{word} {tokens[index + 1]['text']}"
            if _is_compound_candidate(phrase, position):
                results.append((phrase, int(token["start"]), int(tokens[index + 1]["end"])))
        if index + 2 < len(tokens):
            phrase = f"{word} {tokens[index + 1]['text']} {tokens[index + 2]['text']}"
            if _is_compound_candidate(phrase, position):
                results.append((phrase, int(token["start"]), int(tokens[index + 2]["end"])))
    return results


def _is_single_token_candidate(token: str, position: str) -> bool:
    token = token.strip()
    if not token or token.lower() in STOPWORDS or token in PARTICLE_TOKENS:
        return False
    if token[0] in "/-–—" or token[-1] in "/-–—":
        return False
    if _contains_ascii_signal(token):
        return len(token) >= 2 and token.lower() not in {"the", "and", "for", "with"} and not token.lower().startswith(("a ", "b ", "c "))
    if len(token) < 2:
        return False
    if token in BAD_PARTS or token.endswith(BAD_TAILS):
        return False
    lowered = token.lower()
    if lowered in GENERIC_NOUNS:
        return position in {"title", "heading"} and len(token) >= 3
    return True


def _is_compound_candidate(phrase: str, position: str) -> bool:
    parts = [part.strip() for part in phrase.split() if part.strip()]
    if len(parts) < 2 or len(parts) > 3:
        return False
    if phrase.startswith(("/", "-", "–", "—")) or phrase.endswith(("/", "-", "–", "—")):
        return False
    if any(part in PARTICLE_TOKENS for part in parts):
        return False
    if any(part.lower() in {"a", "b", "c"} for part in parts):
        return False
    if any(part.lower() in STOPWORDS for part in parts):
        return False
    if any(part in BAD_PARTS or part.endswith(BAD_TAILS) for part in parts):
        return False
    if all(part.lower() in GENERIC_NOUNS for part in parts):
        return False
    if any(_contains_ascii_signal(part) for part in parts):
        return True
    head = parts[-1]
    if head in COMPOUND_HEADS:
        return True
    if position in {"title", "heading"} and all(_is_single_token_candidate(part, position) for part in parts):
        return True
    return False
