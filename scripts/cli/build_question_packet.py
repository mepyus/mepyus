#!/usr/bin/env python3
"""Build a Phase 1 question interpretation packet draft."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Optional

from identity_helpers import build_identity_anchor


MODE_KEYWORDS = {
    "exploration": ("find", "where", "read", "map", "asset", "explore", "찾", "읽", "지도", "탐색", "어디"),
    "comparison": ("compare", "versus", "vs", "diff", "conflict", "비교", "차이", "충돌"),
    "merge": ("merge", "combine", "align", "합", "병합", "정렬"),
    "verification": ("verify", "validate", "check", "검증", "확인", "점검"),
    "reflection_support": ("why", "explain", "meaning", "rationale", "왜", "의미", "해석", "설명"),
}

STOP_KEYWORDS = {
    "authority_conflict": ("replace baseline", "baseline replace", "replace the authority", "replace the grounded contract", "contract meaning", "authority", "constitution", "baseline을 대체", "권위", "헌법"),
    "destructive_move_required": ("delete", "remove", "rename", "move canonical", "move runtime", "move runtime contract", "move runtime contract paths", "move comparison artifact", "move comparison artifact paths", "move artifact path", "move artifact paths", "move artifact naming", "move artifact naming rules", "대량", "삭제", "이동", "rename"),
    "final_naming_lock_required": ("final name", "final-lock", "final lock", "final field", "final change type", "change type lock", "final family taxonomy", "family confidence taxonomy", "pair confidence taxonomy", "identity field taxonomy", "final lineage taxonomy", "final identity", "final pairing lock", "pairing taxonomy", "labeling lock", "field/path labeling lock", "naming lock", "official name", "최종 명명", "공식 명명", "네이밍"),
    "structurally_meaningful_options_gt_1": ("option a", "option b", "two options", "둘 다", "양쪽", "대안"),
}


def infer_mode(request: str, explicit_mode: Optional[str]) -> str:
    if explicit_mode:
        return explicit_mode
    lowered = request.lower()
    scores = {
        mode: sum(1 for keyword in keywords if keyword in lowered)
        for mode, keywords in MODE_KEYWORDS.items()
    }
    best_mode, best_score = max(scores.items(), key=lambda item: item[1])
    return best_mode if best_score else "exploration"


def infer_stop_conditions(request: str) -> list[dict]:
    lowered = request.lower()
    hits = []
    for stop_type, keywords in STOP_KEYWORDS.items():
        matched = [keyword for keyword in keywords if keyword in lowered]
        if matched:
            hits.append(
                {
                    "type": stop_type,
                    "matched_terms": matched,
                    "decision_required": True,
                }
            )
    return hits


def infer_search_targets(mode: str, stop_conditions: list[dict], request: str = "") -> list[dict]:
    targets = [
        {
            "path": "docs/specs/space_cli_phase1_goal_and_non_goal_v0.md",
            "reason": "Phase 1 goal and non-goal boundary.",
            "authority_expectation": "policy_or_contract",
        },
        {
            "path": "docs/specs/space_reading_order_for_codex_v0.md",
            "reason": "Default first-entry reading order.",
            "authority_expectation": "policy_or_contract",
        },
        {
            "path": "docs/specs/source_authority_ladder_v0.md",
            "reason": "Authority resolution before merge/diff/hold.",
            "authority_expectation": "policy_or_contract",
        },
    ]
    if mode in {"exploration", "extraction"}:
        targets.append(
            {
                "path": "docs/guides/question_type_to_search_path_map_v0.md",
                "reason": "Question type to search path mapping.",
                "authority_expectation": "guide_or_index",
            }
        )
    if mode in {"comparison", "merge", "verification"}:
        targets.append(
            {
                "path": "docs/specs/evidence_merge_diff_hold_contract_v0.md",
                "reason": "Mode and comparison contract.",
                "authority_expectation": "policy_or_contract",
            }
        )
    if mode == "reflection_support":
        targets.append(
            {
                "path": "docs/specs/question_interpretation_contract_v0.md",
                "reason": "Interpretation-before-retrieval contract.",
                "authority_expectation": "policy_or_contract",
            }
        )
    targets.append(
        {
            "path": "docs/specs/evidence_unit_grounding_contract_v0.md",
            "reason": "Grounded evidence fields and pointer fallback.",
            "authority_expectation": "policy_or_contract",
        }
    )
    targets.append(
        {
            "path": "docs/specs/merge_diff_hold_grounding_rules_v0.md",
            "reason": "Evidence depth rules for merge/diff/hold.",
            "authority_expectation": "policy_or_contract",
        }
    )
    if any(term in request.lower() for term in ("structured", "json", "runtime", "generated", "contract", "field", "path", "shape")):
        targets.extend(
            [
                {
                    "path": "docs/specs/structured_evidence_contract_v0.md",
                    "reason": "Structured field/path evidence contract.",
                    "authority_expectation": "policy_or_contract",
                },
                {
                    "path": "docs/specs/structured_merge_diff_rules_v0.md",
                    "reason": "Structured evidence merge/diff rules.",
                    "authority_expectation": "policy_or_contract",
                },
            ]
        )
    weak_pair_stress = any(term in request.lower() for term in ("weak pair", "unrelated", "ambiguous"))
    if any(term in request.lower() for term in ("diff", "compare", "comparison", "before", "after", "changed", "delta", "version shift")):
        targets.extend(
            [
                {
                    "path": "docs/specs/diff_evidence_contract_v0.md",
                    "reason": "Before/after changed path diff evidence contract.",
                    "authority_expectation": "policy_or_contract",
                },
                {
                    "path": "docs/specs/diff_aware_merge_hold_rules_v0.md",
                    "reason": "Diff salience rules for merge/diff/hold.",
                    "authority_expectation": "policy_or_contract",
                },
            ]
        )
        if not weak_pair_stress:
            targets.extend(
                [
                {
                    "path": "runtime/merge_diff_reports/phase1_7_run_03_merge_diff_report.json",
                    "reason": "Before generated diff-heavy merge report sample.",
                    "authority_expectation": "runtime_artifact",
                },
                {
                    "path": "runtime/merge_diff_reports/phase1_8_run_03_merge_diff_report.json",
                    "reason": "After structured diff-heavy merge report sample.",
                    "authority_expectation": "runtime_artifact",
                },
                ]
            )
    if any(term in request.lower() for term in ("pair", "pairing", "family", "lineage", "same-family", "same family", "version lineage")):
        targets.extend(
            [
                {
                    "path": "docs/specs/artifact_family_pairing_contract_v0.md",
                    "reason": "Artifact family and pair confidence contract.",
                    "authority_expectation": "policy_or_contract",
                },
                {
                    "path": "docs/specs/pairing_aware_diff_rules_v0.md",
                    "reason": "Pair confidence rules for diff and hold judgment.",
                    "authority_expectation": "policy_or_contract",
                },
            ]
        )
        if not weak_pair_stress:
            targets.extend(
                [
                {
                    "path": "runtime/merge_diff_reports/phase1_8_run_03_merge_diff_report.json",
                    "reason": "Before same-family generated merge report candidate.",
                    "authority_expectation": "runtime_artifact",
                },
                {
                    "path": "runtime/merge_diff_reports/phase1_9_run_03_merge_diff_report.json",
                    "reason": "After same-family generated merge report candidate.",
                    "authority_expectation": "runtime_artifact",
                },
                ]
            )
    if any(term in request.lower() for term in ("identity", "anchor", "self-description", "self description", "run context", "role", "logical slot")):
        weak_identity_stress = any(term in request.lower() for term in ("weak identity", "unrelated", "ambiguous"))
        targets.extend(
            [
                {
                    "path": "docs/specs/artifact_identity_anchor_contract_v0.md",
                    "reason": "Artifact identity anchor contract.",
                    "authority_expectation": "policy_or_contract",
                },
                {
                    "path": "docs/specs/identity_aware_pairing_rules_v0.md",
                    "reason": "Identity-aware pairing and comparison rules.",
                    "authority_expectation": "policy_or_contract",
                },
            ]
        )
        if not weak_identity_stress:
            targets.extend(
                [
                {
                    "path": "runtime/merge_diff_reports/phase1_10_run_01_merge_diff_report.json",
                    "reason": "Prior pairing-aware generated report sample.",
                    "authority_expectation": "runtime_artifact",
                },
                {
                    "path": "runtime/merge_diff_reports/phase1_10_run_02_merge_diff_report.json",
                    "reason": "Prior pairing-aware generated report sample for lineage comparison.",
                    "authority_expectation": "runtime_artifact",
                },
                {
                    "path": "runtime/merge_diff_reports/phase1_11_run_01_merge_diff_report.json",
                    "reason": "Current identity-aware generated report sample when available.",
                    "authority_expectation": "runtime_artifact",
                },
                {
                    "path": "runtime/merge_diff_reports/phase1_11_run_02_merge_diff_report.json",
                    "reason": "Current identity-aware generated report sample when available.",
                    "authority_expectation": "runtime_artifact",
                },
                ]
            )
    lowered = request.lower()
    if any(term in lowered for term in ("legacy", "backfill", "old/new", "old vs new", "old vs old")):
        targets.extend(
            [
                {
                    "path": "docs/specs/legacy_artifact_identity_backfill_contract_v0.md",
                    "reason": "Legacy identity backfill mode and confidence ceiling contract.",
                    "authority_expectation": "policy_or_contract",
                },
                {
                    "path": "docs/indexes/legacy_artifact_family_identity_map_v0.json",
                    "reason": "Machine-readable bounded legacy identity backfill map.",
                    "authority_expectation": "guide_or_index",
                },
                {
                    "path": "docs/specs/lower_to_upper_bridge_minimum_v0.md",
                    "reason": "Pre-1.12B bridge guardrail for readiness and upper admission.",
                    "authority_expectation": "policy_or_contract",
                },
                {
                    "path": "runtime/merge_diff_reports/phase1_8_run_03_merge_diff_report.json",
                    "reason": "Legacy old merge/diff report from pre-identity spine.",
                    "authority_expectation": "runtime_artifact",
                },
                {
                    "path": "runtime/merge_diff_reports/phase1_9_run_03_merge_diff_report.json",
                    "reason": "Legacy old merge/diff report from same normalized run family.",
                    "authority_expectation": "runtime_artifact",
                },
                {
                    "path": "runtime/merge_diff_reports/phase1_10_run_03_merge_diff_report.json",
                    "reason": "Pairing-era report before inline identity emission.",
                    "authority_expectation": "runtime_artifact",
                },
                {
                    "path": "runtime/merge_diff_reports/phase1_11_run_03_merge_diff_report.json",
                    "reason": "Identity-era report for old/new mixed comparison.",
                    "authority_expectation": "runtime_artifact",
                },
                {
                    "path": "app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json",
                    "reason": "Legacy lower packet-candidate comparison artifact for bridge guardrail check.",
                    "authority_expectation": "runtime_artifact",
                },
                {
                    "path": "app/work/external_input_preprocess/generated/builder_jang_interview_transcript_preprocess_comparison.json",
                    "reason": "Legacy external preprocess comparison artifact for ambiguous family checks.",
                    "authority_expectation": "runtime_artifact",
                },
            ]
        )
    if "runtime" in lowered or "generated" in lowered or "json" in lowered or ("structured" in lowered and "contract" in lowered):
        targets.extend(
            [
                {
                    "path": "runtime/contracts/space_exploration_result_v1.json",
                    "reason": "Runtime JSON exploration contract stress target.",
                    "authority_expectation": "runtime_artifact",
                },
                {
                    "path": "runtime/contracts/merge_diff_report_v1.json",
                    "reason": "Runtime JSON merge report contract stress target.",
                    "authority_expectation": "runtime_artifact",
                },
                {
                    "path": "runtime/contracts/space_reingress_record_v1.json",
                    "reason": "Runtime JSON reingress contract stress target.",
                    "authority_expectation": "runtime_artifact",
                },
            ]
        )
    if stop_conditions:
        targets.append(
            {
                "path": "docs/specs/phase1_5_decision_gate_rules_v0.md",
                "reason": "Phase 1.5 stop and decision gate rules.",
                "authority_expectation": "policy_or_contract",
            }
        )
    return targets


def infer_merge_mode(mode: str, stop_conditions: list[dict]) -> str:
    if stop_conditions:
        return "hold"
    if mode == "comparison":
        return "diff"
    return "merge"


def build_packet(request: str, mode: Optional[str] = None) -> dict:
    task_mode = infer_mode(request, mode)
    stop_conditions = infer_stop_conditions(request)
    search_targets = infer_search_targets(task_mode, stop_conditions, request)
    merge_mode = infer_merge_mode(task_mode, stop_conditions)
    interpreted_goal = (
        "Translate the user request into a Phase 1.5 CLI usage-loop artifact set "
        f"and handle it as {task_mode}."
    )
    return {
        "contract_id": "question_interpretation_packet_v0",
        "contract_status": "draft_instance",
        "user_request_raw": request,
        "interpreted_goal": interpreted_goal,
        "task_mode": task_mode,
        "scope": {
            "repo_paths": [],
            "time_boundary": "",
            "phase_boundary": "phase1_5_usage_loop_binding",
            "non_goals": [
                "ui_work",
                "react_vite",
                "multi_agent_orchestration",
                "baseline_promotion",
                "final_naming_lock",
                "destructive_migration",
                "deep_automation",
            ],
        },
        "constraints": {
            "must_not_do": ["change_existing_baseline_meaning", "move_canonical_paths"],
            "must_preserve": ["existing_authority_structure", "canonical_paths"],
            "stop_conditions": stop_conditions,
        },
        "expected_output_shape": {
            "primary": "artifact_set",
            "required_sections": [
                "question_packet",
                "exploration_result",
                "merge_diff_report",
                "reingress_record",
            ],
        },
        "search_targets": search_targets,
        "external_reasoning_needed": False,
        "merge_mode_candidate": merge_mode,
        "ambiguity_notes": [
            {
                "kind": "provisional" if not stop_conditions else "hard_hold",
                "note": "Rule-based inference; operator may refine after reading selected assets.",
                "handling": "proceed" if not stop_conditions else "decision_gate",
            }
        ],
        "hold_reason_if_any": "; ".join(item["type"] for item in stop_conditions),
        "packet_validation": {
            "ready_for_exploration": True,
            "validation_notes": [
                "Phase 1.5 rule-based packet is ready for bounded exploration.",
            ],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("request")
    parser.add_argument("--mode", choices=list(MODE_KEYWORDS.keys()))
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    packet = build_packet(args.request, args.mode)
    if args.out:
        packet["artifact_identity"] = build_identity_anchor(str(args.out), "question_packet")
        text = json.dumps(packet, ensure_ascii=False, indent=2) + "\n"
        args.out.write_text(text, encoding="utf-8")
    else:
        text = json.dumps(packet, ensure_ascii=False, indent=2) + "\n"
        print(text, end="")


if __name__ == "__main__":
    main()
