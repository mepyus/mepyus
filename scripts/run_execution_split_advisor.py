#!/usr/bin/env python3
"""Advise whether a task should be handled by Codex, a space script, or both."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List


REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = REPO_ROOT / "runtime" / "manifests" / "executable_capability_registry_v0.json"


SCRIPT_FIRST_SAFETY = {
    "stdout_only",
    "workspace_generated_only",
    "generated_output_only",
    "plan_only_default",
    "sandbox_only",
}

SCRIPTISH_CLASSES = {
    "inputter_probe",
    "loop_probe",
    "validation_chain",
    "sandbox_probe",
    "loop",
    "grounded_feed",
    "summary_sink",
}

CODEX_JUDGMENT_HINTS = [
    "분석",
    "구조화",
    "보고",
    "리포트",
    "attach",
    "adopt",
    "적용",
    "방향",
    "가능성",
    "방법",
    "판단",
    "compare",
    "map",
    "structure",
    "report",
    "analysis",
]

EXTERNAL_SCOPE_HINTS = [
    "git_search",
    "references/",
    "외부도구",
    "외부 도구",
    "외부 repo",
    "external repo",
    "repo",
    "reference",
]


def _load_registry() -> Dict[str, Any]:
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def _normalize(text: str) -> str:
    return " ".join(text.lower().split())


def _match_capabilities(intent: str, capabilities: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    norm = _normalize(intent)
    matches: List[Dict[str, Any]] = []
    for cap in capabilities:
        aliases = [_normalize(alias) for alias in cap.get("intent_aliases", [])]
        label = _normalize(cap.get("label", ""))
        if any(alias and alias in norm for alias in aliases) or (label and label in norm):
            matches.append(cap)
    return matches


def _has_judgment_pressure(intent: str) -> bool:
    norm = _normalize(intent)
    return any(hint in norm for hint in CODEX_JUDGMENT_HINTS)


def _has_external_scope_pressure(intent: str) -> bool:
    norm = _normalize(intent)
    return any(hint in norm for hint in EXTERNAL_SCOPE_HINTS)


def _decide_mode(intent: str, matches: List[Dict[str, Any]]) -> str:
    if _has_external_scope_pressure(intent) and _has_judgment_pressure(intent):
        return "hybrid"
    if not matches:
        return "codex-first"
    if _has_judgment_pressure(intent):
        return "hybrid"
    if all(
        cap.get("safety_mode") in SCRIPT_FIRST_SAFETY or cap.get("capability_class") in SCRIPTISH_CLASSES
        for cap in matches
    ):
        return "space-script-first"
    return "hybrid"


def _why(mode: str, intent: str, matches: List[Dict[str, Any]]) -> List[str]:
    reasons: List[str] = []
    if not matches:
        reasons.append("No direct capability alias match was found in the executable capability registry.")
        if _has_external_scope_pressure(intent) and _has_judgment_pressure(intent):
            reasons.append("The task still names external repo scope plus analysis/structuring pressure, so it should use a hybrid path.")
        else:
            reasons.append("The task should begin with Codex-side interpretation and asset selection.")
        return reasons
    reasons.append(f"Matched {len(matches)} executable capability candidates from the registry.")
    if mode == "space-script-first":
        reasons.append("The matched capabilities are probe/validation/loop surfaces with bounded safety modes.")
        reasons.append("The task can begin by collecting evidence through scripts before deeper interpretation.")
    elif mode == "hybrid":
        reasons.append("The task contains scriptable evidence-gathering surfaces and Codex-side judgment/structuring pressure.")
        reasons.append("Use scripts to gather bounded evidence, then let Codex synthesize, compare, or package the result.")
    else:
        reasons.append("Even though related capabilities exist, the request reads mainly as analysis/judgment rather than direct runner invocation.")
    if _has_judgment_pressure(intent):
        reasons.append("The request contains analysis/structuring/report pressure, so final judgment should remain Codex-side.")
    return reasons


def _build_output(intent: str) -> Dict[str, Any]:
    registry = _load_registry()
    capabilities = registry.get("capabilities", [])
    matches = _match_capabilities(intent, capabilities)
    mode = _decide_mode(intent, matches)
    return {
        "intent": intent,
        "recommended_mode": mode,
        "matched_capabilities": [
            {
                "capability_id": cap.get("capability_id"),
                "capability_class": cap.get("capability_class"),
                "label": cap.get("label"),
                "safety_mode": cap.get("safety_mode"),
                "entrypoint_refs": cap.get("entrypoint_refs", []),
                "output_surfaces": cap.get("output_surfaces", []),
            }
            for cap in matches
        ],
        "codex_should_do": [
            "interpret the request in user-purpose terms",
            "choose related internal assets and boundaries",
            "synthesize findings into report/structure/judgment",
        ],
        "space_scripts_should_do": [
            "bounded probes",
            "validation chains",
            "generated evidence collection",
        ],
        "why": _why(mode, intent, matches),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("intent", help="Natural-language task or intent")
    args = parser.parse_args()
    print(json.dumps(_build_output(args.intent), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
