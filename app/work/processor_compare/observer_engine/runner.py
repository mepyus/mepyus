from __future__ import annotations

from .feature_extractor import extract_features
from .merger import merge_observer_outputs
from .profiles import codex_like_observer, chatgpt_like_observer, gemini_like_observer


def run_internal_observers(text: str):
    features = extract_features(text)
    codex = codex_like_observer(features)
    chatgpt = chatgpt_like_observer(features)
    gemini = gemini_like_observer(features)
    merged = merge_observer_outputs([codex, chatgpt, gemini])
    return {
        "features": features.to_record(),
        "codex_like": codex.to_record(),
        "chatgpt_like": chatgpt.to_record(),
        "gemini_like": gemini.to_record(),
        "merged": merged.to_record(),
    }
