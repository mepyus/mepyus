from __future__ import annotations

from typing import Dict

from .dictionaries import acronym_whitelist, discourse_stopwords, weak_generic_nouns


PHRASE_NOISE_PARTS = {
    "하는",
    "있게",
    "된다",
    "한다",
    "했다",
    "수",
    "있는",
    "있다",
    "부터",
    "에서",
}


def compute_weakness_penalty(item: Dict[str, object], distinctiveness_hint: float = 0.5) -> float:
    text = str(item.get("normalized_text", "")).strip()
    display = str(item.get("display_label", "")).strip()
    penalty = 0.0
    stopwords = {value.lower() for value in discourse_stopwords()}
    generic = {value.lower() for value in weak_generic_nouns()}
    tokens = [part for part in text.replace("_", " ").split() if part]

    if text in stopwords:
        penalty += 0.60
    if any(token in stopwords for token in tokens):
        penalty += 0.30
    if text in generic and " " not in text and "_" not in text:
        penalty += 0.35
    if tokens and all(token in generic or token in PHRASE_NOISE_PARTS for token in tokens):
        penalty += 0.40
    if any(token in PHRASE_NOISE_PARTS for token in tokens):
        penalty += 0.25
    if _is_short_non_domain_token(display):
        penalty += 0.20
    if _is_verb_surface(text):
        penalty += 0.25
    if distinctiveness_hint < 0.20:
        penalty += 0.20

    return min(1.0, round(penalty, 3))


def should_drop_weak_anchor(item: Dict[str, object]) -> bool:
    penalty = float(item.get("weakness_penalty", 0.0))
    return penalty >= 0.75


def promotable_after_weak_filter(item: Dict[str, object]) -> bool:
    penalty = float(item.get("weakness_penalty", 0.0))
    return penalty < 0.40


def _is_short_non_domain_token(display: str) -> bool:
    if display in acronym_whitelist():
        return False
    compact = display.replace(" ", "")
    return len(compact) <= 2


def _is_verb_surface(text: str) -> bool:
    return (
        text.endswith("하다")
        or text.endswith("되다")
        or text.endswith("있게")
        or text.endswith("된다")
        or text.endswith("했다")
    )
