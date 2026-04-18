from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Tuple
import html
import json
import re

from app.runtime.vectorfl_page_semi_live_shell import build_vectorfl_page_semi_live_state
from app.runtime.vectorfl_page_semi_live_trace_detail import _slugify_trace_id


OPERABLE_SURFACES = [
    "cases",
    "case-detail",
    "case-inspector",
    "case-routing",
    "internal-recall",
    "external-resources",
    "lane-runs",
    "organs",
    "organ-registry",
    "trace-audit",
]


ORGAN_SPECS: Dict[str, Dict[str, str]] = {
    "input": {
        "label": "Input Organ",
        "role": "docs/specs/vectorfl_input_organ_role_md_draft_v0.md",
        "handoff": "docs/specs/vectorfl_input_organ_handoff_md_draft_v0.md",
        "caution": "docs/specs/vectorfl_input_organ_caution_md_draft_v0.md",
        "return": "docs/specs/vectorfl_input_organ_return_md_draft_v0.md",
    },
    "line-state": {
        "label": "Line / State Organ",
        "role": "docs/specs/vectorfl_line_state_organ_role_md_draft_v0.md",
        "handoff": "docs/specs/vectorfl_line_state_organ_handoff_md_draft_v0.md",
        "caution": "docs/specs/vectorfl_line_state_organ_caution_md_draft_v0.md",
        "return": "docs/specs/vectorfl_line_state_organ_return_md_draft_v0.md",
    },
    "translation": {
        "label": "Translation Organ",
        "role": "docs/specs/vectorfl_translation_organ_role_md_draft_v0.md",
        "handoff": "docs/specs/vectorfl_translation_organ_handoff_md_draft_v0.md",
        "caution": "docs/specs/vectorfl_translation_organ_caution_md_draft_v0.md",
        "return": "docs/specs/vectorfl_translation_organ_return_md_draft_v0.md",
    },
    "flow-interpretation": {
        "label": "Flow Interpretation Organ",
        "role": "docs/specs/vectorfl_flow_interpretation_organ_role_md_draft_v0.md",
        "handoff": "docs/specs/vectorfl_flow_interpretation_organ_handoff_md_draft_v0.md",
        "caution": "docs/specs/vectorfl_flow_interpretation_organ_caution_md_draft_v0.md",
        "return": "docs/specs/vectorfl_flow_interpretation_organ_return_md_draft_v0.md",
    },
    "governance": {
        "label": "Governance Organ",
        "role": "docs/specs/vectorfl_governance_organ_role_md_draft_v0.md",
        "handoff": "docs/specs/vectorfl_governance_organ_handoff_md_draft_v0.md",
        "caution": "docs/specs/vectorfl_governance_organ_caution_md_draft_v0.md",
        "return": "docs/specs/vectorfl_governance_organ_return_md_draft_v0.md",
    },
    "trace-memory": {
        "label": "Trace / Memory Organ",
        "role": "docs/specs/vectorfl_trace_memory_organ_role_md_draft_v0.md",
        "handoff": "docs/specs/vectorfl_trace_memory_organ_handoff_md_draft_v0.md",
        "caution": "docs/specs/vectorfl_trace_memory_organ_caution_md_draft_v0.md",
        "return": "docs/specs/vectorfl_trace_memory_organ_return_md_draft_v0.md",
    },
}


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8").strip()
    except Exception:
        return ""


def _first_non_heading_paragraph(text: str) -> str:
    for block in re.split(r"\n\s*\n", text):
        stripped = block.strip()
        if not stripped or stripped.startswith("#"):
            continue
        return " ".join(line.strip() for line in stripped.splitlines())
    return ""


def _chip(text: str) -> str:
    return f'<span class="chip">{html.escape(text)}</span>'


def _link(href: str, label: str, *, subtle: bool = False) -> str:
    klass = "tool-link subtle" if subtle else "tool-link"
    return f'<a class="{klass}" href="{html.escape(href)}">{html.escape(label)}</a>'


def _esc(value: Any) -> str:
    return html.escape(str(value))


def _friendly_text(value: Any) -> str:
    if isinstance(value, (list, tuple)):
        return " / ".join(_friendly_text(item) for item in value if str(item).strip()) or "없음"
    text = str(value or "").strip()
    if not text:
        return "없음"
    held_match = re.match(r"^(.+?) is being held under (.+?) reading\.$", text)
    if held_match:
        return f"{held_match.group(1)} 자료는 지금 `{held_match.group(2)}` 읽기 단계에서 더 살펴보는 중입니다."
    if text.startswith("mode=space_reading / mode_source="):
        return "원본을 먼저 읽고, 아직 바로 보고나 결론으로 올리지 말라는 사전 읽기 기준입니다."
    if text.startswith("signals={"):
        return "현재 흔적을 보면 연속성은 높고, 잔여는 중간 정도이며, 아직 더 읽을 여지가 남아 있습니다."
    if "line translation and internal recall" in text:
        return "이 단계에서는 line으로 바로 굳히지 않고, 어떻게 나뉘었는지와 각 단위의 역할 단서를 먼저 남겨 둡니다."
    if "No explicit uncertainty captured" in text:
        return "아직 별도로 적어 둔 uncertainty는 없지만, 더 읽으면서 애매한 점을 계속 붙여야 합니다."
    replacements = [
        (
            "The document currently reads as input_to_processing_to_result with 15 units, dominated by heading_block.",
            "이 문서는 지금 입력 -> 처리 -> 결과 흐름으로 읽히며, heading block 중심으로 15개 단위가 잡혀 있습니다.",
        ),
        (
            "This native read keeps segmentation basis, role hints, and relation clues available before line translation and internal recall.",
            "이 단계에서는 line으로 바로 굳히지 않고, 어떻게 나뉘었는지와 각 단위의 역할 단서를 먼저 남겨 둡니다.",
        ),
        (
            "No explicit uncertainty captured beyond the current native read.",
            "아직 별도로 적어 둔 uncertainty는 없지만, 더 읽으면서 애매한 점을 계속 붙여야 합니다.",
        ),
        (
            "Current runtime phase is `thickening` with decision `thickening`. Latent lines: pre_read_eye, raw_return_preservation.",
            "현재는 `thickening` 단계에서 읽히고 있으며, `pre_read_eye`, `raw_return_preservation` 같은 잠재 line을 더 두껍게 보는 중입니다.",
        ),
        (
            "existing latent lines and pre-read gate are stable, but the path is still not closure-ready",
            "기존 잠재 line과 사전 읽기 기준은 유지되고 있지만, 아직 닫아도 될 만큼 충분히 읽힌 상태는 아닙니다.",
        ),
        (
            "internal recall first, then compare if still thin",
            "먼저 내부 자료를 다시 보고, 그래도 얇으면 그때 비교나 외부 검색으로 넘어갑니다.",
        ),
        (
            "Read-first posture that keeps residue and avoids premature closure.",
            "잔여 흔적을 남긴 채 너무 빨리 닫지 않도록, 먼저 읽기를 우선하는 태도입니다.",
        ),
        (
            "Governance-first guard that blocks polished readout before sufficient reading.",
            "충분히 읽히기 전에는 보기 좋게 정리된 결론으로 넘어가지 못하게 막는 보호 규칙입니다.",
        ),
        (
            "Translation and flow interpretation prioritize why the transition matters before surface polish.",
            "표면을 다듬기 전에, 왜 이 전환이 중요한지부터 먼저 읽게 하는 기준입니다.",
        ),
        (
            "The provisional line currently sits in the native document sequence before thicker family rebinding.",
            "이 임시 line은 아직 원본 문서 순서에 가까운 상태에 있고, 더 두꺼운 family 재결합 전 단계에 있습니다.",
        ),
        (
            "line semantics remain thinner than line infrastructure",
            "line을 만들 구조는 많이 생겼지만, line의 실제 뜻은 아직 얇습니다.",
        ),
        (
            "family recall is still weaker than line generation",
            "line을 만드는 힘보다, family와 내부 자료를 다시 불러오는 힘이 아직 약합니다.",
        ),
        (
            "external search should be justified by internal gap first",
            "외부 검색은 먼저 내부에서 무엇이 비는지 확인한 뒤에만 넘어가야 합니다.",
        ),
        (
            "deeper directive recall around host-shell adoption",
            "host shell을 붙일 때 어떤 지시가 기준이 되는지 더 깊게 다시 봐야 합니다.",
        ),
        (
            "line usability proof beyond current case",
            "지금 case를 넘어서도 이 line이 실제로 쓸 만한지 검증이 더 필요합니다.",
        ),
        (
            "Native document sequence is being used as the first family scaffold before thicker internal binding.",
            "지금은 원본 문서 순서를 첫 family 발판으로 쓰고 있고, 이후 내부 자료를 붙여 더 두껍게 만들 예정입니다.",
        ),
        (
            "Reads # raw intake gap analysis before middle-layer fix against 9 internal records before widening.",
            "이 lane은 현재 line을 9개의 내부 기록과 먼저 대조해 본 뒤에야 확장 여부를 판단합니다.",
        ),
        (
            "Reserved for alternative read emphasis once internal recall set is thicker.",
            "내부 recall 재료가 더 두꺼워진 뒤에 다른 읽기 강조를 시험하기 위해 남겨둔 lane입니다.",
        ),
        (
            "Reserved for second read on preserved source order and omitted nuance.",
            "원본 순서와 빠진 뉘앙스를 다시 읽는 두 번째 lane으로 남겨둔 상태입니다.",
        ),
        (
            "Would compare role-hint weighting against the current selected line.",
            "현재 선택된 line과 비교해, 역할 힌트의 가중치를 다르게 읽었을 때 어떤 차이가 나는지 보려는 결과입니다.",
        ),
        (
            "Candidate comparison lane for external resource prompt variation.",
            "외부 검색 질문을 다르게 던졌을 때 어떤 차이가 나는지 비교하기 위한 후보 lane입니다.",
        ),
        (
            "Should be used only after the same fixed pipeline stages are preserved.",
            "같은 고정 파이프라인 단계를 그대로 유지할 수 있을 때만 써야 합니다.",
        ),
        (
            "Would emit diff vs ChatGPT lane, not free-form chat.",
            "자유 대화가 아니라 ChatGPT lane과의 차이만 비교 결과로 내놓도록 설계돼 있습니다.",
        ),
        (
            "Would stress-test omission handling and uncertainty carry.",
            "빠뜨린 부분과 uncertainty를 얼마나 잘 들고 가는지 시험하려는 lane입니다.",
        ),
        (
            "Should propose alternative adoption/search forms only after internal recall.",
            "내부 recall을 먼저 마친 뒤에만, 다른 차용 방식이나 검색 방식을 제안해야 합니다.",
        ),
        (
            "Kept candidate-only to avoid premature lane proliferation.",
            "lane가 너무 빨리 늘어나는 것을 막기 위해 아직 후보 상태로만 두고 있습니다.",
        ),
        (
            "Would compare report readability and omission carry.",
            "보고서가 얼마나 읽기 쉬운지와, 빠진 내용을 얼마나 잘 들고 가는지 비교하려는 결과입니다.",
        ),
        (
            "Most aligned with current GMD-backed first pass.",
            "현재 GMD 기반 first pass와 가장 잘 맞는 lane입니다.",
        ),
        (
            "full paragraph-level nuance omitted",
            "문단 전체의 미묘한 결은 아직 다 담지 못했습니다.",
        ),
        (
            "cross-unit relation must be read with adjacent units",
            "앞뒤 단위와 함께 봐야 관계가 더 정확히 보입니다.",
        ),
        (
            "Use this source as translation_first material while preserving heading_block and uncertainty.",
            "이 자료는 먼저 번역 재료로 쓰되, heading block 구조와 아직 남은 uncertainty를 같이 들고 가야 합니다.",
        ),
        (
            "adoption form",
            "차용할 때의 말",
        ),
        (
            "preserves",
            "보존하는 것",
        ),
        (
            "omits",
            "빠뜨린 것",
        ),
        (
            "reentry cue",
            "다시 열 단서",
        ),
        (
            "No free chat between lanes. Compare only at top.",
            "lane끼리 직접 대화하지 않고, 맨 위에서만 비교합니다.",
        ),
        (
            "Reserved second comparison lane.",
            "두 번째 비교를 위해 비워 둔 lane입니다.",
        ),
        (
            "insufficient_attention_history",
            "이 자료를 충분히 다시 본 흔적이 아직 부족합니다.",
        ),
        (
            "no_previous_state_anchor",
            "이전 상태를 붙잡아 둘 기준점이 아직 없습니다.",
        ),
        (
            "read_runtime_surfaces_only",
            "지금은 runtime 표면을 읽기만 하고 직접 제어하지 않습니다.",
        ),
        (
            "Semi-live shell is read-only; runtime surfaces are translated into current-reading without live control.",
            "지금 화면은 읽기 전용이며, runtime 표면을 current-reading으로 옮겨 보여주기만 합니다.",
        ),
    ]
    for source, target in replacements:
        if text == source:
            return target
    return text


def _bundle_preview(repo_root: Path, rel_path: str) -> Dict[str, str]:
    path = repo_root / rel_path
    content = _read_text(path)
    return {
        "path": rel_path,
        "title": content.splitlines()[0].lstrip("# ").strip() if content else Path(rel_path).name,
        "summary": _first_non_heading_paragraph(content),
        "content": content,
    }


def _load_latest_gmd_native_read(repo_root: Path) -> Dict[str, Any]:
    generated_root = repo_root / "app" / "work" / "observer_ingest_min" / "generated"
    candidates = list(generated_root.glob("gmd_native_read_*.json"))
    if not candidates:
        return {}
    try:
        latest = max(candidates, key=lambda path: path.stat().st_mtime)
        return json.loads(latest.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _load_json_file(path: Path) -> Dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _load_recall_evidence_bundles(repo_root: Path) -> List[Dict[str, Any]]:
    manifest = repo_root / "runtime" / "manifests" / "vectorfl_internal_recall_evidence_bundles_v0.json"
    data = _load_json_file(manifest)
    bundles = data.get("bundles")
    return bundles if isinstance(bundles, list) else []


def _load_paper_proper_bridge_state(repo_root: Path) -> Dict[str, Any]:
    def load(rel_path: str) -> Dict[str, Any]:
        return _load_json_file(repo_root / rel_path)

    paths = {
        "codex_handoff": "runtime/manifests/vectorfl_paper_codex_handoff_latest_v0.json",
        "codex_return": "runtime/manifests/vectorfl_paper_codex_return_latest_v0.json",
        "gemini_review": "runtime/manifests/vectorfl_paper_gemini_review_latest_v0.json",
        "supervisor_decision": "runtime/manifests/vectorfl_paper_supervisor_decision_latest_v0.json",
        "current_slot": "runtime/manifests/vectorfl_paper_actual_export_host_record_slot_v0.json",
        "gate_validation": "runtime/manifests/vectorfl_paper_actual_export_gate_validation_latest_v0.json",
        "dry_run": "runtime/manifests/vectorfl_paper_actual_export_gate_validation_dry_run_v0.json",
        "comparison": "runtime/manifests/vectorfl_paper_reference_candidate_validation_comparison_v0.json",
    }
    handoff = load(paths["codex_handoff"])
    codex_return = load(paths["codex_return"])
    gemini_review = load(paths["gemini_review"])
    supervisor_decision = load(paths["supervisor_decision"])
    current_slot = load(paths["current_slot"])
    gate_validation = load(paths["gate_validation"])
    dry_run = load(paths["dry_run"])
    comparison = load(paths["comparison"])
    supervisor_answers = comparison.get("supervisor_answers") or {}
    handoff_summary = {
        "status": handoff.get("status"),
        "requested_action": handoff.get("requested_action"),
        "emitted_at": handoff.get("emitted_at"),
    }
    codex_return_summary = {
        "status": codex_return.get("status"),
        "summary": codex_return.get("summary"),
        "changed_files": codex_return.get("changed_files") or [],
        "blockers": codex_return.get("blockers") or [],
        "next_recommendation": codex_return.get("next_recommendation"),
        "needs_supervisor_decision": codex_return.get("needs_supervisor_decision"),
        "returned_at": codex_return.get("returned_at"),
    }
    gemini_review_summary = {
        "review_status": gemini_review.get("review_status"),
        "agreement_assessment": gemini_review.get("agreement_assessment"),
        "detected_risks": gemini_review.get("detected_risks") or [],
        "missing_points": gemini_review.get("missing_points") or [],
        "recommendation": gemini_review.get("recommendation"),
        "suggested_supervisor_action": gemini_review.get("suggested_supervisor_action"),
        "reviewed_at": gemini_review.get("reviewed_at"),
    }
    supervisor_decision_summary = {
        "decision": supervisor_decision.get("decision"),
        "rationale": supervisor_decision.get("rationale"),
        "followup_action": supervisor_decision.get("followup_action"),
        "decision_tension": supervisor_decision.get("decision_tension"),
        "validation_reduced": supervisor_decision.get("validation_reduced") or [],
        "pending_validations": supervisor_decision.get("pending_validations") or [],
        "continue_gate": supervisor_decision.get("continue_gate"),
        "decided_at": supervisor_decision.get("decided_at"),
    }
    current_slot_summary = {
        "current_state": current_slot.get("current_state"),
        "current_placeholder_ref": current_slot.get("current_placeholder_ref"),
        "current_validation_anchor_ref": current_slot.get("current_validation_anchor_ref"),
        "validation_anchor_status": current_slot.get("validation_anchor_status"),
        "validation_anchor_note": current_slot.get("validation_anchor_note"),
    }
    gate_validation_summary = {
        "validation_status": gate_validation.get("validation_status"),
        "honesty_class": gate_validation.get("honesty_class"),
        "gate_effect": gate_validation.get("gate_effect"),
        "recommendation": gate_validation.get("recommendation"),
        "validated_at": gate_validation.get("validated_at"),
    }
    dry_run_summary = {
        "source_record_artifact": dry_run.get("source_record_artifact"),
        "validation_status": dry_run.get("validation_status"),
        "honesty_class": dry_run.get("honesty_class"),
        "gate_effect": dry_run.get("gate_effect"),
        "recommendation": dry_run.get("recommendation"),
        "validated_at": dry_run.get("validated_at"),
        "delta_vs_current_anchor": dry_run.get("delta_vs_current_anchor") or {},
    }
    return {
        "source_surface": "vectorfl_paper_proper",
        "target_surface": "vectorfl_operable_surface",
        "merge_rule": "proper grammar is translated into existing operable tabs; no new tab is added",
        "paths": paths,
        "current_posture": supervisor_decision.get("decision") or "waiting_for_actual_export",
        "current_slot_state": current_slot.get("current_state") or "unknown",
        "remaining_gate": "actual_export_only",
        "guard_language": [
            "no gate close",
            "no slot replacement",
            "no candidate promotion",
            "dry-run is preview-only",
        ],
        "current_slot": current_slot_summary,
        "gate_validation": gate_validation_summary,
        "dry_run": dry_run_summary,
        "handoff": handoff_summary,
        "codex_return": codex_return_summary,
        "gemini_review": gemini_review_summary,
        "supervisor_decision": supervisor_decision_summary,
        "codex_top_files": handoff.get("codex_top_files") or handoff.get("relevant_files") or [],
        "gemini_review_top_files": gemini_review.get("gemini_review_top_files") or [],
        "operator_slots": {
            "input": {
                "label": "입력 / 후보 anchor 확인",
                "page": "external-resources.html",
                "manifest": paths["current_slot"],
                "status": current_slot.get("current_state") or "unknown",
                "action": "true host/export candidate가 오기 전까지 current slot은 교체하지 않고 anchor와 dry-run만 구분해 읽습니다.",
            },
            "select": {
                "label": "Codex 작업 입력 선택",
                "page": "external-resources.html",
                "manifest": paths["codex_handoff"],
                "status": handoff.get("status") or "unknown",
                "action": handoff.get("requested_action") or "handoff requested action pending",
            },
            "assign": {
                "label": "Codex / Gemini 역할 지정",
                "page": "agent-mcp-control.html",
                "manifest": paths["gemini_review"],
                "status": gemini_review.get("review_status") or "unknown",
                "action": "Codex는 구현/검증 입력, Gemini는 Codex return 기반 cross-check로 분리합니다.",
            },
            "confirm": {
                "label": "worker return 확인",
                "page": "worker-inbox.html",
                "manifest": paths["codex_return"],
                "status": codex_return.get("status") or "unknown",
                "action": codex_return.get("next_recommendation") or "return recommendation pending",
            },
            "supervise": {
                "label": "감독 판단",
                "page": "trace-audit.html",
                "manifest": paths["supervisor_decision"],
                "status": supervisor_decision.get("decision") or "unknown",
                "action": supervisor_decision.get("continue_gate") or supervisor_decision.get("followup_action") or "continue gate pending",
            },
        },
        "supervisor_answers": supervisor_answers,
    }


def _bundle_index(bundles: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    return {
        str(bundle.get("bundle_id")): bundle
        for bundle in bundles
        if isinstance(bundle, dict) and bundle.get("bundle_id")
    }


def _attach_bundle_reasons(
    bundle_index: Dict[str, Dict[str, Any]],
    bundle_ids: List[str],
    *,
    reason_map: Dict[str, str],
) -> List[Dict[str, Any]]:
    attached: List[Dict[str, Any]] = []
    for bundle_id in bundle_ids:
        bundle = bundle_index.get(bundle_id)
        if not bundle:
            continue
        enriched = dict(bundle)
        enriched["why_it_is_here"] = reason_map.get(bundle_id, "현재 읽기와 직접 닿는 근거라서 같이 붙였습니다.")
        enriched["detail_href"] = f"evidence-bundle-{bundle_id}.html"
        attached.append(enriched)
    return attached


def _attach_bundle_detail_hrefs(bundles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    attached: List[Dict[str, Any]] = []
    for bundle in bundles:
        enriched = dict(bundle)
        bundle_id = str(enriched.get("bundle_id") or "")
        if bundle_id:
            enriched["detail_href"] = f"evidence-bundle-{bundle_id}.html"
        attached.append(enriched)
    return attached


def _bundle_reason_map_for_line(raw_value: str) -> Dict[str, str]:
    lowered = raw_value.lower()
    reason_map = {
        "bundle_01_raw_intake_middle_layer_gap": "이 line이 원본 구조를 너무 빨리 납작하게 만들지 않으려면, 입력기에서 어떤 단서를 남겨야 하는지 보여주는 근거입니다.",
        "bundle_05_visible_split_to_recall_surface": "이 line이 실제 표면에서 읽히려면, 원본 분절과 초기 recall 표면이 얼마나 operator-readable한지 같이 봐야 합니다.",
    }
    if "recall" in lowered or "기록망" in raw_value or "불러오는" in raw_value:
        reason_map.update(
            {
                "bundle_02_reentry_survival_without_promotion": "다시 불러온다고 해서 바로 닫히거나 승격되는 건 아니라는 점을 보여주는 근거입니다.",
                "bundle_03_meaning_vs_format_disentangle": "이 line이 진짜 뜻에서 나온 건지, 형식 echo에 끌린 건지 분리해서 읽게 해 주는 근거입니다.",
            }
        )
    if "business" in lowered or "corridor" in lowered or "축" in raw_value:
        reason_map["bundle_04_business_corridor_subaxis_mix"] = "겉으로 하나의 business line처럼 보여도, 실제로는 여러 축이 섞여 있을 수 있다는 점을 받쳐 주는 근거입니다."
        reason_map["bundle_07_axis_stability_distribution"] = "겉보기에 비슷한 business line도, 축별로 안정도가 다르다는 점을 더 세밀하게 보여주는 근거입니다."
    if "hold" in lowered or "reentry" in lowered or "닫" in raw_value or "승격" in raw_value:
        reason_map["bundle_06_boundary_specificity_without_closure"] = "경계 시험에서 살아남아도 바로 닫히거나 승격되는 건 아니라는 점을 보여주는 근거입니다."
    return reason_map


def _bundle_reason_map_for_routing() -> Dict[str, str]:
    return {
        "bundle_02_reentry_survival_without_promotion": "다시 붙는다고 바로 넘기면 안 되고, hold와 promotion을 분리해서 봐야 한다는 routing 근거입니다.",
        "bundle_06_boundary_specificity_without_closure": "specific하게 살아남는 corridor라도 still_observe에 머물 수 있다는 점을 routing에 같이 들고 가야 합니다.",
        "bundle_04_business_corridor_subaxis_mix": "한 덩어리로 넘기지 말고, 필요한 경우 하위 축으로 다시 나눠서 넘겨야 한다는 근거입니다.",
        "bundle_07_axis_stability_distribution": "하위 축마다 안정도가 달라서, 같은 business 계열이라도 routing 태도를 다르게 잡아야 한다는 근거입니다.",
        "bundle_01_raw_intake_middle_layer_gap": "입력기에서 남긴 구조 단서가 routing 결정에도 계속 살아 있어야 한다는 근거입니다.",
    }


def _bundle_reason_map_for_lane_runs() -> Dict[str, str]:
    return {
        "bundle_01_raw_intake_middle_layer_gap": "lane 비교도 결국 입력기에서 남긴 재료의 밀도 위에서만 의미가 생긴다는 근거입니다.",
        "bundle_03_meaning_vs_format_disentangle": "lane마다 형식 echo와 실제 뜻을 얼마나 다르게 읽는지 비교하게 만드는 근거입니다.",
        "bundle_04_business_corridor_subaxis_mix": "business처럼 평평한 line을 lane마다 얼마나 세분화해 읽는지 비교하게 만드는 근거입니다.",
        "bundle_06_boundary_specificity_without_closure": "lane마다 살아남는 corridor를 얼마나 성급하게 closure로 착각하는지 비교하게 만드는 근거입니다.",
        "bundle_07_axis_stability_distribution": "lane마다 어떤 axis를 더 안정적으로 읽는지 비교하게 만드는 근거입니다.",
    }


def _short_title(path: str) -> str:
    return Path(path).name.replace("_", " ").replace(".md", "")


def build_vectorfl_operable_surface_state(repo_root: Path) -> Dict[str, Any]:
    base = build_vectorfl_page_semi_live_state(repo_root)
    evidence_bundles = _load_recall_evidence_bundles(repo_root)
    evidence_bundle_index = _bundle_index(evidence_bundles)
    gmd_read = _load_latest_gmd_native_read(repo_root)
    gmd_native = gmd_read.get("gmd_native_read") or {}
    gmd_commentary = gmd_read.get("semantic_commentary") or {}
    gmd_material = gmd_read.get("translation_ready_material") or {}
    gmd_source_block = gmd_material.get("source_block") or {}
    gmd_role_block = gmd_material.get("role_block") or []
    gmd_line_block = gmd_material.get("provisional_line_block") or []
    gmd_family_block = gmd_material.get("family_block") or {}
    gmd_use_block = gmd_material.get("use_block") or {}
    gmd_uncertainty_block = gmd_material.get("uncertainty_block") or []
    gmd_segmentation = gmd_native.get("segmentation_basis") or {}
    queue_preview = base.get("queue_preview") or []
    current_reading = base.get("current_reading") or {}
    current_body = current_reading.get("body") or {}
    governance = current_reading.get("governance") or {}
    responsibility = base.get("current_responsibility") or {}
    progression = base.get("progression_preview") or {}
    inputs_preview = base.get("inputs_preview") or {}
    trace_preview = (base.get("history_trace_preview") or {}).get("latest_trace_list") or []
    programs_preview = base.get("programs_connections_preview") or {}
    linked_programs = programs_preview.get("linked_programs") or []
    saved_connection_preview = programs_preview.get("saved_connection_preview") or []
    attention_memory_preview = programs_preview.get("attention_memory_preview") or []

    organ_rows: List[Dict[str, Any]] = []
    order = ["input", "line-state", "translation", "flow-interpretation", "governance", "trace-memory"]
    current_organ_map = {
        "organ:input": "input",
        "organ:line_state": "line-state",
        "organ:translation": "translation",
        "organ:flow_interpretation": "flow-interpretation",
        "organ:governance": "governance",
        "organ:trace_memory": "trace-memory",
    }
    current_slug = current_organ_map.get(str(responsibility.get("current_organ_ref") or ""), "flow-interpretation")
    next_candidates = progression.get("next_candidates") or []
    next_ref = str(next_candidates[0].get("organ_ref") or "") if next_candidates else ""

    next_map = {
        "organ:governance": "governance",
        "organ:flow_interpretation": "flow-interpretation",
        "organ:translation": "translation",
        "organ:line_state": "line-state",
        "organ:trace_memory": "trace-memory",
        "organ:input": "input",
    }
    next_slug = next_map.get(next_ref, "governance")

    for item in queue_preview:
        item["current_detail_href"] = f"organ-detail-{current_slug}.html"
        item["next_detail_href"] = f"organ-detail-{next_slug}.html"

    organ_runtime_profiles = {
        "input": {
            "lens": "scenario-bearing material을 손상 없이 intake packet으로 준비",
            "managing_cli": "gemini-cli",
            "managing_lane_slug": "gemini",
            "md_contracts": ["ROLE", "HANDOFF", "CAUTION", "RETURN"],
            "handoff_targets": ["line-state", "translation"],
            "paired_external_team": "external-resource-team",
            "human_report_format": "무엇을 입력으로 고정했고 왜 아직 launch를 보류하는지 보고",
        },
        "line-state": {
            "lens": "line seed와 unstable pressure를 분리해 읽기 가능한 work packet으로 고정",
            "managing_cli": "codex-cli",
            "managing_lane_slug": "chatgpt",
            "md_contracts": ["ROLE", "HANDOFF", "CAUTION", "RETURN"],
            "handoff_targets": ["translation", "flow-interpretation"],
            "paired_external_team": "comparison-team",
            "human_report_format": "지금 어떤 line이 기준이고 무엇이 아직 불안정한지 보고",
        },
        "translation": {
            "lens": "공간 언어를 감독자 언어와 worker payload 언어로 번역",
            "managing_cli": "codex-cli",
            "managing_lane_slug": "chatgpt",
            "md_contracts": ["ROLE", "HANDOFF", "CAUTION", "RETURN"],
            "handoff_targets": ["flow-interpretation", "governance"],
            "paired_external_team": "external-program-team",
            "human_report_format": "무엇을 사람 말로 바꿨고 무엇이 아직 bundle 근거를 더 필요로 하는지 보고",
        },
        "flow-interpretation": {
            "lens": "현재 case의 reading 단계와 다음 handoff 후보를 결정",
            "managing_cli": "codex-cli",
            "managing_lane_slug": "chatgpt",
            "md_contracts": ["ROLE", "HANDOFF", "CAUTION", "RETURN"],
            "handoff_targets": ["governance", "trace-memory"],
            "paired_external_team": "comparison-team",
            "human_report_format": "왜 지금 이 팀이 맡고 있고 다음으로 누구에게 넘기는지 보고",
        },
        "governance": {
            "lens": "go / hold / reopen / redirect 판단과 보호 규칙 유지",
            "managing_cli": "gemini-cli",
            "managing_lane_slug": "gemini",
            "md_contracts": ["ROLE", "HANDOFF", "CAUTION", "RETURN"],
            "handoff_targets": ["trace-memory", "flow-interpretation"],
            "paired_external_team": "external-resource-team",
            "human_report_format": "무엇이 왜 아직 hold인지와 release condition을 보고",
        },
        "trace-memory": {
            "lens": "run, residue, reopen 단서를 append-only로 보존",
            "managing_cli": "codex-cli",
            "managing_lane_slug": "claude",
            "md_contracts": ["ROLE", "HANDOFF", "CAUTION", "RETURN"],
            "handoff_targets": ["flow-interpretation", "governance"],
            "paired_external_team": "comparison-team",
            "human_report_format": "무엇을 다시 열어야 하는지와 어떤 흔적을 남겨야 하는지 보고",
        },
    }

    for slug in order:
        spec = ORGAN_SPECS[slug]
        bundle = {kind: _bundle_preview(repo_root, rel) for kind, rel in spec.items() if kind in {"role", "handoff", "caution", "return"}}
        runtime_profile = organ_runtime_profiles.get(slug, {})
        organ_rows.append(
            {
                "slug": slug,
                "label": spec["label"],
                "current": slug == current_slug,
                "next_candidate": slug == next_slug,
                "active_case_count": len(queue_preview) if slug in {current_slug, next_slug} else 0,
                "summary": bundle["role"]["summary"],
                "supported_family": gmd_family_block.get("family_position") or "native_document_sequence",
                "supported_gap_count": len(gmd_uncertainty_block),
                "bundle": bundle,
                "lens": runtime_profile.get("lens") or "lens not fixed",
                "managing_cli": runtime_profile.get("managing_cli") or "cli pending",
                "managing_lane_slug": runtime_profile.get("managing_lane_slug") or "chatgpt",
                "md_contracts": runtime_profile.get("md_contracts") or ["ROLE", "HANDOFF", "CAUTION", "RETURN"],
                "handoff_targets": runtime_profile.get("handoff_targets") or [],
                "paired_external_team": runtime_profile.get("paired_external_team") or "none",
                "human_report_format": runtime_profile.get("human_report_format") or "report format pending",
                "detail_href": f"organ-detail-{slug}.html",
                "editor_href": f"organ-editor-{slug}.html",
            }
        )

    internal_recall_docs = [
        "docs/specs/vectorfl_three_layer_structure_lock_v0.md",
        "docs/specs/vectorfl_handoff_boundary_lock_v0.md",
        "docs/specs/vectorfl_external_source_and_host_need_lock_v0.md",
        "docs/specs/vectorfl_canonical_object_ownership_lock_v0.md",
        "docs/specs/vectorfl_minimum_field_schema_lock_v0.md",
        "docs/specs/vectorfl_surface_only_paperclip_adoption_lock_v0.md",
    ]
    recall_rows = [_bundle_preview(repo_root, rel) for rel in internal_recall_docs]
    line_family_rows = [
        {
            "label": "preservation_before_flattening",
            "summary": "Read-first posture that keeps residue and avoids premature closure.",
        },
        {
            "label": "closure_before_presentation",
            "summary": "Governance-first guard that blocks polished readout before sufficient reading.",
        },
        {
            "label": "transition_explanation_first",
            "summary": "Translation and flow interpretation prioritize why the transition matters before surface polish.",
        },
    ]

    selected_line_seed = gmd_line_block[0] if gmd_line_block else {}
    selected_line = {
        "raw_value": selected_line_seed.get("provisional_line") or current_body.get("headline") or current_reading.get("case_header", {}).get("case_id") or "current-line",
        "human_translation": selected_line_seed.get("human_gloss") or gmd_commentary.get("source_summary") or "아직 사람이 읽는 말로 다시 풀어 쓴 설명은 없습니다.",
        "meaning_summary": gmd_commentary.get("structure_summary") or "아직 짧은 뜻풀이가 정리되지 않았습니다.",
        "preserves": selected_line_seed.get("what_it_preserves") or ["source linkage pending"],
        "omits": selected_line_seed.get("what_it_omits") or ["omission detail pending"],
        "uncertainty": (
            gmd_uncertainty_block[0].get("pending_interpretation")
            if gmd_uncertainty_block
            else "아직 별도로 적어 둔 uncertainty는 없지만, 더 읽으면서 애매한 점을 계속 붙여야 합니다."
        ),
        "family": gmd_family_block.get("family_position") or "native_document_sequence",
        "searchable_form": " ".join(
            filter(
                None,
                [
                    str(gmd_source_block.get("source_name") or ""),
                    str(gmd_source_block.get("source_context") or ""),
                    str(selected_line_seed.get("human_gloss") or ""),
                ],
            )
        ).strip() or "searchable form pending",
        "adoption_form": (
            f"Use this source as {gmd_use_block.get('next_team_or_lane') or 'translation_first'} material "
            f"while preserving {gmd_source_block.get('source_unit') or 'native units'} and uncertainty."
        ),
        "next_step_ideas": [
            "Reopen supporting declarations and directives against the provisional line.",
            "Check whether internal records already thicken this line family before external search.",
            "Send to routing only after recall and uncertainty review.",
        ],
        "candidate_handoff": next_ref or "organ:governance",
    }
    def _build_line_dossier(raw_value: str, human_translation: str, uncertainty: str) -> Dict[str, Any]:
        return {
            "friendly_title": "이 line이 왜 중요한가",
            "friendly_summary": "좋은 line은 문장 하나로 끝나는 값이 아니라, 내부 기록과 맥락을 다시 불러와 다음 판단을 가능하게 만드는 입구다.",
            "declaration_linkage": {
                "type": "선언문 / 방향 고정",
                "summary": "이 line은 단순 조회 규칙이 아니라, 공간을 살아 있게 유지하는 원리 line이다.",
                "human_readable": "line은 한 번 읽고 끝나는 값이 아니라, 공간 안에 남은 기억과 기록을 다시 동원하게 만드는 기준이어야 한다.",
            },
            "directive_linkage": {
                "type": "지시문 / 다음 행동",
                "summary": "이 line은 설명 line이 아니라, line 생성 이후의 필수 step을 요구하는 action line이다.",
                "human_readable": "line을 만들었으면 끝이 아니라, 그 line으로 내부 자료를 다시 불러와 강화/충돌/수정을 읽어야 한다.",
            },
            "past_conversation_linkage": {
                "type": "과거 대화 / 반성 / 문제 제기",
                "summary": "이 line은 왜 지금까지 내부 수렴이 반복됐는지를 설명하는 correction line이다.",
                "human_readable": "우리가 line을 값처럼 다뤘기 때문에, line이 내부 자료망을 다시 여는 키로 못 쓰였다.",
            },
            "spec_linkage": {
                "type": "spec / 구조 계약",
                "items": [
                    "source linkage",
                    "family linkage",
                    "declaration/directive linkage",
                    "judgment history linkage",
                    "searchable form",
                    "adoption form",
                    "uncertainty",
                ],
                "human_readable": "line이 내부 기록망의 입구가 되려면, 생성 순간부터 연결 필드가 함께 있어야 한다.",
            },
            "report_validation_linkage": {
                "type": "report / 검증 / close-out",
                "summary": "이 line은 단순 아이디어가 아니라, 왜 이전 결과물이 공허했는지를 설명하는 validation line이다.",
                "human_readable": "line을 내부 자료 recall 없이 쓰면, 화면은 생겨도 사람이 다시 md를 열어 번역해야 한다.",
            },
            "external_reference_linkage": {
                "type": "외부 사례 / 비교 / 차용",
                "summary": "이 line은 내부 반성만이 아니라, 어떤 외부 구조를 왜 가져와야 하는지 설명하는 adoption line이다.",
                "human_readable": "Paperclip는 line recall을 표면화하는 틀을 주고, GMD는 line recall에 필요한 원천 구조를 더 두껍게 만들 수 있다.",
            },
            "runlog_handoff_linkage": {
                "type": "작업 흔적 / 넘김 / residue",
                "summary": "이 line은 생각으로 끝나는 게 아니라, 실제 handoff와 audit를 요구하는 routing line이다.",
                "human_readable": "line recall은 머릿속 행위가 아니라, 어떤 자료를 다시 보고 왜 넘겼는지가 남는 작업 흐름이어야 한다.",
            },
            "family_expansion": {
                "name": "internal-recall family",
                "related_lines": [
                    "line은 혼자 보면 얇다",
                    "line family가 line meaning을 두껍게 만든다",
                    "선언문/지시문/과거 대화는 번역 재료다",
                    "내부를 보는 목적은 수렴이 아니라 외부를 더 잘 받아들이기 위한 정련이다",
                    "VectorFL Paper는 md 파일 재독해 수작업을 표면화하는 제품이어야 한다",
                ],
                "meaning": "이 family는 line이 결과값이 아니라, 내부 기억과 외부 탐색을 연결하는 작동 기준이어야 한다는 뜻을 다룬다.",
            },
            "translation": {
                "core": "좋은 line은 혼자 존재하는 문장이 아니라, 그 line을 둘러싼 내부 기록과 맥락을 다시 불러와 다음 판단을 가능하게 만드는 입구다.",
                "expanded": "따라서 line을 만들었으면 곧바로 잠그는 것이 아니라, 그 line과 닿는 선언문/지시문/과거 논의/검증 흔적을 함께 붙여서 읽어야 한다.",
                "reinforced": "이 line이 맞다면, VectorFL Paper는 line list만 보여주는 앱이 아니라 line을 클릭했을 때 내부 기록망 전체가 펼쳐지는 제품이어야 한다.",
            },
            "search_queries": [
                "context recall system from generated semantic lines",
                "semantic line linked memory retrieval interface",
                "design pattern for line-based context expansion",
                "retrieval UI for generated interpretation traces",
            ],
            "adoption_form_detail": {
                "borrow": [
                    "Paperclip의 detail + inspector 구조",
                    "activity/audit page",
                    "operable routing surface",
                ],
                "connect": [
                    "내부 선언문",
                    "지시문",
                    "과거 대화",
                    "validation notes",
                    "external search plan",
                ],
                "avoid": [
                    "line을 단독 값으로만 보여주기",
                    "line count만 늘리고 recall layer 없이 surface에 올리기",
                    "line 생성 직후 바로 lock하기",
                ],
            },
            "next_step_ideas": [
                "기존 line family 중 graph-like drift / 번역 문제 / 내부 recall 부족 계열을 다시 묶기",
                "선언문/지시문/과거 대화 중 이 line을 지지하는 것들을 먼저 큐레이션하기",
                "semantic retrieval UI / memory recall UI / audit-driven navigation 사례 검색",
                "line 클릭 시 source/family/declaration/directive/judgment/search-plan이 한 번에 뜨는 inspector 설계",
            ],
            "uncertainty_detail": {
                "pending": [
                    "recall 범위를 어디까지 넓힐지",
                    "recall 결과를 사람이 읽는 패널과 agent lane 입력 중 어디에 어떻게 나눌지",
                ],
                "conflict": "recall을 과도하게 붙이면 noise가 늘어날 수 있음",
                "needs_validation": [
                    "어떤 자료 타입이 line translation 강화에 가장 큰 효과를 주는지",
                    "family recall과 direct source recall 중 무엇이 더 먼저 와야 하는지",
                ],
            },
            "raw_value": raw_value,
            "human_translation": human_translation,
            "uncertainty": uncertainty,
        }

    selected_line_dossier = _build_line_dossier(
        selected_line["raw_value"],
        selected_line["human_translation"],
        selected_line["uncertainty"],
    )

    generated_lines = [
        {
            "raw": row.get("provisional_line") or "unknown provisional line",
            "human_translation": row.get("human_gloss") or row.get("provisional_line") or "no gloss",
            "family": gmd_family_block.get("family_position") or "native_document_sequence",
            "status": "selected" if idx == 0 else "usable",
            "line_id": f"line-{idx + 1}",
            "detail_href": f"line-detail-{idx + 1}.html",
            "dossier": _build_line_dossier(
                row.get("provisional_line") or "unknown provisional line",
                row.get("human_gloss") or row.get("provisional_line") or "no gloss",
                (
                    gmd_uncertainty_block[min(idx, len(gmd_uncertainty_block) - 1)].get("pending_interpretation")
                    if gmd_uncertainty_block
                    else "아직 별도로 적어 둔 uncertainty는 없지만, 더 읽으면서 애매한 점을 계속 붙여야 합니다."
                ),
            ),
            "evidence_bundles": _attach_bundle_reasons(
                evidence_bundle_index,
                [
                    "bundle_01_raw_intake_middle_layer_gap",
                    "bundle_05_visible_split_to_recall_surface",
                    *(
                        ["bundle_03_meaning_vs_format_disentangle"]
                        if idx % 2 == 0
                        else ["bundle_02_reentry_survival_without_promotion"]
                    ),
                ],
                reason_map=_bundle_reason_map_for_line(
                    row.get("provisional_line") or row.get("human_gloss") or "line"
                ),
            ),
        }
        for idx, row in enumerate(gmd_line_block[:6])
    ] or [
        {
            "raw": selected_line["raw_value"],
            "human_translation": selected_line["human_translation"],
            "family": selected_line["family"],
            "status": "selected",
            "line_id": "line-1",
            "detail_href": "line-detail-1.html",
            "dossier": selected_line_dossier,
            "evidence_bundles": case_detail_bundles,
        }
    ]
    recall_linkage_rows = [
        {
            "title": "원본 기록",
            "summary": gmd_commentary.get("source_summary") or "Source summary not yet available.",
            "path": gmd_read.get("doc_ref") or "unknown",
        },
        {
            "title": "원본 구조",
            "summary": gmd_commentary.get("structure_summary") or "Structure summary not yet available.",
            "path": f"split_mode={gmd_segmentation.get('split_mode_used') or 'unknown'}",
        },
        {
            "title": "번역 준비 재료",
            "summary": f"{len(gmd_line_block)} provisional lines / {len(gmd_role_block)} role hints / {len(gmd_uncertainty_block)} uncertainties",
            "path": "gmd_native_read",
        },
    ]

    lane_rows = [
        {
            "slug": "chatgpt",
            "label": "ChatGPT lane",
            "adapter_type": "codex_local",
            "provider_model": "openai / gpt-5.x",
            "provider": "OpenAI",
            "model": "gpt-5.x",
            "owning_cli": "codex-cli",
            "managed_team_slugs": ["line-state", "translation", "flow-interpretation"],
            "contract_ref": "vectorfl_paper_internal_read_cell_v0.md",
            "payload_policy": "selected line / bundle / compare target을 고정 payload로 묶음",
            "return_route": "trace-audit -> worker-inbox -> case-detail reinjection",
            "command": "codex",
            "args": "--model gpt-5.x --approval on-request",
            "working_directory": "/workspace/vectorfl_replica",
            "env_status": "ready",
            "env_summary": "OpenAI auth is assumed ready and local sandbox approval remains human-gated.",
            "approvals_policy": "human approval before launch / no silent bypass",
            "sandbox_policy": "workspace-write only",
            "search_policy": "internal-first, external-ready",
            "adapter_test": "pass",
            "enabled": True,
            "status": "active",
            "timeout": "90s",
            "budget": "default",
            "role_md": "Read current source against internal recall before widening.",
            "task_md": "Run Read / Apply / Search / Validate / Report in fixed order.",
            "caution_md": "Do not skip recall. Do not lock directly after line generation.",
            "output_schema": "lane_run_v0",
            "notes": "현재 첫 실행 기준선이며, 다른 lane은 이 결과와 차이를 비교합니다.",
            "detail_href": "lane-detail-chatgpt.html",
            "editor_href": "lane-editor-chatgpt.html",
        },
        {
            "slug": "gemini",
            "label": "Gemini lane",
            "adapter_type": "gemini_local",
            "provider_model": "google / gemini",
            "provider": "Google",
            "model": "gemini",
            "owning_cli": "gemini-cli",
            "managed_team_slugs": ["input", "governance"],
            "contract_ref": "vectorfl_paper_external_resource_cell_v0.md",
            "payload_policy": "보수적 비교 질문과 governance caution을 먼저 강화",
            "return_route": "governance gate -> supervisor board -> reopen or hold",
            "command": "gemini",
            "args": "--model gemini-pro",
            "working_directory": "/workspace/vectorfl_replica",
            "env_status": "check_needed",
            "env_summary": "Provider auth and model discovery should be re-tested before enabling this lane.",
            "approvals_policy": "hold by default until first-pass comparison is requested",
            "sandbox_policy": "workspace-write only",
            "search_policy": "comparison-only until recall gets thicker",
            "adapter_test": "pending",
            "enabled": False,
            "status": "hold",
            "timeout": "90s",
            "budget": "candidate",
            "role_md": "Alternative read emphasis once recall density is thicker.",
            "task_md": "Compare role-hint weighting without changing fixed pipeline.",
            "caution_md": "Do not proliferate before first-pass line recall proves stable.",
            "output_schema": "lane_run_v0",
            "notes": "내부 재독해가 더 두꺼워졌을 때 켤 비교용 lane입니다.",
            "detail_href": "lane-detail-gemini.html",
            "editor_href": "lane-editor-gemini.html",
        },
        {
            "slug": "claude",
            "label": "Claude lane",
            "adapter_type": "claude_local",
            "provider_model": "anthropic / claude",
            "provider": "Anthropic",
            "model": "claude",
            "owning_cli": "codex-cli",
            "managed_team_slugs": ["trace-memory"],
            "contract_ref": "vectorfl_paper_synthesis_cell_v0.md",
            "payload_policy": "trace residue와 omission stress test를 비교 lane으로만 실행",
            "return_route": "lane-runs diff -> trace-memory carry summary",
            "command": "claude",
            "args": "--model claude-sonnet",
            "working_directory": "/workspace/vectorfl_replica",
            "env_status": "hold",
            "env_summary": "Adapter is intentionally held until omission stress testing becomes necessary.",
            "approvals_policy": "manual enable + supervisor approval",
            "sandbox_policy": "workspace-write only",
            "search_policy": "no free external widening",
            "adapter_test": "not_run",
            "enabled": False,
            "status": "hold",
            "timeout": "90s",
            "budget": "candidate",
            "role_md": "Alternative omission and uncertainty reading pass.",
            "task_md": "Stress-test preserve / omit / uncertainty carry after recall.",
            "caution_md": "No free chat between lanes. Compare only at top.",
            "output_schema": "lane_run_v0",
            "notes": "trace와 omission stress test가 필요할 때만 여는 두 번째 비교 lane입니다.",
            "detail_href": "lane-detail-claude.html",
            "editor_href": "lane-editor-claude.html",
        },
    ]

    selected_line_reason_map = _bundle_reason_map_for_line(selected_line["raw_value"])
    case_detail_bundles = _attach_bundle_reasons(
        evidence_bundle_index,
        ["bundle_01_raw_intake_middle_layer_gap", "bundle_05_visible_split_to_recall_surface", "bundle_03_meaning_vs_format_disentangle"],
        reason_map=selected_line_reason_map,
    )
    inspector_bundles = _attach_bundle_reasons(
        evidence_bundle_index,
        ["bundle_01_raw_intake_middle_layer_gap", "bundle_02_reentry_survival_without_promotion", "bundle_03_meaning_vs_format_disentangle", "bundle_05_visible_split_to_recall_surface"],
        reason_map=selected_line_reason_map,
    )
    recall_bundles = _attach_bundle_detail_hrefs(evidence_bundles)
    external_bundles = _attach_bundle_detail_hrefs([bundle for bundle in evidence_bundles if bundle.get("bundle_id") in {
        "bundle_01_raw_intake_middle_layer_gap",
        "bundle_04_business_corridor_subaxis_mix",
        "bundle_05_visible_split_to_recall_surface",
    }] or evidence_bundles[:3])
    routing_bundles = _attach_bundle_reasons(
        evidence_bundle_index,
        ["bundle_02_reentry_survival_without_promotion", "bundle_06_boundary_specificity_without_closure", "bundle_04_business_corridor_subaxis_mix", "bundle_07_axis_stability_distribution", "bundle_01_raw_intake_middle_layer_gap"],
        reason_map=_bundle_reason_map_for_routing(),
    )
    lane_run_bundles = _attach_bundle_reasons(
        evidence_bundle_index,
        ["bundle_01_raw_intake_middle_layer_gap", "bundle_03_meaning_vs_format_disentangle", "bundle_04_business_corridor_subaxis_mix", "bundle_06_boundary_specificity_without_closure", "bundle_07_axis_stability_distribution"],
        reason_map=_bundle_reason_map_for_lane_runs(),
    )
    selected_bundle = case_detail_bundles[0] if case_detail_bundles else {}
    compare_target = generated_lines[1] if len(generated_lines) > 1 else generated_lines[0]
    intake_steps = [
        {
            "label": "source 확인",
            "status": "done",
            "summary": inputs_preview.get("source_id") or current_reading.get("case_header", {}).get("case_id") or "source not fixed",
        },
        {
            "label": "intake 방식 선택",
            "status": "done" if inputs_preview.get("intake_classification") else "active",
            "summary": inputs_preview.get("intake_classification") or "runtime bridge / structured intake pending",
        },
        {
            "label": "bundle / reference 생성",
            "status": "done" if case_detail_bundles else "active",
            "summary": f"{len(case_detail_bundles)} evidence bundles are already linked to the current reading.",
        },
        {
            "label": "launch / hold / preview",
            "status": "hold" if governance.get("hold_state") else "active",
            "summary": governance.get("release_condition") or "Preview only until governance and recall density become clearer.",
        },
    ]
    worker_request = {
        "request_id": "wrk_codex_line_refine_v1",
        "status": "pending_approval" if governance.get("hold_state") else "ready",
        "target_adapter": "codex-cli",
        "target_label": "Codex rewrite worker",
        "intent": "rewrite selected line with bundle-grounded language while preserving recall order",
        "selection_basis": {
            "line": selected_line["raw_value"],
            "bundle_id": selected_bundle.get("bundle_id") or "bundle_pending",
            "family": selected_line["family"],
            "compare_target": compare_target["raw"],
        },
        "payload_preview": {
            "source_line": selected_line["raw_value"],
            "human_translation": selected_line["human_translation"],
            "bundle_ids": [bundle.get("bundle_id") for bundle in case_detail_bundles[:3] if bundle.get("bundle_id")],
            "rewrite_goal": "Keep evidence-grounded wording and expose what still needs reread.",
            "return_format": ["raw", "internal_reading", "refined", "user_language"],
        },
        "request_summary": "Selected line and bundle set are packaged as an explicit request object rather than free-form chat.",
        "approval_gate": governance.get("release_condition") or "Human checks the payload preview before launch.",
        "launch_href": "worker-request-launch.json",
        "export_href": "worker-request-export.md",
        "reopen_href": "worker-inbox.html",
    }
    run_trace_rows = [
        {
            "trace_id": "run_intake_preview_v1",
            "trace_kind": "intake_preview",
            "status": "done",
            "adapter": "surface",
            "started_at": current_reading.get("case_header", {}).get("updated_at") or "unknown",
            "ended_at": current_reading.get("case_header", {}).get("updated_at") or "unknown",
            "selected_line": selected_line["raw_value"],
            "bundle_ids": [bundle.get("bundle_id") for bundle in case_detail_bundles[:2] if bundle.get("bundle_id")],
            "summary": "Intake contract fixed the source, matched context layers, and preserved weak carry flags.",
            "request_payload": {
                "source_id": inputs_preview.get("source_id"),
                "classification": inputs_preview.get("intake_classification"),
                "next_lane_hint": inputs_preview.get("next_lane_hint"),
            },
            "return_text": inputs_preview.get("weakness_note") or "No weakness note recorded.",
            "retry_allowed": True,
            "reopen_allowed": True,
            "artifact_href": "case-detail.html",
        },
        {
            "trace_id": worker_request["request_id"],
            "trace_kind": "worker_rewrite_request",
            "status": worker_request["status"],
            "adapter": worker_request["target_adapter"],
            "started_at": "queued",
            "ended_at": "not_started",
            "selected_line": selected_line["raw_value"],
            "bundle_ids": worker_request["payload_preview"]["bundle_ids"],
            "summary": worker_request["intent"],
            "request_payload": worker_request["payload_preview"],
            "return_text": "Awaiting launch. Result should return as raw / internal reading / refined / user-language packet.",
            "retry_allowed": True,
            "reopen_allowed": True,
            "artifact_href": "external-resources.html",
        },
        {
            "trace_id": "run_lane_compare_v1",
            "trace_kind": "lane_comparison",
            "status": "done",
            "adapter": "lane-suite",
            "started_at": "after internal recall",
            "ended_at": "current surface",
            "selected_line": selected_line["raw_value"],
            "bundle_ids": [bundle.get("bundle_id") for bundle in lane_run_bundles[:3] if bundle.get("bundle_id")],
            "summary": "Lane comparison kept the fixed bottom pipeline and returned diff-only results.",
            "request_payload": {"pipeline": ["Read", "Apply", "Search", "Validate", "Report"]},
            "return_text": "ChatGPT lane remains baseline; Gemini and Claude lanes are still candidate-only.",
            "retry_allowed": False,
            "reopen_allowed": True,
            "artifact_href": "lane-runs.html",
        },
    ]
    rewrite_return_loop = {
        "stages": [
            {"label": "raw", "status": "ready", "summary": selected_line["raw_value"]},
            {
                "label": "internal reading",
                "status": "ready",
                "summary": "Carry bundle rationale and recall-order notes before any cleanup.",
            },
            {
                "label": "refined",
                "status": "queued",
                "summary": "Refine dossier language without disconnecting it from evidence bundles.",
            },
            {
                "label": "user-language",
                "status": "queued",
                "summary": "Return a user-facing version after the refined layer is grounded.",
            },
        ],
        "return_packet": {
            "raw": selected_line["raw_value"],
            "internal_reading": selected_line["human_translation"],
            "refined": "Bundle-grounded refinement pending worker execution.",
            "user_language": "User-language rewrite pending worker execution.",
        },
        "comment_loop": {
            "inbox": "Rewrite return lands in the case inbox rather than overwriting the current page.",
            "comment_target": worker_request["target_label"],
            "reopen_allowed": True,
            "approval_required": True,
        },
    }
    worker_inbox = {
        "title": "Worker Inbox",
        "items": [
            {
                "message_id": "msg_worker_request_pending_v1",
                "status": worker_request["status"],
                "target": worker_request["target_label"],
                "headline": "rewrite request is waiting for approval",
                "summary": worker_request["intent"],
                "comment_hint": "Approval comment or reopen reason should be attached here instead of overwriting the case detail.",
            },
            {
                "message_id": "msg_lane_compare_return_v1",
                "status": "done",
                "target": "lane-suite",
                "headline": "lane comparison return arrived",
                "summary": "ChatGPT lane remains baseline; candidate lanes stayed held.",
                "comment_hint": "Reopen if a second comparison lane needs activation.",
            },
        ],
    }
    paper_proper_bridge = _load_paper_proper_bridge_state(repo_root)

    return {
        "page_title": "VectorFL Paper",
        "core_sentence": "VectorFL Paper는 scenario-bearing material을 받아 내부 재독해, 업무 배정, CLI 실행, 감독 판단, 결과 귀속을 한 흐름으로 운영하는 통합 엔진의 control surface입니다.",
        "paper_proper_bridge": paper_proper_bridge,
        "navigation": [
            {"key": "engine-overview", "label": "엔진 개요", "href": "engine-overview.html"},
            {"key": "cases", "label": "운영 보드", "href": "cases.html"},
            {"key": "case-detail", "label": "현재 케이스", "href": "case-detail.html"},
            {"key": "case-inspector", "label": "해석 인스펙터", "href": "case-inspector.html"},
            {"key": "line-review", "label": "line 검토", "href": "line-review.html"},
            {"key": "case-routing", "label": "업무 배정", "href": "case-routing.html"},
            {"key": "internal-recall", "label": "내부 재독해", "href": "internal-recall.html"},
            {"key": "external-resources", "label": "입력 / 외부 비교", "href": "external-resources.html"},
            {"key": "lanes", "label": "CLI / 어댑터", "href": "lanes.html"},
            {"key": "cli-setup", "label": "CLI 설정 작업공간", "href": "cli-setup.html"},
            {"key": "agent-mcp-control", "label": "에이전트 / MCP 운용", "href": "agent-mcp-control.html"},
            {"key": "lane-runs", "label": "실행 비교", "href": "lane-runs.html"},
            {"key": "organs", "label": "팀 / 운영 셀", "href": "organs.html"},
            {"key": "organ-registry", "label": "팀 계약 / 설정", "href": "organ-registry.html"},
            {"key": "contracts-workspace", "label": "계약 작업공간", "href": "contracts-workspace.html"},
            {"key": "program-workspaces", "label": "프로그램 워크스페이스", "href": "program-workspaces.html"},
            {"key": "trace-audit", "label": "이슈 / 감사", "href": "trace-audit.html"},
            {"key": "worker-inbox", "label": "결과 회신", "href": "worker-inbox.html"},
        ],
        "navigation_groups": [
            {
                "group_key": "board",
                "group_label": "BOARD",
                "vectorfl_meaning": "현재 loop와 감독 판단",
                "item_keys": ["engine-overview", "cases", "trace-audit", "worker-inbox"],
            },
            {
                "group_key": "intake",
                "group_label": "INTAKE",
                "vectorfl_meaning": "재료 확인과 내부/외부 준비",
                "item_keys": ["internal-recall", "external-resources"],
            },
            {
                "group_key": "work",
                "group_label": "WORK",
                "vectorfl_meaning": "케이스 읽기, 해석, 배정",
                "item_keys": ["case-detail", "case-inspector", "line-review", "case-routing"],
            },
            {
                "group_key": "teams",
                "group_label": "TEAMS",
                "vectorfl_meaning": "운영 셀, 계약, 역할 배정",
                "item_keys": ["organs", "organ-registry", "contracts-workspace", "program-workspaces"],
            },
            {
                "group_key": "cli",
                "group_label": "CLI",
                "vectorfl_meaning": "도구 연결, 모델, 실행 비교",
                "item_keys": ["lanes", "cli-setup", "agent-mcp-control", "lane-runs"],
            },
        ],
        "engine_overview": {
            "mission": "VectorFL Paper는 여러 프로그램/팀/CLI가 내부 공간의 line과 기억 자산을 공유 공급원으로 삼아 움직이도록 조율하는 통합 엔진의 시작점입니다.",
            "core_loop": [
                "line 숙성",
                "팀 배정",
                "CLI/MCP 실행",
                "감독 판단",
                "귀속 / 재정돈",
                "다음 프로그램 공급",
            ],
            "active_programs": [
                {
                    "name": "Program Builder Cell",
                    "status": "active",
                    "mission": "Codex를 메인 오케스트레이터로 두고 line 검색 / 생성 / 번역 / 외부자료검색 / 코드실행을 엮어 프로그램 제작 loop를 닫습니다.",
                    "teams": ["input", "line-state", "translation", "flow-interpretation", "governance", "trace-memory"],
                    "cli_stack": ["codex-main", "gemini-support"],
                    "primary_runtime": "Codex main orchestrator",
                    "output_route": "launch manifest -> trace -> return memory",
                },
                {
                    "name": "Publishing House Cell",
                    "status": "planned",
                    "mission": "Codex를 메인 집필 런타임으로 두고 공간의 line을 읽어 글, 해설, 출판형 산출물로 번역하고 다시 line 강화 재료로 돌려줍니다.",
                    "teams": ["line-state", "translation", "trace-memory"],
                    "cli_stack": ["codex-main", "payload-export"],
                    "primary_runtime": "Codex main orchestrator",
                    "output_route": "draft manuscript -> supervisor review -> return memory",
                },
                {
                    "name": "External Research Cell",
                    "status": "active",
                    "mission": "Codex가 감독하고 Gemini가 비교 지원을 맡아 내부 gap을 외부 비교 과제로 바꾸고 reference 후보를 주입 가능한 형태로 되돌립니다.",
                    "teams": ["input", "governance"],
                    "cli_stack": ["codex-supervised", "gemini-support", "payload-export"],
                    "primary_runtime": "Codex supervised / Gemini support",
                    "output_route": "reference candidates -> governance gate -> internal recall",
                },
            ],
            "shared_supply": [
                "internal lines",
                "evidence bundles",
                "conversation-derived directives",
                "supervisor decisions",
                "return memory packets",
            ],
            "supervisor_rules": [
                "감독자는 각 프로그램의 목적과 방향을 강화하지만, 각 팀의 세부 처리까지 다시 수작업으로 대체하지 않습니다.",
                "각 프로그램은 같은 line 공급원을 공유하지만 서로 다른 목적과 출력 형식을 가집니다.",
                "CLI/MCP 실행은 항상 현재 contract, launch manifest, return route와 함께 보여야 합니다.",
            ],
        },
        "engine_state": {
            "selected_program": {
                "name": "program_builder",
                "label": "Program Builder Workspace",
                "objective": "프로그램 제작과 코드 실행 loop를 닫는 현재 기본 워크스페이스",
            },
            "selected_runtime": {
                "name": "codex_runtime",
                "label": "Codex Main Orchestrator",
                "entry": "codex",
                "binding_path": "runtime/manifests/vectorfl_agent_runtime_codex_v0.json",
                "role": "현재 엔진의 기본 운영 CLI",
            },
            "shared_line_supply": "internal lines + evidence bundles + supervisor directives",
            "current_route": "program workspace -> codex-owned team stack -> support runtimes -> trace/inbox -> return memory",
            "supervisor_focus": "지금은 Codex를 메인 오케스트레이터로 고정한 뒤, program_builder 기준의 line 공급 / 계약 / runtime binding을 먼저 안정화합니다.",
        },
        "current_operating_selection": {
            "selection_id": "vectorfl_current_operating_selection_v0",
            "selected_program": "program_builder",
            "selected_program_label": "Program Builder Workspace",
            "selected_runtime": "codex_runtime",
            "selected_runtime_label": "Codex Main Orchestrator",
            "selected_contract_path": "runtime/manifests/vectorfl_paper_internal_read_cell_draft_v0.md",
            "selected_contract_label": "Internal Read Draft",
            "selected_launch_manifest_path": "runtime/manifests/vectorfl_operable_surface_launch_chatgpt_v0.json",
            "selected_launch_manifest_label": "ChatGPT lane launch manifest",
            "selected_team_slug": "flow-interpretation",
            "selected_lane_slug": "chatgpt",
            "selection_reason": "현재는 Codex가 program_builder의 메인 오케스트레이터이므로, 내부 읽기 계약과 codex launch manifest를 기본 운용 기준으로 먼저 잠급니다.",
            "save_target_path": "runtime/manifests/vectorfl_operable_surface_current_selection_v0.json",
        },
        "program_workspaces": {
            "workspace_rows": [
                {
                    "name": "program_builder",
                    "label": "Program Builder Workspace",
                    "status": "active",
                    "objective": "프로그램 제작과 코드 실행 loop를 닫는 워크스페이스",
                    "line_supply": ["internal lines", "evidence bundles", "supervisor directives"],
                    "team_stack": ["input", "line-state", "translation", "flow-interpretation", "governance", "trace-memory"],
                    "cli_stack": ["codex-main", "gemini-support"],
                    "primary_runtime": "Codex main orchestrator",
                    "current_artifacts": ["launch manifest", "worker request", "trace updates"],
                },
                {
                    "name": "publishing_house",
                    "label": "Publishing House Workspace",
                    "status": "planned",
                    "objective": "공간의 line을 읽어 글과 설명 산출물을 만드는 워크스페이스",
                    "line_supply": ["line families", "conversation traces", "return memory"],
                    "team_stack": ["line-state", "translation", "trace-memory"],
                    "cli_stack": ["codex-main"],
                    "primary_runtime": "Codex main orchestrator",
                    "current_artifacts": ["draft outline", "editorial return packet"],
                },
                {
                    "name": "research_bridge",
                    "label": "Research Bridge Workspace",
                    "status": "active",
                    "objective": "외부 비교/검색/주입을 전담하는 워크스페이스",
                    "line_supply": ["uncertainty rows", "searchable forms", "selection state"],
                    "team_stack": ["input", "governance"],
                    "cli_stack": ["codex-supervised", "gemini-support", "payload-export"],
                    "primary_runtime": "Codex supervised / Gemini support",
                    "current_artifacts": ["reference candidates", "injection review notes"],
                },
            ],
            "workspace_rules": [
                "프로그램 하나가 팀 하나가 아니라, 여러 팀과 CLI가 얽힌 하나의 운영 loop입니다.",
                "모든 프로그램은 shared line supply를 먹고 다시 return memory를 남겨야 합니다.",
                "지금 기준으로는 새 프로그램을 추가할 때 Codex가 메인인지, Gemini/MCP가 어떤 보조 역할인지까지 함께 정의해야 합니다.",
            ],
            "manifest_rows": [
                {
                    "label": "Program Builder Workspace",
                    "path": "runtime/manifests/vectorfl_program_workspace_program_builder_v0.json",
                    "purpose": "프로그램 제작 loop의 현재 team/cli/output route를 저장하는 시작 manifest",
                },
                {
                    "label": "Publishing House Workspace",
                    "path": "runtime/manifests/vectorfl_program_workspace_publishing_house_v0.json",
                    "purpose": "글쓰기/출판 셀의 line supply와 return route를 잡는 manifest",
                },
                {
                    "label": "Research Bridge Workspace",
                    "path": "runtime/manifests/vectorfl_program_workspace_research_bridge_v0.json",
                    "purpose": "외부 비교/주입 전용 워크스페이스의 launch 기준을 잡는 manifest",
                },
            ],
        },
        "agent_mcp_control": {
            "runtime_rows": [
                {
                    "label": "Codex Main Orchestrator",
                    "mode": "active",
                    "type": "agent runtime",
                    "role": "메인 운영 CLI",
                    "owns": ["program_builder", "publishing_house", "default routing control"],
                    "entry": "codex",
                    "contract_link": "docs/contracts/vectorfl_paper_internal_read_cell_v0.md",
                    "return_route": "worker-inbox -> trace-audit -> return memory",
                },
                {
                    "label": "Gemini CLI",
                    "mode": "active",
                    "type": "agent runtime",
                    "role": "비교 / 외부 탐색 지원",
                    "owns": ["research_bridge", "comparison support"],
                    "entry": "gemini",
                    "contract_link": "docs/contracts/vectorfl_paper_external_resource_cell_v0.md",
                    "return_route": "governance gate -> worker-inbox -> internal recall",
                },
                {
                    "label": "MCP Bridge",
                    "mode": "planned",
                    "type": "context / tool bridge",
                    "role": "미래 연결 브리지",
                    "owns": ["future external connectors"],
                    "entry": "mcp connector slots",
                    "contract_link": "docs/contracts/vectorfl_paper_operating_cell_schema_v0.md",
                    "return_route": "tool output -> trace -> workspace packet",
                },
            ],
            "control_rules": [
                "에이전트와 MCP는 Paper 바깥에서 떠다니는 부속품이 아니라, 각 프로그램 워크스페이스에 소속된 실행층입니다.",
                "현재 기준으로 Codex는 메인 오케스트레이터이고, 다른 런타임은 Codex 아래의 보조 / 비교 / 연결 층으로 배치합니다.",
                "runtime owner, contract link, return route가 안 보이면 아직 통합 운용면이 아닙니다.",
                "MCP도 결국 line 공급과 return memory 강화에 기여할 때만 연결 대상으로 봅니다.",
            ],
            "manifest_rows": [
                {
                    "label": "Codex Runtime Binding",
                    "path": "runtime/manifests/vectorfl_agent_runtime_codex_v0.json",
                    "purpose": "Codex CLI가 어떤 프로그램과 계약에 묶이는지 저장하는 binding",
                },
                {
                    "label": "Gemini Runtime Binding",
                    "path": "runtime/manifests/vectorfl_agent_runtime_gemini_v0.json",
                    "purpose": "Gemini CLI의 비교/거버넌스 담당 범위를 저장하는 binding",
                },
                {
                    "label": "MCP Bridge Binding",
                    "path": "runtime/manifests/vectorfl_agent_runtime_mcp_bridge_v0.json",
                    "purpose": "미래 connector와 tool bridge가 어떤 return route를 가지는지 저장하는 binding",
                },
            ],
        },
        "cases": [
            {
                **item,
                "source_title": item.get("headline") or item.get("case_id") or "source",
                "source_title": gmd_source_block.get("source_name") or item.get("headline") or item.get("case_id") or "source",
                "source_type": gmd_source_block.get("source_type") or "external_case_md",
                "current_stage": gmd_use_block.get("next_team_or_lane") or item.get("lane_kind") or "unknown",
                "generated_line_count": len(generated_lines),
                "family_count": len(gmd_family_block.get("related_lines") or line_family_rows),
                "unresolved_count": len(gmd_uncertainty_block) or 1,
                "next_action_hint": item.get("preferred_next_candidate") or next_ref or "none",
                "internal_reuse_hint": "available" if recall_rows else "thin",
            }
            for item in queue_preview
        ],
        "case_detail": {
            "case_header": current_reading.get("case_header") or {},
            "body": current_body,
            "lane": current_reading.get("lane") or {},
            "governance": governance,
            "responsibility": responsibility,
            "progression": progression,
            "trace_preview": trace_preview,
            "linked_programs": programs_preview.get("linked_programs") or [],
            "internal_recall_docs": recall_rows[:3],
            "line_family_rows": line_family_rows,
            "source_summary": {
                "title": gmd_source_block.get("source_name") or inputs_preview.get("requested_artifact_ref") or current_body.get("headline") or "source",
                "source_type": gmd_source_block.get("source_type") or "external_case_md",
                "native_structure_summary": gmd_commentary.get("structure_summary") or "Native structure summary not yet available.",
                "segmentation_basis": (
                    f"split_mode={gmd_segmentation.get('split_mode_used') or 'unknown'} / "
                    f"dominant_unit={gmd_segmentation.get('dominant_unit_type') or 'unknown'}"
                ),
                "segmentation_reason": gmd_commentary.get("why_this_structure_matters") or "아직 왜 이렇게 나눠 읽는지가 정리되지 않았습니다.",
            },
            "generated_lines": generated_lines,
            "family_clusters": [
                {
                    "label": selected_line["family"],
                    "summary": "Native document sequence is being used as the first family scaffold before thicker internal binding.",
                },
                *line_family_rows[:2],
            ],
            "selected_line": selected_line,
            "selected_line_dossier": selected_line_dossier,
            "internal_existing": [
                "three-layer structure lock",
                "handoff boundary lock",
                "surface-only Paperclip adoption lock",
            ],
            "internal_missing": [
                *(row.get("pending_interpretation") for row in gmd_uncertainty_block[:3] if row.get("pending_interpretation")),
                "deeper directive recall around host-shell adoption",
                "line usability proof beyond current case",
            ],
            "evidence_bundles": case_detail_bundles,
        },
        "operating_board": {
            "current_case": current_reading.get("case_header", {}).get("case_id") or "unknown",
            "selected_line_family": selected_line["family"],
            "selected_bundle_count": len(case_detail_bundles),
            "pending_approvals": 1 if worker_request["status"] == "pending_approval" else 0,
            "active_runs": sum(1 for row in run_trace_rows if row["status"] in {"active", "ready", "pending_approval"}),
            "control_note": "VectorFL Paper is treated as a reading-surface control plane: selection, launch, trace, approval, and return stay visible together.",
            "decision_queue": [
                {
                    "label": "rewrite launch approval",
                    "status": worker_request["status"],
                    "owner": worker_request["target_label"],
                    "reason": worker_request["approval_gate"],
                    "action_href": worker_request["reopen_href"],
                },
                {
                    "label": "next team handoff review",
                    "status": governance.get("hold_state") or "active",
                    "owner": responsibility.get("current_organ_ref") or "organ:flow_interpretation",
                    "reason": governance.get("reason_summary") or "현재 handoff와 hold를 같이 검토해야 합니다.",
                    "action_href": "case-routing.html",
                },
            ],
            "active_team_cli_rows": [
                {
                    "team": organ["label"],
                    "cli": organ["managing_cli"],
                    "lane": organ["managing_lane_slug"],
                    "mode": "current" if organ["current"] else ("next" if organ["next_candidate"] else "available"),
                }
                for organ in organ_rows
                if organ["current"] or organ["next_candidate"] or organ["slug"] in {"input", "trace-memory"}
            ],
            "latest_updates": [
                {
                    "kind": row.get("trace_kind") or "trace",
                    "summary": row.get("summary") or "update",
                    "status": row.get("status") or "done",
                    "href": row.get("artifact_href") or "trace-audit.html",
                }
                for row in run_trace_rows[:3]
            ],
        },
        "selection_state": {
            "selected_line": selected_line,
            "selected_bundle": {
                "bundle_id": selected_bundle.get("bundle_id") or "bundle_pending",
                "theme": selected_bundle.get("theme") or "No bundle selected yet.",
                "why_it_is_here": selected_bundle.get("why_it_is_here") or "Bundle rationale pending.",
            },
            "selected_family": selected_line["family"],
            "current_compare_target": {
                "line_id": compare_target["line_id"],
                "raw": compare_target["raw"],
                "status": compare_target["status"],
            },
            "actions": [
                {"label": "clear selection", "mode": "destructive-safe", "summary": "현재 line / bundle / compare target을 비웁니다."},
                {"label": "replace bundle", "mode": "replace", "summary": "selected line은 유지하고 bundle set만 다시 고릅니다."},
                {"label": "inspect selection", "mode": "inspect", "summary": "선택 객체를 dossier / routing / trace에서 같이 엽니다."},
                {"label": "reset view", "mode": "reset", "summary": "current reading 기준으로 돌아가되 trace는 지우지 않습니다."},
            ],
        },
        "intake_wizard": {
            "steps": intake_steps,
            "current_stage": intake_steps[1]["label"],
            "launch_modes": ["launch", "hold", "preview only"],
            "source_confirmation": inputs_preview.get("requested_artifact_ref") or inputs_preview.get("source_id") or "source pending",
            "reference_creation_rule": "bundle/reference 생성은 launch 전 단계에서 분리해서 확인합니다.",
        },
        "worker_bridge": {
            "available_adapters": [
                {"adapter": "codex-cli", "status": "ready", "best_for": "rewrite selected line / refine dossier language"},
                {"adapter": "gemini-cli", "status": "candidate", "best_for": "compare reread with bundles / alternative recall ordering"},
                {"adapter": "payload-export", "status": "ready", "best_for": "manual launch outside the surface while keeping request trace"},
            ],
            "current_request": worker_request,
            "return_loop": rewrite_return_loop,
            "inbox": worker_inbox,
        },
        "case_inspector": {
            "governance": governance,
            "inputs_preview": inputs_preview,
            "next_candidates": next_candidates,
            "selected_context_layers": inputs_preview.get("matched_context_layers") or [],
            "selected_artifact_refs": inputs_preview.get("selected_artifact_refs") or [],
            "release_condition": governance.get("release_condition"),
            "next_check_trigger": governance.get("next_check_trigger"),
            "selected_line": selected_line,
            "selected_line_dossier": selected_line_dossier,
            "source_linkage": [
                gmd_read.get("doc_ref") or inputs_preview.get("requested_artifact_ref") or "requested artifact",
                * (inputs_preview.get("selected_artifact_refs") or [])[:3],
            ],
            "family_linkage": [selected_line["family"], *[item["label"] for item in line_family_rows[:2]]],
            "declaration_linkage": [item["title"] for item in recall_rows[:3]],
            "judgment_history_linkage": [item.get("summary") or "judgment" for item in trace_preview[:2]],
            "searchable_form": selected_line["searchable_form"],
            "adoption_form": selected_line["adoption_form"],
            "candidate_handoff": selected_line["candidate_handoff"],
            "what_it_preserves": selected_line["preserves"],
            "what_it_omits": selected_line["omits"],
            "uncertainty": selected_line["uncertainty"],
            "related_internal_records": [row.get("title") for row in recall_linkage_rows + recall_rows[:3]],
            "usable_targets": [
                gmd_use_block.get("next_team_or_lane") or "translation_first",
                responsibility.get("current_organ_ref") or "organ:translation",
                *(item.get("organ_ref") for item in next_candidates[:2] if item.get("organ_ref")),
            ],
            "adoption_hints": selected_line["next_step_ideas"],
            "evidence_bundles": inspector_bundles,
        },
        "case_routing": {
            "current_organ_ref": responsibility.get("current_organ_ref"),
            "current_lane_ref": responsibility.get("current_lane_ref"),
            "placement_reason": responsibility.get("placement_reason"),
            "next_candidates": next_candidates,
            "restriction_flags": governance.get("restriction_flags") or [],
            "release_condition": governance.get("release_condition"),
            "linked_programs": linked_programs,
            "external_resource_teams": [
                {"name": "reference-research", "enabled": True, "mode": "agent-led"},
                {"name": "comparative-source", "enabled": True, "mode": "agent-led"},
                {"name": "field-validation", "enabled": False, "mode": "hybrid"},
            ],
            "external_program_teams": [
                {"name": "program-bridge", "enabled": True, "mode": "hybrid"},
                {"name": "action-request", "enabled": False, "mode": "human-gated"},
            ],
            "routing_basis": {
                "selected_line": selected_line["raw_value"],
                "search_trigger": bool(gmd_uncertainty_block),
                "search_reason": (
                    gmd_uncertainty_block[0].get("pending_interpretation")
                    if gmd_uncertainty_block
                    else "internal recall first, then compare if still thin"
                ),
                "current_material_stage": gmd_use_block.get("next_team_or_lane") or "translation_first",
            },
            "team_assignment_options": [
                {
                    "team": organ["label"],
                    "slug": organ["slug"],
                    "managing_cli": organ["managing_cli"],
                    "paired_external_team": organ["paired_external_team"],
                    "handoff_targets": organ["handoff_targets"],
                }
                for organ in organ_rows
            ],
            "cli_assignment_options": [
                {
                    "lane": lane["label"],
                    "slug": lane["slug"],
                    "provider_model": lane["provider_model"],
                    "owning_cli": lane["owning_cli"],
                    "managed_team_slugs": lane["managed_team_slugs"],
                }
                for lane in lane_rows
            ],
            "evidence_bundles": routing_bundles,
        },
        "internal_recall": {
            "selected_line": selected_line["raw_value"],
            "recall_docs": [*recall_linkage_rows, *recall_rows],
            "line_family_rows": [
                {
                    "label": selected_line["family"],
                    "summary": "The provisional line currently sits in the native document sequence before thicker family rebinding.",
                },
                *line_family_rows,
            ],
            "trace_rows": trace_preview,
            "gap_summary": [
                "line semantics remain thinner than line infrastructure",
                "family recall is still weaker than line generation",
                "external search should be justified by internal gap first",
                *(row.get("pending_interpretation") for row in gmd_uncertainty_block[:2] if row.get("pending_interpretation")),
            ],
            "role_hints": gmd_role_block[:6],
            "relation_clues": (gmd_native.get("relation_clues") or [])[:6],
            "provisional_line_block": gmd_line_block[:6],
            "evidence_bundles": recall_bundles,
        },
        "external_resources": {
            "trigger_line": selected_line["raw_value"],
            "trigger_reason": (
                gmd_uncertainty_block[0].get("pending_interpretation")
                if gmd_uncertainty_block
                else governance.get("reason_summary") or "Need external reinforcement where internal recall remains thin."
            ),
            "question_set": [
                f"What external source clarifies this line: {selected_line['raw_value']}?",
                "Which reference sharpens the current uncertainty without flattening the source structure?",
                "Which source helps compare host-shell adoption while preserving VectorFL core semantics?",
            ],
            "wanted_material_types": ["product page grammar", "operable detail reference", "routing editor example"],
            "excluded_material_types": ["marketing landing page", "style-only admin dashboard", "color-theme inspiration only"],
            "candidate_sources": saved_connection_preview,
            "attention_rows": attention_memory_preview,
            "uncertainty_rows": gmd_uncertainty_block[:6],
            "searchable_form": selected_line["searchable_form"],
            "setup_steps": [
                {
                    "label": "scenario entry",
                    "status": "done",
                    "summary": inputs_preview.get("requested_artifact_ref") or selected_line["raw_value"],
                },
                {
                    "label": "material bundle review",
                    "status": "done",
                    "summary": f"{len(case_detail_bundles)} bundles are already attached to this case.",
                },
                {
                    "label": "team assignment",
                    "status": "active",
                    "summary": "Choose internal owner and paired external team before widening.",
                },
                {
                    "label": "cli adapter selection",
                    "status": "active",
                    "summary": "Pick owning CLI, provider, model, and contract path.",
                },
                {
                    "label": "launch decision",
                    "status": "hold" if governance.get("hold_state") else "active",
                    "summary": worker_request["approval_gate"],
                },
            ],
            "scenario_entry": {
                "objective": current_reading.get("case_header", {}).get("headline") or "current scenario objective pending",
                "seed_reason": "Scenario-bearing material should enter as a loop seed, not as a flat TODO.",
                "source_confirmation": inputs_preview.get("source_id") or inputs_preview.get("requested_artifact_ref") or "source pending",
            },
            "material_bundle_review": {
                "selected_refs": inputs_preview.get("selected_artifact_refs") or [],
                "reference_rule": "launch 전에 bundle/reference 생성 여부를 한 번 더 확인합니다.",
                "linked_bundle_ids": [bundle.get("bundle_id") for bundle in case_detail_bundles if bundle.get("bundle_id")],
            },
            "team_cli_setup": {
                "selected_team": responsibility.get("current_organ_ref") or "organ:flow_interpretation",
                "paired_external_team": "reference-research",
                "owning_cli": worker_request["target_adapter"],
                "provider": lane_rows[0]["provider"],
                "model": lane_rows[0]["model"],
                "md_contracts": [
                    "vectorfl_paper_internal_read_cell_v0.md",
                    "vectorfl_paper_external_resource_cell_v0.md",
                    "vectorfl_paper_synthesis_cell_v0.md",
                ],
                "env_check": lane_rows[0]["env_summary"],
            },
            "launch_decision": {
                "modes": ["preview", "hold", "launch"],
                "current_mode": "hold" if governance.get("hold_state") else "preview",
                "reason": worker_request["approval_gate"],
            },
            "live_updates": [
                {
                    "headline": "rewrite packet is staged but still waiting for approval",
                    "status": worker_request["status"],
                    "owner": worker_request["target_label"],
                },
                {
                    "headline": "paired external team should only widen after current uncertainty is restated",
                    "status": "active",
                    "owner": "reference-research",
                },
            ],
            "evidence_bundles": external_bundles,
            "worker_request": worker_request,
        },
        "lanes": {
            "top_note": "최종 판단권은 lane 자체가 아니라 감독 표면이 가집니다. lane은 비교 실행과 결과 반환을 맡습니다.",
            "middle_note": "각 lane은 교체 가능하지만, 같은 bottom pipeline과 같은 selection object를 공유해야만 비교가 성립합니다.",
            "bottom_pipeline": ["Read", "Apply", "Search", "Validate", "Report"],
            "lane_rows": lane_rows,
        },
        "lane_runs": {
            "lanes": [
                {
                    "name": "ChatGPT lane",
                    "mode": "hybrid",
                    "read_result": f"Reads {selected_line['raw_value']} against {len(recall_linkage_rows) + len(recall_rows)} internal records before widening.",
                    "apply_result": f"Uses {len(gmd_line_block)} provisional lines and {len(gmd_role_block)} role hints as translation-ready material.",
                    "search_result": (
                        gmd_uncertainty_block[0].get("pending_interpretation")
                        if gmd_uncertainty_block
                        else "아직 외부 검색으로 바로 키우기보다, 내부 recall을 먼저 다시 보는 편이 맞습니다."
                    ),
                    "validate_result": f"Checks governance hold={governance.get('hold_state') or 'none'} and unresolved_count={len(gmd_uncertainty_block)} before lock.",
                    "report_result": f"선택된 line family {selected_line['family']} 기준으로 검색용 말과 차용용 말을 다시 정리합니다.",
                    "status": "active",
                    "diff_note": "Most aligned with current GMD-backed first pass.",
                },
                {
                    "name": "Gemini lane",
                    "mode": "candidate",
                    "read_result": "내부 recall이 더 두꺼워졌을 때 다른 강조점으로 다시 읽어보는 후보 lane입니다.",
                    "apply_result": "현재 선택된 line에 대해 role hint 비중을 다르게 읽었을 때 차이가 생기는지 비교합니다.",
                    "search_result": "외부 자료 질문을 조금 다르게 짜 봐야 할 때 쓰는 후보 비교 lane입니다.",
                    "validate_result": "같은 고정 pipeline을 유지할 수 있을 때만 비교에 투입합니다.",
                    "report_result": "자유 대화가 아니라 ChatGPT lane과의 차이만 보고합니다.",
                    "status": "hold",
                    "diff_note": "Held until first-pass recall density is less thin.",
                },
                {
                    "name": "Claude lane",
                    "mode": "candidate",
                    "read_result": "원본 순서 보존과 빠뜨린 nuance를 다시 보는 두 번째 읽기용 후보 lane입니다.",
                    "apply_result": "omission handling과 uncertainty carry가 얼마나 버티는지 점검합니다.",
                    "search_result": "내부 recall 이후에만 다른 차용형/검색형 문장을 제안해야 합니다.",
                    "validate_result": "lane를 너무 빨리 늘리지 않기 위해 candidate 상태로만 둡니다.",
                    "report_result": "보고 문장의 읽힘과 omission carry 차이를 비교합니다.",
                    "status": "hold",
                    "diff_note": "Held until the first lane proves stable and reusable.",
                },
            ],
            "selected_line": selected_line["raw_value"],
            "fixed_pipeline": ["Read", "Apply", "Search", "Validate", "Report"],
            "lane_rule_note": "Lanes do not directly chat with each other; they run the same bottom pipeline and are compared only at the top.",
            "evidence_bundles": lane_run_bundles,
            "run_trace_rows": run_trace_rows,
        },
        "organs": organ_rows,
        "organ_registry": {
            "organ_rows": organ_rows,
            "available_extension_slots": [
                {"name": "external-resource-team", "status": "available"},
                {"name": "external-program-team", "status": "available"},
                {"name": "comparison-team", "status": "reserved"},
            ],
            "bundle_modes": ["ROLE", "HANDOFF", "CAUTION", "RETURN"],
        },
        "contracts_workspace": {
            "contract_rows": [
                {
                    "label": "Operating Cell Schema",
                    "path": "docs/contracts/vectorfl_paper_operating_cell_schema_v0.md",
                    "scope": "전체 팀 구조",
                    "used_by": ["all teams"],
                    "why": "팀이 단순 이름이 아니라 lens / cli / handoff / report를 갖는 운영 셀임을 고정합니다.",
                },
                {
                    "label": "Internal Read Cell",
                    "path": "docs/contracts/vectorfl_paper_internal_read_cell_v0.md",
                    "scope": "internal_read",
                    "used_by": ["line-state", "translation"],
                    "why": "내부 재독해와 line seed 추출의 최소 계약을 고정합니다.",
                },
                {
                    "label": "External Resource Cell",
                    "path": "docs/contracts/vectorfl_paper_external_resource_cell_v0.md",
                    "scope": "external_resource",
                    "used_by": ["input", "governance"],
                    "why": "외부 비교 질문과 주입 후보 판정을 다룹니다.",
                },
                {
                    "label": "Synthesis Cell",
                    "path": "docs/contracts/vectorfl_paper_synthesis_cell_v0.md",
                    "scope": "synthesis",
                    "used_by": ["trace-memory"],
                    "why": "내부/외부 결과를 human-readable report로 묶습니다.",
                },
                {
                    "label": "Supervisor Report Format",
                    "path": "docs/contracts/vectorfl_paper_supervisor_report_format_v0.md",
                    "scope": "supervision",
                    "used_by": ["governance", "all returns"],
                    "why": "감독자가 읽을 수 있는 보고 형식을 강제합니다.",
                },
                {
                    "label": "Conversation To Line",
                    "path": "docs/contracts/vectorfl_paper_conversation_to_line_procedure_v0.md",
                    "scope": "line extraction",
                    "used_by": ["input", "line-state", "trace-memory"],
                    "why": "대화 흐름 자체를 line 재료로 다시 읽는 절차입니다.",
                },
            ],
            "workspace_rules": [
                "계약 파일은 팀 라벨보다 먼저 수정 대상입니다.",
                "CLI를 붙이기 전에 md contract path가 먼저 고정되어야 합니다.",
                "새 팀은 ROLE / HANDOFF / CAUTION / RETURN과 supervisor report 형식을 같이 가져야 합니다.",
            ],
            "draft_targets": [
                {
                    "label": "Internal Read Draft",
                    "path": "runtime/manifests/vectorfl_paper_internal_read_cell_draft_v0.md",
                    "source_contract": "docs/contracts/vectorfl_paper_internal_read_cell_v0.md",
                    "purpose": "internal_read 셀 수정 실험을 본 계약과 분리해서 먼저 적어보는 draft slot",
                    "team_slug": "line-state",
                },
                {
                    "label": "External Resource Draft",
                    "path": "runtime/manifests/vectorfl_paper_external_resource_cell_draft_v0.md",
                    "source_contract": "docs/contracts/vectorfl_paper_external_resource_cell_v0.md",
                    "purpose": "외부 비교 지시와 주입 기준을 바꾸기 전에 임시 draft로 검토하는 slot",
                    "team_slug": "input",
                },
                {
                    "label": "Synthesis Draft",
                    "path": "runtime/manifests/vectorfl_paper_synthesis_cell_draft_v0.md",
                    "source_contract": "docs/contracts/vectorfl_paper_synthesis_cell_v0.md",
                    "purpose": "감독 보고 형식과 종합 규칙을 수정할 때 먼저 써 보는 slot",
                    "team_slug": "trace-memory",
                },
            ],
        },
        "cli_setup_workspace": {
            "tool_rows": [
                {
                    "label": lane["label"],
                    "adapter_type": lane["adapter_type"],
                    "command": lane["command"],
                    "args": lane["args"],
                    "working_directory": lane["working_directory"],
                    "env_status": lane["env_status"],
                    "env_summary": lane["env_summary"],
                    "managed_teams": lane["managed_team_slugs"],
                    "contract_ref": lane["contract_ref"],
                    "launch_route": lane["return_route"],
                }
                for lane in lane_rows
            ],
            "launch_sequence": [
                "team 선택",
                "contract path 확인",
                "adapter type / provider / model 확인",
                "env test",
                "payload preview",
                "human approval",
                "launch",
                "return -> inbox -> trace",
            ],
            "workspace_rules": [
                "CLI는 외부 도구가 아니라 팀을 관리하는 셀 관리자처럼 연결합니다.",
                "command / args / workdir / env status가 보이지 않으면 아직 실제 setup 면이 아닙니다.",
                "launch 전에는 payload preview와 approval gate가 반드시 함께 보여야 합니다.",
            ],
            "launch_manifests": [
                {
                    "label": lane["label"],
                    "path": f"runtime/manifests/vectorfl_operable_surface_launch_{lane['slug']}_v0.json",
                    "adapter_type": lane["adapter_type"],
                    "command": lane["command"],
                    "args": lane["args"],
                    "contract_ref": lane["contract_ref"],
                    "lane_slug": lane["slug"],
                }
                for lane in lane_rows
            ],
        },
        "trace_audit": {
            "trace_rows": [*trace_preview, *run_trace_rows],
            "decision_anchor": (base.get("history_trace_preview") or {}).get("decision_trace_anchor"),
            "reentry_cues": (base.get("history_trace_preview") or {}).get("reentry_cues") or [],
            "residue_emphasis": (base.get("history_trace_preview") or {}).get("residue_emphasis") or [],
            "issue_updates": [
                {
                    "issue_title": worker_request["intent"],
                    "owner": worker_request["target_label"],
                    "status": worker_request["status"],
                    "next_action": "approve or reopen before launch",
                    "href": worker_request["reopen_href"],
                },
                {
                    "issue_title": "lane comparison return review",
                    "owner": "lane-suite",
                    "status": "done",
                    "next_action": "decide whether to activate a second comparison lane",
                    "href": "lane-runs.html",
                },
            ],
            "approval_cards": [
                {
                    "label": "rewrite launch approval",
                    "status": "pending" if worker_request["status"] == "pending_approval" else "ready",
                    "requester": worker_request["target_label"],
                    "payload_summary": worker_request["intent"],
                    "decision_note": worker_request["approval_gate"],
                },
                {
                    "label": "lane activation review",
                    "status": "revision_requested",
                    "requester": "lane-suite",
                    "payload_summary": "Activate a second comparison lane only if first-pass reread is stable enough.",
                    "decision_note": "Do not widen lane count before internal reread remains understandable to the supervisor.",
                },
            ],
        },
        "programs_preview": programs_preview,
        "worker_artifacts": {
            "launch_request": {
                "request_id": worker_request["request_id"],
                "adapter": worker_request["target_adapter"],
                "selection_basis": worker_request["selection_basis"],
                "payload": worker_request["payload_preview"],
                "approval_gate": worker_request["approval_gate"],
            },
            "export_packet_markdown": "\n".join(
                [
                    "# worker request export",
                    f"- request_id: `{worker_request['request_id']}`",
                    f"- adapter: `{worker_request['target_adapter']}`",
                    f"- target: `{worker_request['target_label']}`",
                    f"- selected_line: `{selected_line['raw_value']}`",
                    f"- selected_bundle: `{selected_bundle.get('bundle_id') or 'bundle_pending'}`",
                    f"- compare_target: `{compare_target['raw']}`",
                    "",
                    "## intent",
                    worker_request["intent"],
                    "",
                    "## payload",
                    json.dumps(worker_request["payload_preview"], ensure_ascii=False, indent=2),
                    "",
                    "## approval gate",
                    worker_request["approval_gate"],
                ]
            ),
            "inbox": worker_inbox,
        },
        "worker_return_board": {
            "current_request_id": worker_request["request_id"],
            "return_route": "worker-inbox -> trace-audit -> case-detail reinjection",
            "pending_comments": len(worker_inbox.get("items") or []),
            "reopen_policy": "결과는 case를 덮어쓰지 않고 comment와 reopen 사유를 붙여 다시 감독 판단으로 돌립니다.",
        },
    }


def _base_html(title: str, payload: Dict[str, Any], body_html: str) -> str:
    data = json.dumps(payload, ensure_ascii=False)
    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>
    :root {{
      --bg: #09090b;
      --bg-soft: #111113;
      --panel: #18181b;
      --panel-soft: rgba(24, 24, 27, 0.82);
      --line: #27272a;
      --line-soft: #303036;
      --ink: #f4f4f5;
      --muted: #a1a1aa;
      --chip: #202024;
      --warn-bg: rgba(239, 68, 68, 0.12);
      --warn-line: #ef4444;
      --accent: #3b82f6;
      --accent-strong: #2563eb;
      --accent-bg: rgba(59, 130, 246, 0.14);
      --input-bg: #121214;
      --success-bg: rgba(16, 185, 129, 0.16);
      --hold-bg: rgba(239, 68, 68, 0.12);
      --shadow: 0 24px 48px rgba(0, 0, 0, 0.28);
    }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; background:
      radial-gradient(circle at top left, rgba(59, 130, 246, 0.12), transparent 24%),
      radial-gradient(circle at top right, rgba(16, 185, 129, 0.08), transparent 18%),
      linear-gradient(180deg, #09090b 0%, #0d0d10 100%);
      color: var(--ink); font-family: Inter, "Geist Sans", ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
    a {{ color: inherit; text-decoration: none; }}
    .page {{ max-width: 1600px; margin: 0 auto; padding: 16px; display: grid; gap: 16px; }}
    .hero, .panel {{ background: var(--panel); border: 1px solid var(--line); border-radius: 12px; box-shadow: var(--shadow); }}
    .hero {{ padding: 14px 16px; display: grid; gap: 10px; }}
    .frame {{ display: grid; grid-template-columns: 240px minmax(0, 1fr); gap: 14px; align-items: start; }}
    .frame.with-right {{ grid-template-columns: 240px minmax(0, 1fr) 340px; }}
    .panel {{ padding: 12px; display: grid; gap: 10px; }}
    .panel.soft {{ background: var(--panel-soft); }}
    .frame > aside.panel {{
      background: rgba(24, 24, 27, 0.8);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
    }}
    .stack {{ display: grid; gap: 10px; }}
    .nav-stack, .list-shell {{ border: 1px solid var(--line); background: rgba(255, 255, 255, 0.02); border-radius: 10px; display: grid; gap: 0; overflow: hidden; }}
    .nav-item, .list-row {{ border-bottom: 1px solid var(--line); padding: 10px 12px; display: grid; gap: 5px; }}
    .nav-item:last-child, .list-row:last-child {{ border-bottom: 0; }}
    .nav-item {{ background: transparent; }}
    .nav-item.active {{ background: linear-gradient(180deg, rgba(59, 130, 246, 0.18), rgba(59, 130, 246, 0.06)); border-left: 2px solid var(--accent); }}
    .kicker, .label {{ color: var(--muted); font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: .08em; }}
    h1, h2, h3 {{ margin: 0; color: var(--ink); }}
    h1 {{ font-size: 19px; font-weight: 700; letter-spacing: -.01em; }}
    h2 {{ font-size: 15px; font-weight: 600; }}
    h3 {{ font-size: 13px; font-weight: 600; }}
    .meta {{ color: var(--muted); font-size: 13px; line-height: 1.5; }}
    .mono {{ font-family: "Geist Mono", "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12px; color: var(--muted); letter-spacing: -.02em; }}
    .section-head {{ display: flex; align-items: end; justify-content: space-between; gap: 12px; }}
    .metric-strip {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); border: 1px solid var(--line); border-radius: 10px; background: rgba(255, 255, 255, 0.02); overflow: hidden; }}
    .metric {{ padding: 10px 12px; border-right: 1px solid var(--line); display: grid; gap: 3px; }}
    .metric:last-child {{ border-right: 0; }}
    .metric-value {{ font-size: 18px; font-weight: 700; line-height: 1; }}
    .entity-row {{ display: grid; grid-template-columns: minmax(0, 1.5fr) minmax(0, .9fr) auto; gap: 12px; align-items: center; }}
    .entity-main, .entity-meta {{ display: grid; gap: 4px; min-width: 0; }}
    .entity-title {{ font-size: 13px; font-weight: 600; }}
    .entity-sub {{ color: var(--muted); font-size: 12px; line-height: 1.45; }}
    .entity-actions {{ display: flex; flex-wrap: wrap; justify-content: flex-end; gap: 6px; }}
    .tool-link {{ border: 1px solid var(--line); border-radius: 999px; padding: 5px 8px; font-size: 11px; text-transform: uppercase; letter-spacing: .04em; background: #151519; }}
    .tool-link.subtle {{ background: var(--panel-soft); }}
    .chip-row {{ display: flex; flex-wrap: wrap; gap: 6px; }}
    .chip {{ display: inline-flex; padding: 4px 8px; border: 1px solid var(--line); border-radius: 999px; background: var(--chip); font-size: 11px; }}
    .reading-block {{ border-left: 2px solid var(--accent); padding-left: 12px; display: grid; gap: 8px; }}
    .body-copy {{ font-size: 13px; line-height: 1.65; white-space: pre-wrap; }}
    .summary-grid {{ display: grid; grid-template-columns: 1.25fr .95fr; gap: 10px; }}
    .inspector-grid {{ display: grid; gap: 10px; }}
    .inspector-block {{ border: 1px solid var(--line); border-radius: 10px; background: rgba(255, 255, 255, 0.02); padding: 10px; display: grid; gap: 7px; }}
    .warn {{ border: 1px solid var(--warn-line); border-radius: 10px; background: var(--warn-bg); padding: 10px; display: grid; gap: 6px; }}
    .bundle-grid {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }}
    .bundle-card {{ border: 1px solid var(--line); border-radius: 10px; background: rgba(255, 255, 255, 0.02); padding: 10px; display: grid; gap: 6px; }}
    .code-block {{ border: 1px solid var(--line-soft); border-radius: 10px; background: #101014; padding: 10px; font: 12px/1.55 "Geist Mono", "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; white-space: pre-wrap; }}
    .audit-row {{ border-bottom: 1px solid var(--line); padding: 10px 12px; display: grid; gap: 5px; }}
    .audit-row:last-child {{ border-bottom: 0; }}
    .form-grid {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; }}
    .field {{ display: grid; gap: 6px; }}
    .field input, .field select, .field textarea {{
      width: 100%;
      border: 1px solid var(--line);
      border-radius: 10px;
      background: var(--input-bg);
      color: var(--ink);
      font: inherit;
      padding: 8px 10px;
    }}
    .field textarea {{ min-height: 180px; resize: vertical; font-family: "Geist Mono", "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12px; line-height: 1.55; }}
    .check-list {{ display: grid; gap: 8px; }}
    .check-row {{ display: flex; align-items: center; justify-content: space-between; gap: 12px; border: 1px solid var(--line); border-radius: 10px; background: rgba(255, 255, 255, 0.02); padding: 8px 10px; }}
    .check-row .meta {{ font-size: 12px; }}
    .tool-row {{ display: flex; flex-wrap: wrap; gap: 6px; }}
    .status-list {{ display: grid; gap: 8px; }}
    .status-row {{ border: 1px solid var(--line); border-radius: 10px; background: rgba(255, 255, 255, 0.02); padding: 10px; display: grid; gap: 5px; }}
    .status-row.active {{ border-color: var(--accent); background: linear-gradient(180deg, rgba(59, 130, 246, 0.16), rgba(59, 130, 246, 0.04)); animation: activePulse 2.4s ease-in-out infinite; }}
    .pill {{ display: inline-flex; align-items: center; gap: 6px; padding: 2px 8px; border: 1px solid var(--line); border-radius: 999px; background: var(--chip); font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: .08em; }}
    .pill.done {{ background: var(--success-bg); color: #d1fae5; border-color: #10b981; }}
    .pill.active {{ background: rgba(59, 130, 246, 0.22); border-color: var(--accent); color: #dbeafe; }}
    .pill.hold, .pill.pending_approval {{ background: var(--hold-bg); color: #fecaca; border-color: #ef4444; }}
    @keyframes activePulse {{
      0% {{ box-shadow: 0 0 0 rgba(59, 130, 246, 0); }}
      50% {{ box-shadow: 0 0 0 1px rgba(59, 130, 246, 0.18), 0 0 18px rgba(59, 130, 246, 0.08); }}
      100% {{ box-shadow: 0 0 0 rgba(59, 130, 246, 0); }}
    }}
  </style>
</head>
<body>
  <script type="application/json" id="vectorfl-operable-surface-data">{html.escape(data)}</script>
  {body_html}
</body>
</html>"""


def _render_nav(data: Dict[str, Any], active_key: str) -> str:
    nav = data["navigation"]
    nav_map = {item["key"]: item for item in nav}
    groups = data.get("navigation_groups") or []
    rows = []
    for group in groups:
        item_rows = []
        for key in group.get("item_keys") or []:
            item = nav_map.get(key)
            if not item:
                continue
            klass = "nav-item active" if item["key"] == active_key else "nav-item"
            item_rows.append(
                f'<a class="{klass}" href="{html.escape(item["href"])}"><strong>{html.escape(item["label"])}</strong>'
                f'<div class="meta">{"지금 보고 있는 페이지" if item["key"] == active_key else "열어 보기"}</div></a>'
            )
        if not item_rows:
            continue
        rows.append(
            f'<section class="stack"><div><div class="kicker">{html.escape(group.get("group_label") or "GROUP")}</div>'
            f'<div class="meta">{html.escape(group.get("vectorfl_meaning") or "")}</div></div>'
            f'<div class="nav-stack">{"".join(item_rows)}</div></section>'
        )
    if not rows:
        fallback_rows = []
        for item in nav:
            klass = "nav-item active" if item["key"] == active_key else "nav-item"
            fallback_rows.append(
                f'<a class="{klass}" href="{html.escape(item["href"])}"><strong>{html.escape(item["label"])}</strong>'
                f'<div class="meta">{"지금 보고 있는 페이지" if item["key"] == active_key else "열어 보기"}</div></a>'
            )
        rows.append('<div class="nav-stack">' + "".join(fallback_rows) + "</div>")
    return (
        '<aside class="panel">'
        '<div class="kicker">Workspace</div>'
        '<h3>VectorFL Paper</h3>'
        '<div class="meta">Paperclip의 그룹 구조를 빌리되, 각 그룹은 VectorFL 읽기 운용 객체로 채웁니다.</div>'
        f'{"".join(rows)}'
        "</aside>"
    )


def _render_engine_state(engine_state: Dict[str, Any]) -> str:
    selected_program = engine_state.get("selected_program") or {}
    selected_runtime = engine_state.get("selected_runtime") or {}
    return f"""
    <section class="panel soft">
      <div class="section-head"><div><div class="kicker">Engine State</div><h3>지금 이 엔진이 붙잡고 있는 기준</h3></div><div class="mono">shared operating object</div></div>
      <div class="inspector-block">
        <div class="label">selected program</div>
        <div class="body-copy">{html.escape(str(selected_program.get('label') or 'program pending'))}</div>
        <div class="meta">{html.escape(str(selected_program.get('objective') or ''))}</div>
      </div>
      <div class="inspector-block">
        <div class="label">selected runtime</div>
        <div class="body-copy">{html.escape(str(selected_runtime.get('label') or 'runtime pending'))}</div>
        <div class="meta">role={html.escape(str(selected_runtime.get('role') or 'runtime role pending'))}</div>
        <div class="meta">entry={html.escape(str(selected_runtime.get('entry') or 'none'))} / binding={html.escape(str(selected_runtime.get('binding_path') or 'none'))}</div>
      </div>
      <div class="inspector-block">
        <div class="label">shared line supply</div>
        <div class="body-copy">{html.escape(str(engine_state.get('shared_line_supply') or ''))}</div>
        <div class="label">current route</div>
        <div class="body-copy">{html.escape(str(engine_state.get('current_route') or ''))}</div>
      </div>
      <div class="meta">{html.escape(str(engine_state.get('supervisor_focus') or ''))}</div>
    </section>
    """


def _render_current_operating_selection(selection: Dict[str, Any]) -> str:
    return f"""
    <section class="panel soft">
      <div class="section-head"><div><div class="kicker">Current Operating Selection</div><h3>지금 저장할 기본 운용 선택</h3></div><div class="mono">selection manifest</div></div>
      <div class="inspector-block">
        <div class="label">program</div>
        <div class="body-copy">{html.escape(str(selection.get('selected_program_label') or 'program pending'))}</div>
        <div class="label">runtime</div>
        <div class="body-copy">{html.escape(str(selection.get('selected_runtime_label') or 'runtime pending'))}</div>
      </div>
      <div class="inspector-block">
        <div class="label">contract draft</div>
        <div class="body-copy">{html.escape(str(selection.get('selected_contract_label') or 'draft pending'))}</div>
        <div class="meta">{html.escape(str(selection.get('selected_contract_path') or 'none'))}</div>
      </div>
      <div class="inspector-block">
        <div class="label">launch manifest</div>
        <div class="body-copy">{html.escape(str(selection.get('selected_launch_manifest_label') or 'launch pending'))}</div>
        <div class="meta">{html.escape(str(selection.get('selected_launch_manifest_path') or 'none'))}</div>
      </div>
      <div class="inspector-block">
        <div class="label">team / lane</div>
        <div class="body-copy">{html.escape(str(selection.get('selected_team_slug') or 'team pending'))} / {html.escape(str(selection.get('selected_lane_slug') or 'lane pending'))}</div>
      </div>
      <div class="body-copy">{html.escape(str(selection.get('selection_reason') or ''))}</div>
      <div class="meta">save target={html.escape(str(selection.get('save_target_path') or 'none'))}</div>
    </section>
    """


def _render_evidence_bundle_cards(bundles: List[Dict[str, Any]]) -> str:
    if not bundles:
        return '<div class="bundle-card"><strong>아직 연결된 근거 묶음이 없습니다</strong></div>'
    cards = []
    for bundle in bundles:
        cards.append(
            f"""
            <div class="bundle-card">
              <div class="section-head">
                <div>
                  <div class="kicker">근거 묶음</div>
                  <h3>{html.escape(str(bundle.get('bundle_id') or 'bundle'))}</h3>
                </div>
                <div class="mono">{html.escape(str(bundle.get('recognition_level') or 'unknown'))}</div>
              </div>
              <div class="label">주제</div>
              <div class="body-copy">{html.escape(_friendly_text(bundle.get('theme') or 'none'))}</div>
              <div class="label">왜 지금 이 근거를 붙였는가</div>
              <div class="body-copy">{html.escape(_friendly_text(bundle.get('why_it_is_here') or '현재 읽기와 직접 닿는 근거라서 같이 붙였습니다.'))}</div>
              <div class="label">확실히 말할 수 있는 점</div>
              <div class="chip-row">{''.join(_chip(item) for item in (bundle.get('confident_points') or []))}</div>
              <div class="label">아직 비는 점</div>
              <div class="chip-row">{''.join(_chip(item) for item in (bundle.get('open_limits') or []))}</div>
              <div class="entity-actions">{_link(bundle.get('detail_href') or '#', '근거 묶음 자세히 보기', subtle=True)}</div>
            </div>
            """
        )
    return "".join(cards)


def _render_operating_board(board: Dict[str, Any]) -> str:
    return f"""
    <section class="panel">
      <div class="section-head"><div><div class="kicker">Operating Board</div><h2>지금 이 loop의 현재 상태</h2></div><div class="mono">supervisor view</div></div>
      <div class="metric-strip">
        <div class="metric"><div class="kicker">지금 읽는 case</div><div class="metric-value" style="font-size:14px;">{html.escape(str(board.get('current_case') or 'unknown'))}</div><div class="meta">현재 감독 기준이 되는 case</div></div>
        <div class="metric"><div class="kicker">지금 붙잡은 line family</div><div class="metric-value" style="font-size:14px;">{html.escape(str(board.get('selected_line_family') or 'unknown'))}</div><div class="meta">선택 line이 기대고 있는 meaning 묶음</div></div>
        <div class="metric"><div class="kicker">붙은 근거 묶음</div><div class="metric-value">{html.escape(str(board.get('selected_bundle_count') or 0))}</div><div class="meta">현재 판단을 받치는 evidence 수</div></div>
        <div class="metric"><div class="kicker">지금 확인이 필요한 승인</div><div class="metric-value">{html.escape(str(board.get('pending_approvals') or 0))}</div><div class="meta">launch 전에 사람이 확인할 것</div></div>
        <div class="metric"><div class="kicker">남아 있는 실행</div><div class="metric-value">{html.escape(str(board.get('active_runs') or 0))}</div><div class="meta">trace에 계속 붙어 있는 run</div></div>
      </div>
      <div class="meta">{html.escape(_friendly_text(board.get('control_note') or ''))}</div>
    </section>
    """


def _render_supervisor_checkpoint(data: Dict[str, Any], *, page_title: str, page_reason: str) -> str:
    detail = data.get("case_detail") or {}
    selected_line = detail.get("selected_line") or {}
    governance = detail.get("governance") or {}
    worker_request = ((data.get("worker_bridge") or {}).get("current_request")) or {}
    operating_board = data.get("operating_board") or {}
    current_case = operating_board.get("current_case") or "unknown"
    current_team = (detail.get("responsibility") or {}).get("current_organ_ref") or "unknown"
    current_line = selected_line.get("human_translation") or selected_line.get("raw_value") or "selected line pending"
    missing = (detail.get("internal_missing") or [])
    remaining_gate = missing[0] if missing else governance.get("release_condition") or "현재 남은 판단 기준을 다시 정리해야 합니다."
    decision_needed = worker_request.get("status") or governance.get("hold_state") or "none"
    next_candidates = ((detail.get("progression") or {}).get("next_candidates")) or []
    next_move = next_candidates[0].get("organ_ref") if next_candidates else detail.get("linked_programs", [None])[0]
    next_move_text = next_move or "next move pending"
    return f"""
    <section class="panel soft">
      <div class="section-head"><div><div class="kicker">Supervisor Read</div><h3>{html.escape(page_title)}</h3></div><div class="mono">human-first</div></div>
      <div class="body-copy">{html.escape(page_reason)}</div>
      <div class="label">지금 무엇을 하는 중인가</div>
      <div class="body-copy">현재 case <strong>{html.escape(str(current_case))}</strong>에서 <strong>{html.escape(str(current_line))}</strong>을 중심으로 읽기, 실행, 귀속을 묶는 중입니다.</div>
      <div class="label">이미 읽힌 것</div>
      <div class="chip-row">{_chip('current_team=' + str(current_team))}{_chip('line_family=' + str(operating_board.get('selected_line_family') or 'unknown'))}{_chip('bundles=' + str(operating_board.get('selected_bundle_count') or 0))}</div>
      <div class="label">남은 핵심 관문</div>
      <div class="body-copy">{html.escape(_friendly_text(remaining_gate))}</div>
      <div class="label">지금 필요한 판단</div>
      <div class="chip-row">{_chip('decision=' + str(decision_needed))}{_chip('next=' + str(next_move_text))}</div>
    </section>
    """


def _render_selection_state(selection: Dict[str, Any]) -> str:
    selected_line = selection.get("selected_line") or {}
    selected_bundle = selection.get("selected_bundle") or {}
    compare_target = selection.get("current_compare_target") or {}
    actions = "".join(
        f'<div class="status-row"><div class="section-head"><strong>{html.escape(item.get("label") or "action")}</strong><div class="pill {html.escape(item.get("mode") or "")}">{html.escape(item.get("mode") or "mode")}</div></div><div class="meta">{html.escape(item.get("summary") or "")}</div></div>'
        for item in selection.get("actions") or []
    )
    return f"""
    <section class="panel soft">
      <div class="section-head"><div><div class="kicker">Selection Grammar</div><h3>지금 고정해 둔 선택 객체</h3></div><div class="mono">shared state</div></div>
      <div class="status-list">
        <div class="status-row active">
          <div class="label">지금 기준이 되는 line</div>
          <div class="body-copy">{html.escape(str(selected_line.get('raw_value') or 'none'))}</div>
          <div class="meta">{html.escape(str(selected_line.get('human_translation') or 'no translation'))}</div>
        </div>
        <div class="status-row">
          <div class="label">같이 들고 가는 근거 묶음</div>
          <strong>{html.escape(str(selected_bundle.get('bundle_id') or 'bundle_pending'))}</strong>
          <div class="meta">{html.escape(_friendly_text(selected_bundle.get('why_it_is_here') or ''))}</div>
        </div>
        <div class="status-row">
          <div class="label">같이 비교하는 대상</div>
          <div class="meta">family={html.escape(str(selection.get('selected_family') or 'unknown'))}</div>
          <div class="body-copy">{html.escape(str(compare_target.get('raw') or 'compare target none'))}</div>
        </div>
      </div>
      <div class="label">지금 가능한 선택 조작</div>
      <div class="status-list">{actions}</div>
    </section>
    """


def _render_intake_wizard(wizard: Dict[str, Any]) -> str:
    steps = "".join(
        f'<div class="status-row {"active" if item.get("status") == "active" else ""}"><div class="section-head"><strong>{html.escape(item.get("label") or "step")}</strong><div class="pill {html.escape(item.get("status") or "")}">{html.escape(item.get("status") or "unknown")}</div></div><div class="meta">{html.escape(_friendly_text(item.get("summary") or ""))}</div></div>'
        for item in wizard.get("steps") or []
    )
    return f"""
    <section class="panel soft">
      <div class="section-head"><div><div class="kicker">Intake Wizard</div><h3>입력 진입 순서</h3></div><div class="mono">{html.escape(str(wizard.get('current_stage') or 'unknown'))}</div></div>
      <div class="meta">source={html.escape(str(wizard.get('source_confirmation') or 'source pending'))}</div>
      <div class="status-list">{steps}</div>
      <div class="label">launch modes</div>
      <div class="chip-row">{''.join(_chip(item) for item in (wizard.get('launch_modes') or []))}</div>
      <div class="meta">{html.escape(_friendly_text(wizard.get('reference_creation_rule') or ''))}</div>
    </section>
    """


def _render_worker_bridge(worker_bridge: Dict[str, Any]) -> str:
    request = worker_bridge.get("current_request") or {}
    payload = request.get("payload_preview") or {}
    adapter_rows = "".join(
        f'<div class="status-row"><div class="section-head"><strong>{html.escape(item.get("adapter") or "adapter")}</strong><div class="pill {html.escape(item.get("status") or "")}">{html.escape(item.get("status") or "unknown")}</div></div><div class="meta">{html.escape(item.get("best_for") or "")}</div></div>'
        for item in worker_bridge.get("available_adapters") or []
    )
    return_loop = worker_bridge.get("return_loop") or {}
    stage_rows = "".join(
        f'<div class="status-row"><div class="section-head"><strong>{html.escape(item.get("label") or "stage")}</strong><div class="pill {html.escape(item.get("status") or "")}">{html.escape(item.get("status") or "unknown")}</div></div><div class="meta">{html.escape(item.get("summary") or "")}</div></div>'
        for item in return_loop.get("stages") or []
    )
    action_rows = "".join(
        [
            f'<a class="tool-link" href="{html.escape(str(request.get("launch_href") or "#"))}">launch request</a>',
            f'<a class="tool-link subtle" href="{html.escape(str(request.get("export_href") or "#"))}">payload export</a>',
            f'<a class="tool-link subtle" href="{html.escape(str(request.get("reopen_href") or "#"))}">reopen in inbox</a>',
        ]
    )
    return f"""
    <section class="panel">
      <div class="section-head"><div><div class="kicker">Worker Bridge</div><h2>adapter 선택 / payload / return</h2></div><div class="mono">{html.escape(str(request.get('target_adapter') or 'adapter'))}</div></div>
      <div class="summary-grid">
        <div class="stack">
          <div class="status-list">{adapter_rows}</div>
          <div class="inspector-block">
            <div class="label">current request</div>
            <strong>{html.escape(str(request.get('intent') or 'no request'))}</strong>
            <div class="meta">request_id={html.escape(str(request.get('request_id') or 'unknown'))} / status={html.escape(str(request.get('status') or 'unknown'))}</div>
            <div class="body-copy">{html.escape(_friendly_text(request.get('request_summary') or ''))}</div>
          </div>
        </div>
        <div class="stack">
          <div class="inspector-block">
            <div class="label">payload preview</div>
            <div class="code-block">{html.escape(json.dumps(payload, ensure_ascii=False, indent=2))}</div>
          </div>
          <div class="warn"><strong>approval gate</strong><div>{html.escape(_friendly_text(request.get('approval_gate') or 'none'))}</div></div>
          <div class="inspector-block">
            <div class="label">actions</div>
            <div class="tool-row">{action_rows}</div>
            <div class="meta">surface 안에서 launch / export / reopen 자리를 먼저 고정하고, 실제 adapter execution은 이 seam 위에 붙입니다.</div>
          </div>
        </div>
      </div>
      <div class="section-head"><div><div class="kicker">Rewrite Return Loop</div><h3>request -> return -> comment -> reopen</h3></div><div class="mono">issue / inbox grammar</div></div>
      <div class="summary-grid">
        <div class="status-list">{stage_rows}</div>
        <div class="stack">
          <div class="inspector-block">
            <div class="label">return packet preview</div>
            <div class="code-block">{html.escape(json.dumps(return_loop.get('return_packet') or {}, ensure_ascii=False, indent=2))}</div>
          </div>
          <div class="inspector-block">
            <div class="label">comment loop</div>
            <div class="meta">{html.escape(_friendly_text((return_loop.get('comment_loop') or {}).get('inbox') or ''))}</div>
            <div class="chip-row">
              {_chip(f"comment target={(return_loop.get('comment_loop') or {}).get('comment_target') or 'none'}")}
              {_chip(f"reopen={str((return_loop.get('comment_loop') or {}).get('reopen_allowed') or False).lower()}")}
              {_chip(f"approval={str((return_loop.get('comment_loop') or {}).get('approval_required') or False).lower()}")}
            </div>
          </div>
        </div>
      </div>
    </section>
    """


def _short_list(items: Any, *, limit: int = 4) -> str:
    if not isinstance(items, list):
        return "없음"
    rows = [str(item) for item in items[:limit] if str(item).strip()]
    if len(items) > limit:
        rows.append(f"+{len(items) - limit} more")
    return ", ".join(rows) or "없음"


def _render_paper_proper_bridge_panel(data: Dict[str, Any], *, mode: str) -> str:
    bridge = data.get("paper_proper_bridge") or {}
    paths = bridge.get("paths") or {}
    handoff = bridge.get("handoff") or {}
    codex_return = bridge.get("codex_return") or {}
    gemini_review = bridge.get("gemini_review") or {}
    decision = bridge.get("supervisor_decision") or {}
    current_slot = bridge.get("current_slot") or {}
    gate_validation = bridge.get("gate_validation") or {}
    dry_run = bridge.get("dry_run") or {}
    comparison = bridge.get("comparison") or {}
    answers = bridge.get("supervisor_answers") or {}
    slots = bridge.get("operator_slots") or {}
    guard = "".join(_chip(item) for item in bridge.get("guard_language") or [])

    if mode == "overview":
        return f"""
        <section class="panel">
          <div class="section-head"><div><div class="kicker">Paper Proper Merge</div><h2>현재 감독 posture</h2></div><div class="mono">proper grammar inside operable surface</div></div>
          <div class="metric-strip">
            <div class="metric"><div class="kicker">current SSOT</div><div class="metric-value" style="font-size:13px;">{html.escape(str(current_slot.get('current_state') or 'unknown'))}</div><div class="meta">{html.escape(paths.get('current_slot') or '')}</div></div>
            <div class="metric"><div class="kicker">decision</div><div class="metric-value" style="font-size:13px;">{html.escape(str(decision.get('decision') or bridge.get('current_posture') or 'unknown'))}</div><div class="meta">hold current / bounded reopen</div></div>
            <div class="metric"><div class="kicker">gate validation</div><div class="metric-value" style="font-size:13px;">{html.escape(str(gate_validation.get('gate_effect') or 'unknown'))}</div><div class="meta">{html.escape(str(gate_validation.get('honesty_class') or 'unknown'))}</div></div>
            <div class="metric"><div class="kicker">dry-run</div><div class="metric-value" style="font-size:13px;">{html.escape(str(dry_run.get('gate_effect') or 'none'))}</div><div class="meta">preview only</div></div>
          </div>
          <div class="warn"><strong>guard</strong><div class="chip-row">{guard}</div></div>
        </section>
        """

    if mode == "input":
        return f"""
        <section class="panel">
          <div class="section-head"><div><div class="kicker">Paper Proper Intake Slot</div><h2>입력 / 후보 anchor를 여기서 고정해 읽는다</h2></div><div class="mono">input + select</div></div>
          <div class="summary-grid">
            <div class="inspector-block">
              <div class="label">current SSOT slot</div>
              <div class="body-copy">{html.escape(str(paths.get('current_slot') or 'slot missing'))}</div>
              <div class="chip-row">{_chip('state=' + str(current_slot.get('current_state') or 'unknown'))}{_chip('anchor=' + str(current_slot.get('current_validation_anchor_ref') or current_slot.get('current_placeholder_ref') or 'unknown'))}</div>
              <div class="meta">{html.escape(str(current_slot.get('validation_anchor_note') or ''))}</div>
            </div>
            <div class="inspector-block">
              <div class="label">dry-run preview</div>
              <div class="body-copy">{html.escape(str(dry_run.get('source_record_artifact') or 'dry-run missing'))}</div>
              <div class="chip-row">{_chip('status=' + str(dry_run.get('validation_status') or 'unknown'))}{_chip('honesty=' + str(dry_run.get('honesty_class') or 'unknown'))}{_chip('effect=' + str(dry_run.get('gate_effect') or 'unknown'))}</div>
              <div class="meta">preview-only. current SSOT와 섞지 않습니다.</div>
            </div>
          </div>
          <div class="inspector-block">
            <div class="label">Codex handoff action</div>
            <div class="body-copy">{html.escape(str(handoff.get('requested_action') or 'requested action pending'))}</div>
            <div class="meta">handoff={html.escape(str(paths.get('codex_handoff') or ''))}</div>
          </div>
        </section>
        """

    if mode == "assignment":
        return f"""
        <section class="panel">
          <div class="section-head"><div><div class="kicker">Paper Proper Worker Assignment</div><h2>Codex와 Gemini 입력 재료를 역할별로 분리한다</h2></div><div class="mono">assign + prepare</div></div>
          <div class="summary-grid">
            <div class="inspector-block">
              <div class="label">Codex top files</div>
              <div class="chip-row">{''.join(_chip(item) for item in bridge.get('codex_top_files') or [])}</div>
              <div class="body-copy">Codex는 파일 검사, 구현/검증 판단, line tracing 쪽 입력을 먼저 받습니다.</div>
            </div>
            <div class="inspector-block">
              <div class="label">Gemini review top files</div>
              <div class="chip-row">{''.join(_chip(item) for item in bridge.get('gemini_review_top_files') or [])}</div>
              <div class="body-copy">Gemini는 Codex return, supervisor decision, actual export gate 근거를 중심으로 누락/위험을 다시 봅니다.</div>
            </div>
          </div>
          <div class="form-grid">
            <label class="field"><span class="label">Codex bridge</span><input value="python3 scripts/run_vectorfl_paper_codex_bridge.py" readonly></label>
            <label class="field"><span class="label">Gemini cross-check</span><input value="python3 scripts/run_vectorfl_paper_gemini_crosscheck_bridge.py" readonly></label>
            <label class="field"><span class="label">Codex handoff manifest</span><input value="{html.escape(str(paths.get('codex_handoff') or ''))}" readonly></label>
            <label class="field"><span class="label">Gemini review manifest</span><input value="{html.escape(str(paths.get('gemini_review') or ''))}" readonly></label>
          </div>
        </section>
        """

    if mode == "return":
        blockers = codex_return.get("blockers") or []
        risks = gemini_review.get("detected_risks") or []
        return f"""
        <section class="panel">
          <div class="section-head"><div><div class="kicker">Paper Proper Result Intake</div><h2>worker return과 cross-check를 여기서 확인한다</h2></div><div class="mono">confirm + return</div></div>
          <div class="summary-grid">
            <div class="inspector-block">
              <div class="label">Codex return</div>
              <div class="chip-row">{_chip('status=' + str(codex_return.get('status') or 'unknown'))}{_chip('changed_files=' + str(len(codex_return.get('changed_files') or [])))}{_chip('blockers=' + str(len(blockers)))}</div>
              <div class="body-copy">{html.escape(str(codex_return.get('summary') or 'summary pending'))}</div>
              <div class="meta">return={html.escape(str(paths.get('codex_return') or ''))}</div>
            </div>
            <div class="inspector-block">
              <div class="label">Gemini cross-check</div>
              <div class="chip-row">{_chip('status=' + str(gemini_review.get('review_status') or 'unknown'))}{_chip('agreement=' + str(gemini_review.get('agreement_assessment') or 'unknown'))}{_chip('risks=' + str(len(risks)))}</div>
              <div class="body-copy">{html.escape(str(gemini_review.get('recommendation') or 'recommendation pending'))}</div>
              <div class="meta">review={html.escape(str(paths.get('gemini_review') or ''))}</div>
            </div>
          </div>
        </section>
        """

    if mode == "supervise":
        pending = decision.get("pending_validations") or []
        validation_reduced = decision.get("validation_reduced") or []
        comparison_summary = answers.get("is_candidate_for_reopen_validation_repeatable") or answers.get("any_candidate_close_to_gate_close") or "comparison summary pending"
        return f"""
        <section class="panel">
          <div class="section-head"><div><div class="kicker">Paper Proper Supervisor Gate</div><h2>hold / reopen 판단을 여기서 감독한다</h2></div><div class="mono">supervise</div></div>
          <div class="inspector-block">
            <div class="label">current decision</div>
            <div class="chip-row">{_chip('decision=' + str(decision.get('decision') or 'unknown'))}{_chip('tension=' + str(decision.get('decision_tension') or 'unknown'))}</div>
            <div class="body-copy">{html.escape(str(decision.get('rationale') or 'rationale pending'))}</div>
            <div class="meta">decision={html.escape(str(paths.get('supervisor_decision') or ''))}</div>
          </div>
          <div class="summary-grid">
            <div class="inspector-block">
              <div class="label">pending validations</div>
              <div class="chip-row">{''.join(_chip(item) for item in pending) or _chip('none recorded')}</div>
              <div class="label">validation reduced</div>
              <div class="chip-row">{''.join(_chip(item) for item in validation_reduced) or _chip('none recorded')}</div>
            </div>
            <div class="inspector-block">
              <div class="label">comparison summary only</div>
              <div class="body-copy">{html.escape(str(comparison_summary))}</div>
              <div class="meta">comparison={html.escape(str(paths.get('comparison') or ''))}</div>
            </div>
          </div>
          <div class="warn"><strong>continue gate</strong><div>{html.escape(str(decision.get('continue_gate') or 'continue gate pending'))}</div><div class="chip-row">{guard}</div></div>
        </section>
        """

    action_rows = "".join(
        f'<div class="status-row"><div class="section-head"><strong>{html.escape(str(slot.get("label") or key))}</strong><div class="pill">{html.escape(str(slot.get("status") or "unknown"))}</div></div><div class="meta">{html.escape(str(slot.get("page") or ""))} / {html.escape(str(slot.get("manifest") or ""))}</div><div class="body-copy">{html.escape(str(slot.get("action") or ""))}</div></div>'
        for key, slot in slots.items()
    )
    return f"""
    <section class="panel">
      <div class="section-head"><div><div class="kicker">Paper Proper Operator Slots</div><h2>입력 / 선택 / 지정 / 확인 / 감독</h2></div><div class="mono">no new tabs</div></div>
      <div class="status-list">{action_rows}</div>
    </section>
    """


def _render_worker_request_summary(worker_bridge: Dict[str, Any], *, title: str = "request seam", compact: bool = False) -> str:
    request = worker_bridge.get("current_request") or {}
    payload = request.get("payload_preview") or {}
    actions = "".join(
        [
            f'<a class="tool-link" href="{html.escape(str(request.get("launch_href") or "#"))}">launch request</a>',
            f'<a class="tool-link subtle" href="{html.escape(str(request.get("export_href") or "#"))}">payload export</a>',
            f'<a class="tool-link subtle" href="{html.escape(str(request.get("reopen_href") or "#"))}">reopen in inbox</a>',
        ]
    )
    if compact:
        return f"""
        <section class="panel soft">
          <div class="kicker">Worker Request</div>
          <h3>{html.escape(title)}</h3>
          <div class="body-copy">{html.escape(_friendly_text(request.get('intent') or 'no request'))}</div>
          <div class="meta">실행 대상={html.escape(str(request.get('target_adapter') or 'unknown'))} / 현재 상태={html.escape(str(request.get('status') or 'unknown'))}</div>
          <div class="chip-row">
            {_chip(f"기준 line={str(request.get('selection_basis', {}).get('line') or 'none')}")}
            {_chip(f"근거 bundle={str(request.get('selection_basis', {}).get('bundle_id') or 'none')}")}
          </div>
          <div class="tool-row">{actions}</div>
        </section>
        """
    return f"""
    <section class="panel">
      <div class="section-head"><div><div class="kicker">Worker Request</div><h2>{html.escape(title)}</h2></div><div class="mono">{html.escape(str(request.get('request_id') or 'unknown'))}</div></div>
      <div class="summary-grid">
        <div class="stack">
          <div class="inspector-block">
            <div class="label">지금 worker에게 시키려는 일</div>
            <div class="body-copy">{html.escape(_friendly_text(request.get('intent') or 'no request'))}</div>
          </div>
          <div class="inspector-block">
            <div class="label">이 요청이 기대는 선택 기준</div>
            <div class="chip-row">
              {_chip(f"line={str(request.get('selection_basis', {}).get('line') or 'none')}")}
              {_chip(f"bundle={str(request.get('selection_basis', {}).get('bundle_id') or 'none')}")}
              {_chip(f"family={str(request.get('selection_basis', {}).get('family') or 'none')}")}
            </div>
            <div class="meta">{html.escape(_friendly_text(request.get('selection_basis', {}).get('compare_target') or 'compare target none'))}</div>
          </div>
        </div>
        <div class="stack">
          <div class="inspector-block">
            <div class="label">payload에 포함된 항목</div>
            <div class="chip-row">{''.join(_chip(str(key)) for key in payload.keys())}</div>
          </div>
          <div class="warn"><strong>승인 전에 다시 볼 기준</strong><div>{html.escape(_friendly_text(request.get('approval_gate') or 'none'))}</div></div>
          <div class="tool-row">{actions}</div>
        </div>
      </div>
    </section>
    """


def _render_selection_impact(data: Dict[str, Any], *, title: str, mode_label: str) -> str:
    selection = data.get("selection_state") or {}
    worker_bridge = data.get("worker_bridge") or {}
    request = worker_bridge.get("current_request") or {}
    selected_line = selection.get("selected_line") or {}
    selected_bundle = selection.get("selected_bundle") or {}
    compare_target = selection.get("current_compare_target") or {}
    return f"""
    <section class="panel soft">
      <div class="section-head"><div><div class="kicker">Selection Impact</div><h3>{html.escape(title)}</h3></div><div class="mono">{html.escape(mode_label)}</div></div>
      <div class="status-list">
        <div class="status-row active">
          <div class="label">이 판단이 기대는 line</div>
          <div class="body-copy">{html.escape(str(selected_line.get('raw_value') or 'none'))}</div>
          <div class="meta">line family: {html.escape(str(selected_line.get('family') or 'family none'))}</div>
        </div>
        <div class="status-row">
          <div class="label">같이 따라가는 근거 묶음</div>
          <strong>{html.escape(str(selected_bundle.get('bundle_id') or 'bundle none'))}</strong>
          <div class="meta">{html.escape(_friendly_text(selected_bundle.get('why_it_is_here') or ''))}</div>
        </div>
        <div class="status-row">
          <div class="label">지금 비교 중인 대상</div>
          <div class="body-copy">{html.escape(str(compare_target.get('raw') or 'none'))}</div>
          <div class="meta">연결된 request_id={html.escape(str(request.get('request_id') or 'unknown'))}</div>
        </div>
      </div>
    </section>
    """


def _render_function_process(data: Dict[str, Any]) -> str:
    selection = data.get("selection_state") or {}
    worker_bridge = data.get("worker_bridge") or {}
    request = worker_bridge.get("current_request") or {}
    intake = data.get("intake_wizard") or {}
    selected_line = selection.get("selected_line") or {}
    selected_bundle = selection.get("selected_bundle") or {}
    compare_target = selection.get("current_compare_target") or {}
    current_organ = next((organ for organ in data.get("organs") or [] if organ.get("current")), {})
    next_organ = next((organ for organ in data.get("organs") or [] if organ.get("next_candidate")), {})
    stages = [
        {
            "label": "1. intake",
            "status": "done",
            "summary": intake.get("source_confirmation") or "source pending",
            "detail": intake.get("current_stage") or "intake stage pending",
        },
        {
            "label": "2. selection",
            "status": "active",
            "summary": selected_line.get("raw_value") or "line pending",
            "detail": selected_bundle.get("bundle_id") or "bundle pending",
        },
        {
            "label": "3. interpretation / handoff",
            "status": "active",
            "summary": current_organ.get("label") or "current organ pending",
            "detail": f"next={next_organ.get('label') or 'none'} / compare={compare_target.get('line_id') or 'none'}",
        },
        {
            "label": "4. worker request",
            "status": request.get("status") or "pending",
            "summary": request.get("target_label") or "worker pending",
            "detail": request.get("intent") or "worker intent pending",
        },
        {
            "label": "5. trace / return",
            "status": "ready",
            "summary": "실행 흔적과 rewrite 반환이 이 case에 계속 붙어 있도록 유지합니다.",
            "detail": "request -> return -> comment -> reopen 순서로 다시 감독 판단에 연결됩니다.",
        },
    ]
    stage_rows = "".join(
        f'<div class="status-row {"active" if item.get("status") in {"active", "pending_approval", "ready"} else ""}"><div class="section-head"><strong>{html.escape(item.get("label") or "stage")}</strong><div class="pill {html.escape(item.get("status") or "")}">{html.escape(item.get("status") or "unknown")}</div></div><div class="body-copy">{html.escape(_friendly_text(item.get("summary") or ""))}</div><div class="meta">{html.escape(_friendly_text(item.get("detail") or ""))}</div></div>'
        for item in stages
    )
    return f"""
    <section class="panel">
      <div class="section-head"><div><div class="kicker">Function Process</div><h2>지금 이 일이 어떤 순서로 흘러가는가</h2></div><div class="mono">current loop</div></div>
      <div class="status-list">{stage_rows}</div>
    </section>
    """


def _render_case_process_strip(data: Dict[str, Any]) -> str:
    selection = data.get("selection_state") or {}
    intake = data.get("intake_wizard") or {}
    worker_bridge = data.get("worker_bridge") or {}
    request = worker_bridge.get("current_request") or {}
    current_organ = (data.get("case_detail") or {}).get("responsibility", {}).get("current_organ_ref") or "unknown"
    next_candidates = ((data.get("case_detail") or {}).get("progression") or {}).get("next_candidates") or []
    next_organ = next_candidates[0].get("organ_ref") if next_candidates else "none"
    steps = [
        ("intake", intake.get("current_stage") or "source check"),
        ("selection", (selection.get("selected_bundle") or {}).get("bundle_id") or "bundle pending"),
        ("handoff", f"{current_organ} -> {next_organ}"),
        ("worker", request.get("status") or "pending"),
        ("return", "trace linked"),
    ]
    return (
        '<section class="panel soft"><div class="section-head"><div><div class="kicker">Process Strip</div><h3>상세를 읽는 현재 순서</h3></div><div class="mono">sticky summary</div></div>'
        '<div class="chip-row">'
        + "".join(_chip(f"{label}: {value}") for label, value in steps)
        + "</div></section>"
    )


def render_cases_page(data: Dict[str, Any]) -> str:
    operating_board = _render_operating_board(data["operating_board"])
    engine_state_panel = _render_engine_state(data["engine_state"])
    supervisor_checkpoint = _render_supervisor_checkpoint(
        data,
        page_title="지금 이 보드를 왜 보는가",
        page_reason="이 첫 화면은 보기 좋은 overview가 아니라, 지금 어떤 loop가 열려 있고 어디에 감독 판단이 필요한지 먼저 잡는 면입니다.",
    )
    function_process = _render_function_process(data)
    rows = []
    for item in data["cases"]:
        current_step = item.get("current_stage") or "unknown"
        next_step = item.get("next_action_hint") or "none"
        unread_or_gap = " / ".join(_friendly_text(flag) for flag in (item.get("restriction_flags") or [])[:2]) or "추가 판단 필요"
        rows.append(
            f"""
            <div class="list-row">
              <div class="entity-row">
                <div class="entity-main">
                  <div class="section-head"><div class="entity-title">{html.escape(item.get('source_title') or item.get('case_id') or 'case')}</div><div class="mono">{html.escape(item.get('case_id') or 'unknown')}</div></div>
                  <div class="entity-sub">자료 유형: {html.escape(item.get('source_type') or 'unknown')} / 현재 읽기 단계: {html.escape(item.get('current_stage') or 'unknown')}</div>
                  <div class="entity-sub">{html.escape(_friendly_text(item.get('placement_reason_short') or 'no placement reason'))}</div>
                  <div class="entity-sub">지금 이 case를 보는 이유: {html.escape(unread_or_gap)}</div>
                  <div class="chip-row">{_chip(f"now: {current_step}")}{_chip(f"next: {next_step}")}</div>
                </div>
                <div class="entity-meta">
                  <div class="mono">지금 맡는 팀: {html.escape(item.get('current_organ_ref') or 'unknown')}</div>
                  <div class="meta">생성된 line {item.get('generated_line_count') or 0} / family {item.get('family_count') or 0} / 아직 안 닫힌 점 {item.get('unresolved_count') or 0}</div>
                  <div class="chip-row">{''.join(_chip(flag) for flag in (item.get('restriction_flags') or []))}</div>
                  <div class="meta">다음 후보: {html.escape(item.get('next_action_hint') or 'none')} / 내부 재사용 가능성: {html.escape(item.get('internal_reuse_hint') or 'unknown')}</div>
                </div>
                <div class="entity-actions">
                  {_link('case-detail.html', '작업 상세 열기')}
                  {_link(item.get('current_detail_href') or '#', '현재 팀 보기', subtle=True)}
                  {_link(item.get('next_detail_href') or '#', '다음 후보 보기', subtle=True)}
                </div>
              </div>
            </div>
            """
        )
    decision_queue_rows = "".join(
        f'<div class="status-row {"active" if item.get("status") in {"active", "pending_approval", "mixed_hold"} else ""}">'
        f'<div class="section-head"><strong>{html.escape(str(item.get("label") or "decision"))}</strong><div class="pill {html.escape(str(item.get("status") or ""))}">{html.escape(str(item.get("status") or "unknown"))}</div></div>'
        f'<div class="meta">owner={html.escape(str(item.get("owner") or "unknown"))}</div>'
        f'<div class="body-copy">{html.escape(_friendly_text(item.get("reason") or ""))}</div>'
        f'<div class="tool-row">{_link(item.get("action_href") or "case-routing.html", "지금 처리하기")}</div></div>'
        for item in data["operating_board"].get("decision_queue") or []
    ) or '<div class="status-row"><strong>지금 당장 처리할 decision queue가 없습니다</strong></div>'
    active_team_cli_rows = "".join(
        f'<div class="list-row"><div class="entity-row"><div class="entity-main"><div class="entity-title">{html.escape(str(item.get("team") or "team"))}</div><div class="entity-sub">관리 CLI={html.escape(str(item.get("cli") or "unknown"))} / lane={html.escape(str(item.get("lane") or "unknown"))}</div></div><div class="entity-meta"><div class="chip-row">{_chip(str(item.get("mode") or "unknown"))}</div></div></div></div>'
        for item in data["operating_board"].get("active_team_cli_rows") or []
    ) or '<div class="list-row"><div class="entity-title">활성 팀 / CLI가 아직 없습니다</div></div>'
    latest_updates_rows = "".join(
        f'<div class="list-row"><div class="entity-row"><div class="entity-main"><div class="entity-title">{html.escape(str(item.get("kind") or "update"))}</div><div class="entity-sub">{html.escape(_friendly_text(item.get("summary") or ""))}</div></div><div class="entity-meta"><div class="chip-row">{_chip(str(item.get("status") or "done"))}</div></div><div class="entity-actions">{_link(item.get("href") or "trace-audit.html", "업데이트 열기")}</div></div></div>'
        for item in data["operating_board"].get("latest_updates") or []
    ) or '<div class="list-row"><div class="entity-title">최근 업데이트가 아직 없습니다</div></div>'
    body = f"""
    <div class="page">
      <section class="hero">
        <div class="kicker">VectorFL Paper</div>
        <div class="section-head"><h1>운영 보드</h1><div class="mono">현재 감독 보드</div></div>
        <div class="meta">이 화면은 자료를 나열하는 목록이 아니라, 어떤 case가 지금 멈춰 있고 무엇이 이미 읽혔으며 어디에 다음 판단이 필요한지 먼저 잡는 감독 보드입니다.</div>
      </section>
      <div class="frame">
        {_render_nav(data, 'cases')}
        <main class="stack">
          {supervisor_checkpoint}
          {engine_state_panel}
          {operating_board}
          <section class="panel">
            <div class="section-head"><div><div class="kicker">decision queue</div><h2>지금 먼저 결정해야 하는 것</h2></div><div class="mono">approve / hold / route</div></div>
            <div class="status-list">{decision_queue_rows}</div>
          </section>
          <section class="panel">
            <div class="metric-strip">
              <div class="metric"><div class="kicker">지금 보이는 case</div><div class="metric-value">{len(data['cases'])}</div><div class="meta">현재 감독 범위 안에 있는 자료</div></div>
              <div class="metric"><div class="kicker">현재 case의 line</div><div class="metric-value">{len(data['case_detail']['generated_lines'])}</div><div class="meta">지금 기준 case에서 읽힌 line</div></div>
              <div class="metric"><div class="kicker">family 묶음</div><div class="metric-value">{len(data['case_detail']['family_clusters'])}</div><div class="meta">의미를 두껍게 하는 연결</div></div>
              <div class="metric"><div class="kicker">다시 읽어야 할 점</div><div class="metric-value">{len(data['case_detail']['internal_missing'])}</div><div class="meta">바로 닫지 말아야 하는 빈 곳</div></div>
              <div class="metric"><div class="kicker">현재 제약</div><div class="metric-value">{len(data['case_detail']['governance'].get('restriction_flags') or [])}</div><div class="meta">{html.escape(data['case_detail']['governance'].get('hold_state') or 'none')}</div></div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">active teams / cli</div><h2>지금 움직이는 팀과 도구</h2></div><div class="mono">team ownership</div></div>
            <div class="list-shell">{active_team_cli_rows}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">latest updates</div><h2>최근 이슈 업데이트와 회신</h2></div><div class="mono">issue-like feed</div></div>
            <div class="list-shell">{latest_updates_rows}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">quick actions</div><h2>지금 바로 열어야 하는 운용면</h2></div><div class="mono">board operator</div></div>
            <div class="tool-row">
              {_link('engine-overview.html', '엔진 개요')}
              {_link('external-resources.html', '입력 시작 / 비교 설정')}
              {_link('case-routing.html', '팀 / CLI 배정')}
              {_link('organ-registry.html', '팀 계약 / 설정', subtle=True)}
              {_link('cli-setup.html', 'CLI 설정 작업공간', subtle=True)}
              {_link('program-workspaces.html', '프로그램 워크스페이스', subtle=True)}
              {_link('worker-inbox.html', '회신 / reopen 보기', subtle=True)}
            </div>
          </section>
          {function_process}
          <section class="panel">
            <div class="section-head"><div><div class="kicker">목록</div><h2>지금 감독해야 하는 case들</h2></div><div class="mono">상세로 들어가기</div></div>
            <div class="list-shell">{''.join(rows)}</div>
          </section>
        </main>
      </div>
    </div>"""
    return _base_html("VectorFL Operable Surfaces / Cases", data, body)


def render_case_detail_page(data: Dict[str, Any]) -> str:
    detail = data["case_detail"]
    dossier = detail["selected_line_dossier"]
    operating_board = _render_operating_board(data["operating_board"])
    supervisor_checkpoint = _render_supervisor_checkpoint(
        data,
        page_title="이 상세를 왜 읽는가",
        page_reason="이 페이지는 source, line, evidence, next action을 한 흐름으로 읽게 해서, 사용자가 파일 더미를 해석하지 않고도 현재 case를 감독할 수 있게 만드는 중심면입니다.",
    )
    process_strip = _render_case_process_strip(data)
    selection_panel = _render_selection_state(data["selection_state"])
    intake_panel = _render_intake_wizard(data["intake_wizard"])
    worker_request_panel = _render_worker_request_summary(data["worker_bridge"], title="selected line request seam", compact=True)
    evidence_bundle_cards = _render_evidence_bundle_cards(detail.get("evidence_bundles") or [])
    trace_rows = "".join(
        f'<div class="audit-row"><div class="label">{html.escape(item.get("trace_kind") or "trace")}</div><strong>{html.escape(_friendly_text(item.get("summary") or "none"))}</strong><div class="meta">남아 있는 흔적: {html.escape(_friendly_text(item.get("residue_note") or "none"))}</div><div class="body-copy">{html.escape(_friendly_text(item.get("reentry_hint") or "none"))}</div></div>'
        for item in detail["trace_preview"][:2]
    )
    next_rows = "".join(
        f'<div class="inspector-block"><div class="label">다음 후보</div><strong>{html.escape(item.get("organ_ref") or "unknown")}</strong><div class="meta">lane={html.escape(item.get("lane_ref") or "unknown")} / status={html.escape(item.get("status") or "unknown")}</div><div class="tool-row">{_link("case-inspector.html", "제약 보기")}{_link("organ-detail-governance.html", "팀 열기", subtle=True)}</div></div>'
        for item in (detail["progression"].get("next_candidates") or [])
    )
    generated_line_rows = "".join(
        f'<div class="list-row"><div class="section-head"><div class="entity-title">{html.escape(item["raw"])}</div><div class="mono">{html.escape(item["status"])}</div></div><div class="entity-sub">{html.escape(item["human_translation"])}</div><div class="label">왜 중요한가</div><div class="body-copy">{html.escape(item["dossier"]["friendly_summary"])}</div><div class="meta">묶음: {html.escape(item["family"])}</div><div class="entity-actions">{_link(item["detail_href"], "이 line 자세히 보기")}{_link("case-inspector.html", "line 들여다보기", subtle=True)}</div></div>'
        for item in detail["generated_lines"]
    )
    line_preview_rows = "".join(
        f'<div class="bundle-card"><div class="label">빠르게 보기</div><strong>{html.escape(item["raw"])}</strong><div class="body-copy">{html.escape(item["dossier"]["translation"]["core"])}</div><div class="meta">아직 애매한 점: {html.escape(_friendly_text(item["dossier"]["uncertainty"]))}</div><div class="entity-actions">{_link(item["detail_href"], "line 상세", subtle=True)}</div></div>'
        for item in detail["generated_lines"][:3]
    )
    family_rows = "".join(
        f'<div class="bundle-card"><div class="label">묶음</div><strong>{html.escape(item["label"])}</strong><div class="body-copy">{html.escape(_friendly_text(item["summary"]))}</div></div>'
        for item in detail["family_clusters"]
    )
    recall_doc_rows = "".join(
        f'<div class="list-row"><div class="entity-title">{html.escape(item["title"])}</div><div class="entity-sub">{html.escape(_friendly_text(item["summary"] or "no summary"))}</div></div>'
        for item in detail["internal_recall_docs"]
    )
    selected = detail["selected_line"]
    status_strip = "".join(
        [
            f'<div class="metric"><div class="kicker">현재 팀</div><div class="metric-value" style="font-size:14px;">{html.escape(detail["responsibility"].get("current_organ_ref") or "unknown")}</div><div class="meta">지금 맡고 있는 곳</div></div>',
            f'<div class="metric"><div class="kicker">생성된 line</div><div class="metric-value">{len(detail["generated_lines"])}</div><div class="meta">지금 바로 읽어볼 수 있는 line</div></div>',
            f'<div class="metric"><div class="kicker">family</div><div class="metric-value">{len(detail["family_clusters"])}</div><div class="meta">line meaning을 두껍게 하는 묶음</div></div>',
            f'<div class="metric"><div class="kicker">비어 있는 점</div><div class="metric-value">{len(detail["internal_missing"])}</div><div class="meta">다시 보거나 찾아야 함</div></div>',
        ]
    )
    body = f"""
    <div class="page">
      <section class="hero">
        <div class="kicker">VectorFL Paper</div>
        <div class="section-head"><h1>현재 케이스</h1><div class="mono">case 감독 중심면</div></div>
        <div class="meta">이 화면은 자료 하나를 깊게 읽되, 사용자가 지금 무엇을 이해했고 무엇이 아직 안 닫혔는지 바로 감독할 수 있게 source, line, 근거, 다음 행동을 한 흐름으로 묶는 중심면입니다.</div>
      </section>
      <div class="frame with-right">
        {_render_nav(data, 'case-detail')}
        <main class="stack">
          {supervisor_checkpoint}
          {operating_board}
          {process_strip}
          <section class="panel">
            <div class="section-head"><div><div class="kicker">먼저 보기</div><h2>{html.escape(detail['body'].get('headline') or detail['case_header'].get('case_id') or 'case')}</h2></div><div class="mono">{html.escape(detail['case_header'].get('case_id') or 'unknown')}</div></div>
            <div class="meta">이 case는 지금 {html.escape(detail['case_header'].get('case_status') or 'unknown')} 상태이며, 마지막 업데이트는 {html.escape(detail['case_header'].get('updated_at') or 'unknown')} 입니다.</div>
          </section>
          <section class="panel">
            <div class="metric-strip">{status_strip}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">1. 원본 읽기</div><h2>원본이 어떻게 나뉘었는지</h2></div><div class="mono">원본부터 읽기</div></div>
            <div class="meta">지금은 line을 고치기 전에 source structure와 segmentation basis를 먼저 확인해서, 이후 정제가 원본과 끊기지 않게 잡습니다.</div>
            <div class="summary-grid" style="grid-template-columns:.95fr 1.05fr;">
              <div class="stack">
                <div class="inspector-block">
                  <div class="kicker">원본</div>
                  <h3>{html.escape(detail['source_summary']['title'])}</h3>
                  <div class="meta">자료 유형: {html.escape(detail['source_summary']['source_type'])}</div>
                </div>
                <div class="inspector-block">
                  <div class="label">원본 구조 요약</div>
                  <div class="body-copy">{html.escape(_friendly_text(detail['source_summary']['native_structure_summary']))}</div>
                </div>
                <div class="inspector-block">
                  <div class="label">이렇게 나눈 기준</div>
                  <div class="body-copy">{html.escape(detail['source_summary']['segmentation_basis'])}</div>
                  <div class="meta">{html.escape(_friendly_text(detail['source_summary']['segmentation_reason']))}</div>
                </div>
              </div>
              <div class="stack">
                <div class="inspector-block">
                  <div class="label">왜 이 구조가 중요한가</div>
                  <div class="body-copy">{html.escape(_friendly_text(detail['source_summary']['native_structure_summary']))}</div>
                </div>
                <div class="reading-block">
                  <div class="kicker">지금 보고 있는 line</div>
                  <div class="body-copy">{html.escape(selected['raw_value'])}</div>
                </div>
                <div class="inspector-block">
                  <div class="label">사람이 읽는 말</div>
                  <div class="body-copy">{html.escape(selected['human_translation'])}</div>
                </div>
                <div class="inspector-block">
                  <div class="label">짧은 뜻풀이</div>
                  <div class="body-copy">{html.escape(_friendly_text(selected['meaning_summary']))}</div>
                  <div class="meta">아직 애매한 점: {html.escape(_friendly_text(selected['uncertainty']))}</div>
                </div>
                <div class="inspector-block">
                  <div class="label">지금 맡고 있는 팀</div>
                  <strong>{html.escape(detail['responsibility'].get('current_organ_ref') or 'unknown')}</strong>
                  <div class="body-copy">{html.escape(_friendly_text(detail['responsibility'].get('placement_reason') or 'no placement reason'))}</div>
                </div>
              </div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">2. line 읽기</div><h2>무슨 line이 생겼고 어디가 비는가</h2></div><div class="mono">생성된 line</div></div>
            <div class="meta">여기서는 생성된 line을 소비하는 대신, 어떤 line이 usable하고 어떤 family와 gap이 같이 따라오는지 판단 기준으로 읽습니다.</div>
            <div class="summary-grid">
              <div class="stack">
                <div class="list-shell">{generated_line_rows}</div>
                <div class="bundle-grid">{family_rows}</div>
              </div>
              <div class="stack">
                <div class="bundle-grid">{line_preview_rows}</div>
                <div class="inspector-block">
                  <div class="label">이미 내부에 있는 것</div>
                  <div class="chip-row">{''.join(_chip(item) for item in detail['internal_existing'])}</div>
                </div>
                <div class="warn">
                  <strong>아직 비어 있는 것</strong>
                <div class="chip-row">{''.join(_chip(_friendly_text(item)) for item in detail['internal_missing'])}</div>
                </div>
                <div class="inspector-block">
                  <div class="label">다시 봐야 하는 내부 자료</div>
                  <div class="list-shell">{recall_doc_rows}</div>
                </div>
                <div class="entity-actions">{_link('line-review.html', 'line 비교 열기')}{_link('internal-recall.html', '내부 자료 다시 보기', subtle=True)}{_link('external-resources.html', '외부 자료 계획 보기', subtle=True)}</div>
              </div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">3. 다음 행동</div><h2>어디로 넘기고 무엇을 남길지</h2></div><div class="mono">{len(detail['trace_preview'])}개 흔적</div></div>
            <div class="meta">이 구간은 현재 읽기를 다음 organ이나 worker request로 어떻게 넘길지, 그리고 어떤 residue를 trace로 남겨야 하는지 정하는 단계입니다.</div>
            <div class="summary-grid">
              <div class="inspector-grid">
                <div class="inspector-block"><div class="label">지금 단계</div><strong>{html.escape((detail['progression'].get('current_step') or {}).get('organ_ref') or 'none')}</strong><div class="body-copy">{html.escape(_friendly_text((detail['progression'].get('current_step') or {}).get('summary') or 'none'))}</div></div>
                {next_rows}
              </div>
              <div class="list-shell">{trace_rows}</div>
            </div>
            <div class="entity-actions">{_link('line-review.html', 'line 비교 열기')}{_link('internal-recall.html', '내부 자료 다시 보기', subtle=True)}{_link('external-resources.html', '외부 자료 계획 보기', subtle=True)}{_link('lane-runs.html', 'lane 비교 결과 보기', subtle=True)}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">4. 지금 붙는 근거 묶음</div><h2>line recall evidence</h2></div><div class="mono">{len(detail.get('evidence_bundles') or [])} bundles</div></div>
            <div class="meta">마지막으로 지금 판단이 어떤 evidence bundle 위에 서 있는지 확인해서, rewrite와 compare가 source-grounded 상태를 유지하도록 합니다.</div>
            <div class="bundle-grid">{evidence_bundle_cards}</div>
          </section>
        </main>
        <aside class="stack">
          {selection_panel}
          {intake_panel}
          {worker_request_panel}
          <section class="panel soft">
            <div class="kicker">한눈에 보기</div>
            <h3>이 line이 붙잡고 있는 것</h3>
            <div class="label">보존하는 것</div>
            <div class="chip-row">{''.join(_chip(item) for item in selected['preserves'])}</div>
            <div class="label">빠뜨린 것</div>
            <div class="chip-row">{''.join(_chip(item) for item in selected['omits'])}</div>
            <div class="label">아직 애매한 점</div>
            <div class="body-copy">{html.escape(_friendly_text(selected['uncertainty']))}</div>
            <div class="label">검색에 쓸 말</div>
            <div class="body-copy">{html.escape(selected['searchable_form'])}</div>
            <div class="label">차용할 때의 말</div>
            <div class="body-copy">{html.escape(selected['adoption_form'])}</div>
            <div class="label">다음에 할 일</div>
            <div class="chip-row">{''.join(_chip(item) for item in selected['next_step_ideas'])}</div>
            <div class="entity-actions">{_link('case-inspector.html', 'line 들여다보기 열기')}</div>
          </section>
          <section class="panel soft">
            <div class="kicker">왜 중요한가</div>
            <h3>{html.escape(dossier['friendly_title'])}</h3>
            <div class="body-copy">{html.escape(dossier['friendly_summary'])}</div>
            <div class="label">핵심 번역</div>
            <div class="body-copy">{html.escape(dossier['translation']['core'])}</div>
            <div class="label">조금 더 풀어쓴 말</div>
            <div class="body-copy">{html.escape(dossier['translation']['expanded'])}</div>
          </section>
          <section class="panel soft">
            <div class="kicker">제약과 연결</div>
            <div class="body-copy">{html.escape(_friendly_text(detail['governance'].get('reason_summary') or 'no governance summary'))}</div>
            <div class="chip-row">{''.join(_chip(flag) for flag in (detail['governance'].get('restriction_flags') or []))}</div>
            <div class="chip-row">{''.join(_chip(item) for item in detail['linked_programs'])}</div>
            <div class="entity-actions">{_link('trace-audit.html', '흔적 감사 열기')}{_link('organs.html', '팀 보기', subtle=True)}</div>
          </section>
        </aside>
      </div>
    </div>"""
    return _base_html("VectorFL Operable Surfaces / Case Detail", data, body)


def render_case_inspector_page(data: Dict[str, Any]) -> str:
    inspector = data["case_inspector"]
    dossier = inspector["selected_line_dossier"]
    supervisor_checkpoint = _render_supervisor_checkpoint(
        data,
        page_title="왜 이 line을 다시 들여다보는가",
        page_reason="이 페이지는 line 설명을 모아두는 곳이 아니라, 지금 선택된 line이 왜 중요하고 무엇이 아직 비어 있으며 어떤 판단을 위해 다시 읽어야 하는지 고정하는 inspection 면입니다.",
    )
    evidence_bundle_cards = _render_evidence_bundle_cards(inspector.get("evidence_bundles") or [])
    next_rows = "".join(
        f'<div class="bundle-card"><div class="label">후보</div><strong>{html.escape(item.get("organ_ref") or "unknown")}</strong><div class="meta">lane={html.escape(item.get("lane_ref") or "unknown")} / status={html.escape(item.get("status") or "unknown")}</div></div>'
        for item in inspector["next_candidates"]
    ) or '<div class="bundle-card"><strong>아직 다음 후보가 없습니다</strong></div>'
    body = f"""
    <div class="page">
      <section class="hero">
        <div class="kicker">VectorFL Paper</div>
        <div class="section-head"><h1>해석 인스펙터</h1><div class="mono">선택한 line 뒤의 자료망 보기</div></div>
        <div class="meta">선택한 line 하나를 중심으로, 왜 중요한지, 어떤 내부 자료와 붙는지, 지금 무엇이 비고 다음에 어디로 갈지를 한 자리에서 확인합니다. 여기서 보이는 문장과 묶음은 결과 요약이 아니라, 원본을 다시 읽게 만드는 번역기 역할을 합니다.</div>
      </section>
      <div class="frame">
        {_render_nav(data, 'case-inspector')}
        <main class="stack">
          {supervisor_checkpoint}
          <section class="panel">
            <div class="section-head"><div><div class="kicker">1. 한눈에 보기</div><h2>지금 보고 있는 line</h2></div><div class="mono">{_esc(inspector['governance'].get('hold_state') or 'none')}</div></div>
            <div class="meta">이 첫 블록은 line을 단독 문장으로 소비하지 않고, 지금 어떤 line을 기준 객체로 잡고 있는지 고정하는 단계입니다.</div>
            <div class="inspector-block">
              <div class="label">원문 line</div>
              <div class="body-copy">{html.escape(inspector['selected_line']['raw_value'])}</div>
              <div class="label">사람이 읽는 말</div>
              <div class="body-copy">{html.escape(inspector['selected_line']['human_translation'])}</div>
              <div class="label">짧은 뜻풀이</div>
              <div class="body-copy">{html.escape(inspector['selected_line']['meaning_summary'])}</div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">2. 왜 중요한가</div><h2>{html.escape(dossier['friendly_title'])}</h2></div><div class="mono">사람이 읽는 설명</div></div>
            <div class="meta">여기서는 line을 사람 말로 다시 풀어, 왜 이 line이 다음 판단과 rewrite 요청의 기준이 되는지 명확히 합니다.</div>
            <div class="inspector-block">
              <div class="body-copy">{html.escape(dossier['friendly_summary'])}</div>
              <div class="label">사람이 읽는 말</div>
              <div class="body-copy">{html.escape(dossier['declaration_linkage']['human_readable'])}</div>
              <div class="label">지금 필요한 행동</div>
              <div class="body-copy">{html.escape(dossier['directive_linkage']['human_readable'])}</div>
              <div class="label">왜 교정이 필요한가</div>
              <div class="body-copy">{html.escape(dossier['past_conversation_linkage']['human_readable'])}</div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">3. 지금 막히는 이유</div><h2>보류 / 해제 조건</h2></div><div class="mono">{_esc(inspector['governance'].get('hold_state') or 'none')}</div></div>
            <div class="meta">이 구간은 현재 line이 왜 바로 승격되지 않는지, 무엇을 더 확인해야 하는지 governance 문법으로 읽는 단계입니다.</div>
            <div class="warn"><strong>{_esc(_friendly_text(inspector['governance'].get('reason_summary') or 'no governance summary'))}</strong><div>해제 조건: {_esc(_friendly_text(inspector.get('release_condition') or 'none'))}</div><div>다음 확인: {_esc(_friendly_text(inspector.get('next_check_trigger') or 'none'))}</div></div>
            <div class="chip-row">{''.join(_chip(flag) for flag in (inspector['governance'].get('restriction_flags') or []))}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">4. 무엇과 연결되는가</div><h2>원본 / family / 규칙 / 판단 기록</h2></div><div class="mono">{len(inspector['selected_artifact_refs'])} artifact refs</div></div>
            <div class="meta">이 단계에서는 선택된 line이 source, family, declaration, judgment history와 어디서 이어지는지 다시 붙여 읽습니다.</div>
            <div class="inspector-block"><div class="label">원본 연결</div><div class="chip-row">{''.join(_chip(item) for item in inspector['source_linkage'])}</div></div>
            <div class="inspector-block"><div class="label">묶음 연결</div><div class="chip-row">{''.join(_chip(item) for item in inspector['family_linkage'])}</div></div>
            <div class="inspector-block"><div class="label">선언문 / 지시문 연결</div><div class="chip-row">{''.join(_chip(item) for item in inspector['declaration_linkage'])}</div></div>
            <div class="inspector-block"><div class="label">판단 기록 연결</div><div class="chip-row">{''.join(_chip(item) for item in inspector['judgment_history_linkage'])}</div></div>
            <div class="inspector-block">
              <div class="label">검색에 쓸 말</div>
              <div class="body-copy">{html.escape(inspector['searchable_form'])}</div>
              <div class="label">차용에 쓸 말</div>
              <div class="body-copy">{html.escape(inspector['adoption_form'])}</div>
              <div class="label">넘겨볼 후보</div>
              <div class="body-copy">{html.escape(inspector['candidate_handoff'])}</div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">5. 이 line의 상태</div><h2>무엇을 살리고 무엇이 빠졌는가</h2></div><div class="mono">line readiness</div></div>
            <div class="meta">여기서는 preserve / omit / uncertainty를 분리해서, 이 line이 지금 어느 정도까지 operational한지 가늠합니다.</div>
            <div class="summary-grid">
              <div class="stack">
                <div class="inspector-block"><div class="label">보존하는 것</div><div class="chip-row">{''.join(_chip(item) for item in inspector['what_it_preserves'])}</div></div>
                <div class="inspector-block"><div class="label">빠뜨린 것</div><div class="chip-row">{''.join(_chip(item) for item in inspector['what_it_omits'])}</div></div>
              </div>
              <div class="stack">
                <div class="warn"><strong>아직 애매한 점</strong><div>{html.escape(_friendly_text(inspector['uncertainty']))}</div></div>
                <div class="inspector-block"><div class="label">바로 쓸 수 있는 곳</div><div class="chip-row">{''.join(_chip(item) for item in inspector['usable_targets'])}</div></div>
                <div class="inspector-block"><div class="label">다음 행동 힌트</div><div class="chip-row">{''.join(_chip(item) for item in inspector['adoption_hints'])}</div></div>
              </div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">6. 어떤 재료가 이 line을 두껍게 만드는가</div><h2>선언문 / 지시문 / 검증 / 외부 참고</h2></div><div class="mono">line dossier</div></div>
            <div class="meta">이 블록은 line 하나를 지지하는 재료층을 펼쳐서, rewrite나 search가 공중에 뜨지 않도록 바닥을 보여줍니다.</div>
            <div class="bundle-grid">
              <div class="bundle-card"><div class="label">{html.escape(dossier['declaration_linkage']['type'])}</div><div class="body-copy">{html.escape(dossier['declaration_linkage']['summary'])}</div></div>
              <div class="bundle-card"><div class="label">{html.escape(dossier['directive_linkage']['type'])}</div><div class="body-copy">{html.escape(dossier['directive_linkage']['summary'])}</div></div>
              <div class="bundle-card"><div class="label">{html.escape(dossier['report_validation_linkage']['type'])}</div><div class="body-copy">{html.escape(dossier['report_validation_linkage']['summary'])}</div></div>
              <div class="bundle-card"><div class="label">{html.escape(dossier['external_reference_linkage']['type'])}</div><div class="body-copy">{html.escape(dossier['external_reference_linkage']['summary'])}</div></div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">7. line family</div><h2>{html.escape(dossier['family_expansion']['name'])}</h2></div><div class="mono">묶음이 line을 두껍게 만드는 방식</div></div>
            <div class="chip-row">{''.join(_chip(item) for item in dossier['family_expansion']['related_lines'])}</div>
            <div class="body-copy">{html.escape(dossier['family_expansion']['meaning'])}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">8. 외부로 펼치기</div><h2>검색 / 차용 계획</h2></div><div class="mono">next use</div></div>
            <div class="meta">이 단계는 외부 검색과 차용을 자유 발상으로 두지 않고, 지금 line에서 파생된 질문과 제외 조건으로 묶는 곳입니다.</div>
            <div class="inspector-block">
              <div class="label">추천 검색어</div>
              <div class="chip-row">{''.join(_chip(item) for item in dossier['search_queries'])}</div>
              <div class="label">무엇을 가져올까</div>
              <div class="chip-row">{''.join(_chip(item) for item in dossier['adoption_form_detail']['borrow'])}</div>
              <div class="label">무엇과 연결할까</div>
              <div class="chip-row">{''.join(_chip(item) for item in dossier['adoption_form_detail']['connect'])}</div>
              <div class="label">무엇은 피할까</div>
              <div class="chip-row">{''.join(_chip(item) for item in dossier['adoption_form_detail']['avoid'])}</div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">9. 바로 다시 볼 기록</div><h2>Recall backing</h2></div><div class="mono">{len(inspector['related_internal_records'])} records</div></div>
            <div class="meta">여기서는 지금 line을 다시 열 때 바로 불러올 내부 기록을 붙여, recall order가 surface 안에서 유지되도록 합니다.</div>
            <div class="list-shell">{''.join(f'<div class="list-row"><div class="entity-title">{html.escape(item)}</div></div>' for item in inspector['related_internal_records'])}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">10. 실제 근거 묶음</div><h2>spec + generated evidence</h2></div><div class="mono">{len(inspector.get('evidence_bundles') or [])} bundles</div></div>
            <div class="meta">마지막 evidence 확인 단계로, 지금 읽기와 rewrite 계획이 실제 bundle 위에서 서 있는지 점검합니다.</div>
            <div class="bundle-grid">{evidence_bundle_cards}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">11. 다음에 어디로 갈까</div><h2>다음으로 넘길 후보</h2></div><div class="mono">미리 보기</div></div>
            <div class="bundle-grid">{next_rows}</div>
            <div class="entity-actions">{_link('case-routing.html', '넘김과 배정 열기')}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">12. 바로 이어서 보기</div><h2>다시 보기 / 외부 찾기 / lane 비교</h2></div><div class="mono">line을 다음 행동으로 잇기</div></div>
            <div class="tool-row">{_link('line-review.html', 'line 비교 열기')}{_link('internal-recall.html', '내부 자료 다시 보기', subtle=True)}{_link('external-resources.html', '외부 자료 계획 보기', subtle=True)}{_link('lane-runs.html', 'lane 비교 결과 보기', subtle=True)}</div>
            <div class="label">다음 단계 아이디어</div>
            <div class="chip-row">{''.join(_chip(item) for item in dossier['next_step_ideas'])}</div>
            <div class="label">보류 / 충돌 / 추가 검증</div>
            <div class="chip-row">{''.join(_chip(item) for item in dossier['uncertainty_detail']['pending'])}{_chip(dossier['uncertainty_detail']['conflict'])}{''.join(_chip(item) for item in dossier['uncertainty_detail']['needs_validation'])}</div>
          </section>
        </main>
      </div>
    </div>"""
    return _base_html("VectorFL Operable Surfaces / Case Inspector", data, body)


def render_line_review_page(data: Dict[str, Any]) -> str:
    detail = data["case_detail"]
    rows = []
    for idx, item in enumerate(detail["generated_lines"][:5], start=1):
        dossier = item["dossier"]
        bundle_preview = "".join(
            f'<div class="bundle-card"><div class="label">{html.escape(bundle.get("bundle_id") or "bundle")}</div><div class="body-copy">{html.escape(_friendly_text(bundle.get("why_it_is_here") or "현재 line과 직접 닿는 근거입니다."))}</div></div>'
            for bundle in (item.get("evidence_bundles") or [])[:2]
        ) or '<div class="bundle-card"><strong>아직 붙은 근거 묶음이 없습니다</strong></div>'
        rows.append(
            f"""
            <section class="panel">
              <div class="section-head"><div><div class="kicker">Line {idx}</div><h2>{html.escape(item['raw'])}</h2></div><div class="mono">{html.escape(item['status'])}</div></div>
              <div class="meta">{html.escape(item['human_translation'])}</div>
              <div class="summary-grid">
                <div class="stack">
                  <div class="inspector-block">
                    <div class="label">왜 중요한가</div>
                    <div class="body-copy">{html.escape(dossier['friendly_summary'])}</div>
                  </div>
                  <div class="inspector-block">
                    <div class="label">핵심 번역</div>
                    <div class="body-copy">{html.escape(dossier['translation']['core'])}</div>
                  </div>
                  <div class="inspector-block">
                    <div class="label">조금 더 풀어쓴 말</div>
                    <div class="body-copy">{html.escape(dossier['translation']['expanded'])}</div>
                  </div>
                </div>
                <div class="stack">
                  <div class="inspector-block"><div class="label">어디와 연결되는가</div><div class="chip-row">{''.join(_chip(x) for x in detail['generated_lines'][idx-1]['dossier']['adoption_form_detail']['connect'][:3])}</div></div>
                  <div class="warn"><strong>아직 애매한 점</strong><div>{html.escape(dossier['uncertainty'])}</div></div>
                  <div class="inspector-block"><div class="label">검색어 후보</div><div class="chip-row">{''.join(_chip(x) for x in dossier['search_queries'])}</div></div>
                </div>
              </div>
              <div class="bundle-grid">
                <div class="bundle-card"><div class="label">선언문 쪽에서 보면</div><div class="body-copy">{html.escape(dossier['declaration_linkage']['human_readable'])}</div></div>
                <div class="bundle-card"><div class="label">지시문 쪽에서 보면</div><div class="body-copy">{html.escape(dossier['directive_linkage']['human_readable'])}</div></div>
                <div class="bundle-card"><div class="label">family 의미</div><div class="body-copy">{html.escape(dossier['family_expansion']['meaning'])}</div></div>
                <div class="bundle-card"><div class="label">다음 단계</div><div class="chip-row">{''.join(_chip(x) for x in dossier['next_step_ideas'][:3])}</div></div>
              </div>
              <div class="section-head"><div><div class="kicker">붙어 있는 근거</div><h3>왜 이 line에 이 묶음이 붙는가</h3></div><div class="mono">{len(item.get('evidence_bundles') or [])} bundles</div></div>
              <div class="bundle-grid">{bundle_preview}</div>
            </section>
            """
        )
    body = f"""
    <div class="page">
      <section class="hero">
        <div class="kicker">VectorFL Paper</div>
        <div class="section-head"><h1>line 비교</h1><div class="mono">여러 line을 나란히 읽기</div></div>
        <div class="meta">여러 line을 나란히 보면서, 어떤 line이 더 읽기 쉽고 더 잘 연결되며 다음 행동으로 이어지기 쉬운지 비교합니다.</div>
      </section>
      <div class="frame with-right">
        {_render_nav(data, 'line-review')}
        <main class="stack">
          {''.join(rows)}
        </main>
        <aside class="stack">
          <section class="panel soft">
            <div class="kicker">비교 기준</div>
            <div class="body-copy">좋은 line은 문장 하나로 끝나지 않습니다. 관련 기록을 다시 열 수 있어야 하고, 애매한 점이 보여야 하며, 다음 행동이 더 또렷해야 합니다.</div>
          </section>
          <section class="panel soft">
            <div class="entity-actions">{_link('case-detail.html', '작업 상세로 돌아가기')}{_link('case-inspector.html', 'line 들여다보기', subtle=True)}</div>
          </section>
        </aside>
      </div>
    </div>"""
    return _base_html("VectorFL Operable Surfaces / Line Review", data, body)


def render_line_detail_page(data: Dict[str, Any], line_index: int) -> str:
    lines = data["case_detail"]["generated_lines"]
    safe_index = max(0, min(line_index, len(lines) - 1))
    line = lines[safe_index]
    dossier = line["dossier"]
    evidence_bundle_cards = _render_evidence_bundle_cards(line.get("evidence_bundles") or [])
    request_panel = _render_worker_request_summary(data["worker_bridge"], title="이 line에서 이어지는 worker request", compact=True)
    selection_impact_panel = _render_selection_impact(data, title="이 line이 handoff와 rewrite에 주는 영향", mode_label="line detail")
    body = f"""
    <div class="page">
      <section class="hero">
        <div class="kicker">VectorFL Paper</div>
        <div class="section-head"><h1>line 상세</h1><div class="mono">{html.escape(line['line_id'])}</div></div>
        <div class="meta">line 하나를 따로 열어, 이 line이 왜 중요하고 무엇과 연결되며 다음에 무엇을 해야 하는지 차분히 읽는 페이지입니다.</div>
      </section>
      <div class="frame with-right">
        {_render_nav(data, 'line-review')}
        <main class="stack">
          <section class="panel">
            <div class="section-head"><div><div class="kicker">1. line 자체</div><h2>{html.escape(line['raw'])}</h2></div><div class="mono">{html.escape(line['status'])}</div></div>
            <div class="inspector-block">
              <div class="label">사람이 읽는 말</div>
              <div class="body-copy">{html.escape(line['human_translation'])}</div>
              <div class="label">짧은 뜻풀이</div>
              <div class="body-copy">{html.escape(dossier['translation']['core'])}</div>
              <div class="label">조금 더 풀어쓴 말</div>
              <div class="body-copy">{html.escape(dossier['translation']['expanded'])}</div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">2. 왜 중요한가</div><h2>{html.escape(dossier['friendly_title'])}</h2></div><div class="mono">{html.escape(line['family'])}</div></div>
            <div class="summary-grid">
              <div class="stack">
                <div class="inspector-block"><div class="label">친화적 요약</div><div class="body-copy">{html.escape(dossier['friendly_summary'])}</div></div>
                <div class="inspector-block"><div class="label">보존하는 것</div><div class="chip-row">{''.join(_chip(item) for item in data['case_inspector']['what_it_preserves'])}</div></div>
                <div class="inspector-block"><div class="label">빠뜨린 것</div><div class="chip-row">{''.join(_chip(item) for item in data['case_inspector']['what_it_omits'])}</div></div>
              </div>
              <div class="stack">
                <div class="warn"><strong>아직 애매한 점</strong><div>{html.escape(_friendly_text(dossier['uncertainty']))}</div></div>
                <div class="inspector-block"><div class="label">검색에 쓸 말</div><div class="body-copy">{html.escape(data['case_inspector']['searchable_form'])}</div></div>
                <div class="inspector-block"><div class="label">차용할 때의 말</div><div class="body-copy">{html.escape(data['case_inspector']['adoption_form'])}</div></div>
              </div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">3. 연결과 다음 단계</div><h2>무엇과 붙고 어디로 이어지는가</h2></div><div class="mono">recall / routing</div></div>
            <div class="bundle-grid">
              <div class="bundle-card"><div class="label">선언문 쪽에서 보면</div><div class="body-copy">{html.escape(dossier['declaration_linkage']['human_readable'])}</div></div>
              <div class="bundle-card"><div class="label">지시문 쪽에서 보면</div><div class="body-copy">{html.escape(dossier['directive_linkage']['human_readable'])}</div></div>
              <div class="bundle-card"><div class="label">과거 대화 쪽에서 보면</div><div class="body-copy">{html.escape(dossier['past_conversation_linkage']['human_readable'])}</div></div>
              <div class="bundle-card"><div class="label">family 의미</div><div class="body-copy">{html.escape(dossier['family_expansion']['meaning'])}</div></div>
            </div>
            <div class="entity-actions">{_link('case-inspector.html', 'line 들여다보기')}{_link('internal-recall.html', '내부 자료 다시 보기', subtle=True)}{_link('external-resources.html', '외부 자료 계획 보기', subtle=True)}{_link('case-routing.html', '넘김과 배정 보기', subtle=True)}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">4. 이 line을 떠받치는 근거</div><h2>이 line에 직접 붙는 근거 묶음</h2></div><div class="mono">{len(line.get('evidence_bundles') or [])} bundles</div></div>
            <div class="bundle-grid">{evidence_bundle_cards}</div>
          </section>
        </main>
        <aside class="stack">
          {selection_impact_panel}
          {request_panel}
          <section class="panel soft">
            <div class="kicker">검색어 후보</div>
            <div class="chip-row">{''.join(_chip(item) for item in dossier['search_queries'])}</div>
          </section>
          <section class="panel soft">
            <div class="kicker">다음 단계 아이디어</div>
            <div class="chip-row">{''.join(_chip(item) for item in dossier['next_step_ideas'])}</div>
          </section>
          <section class="panel soft">
            <div class="kicker">바로 이어서 보기</div>
            <div class="tool-row">
              {_link('case-detail.html', '작업 상세로 돌아가기')}
              {_link('line-review.html', 'line 비교 보기', subtle=True)}
            </div>
          </section>
        </aside>
      </div>
    </div>"""
    return _base_html(f"VectorFL Operable Surfaces / {line['line_id']}", data, body)


def render_case_routing_page(data: Dict[str, Any]) -> str:
    routing = data["case_routing"]
    basis = routing.get("routing_basis") or {}
    current_selection = data.get("current_operating_selection") or {}
    supervisor_checkpoint = _render_supervisor_checkpoint(
        data,
        page_title="왜 지금 routing을 읽는가",
        page_reason="이 페이지는 보기용 흐름도가 아니라, 지금 선택된 line과 bundle을 어느 팀과 다음 단계로 넘겨야 하는지, 그리고 왜 그 handoff가 필요한지 감독자 언어로 확인하는 배정면입니다.",
    )
    selection_panel = _render_selection_state(data["selection_state"])
    engine_state_panel = _render_engine_state(data["engine_state"])
    current_selection_panel = _render_current_operating_selection(data["current_operating_selection"])
    intake_panel = _render_intake_wizard(data["intake_wizard"])
    selection_impact_panel = _render_selection_impact(data, title="현재 선택이 routing 판단에 미치는 영향", mode_label="routing")
    request_panel = _render_worker_request_summary(data["worker_bridge"], title="handoff 전에 확인할 worker request", compact=True)
    evidence_bundle_cards = _render_evidence_bundle_cards(routing.get("evidence_bundles") or [])
    organ_options = "".join(
        f'<option value="{html.escape(organ["slug"])}"{" selected" if organ["current"] else ""}>{html.escape(organ["label"])}</option>'
        for organ in data["organs"]
    )
    next_options = "".join(
        f'<option value="{html.escape(organ["slug"])}"{" selected" if organ["next_candidate"] else ""}>{html.escape(organ["label"])}</option>'
        for organ in data["organs"]
    )
    resource_rows = "".join(
        f'<div class="check-row"><div><strong>{html.escape(team["name"])}</strong><div class="meta">{html.escape(team["mode"])}</div></div><input type="checkbox" {"checked" if team["enabled"] else ""}></div>'
        for team in routing["external_resource_teams"]
    )
    program_rows = "".join(
        f'<div class="check-row"><div><strong>{html.escape(team["name"])}</strong><div class="meta">{html.escape(team["mode"])}</div></div><input type="checkbox" {"checked" if team["enabled"] else ""}></div>'
        for team in routing["external_program_teams"]
    )
    team_assignment_rows = "".join(
        f'<div class="list-row"><div class="entity-row"><div class="entity-main"><div class="entity-title">{html.escape(item["team"])}</div><div class="entity-sub">관리 CLI={html.escape(item["managing_cli"])} / paired external={html.escape(item["paired_external_team"])}</div><div class="entity-sub">handoff={html.escape(" -> ".join(item.get("handoff_targets") or ["none"]))}</div></div><div class="entity-meta"><div class="chip-row">{_chip("current team") if item.get("slug") == current_selection.get("selected_team_slug") else ""}</div></div></div></div>'
        for item in routing.get("team_assignment_options") or []
    ) or '<div class="list-row"><div class="entity-title">팀 배정 후보가 아직 없습니다</div></div>'
    cli_assignment_rows = "".join(
        f'<div class="list-row"><div class="entity-row"><div class="entity-main"><div class="entity-title">{html.escape(item["lane"])}</div><div class="entity-sub">owning cli={html.escape(item["owning_cli"])} / {html.escape(item["provider_model"])}</div><div class="entity-sub">맡은 팀={html.escape(", ".join(item.get("managed_team_slugs") or []))}</div></div><div class="entity-meta"><div class="chip-row">{_chip("current lane") if item.get("slug") == current_selection.get("selected_lane_slug") else ""}</div></div></div></div>'
        for item in routing.get("cli_assignment_options") or []
    ) or '<div class="list-row"><div class="entity-title">CLI 배정 후보가 아직 없습니다</div></div>'
    restriction_rows = "".join(
        f'<div class="check-row"><div><strong>{html.escape(flag)}</strong><div class="meta">governance restriction</div></div><input type="checkbox" checked></div>'
        for flag in routing["restriction_flags"]
    ) or '<div class="check-row"><div><strong>none</strong><div class="meta">no active restriction</div></div><input type="checkbox"></div>'
    body = f"""
    <div class="page">
      <section class="hero">
        <div class="kicker">VectorFL Paper</div>
        <div class="section-head"><h1>업무 배정</h1><div class="mono">다음 행동과 담당 정하기</div></div>
        <div class="meta">지금 누가 맡고 있는지, 다음에 누구에게 넘길지, 외부 도움이 필요한지, 제약을 같이 들고 가야 하는지를 정리하는 페이지입니다.</div>
      </section>
      <div class="frame with-right">
        {_render_nav(data, 'case-routing')}
        <main class="stack">
          {supervisor_checkpoint}
          {engine_state_panel}
          {current_selection_panel}
          <section class="panel">
            <div class="section-head"><div><div class="kicker">1. 지금 맡는 곳</div><h2>현재 팀과 다음 후보</h2></div><div class="mono">{html.escape(str(routing.get('current_lane_ref') or 'unknown'))}</div></div>
            <div class="form-grid">
              <label class="field"><span class="label">현재 팀</span><select>{organ_options}</select></label>
              <label class="field"><span class="label">다음 후보 팀</span><select>{next_options}</select></label>
              <label class="field"><span class="label">해제 조건</span><input value="{html.escape(str(routing.get('release_condition') or 'none'))}"></label>
              <label class="field"><span class="label">연결된 프로그램</span><input value="{html.escape(', '.join(routing.get('linked_programs') or []))}"></label>
            </div>
            <label class="field"><span class="label">왜 이 팀이 맡고 있는가</span><textarea>{html.escape(str(routing.get('placement_reason') or ''))}</textarea></label>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">2. 넘기는 근거</div><h2>왜 다음으로 가야 하는가</h2></div><div class="mono">{html.escape(str(basis.get('current_material_stage') or 'unknown'))}</div></div>
            <div class="inspector-block">
              <div class="label">지금 기준이 되는 line</div>
              <div class="body-copy">{html.escape(str(basis.get('selected_line') or 'none'))}</div>
              <div class="label">검색이 필요한가</div>
              <div class="meta">{html.escape(str(basis.get('search_trigger') or False))}</div>
              <div class="label">왜 검색이 필요한가</div>
              <div class="body-copy">{html.escape(str(basis.get('search_reason') or 'none'))}</div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">3. intake -> selection -> handoff</div><h2>운용 순서 확인</h2></div><div class="mono">wizarded routing</div></div>
            <div class="summary-grid">
              <div class="stack">{intake_panel}</div>
              <div class="stack">{selection_panel}</div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">4. 외부 도움</div><h2>리소스 팀 / 프로그램 팀</h2></div><div class="mono">여기서 함께 고르기</div></div>
            <div class="form-grid">
              <div class="field"><span class="label">외부 리소스 팀</span><div class="check-list">{resource_rows}</div></div>
              <div class="field"><span class="label">외부 프로그램 팀</span><div class="check-list">{program_rows}</div></div>
            </div>
            <div class="meta">선택된 program workspace와 runtime binding을 같이 보려면 엔진 개요와 프로그램 워크스페이스를 함께 읽어야 합니다.</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">5. 팀 배정 후보</div><h2>어느 팀에게 맡길 수 있는가</h2></div><div class="mono">cell assignment</div></div>
            <div class="list-shell">{team_assignment_rows}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">6. CLI 배정 후보</div><h2>어떤 CLI와 모델을 붙일 수 있는가</h2></div><div class="mono">cli ownership</div></div>
            <div class="list-shell">{cli_assignment_rows}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">7. 이 넘김을 떠받치는 근거</div><h2>왜 이렇게 넘기려는지 보여주는 근거 묶음</h2></div><div class="mono">{len(routing.get('evidence_bundles') or [])} bundles</div></div>
            <div class="bundle-grid">{evidence_bundle_cards}</div>
          </section>
        </main>
        <aside class="stack">
          {selection_impact_panel}
          {request_panel}
          <section class="panel soft">
            <div class="kicker">같이 들고 가는 제약</div>
            <h3>들고 가는 제약</h3>
            <div class="check-list">{restriction_rows}</div>
          </section>
          <section class="panel soft">
            <div class="kicker">마지막 확인</div>
            <div class="tool-row">
              {_link('case-detail.html', '작업 상세로 돌아가기')}
              {_link('case-inspector.html', 'line 들여다보기', subtle=True)}
            </div>
            <div class="meta">지금은 surface-only 단계라 실제 저장은 없지만, 어떤 결정을 내려야 하는지는 여기서 한눈에 보이게 유지합니다.</div>
          </section>
        </aside>
      </div>
    </div>"""
    return _base_html("VectorFL Operable Surfaces / Case Routing", data, body)


def render_internal_recall_page(data: Dict[str, Any]) -> str:
    recall = data["internal_recall"]
    supervisor_checkpoint = _render_supervisor_checkpoint(
        data,
        page_title="왜 내부 자료를 먼저 다시 보는가",
        page_reason="이 페이지는 참고 문서를 모아두는 곳이 아니라, 외부를 더 보기 전에 무엇이 이미 내부에 있고 무엇이 아직 잘 안 읽혔는지 다시 확인해서 internal-first 판단을 지키는 recall 면입니다.",
    )
    evidence_bundle_cards = _render_evidence_bundle_cards(recall.get("evidence_bundles") or [])
    doc_rows = "".join(
        f'<div class="list-row"><div class="entity-row"><div class="entity-main"><div class="entity-title">{html.escape(item["title"])}</div><div class="entity-sub">{html.escape(_friendly_text(item["summary"] or "no summary"))}</div></div><div class="entity-meta"><div class="mono">{html.escape(item["path"])}</div></div></div></div>'
        for item in recall["recall_docs"]
    )
    family_rows = "".join(
        f'<div class="bundle-card"><div class="label">line 묶음</div><strong>{html.escape(item["label"])}</strong><div class="body-copy">{html.escape(_friendly_text(item["summary"]))}</div></div>'
        for item in recall["line_family_rows"]
    )
    role_rows = "".join(
        f'<div class="list-row"><div class="entity-row"><div class="entity-main"><div class="entity-title">{html.escape(item.get("unit_id") or "unit")}</div><div class="entity-sub">{html.escape(item.get("function_in_source") or "none")}</div></div><div class="entity-meta"><div class="mono">{html.escape(item.get("role_type") or "unknown")}</div></div></div></div>'
        for item in recall.get("role_hints") or []
    ) or '<div class="list-row"><div class="entity-title">역할 힌트가 아직 없습니다</div></div>'
    relation_rows = "".join(
        f'<div class="bundle-card"><div class="label">{html.escape(item.get("relation_type") or "relation")}</div><strong>{html.escape(str(item.get("from_unit_id") or "from"))}</strong><div class="meta">to {html.escape(str(item.get("to_unit_id") or "to"))}</div></div>'
        for item in recall.get("relation_clues") or []
    ) or '<div class="bundle-card"><strong>관계 단서가 아직 없습니다</strong></div>'
    provisional_rows = "".join(
        f'<div class="list-row"><div class="entity-title">{html.escape(item.get("provisional_line") or "unknown")}</div><div class="entity-sub">보존하는 것: {html.escape(_friendly_text(item.get("what_it_preserves") or []))}</div></div>'
        for item in recall.get("provisional_line_block") or []
    ) or '<div class="list-row"><div class="entity-title">임시 line이 아직 없습니다</div></div>'
    gap_rows = "".join(f"<li>{html.escape(_friendly_text(item))}</li>" for item in recall["gap_summary"])
    body = f"""
    <div class="page">
      <section class="hero">
        <div class="kicker">VectorFL Paper</div>
        <div class="section-head"><h1>내부 재독해</h1><div class="mono">line 뒤의 기록을 다시 열기</div></div>
        <div class="meta">line이 쓸 만한 상태인지 보려면, 외부 검색 전에 먼저 내부 선언문, 지시문, 과거 판단, trace, family를 다시 불러와야 합니다. 이 페이지는 reference list가 아니라, 내가 무엇을 어떤 순서로 다시 보는지를 드러내는 읽기 기관입니다.</div>
      </section>
      <div class="frame with-right">
        {_render_nav(data, 'internal-recall')}
        <main class="stack">
          {supervisor_checkpoint}
          <section class="panel">
            <div class="section-head"><div><div class="kicker">1. 다시 볼 기준</div><h2>{html.escape(recall['selected_line'])}</h2></div><div class="mono">다시 보기 시작점</div></div>
            <div class="meta">이 페이지는 line 하나를 문장으로 끝내지 않고, 내부 기록망을 다시 여는 기준으로 쓰기 위해 존재합니다.</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">2. 먼저 다시 볼 문서</div><h2>선언문 / 잠금 / 기준 문서</h2></div><div class="mono">{len(recall['recall_docs'])} docs</div></div>
            <div class="meta">첫 단계에서는 line과 직접 닿는 선언문, lock, 기준 문서를 다시 불러와 현재 판단의 바닥을 먼저 점검합니다.</div>
            <div class="list-shell">{doc_rows}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">3. 같이 읽어야 하는 family</div><h2>같이 읽어야 하는 line 묶음</h2></div><div class="mono">{len(recall['line_family_rows'])}개 묶음</div></div>
            <div class="meta">여기서는 line을 혼자 두지 않고, 같이 살아 있어야 meaning이 두꺼워지는 family를 묶어서 다시 확인합니다.</div>
            <div class="bundle-grid">{family_rows}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">4. 원본에서 다시 꺼낼 재료</div><h2>역할 / 관계 / 임시 line</h2></div><div class="mono">원본 기반 다시 보기</div></div>
            <div class="meta">이 구간은 원본의 role hint, relation clue, provisional line을 다시 꺼내서 현재 line이 무엇을 놓치고 있는지 확인하는 단계입니다.</div>
            <div class="summary-grid">
              <div class="list-shell">{role_rows}</div>
              <div class="stack">
                <div class="bundle-grid">{relation_rows}</div>
                <div class="list-shell">{provisional_rows}</div>
              </div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">5. 지금 묶여 있는 근거</div><h2>recall evidence bundles</h2></div><div class="mono">{len(recall.get('evidence_bundles') or [])} bundles</div></div>
            <div class="meta">마지막으로 recall이 실제 evidence bundle 위에서 유지되는지 확인해서, 다음 search나 rewrite가 내부 기억과 끊기지 않게 만듭니다.</div>
            <div class="bundle-grid">{evidence_bundle_cards}</div>
          </section>
        </main>
        <aside class="stack">
          <section class="panel soft">
            <div class="kicker">왜 먼저 다시 봐야 하나</div>
            <h3>왜 내부를 먼저 다시 봐야 하나</h3>
            <ul class="meta">{gap_rows}</ul>
          </section>
          <section class="panel soft">
            <div class="kicker">바로 이어서 보기</div>
            <div class="tool-row">
              {_link('external-resources.html', '외부 자료 계획 보기')}
              {_link('lane-runs.html', 'lane 비교 결과 보기', subtle=True)}
            </div>
          </section>
        </aside>
      </div>
    </div>"""
    return _base_html("VectorFL Operable Surfaces / Internal Recall", data, body)


def render_external_resources_page(data: Dict[str, Any]) -> str:
    ext = data["external_resources"]
    supervisor_checkpoint = _render_supervisor_checkpoint(
        data,
        page_title="왜 지금 외부 자료 계획으로 넘어가는가",
        page_reason="이 페이지는 검색 아이디어를 늘어놓는 곳이 아니라, 내부에서 남은 gap을 어떤 질문으로 외부 비교에 넘길지와 그 결과를 다시 어디로 귀속시킬지를 결정하는 외부 비교 계획면입니다.",
    )
    worker_bridge = _render_worker_bridge(data["worker_bridge"])
    selection_impact_panel = _render_selection_impact(data, title="검색 질문과 rewrite 요청이 공유하는 선택 기준", mode_label="search bridge")
    evidence_bundle_cards = _render_evidence_bundle_cards(ext.get("evidence_bundles") or [])
    question_rows = "".join(f'<div class="list-row"><div class="entity-title">{html.escape(q)}</div></div>' for q in ext["question_set"])
    candidate_rows = "".join(
        f'<div class="list-row"><div class="entity-row"><div class="entity-main"><div class="entity-title">{html.escape(item.get("value_label") or item.get("id") or "candidate")}</div><div class="entity-sub">{html.escape(_friendly_text(item.get("relation_summary") or "no relation summary"))}</div></div><div class="entity-meta"><div class="mono">{html.escape(item.get("source_pointer") or "unknown")}</div></div></div></div>'
        for item in ext["candidate_sources"]
    ) or '<div class="list-row"><div class="entity-title">후보 자료가 아직 없습니다</div></div>'
    attention_rows = "".join(
        f'<div class="bundle-card"><div class="label">주의 신호</div><strong>{html.escape(item.get("asset_id") or "unknown")}</strong><div class="body-copy">{html.escape(_friendly_text(item.get("attention_pattern_summary") or "none"))}</div></div>'
        for item in ext["attention_rows"]
    ) or '<div class="bundle-card"><strong>주의 신호가 아직 없습니다</strong></div>'
    uncertainty_rows = "".join(
        f'<div class="list-row"><div class="entity-title">{html.escape(item.get("unit_id") or "unknown")}</div><div class="entity-sub">{html.escape(_friendly_text(item.get("pending_interpretation") or item.get("ambiguity") or "none"))}</div></div>'
        for item in ext.get("uncertainty_rows") or []
    ) or '<div class="list-row"><div class="entity-title">불확실성 기록이 아직 없습니다</div></div>'
    setup_steps = "".join(
        f'<div class="list-row"><div class="entity-row"><div class="entity-main"><div class="entity-title">{html.escape(step["label"])}</div><div class="entity-sub">{html.escape(_friendly_text(step["summary"]))}</div></div><div class="entity-meta"><div class="chip-row">{_chip(step["status"])}</div></div></div></div>'
        for step in ext.get("setup_steps") or []
    )
    scenario_entry = ext.get("scenario_entry") or {}
    material_review = ext.get("material_bundle_review") or {}
    team_cli_setup = ext.get("team_cli_setup") or {}
    launch_decision = ext.get("launch_decision") or {}
    live_updates = "".join(
        f'<div class="list-row"><div class="entity-row"><div class="entity-main"><div class="entity-title">{html.escape(str(item.get("headline") or "update"))}</div><div class="entity-sub">owner={html.escape(str(item.get("owner") or "unknown"))}</div></div><div class="entity-meta"><div class="chip-row">{_chip(str(item.get("status") or "unknown"))}</div></div></div></div>'
        for item in ext.get("live_updates") or []
    ) or '<div class="list-row"><div class="entity-title">아직 live update가 없습니다</div></div>'
    body = f"""
    <div class="page">
      <section class="hero">
        <div class="kicker">VectorFL Paper</div>
        <div class="section-head"><h1>입력 / 외부 비교</h1><div class="mono">입력 확인과 검색 계획</div></div>
        <div class="meta">이 페이지는 검색 목록이 아니라 onboarding 면입니다. 시나리오 재료를 확인하고, 어떤 팀과 CLI를 붙이고, 어떤 계약과 모델을 쓸지 정한 뒤, hold / preview / launch를 결정합니다.</div>
      </section>
      <div class="frame with-right">
        {_render_nav(data, 'external-resources')}
        <main class="stack">
          {supervisor_checkpoint}
          {_render_paper_proper_bridge_panel(data, mode='input')}
          <section class="panel">
            <div class="section-head"><div><div class="kicker">1. intake setup</div><h2>입력에서 launch까지 밟는 순서</h2></div><div class="mono">scenario -> team -> cli -> launch</div></div>
            <div class="list-shell">{setup_steps}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">2. scenario entry</div><h2>이번 loop를 왜 시작하는가</h2></div><div class="mono">{html.escape(str(scenario_entry.get('source_confirmation') or 'source pending'))}</div></div>
            <div class="inspector-block">
              <div class="label">objective</div>
              <div class="body-copy">{html.escape(str(scenario_entry.get('objective') or 'objective pending'))}</div>
              <div class="label">seed reason</div>
              <div class="body-copy">{html.escape(str(scenario_entry.get('seed_reason') or ''))}</div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">3. material bundle review</div><h2>이번 입력에 묶는 내부 재료</h2></div><div class="mono">{len(material_review.get('linked_bundle_ids') or [])} bundles</div></div>
            <div class="inspector-block">
              <div class="label">selected refs</div>
              <div class="body-copy">{html.escape(', '.join(material_review.get('selected_refs') or []) or 'selected refs pending')}</div>
              <div class="label">reference rule</div>
              <div class="body-copy">{html.escape(str(material_review.get('reference_rule') or ''))}</div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">4. team / cli setup</div><h2>어느 팀에 어떤 CLI와 모델을 붙일까</h2></div><div class="mono">assignment before launch</div></div>
            <div class="form-grid">
              <label class="field"><span class="label">selected team</span><input value="{html.escape(str(team_cli_setup.get('selected_team') or 'team pending'))}" readonly></label>
              <label class="field"><span class="label">paired external team</span><input value="{html.escape(str(team_cli_setup.get('paired_external_team') or 'none'))}" readonly></label>
              <label class="field"><span class="label">owning CLI</span><input value="{html.escape(str(team_cli_setup.get('owning_cli') or 'cli pending'))}" readonly></label>
              <label class="field"><span class="label">provider / model</span><input value="{html.escape(f'{team_cli_setup.get("provider") or "provider"} / {team_cli_setup.get("model") or "model"}')}" readonly></label>
              <label class="field"><span class="label">md contracts</span><input value="{html.escape(', '.join(team_cli_setup.get('md_contracts') or []) or 'contracts pending')}" readonly></label>
              <label class="field"><span class="label">env check</span><input value="{html.escape(str(team_cli_setup.get('env_check') or 'env check pending'))}" readonly></label>
            </div>
          </section>
          {worker_bridge}
          <section class="panel">
            <div class="section-head"><div><div class="kicker">6. 무엇을 물을까</div><h2>검색 질문</h2></div><div class="mono">{len(ext['question_set'])} prompts</div></div>
            <div class="list-shell">{question_rows}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">7. 어떤 점이 아직 비는가</div><h2>불확실성 / 미해석</h2></div><div class="mono">차용 전 다시 확인</div></div>
            <div class="inspector-block">
              <div class="label">검색에 쓸 말</div>
              <div class="body-copy">{html.escape(ext.get('searchable_form') or 'none')}</div>
            </div>
            <div class="list-shell">{uncertainty_rows}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">8. 지금 후보가 되는 자료</div><h2>외부 참고 후보</h2></div><div class="mono">{len(ext['candidate_sources'])} options</div></div>
            <div class="list-shell">{candidate_rows}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">9. launch decision</div><h2>지금 보류할지, 미리보기로 둘지, 실행할지</h2></div><div class="mono">{html.escape(str(launch_decision.get('current_mode') or 'preview'))}</div></div>
            <div class="inspector-block">
              <div class="label">available modes</div>
              <div class="chip-row">{''.join(_chip(mode) for mode in launch_decision.get('modes') or [])}</div>
              <div class="label">current reason</div>
              <div class="body-copy">{html.escape(str(launch_decision.get('reason') or ''))}</div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">10. live updates</div><h2>이 intake loop가 만든 현재 업데이트</h2></div><div class="mono">issue-like feed</div></div>
            <div class="list-shell">{live_updates}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">11. 왜 이 검색이 생겼는가</div><h2>search justification bundles</h2></div><div class="mono">{len(ext.get('evidence_bundles') or [])} bundles</div></div>
            <div class="bundle-grid">{evidence_bundle_cards}</div>
          </section>
        </main>
        <aside class="stack">
          {selection_impact_panel}
          <section class="panel soft">
            <div class="kicker">원하는 자료 유형</div>
            <div class="chip-row">{''.join(_chip(item) for item in ext['wanted_material_types'])}</div>
          </section>
          <section class="panel soft">
            <div class="kicker">빼고 싶은 자료 유형</div>
            <div class="chip-row">{''.join(_chip(item) for item in ext['excluded_material_types'])}</div>
          </section>
          <section class="panel soft">
            <div class="kicker">주의 신호</div>
            <div class="bundle-grid">{attention_rows}</div>
          </section>
        </aside>
      </div>
    </div>"""
    return _base_html("VectorFL Operable Surfaces / External Resources", data, body)


def render_lanes_page(data: Dict[str, Any]) -> str:
    lanes = data["lanes"]
    rows = []
    for lane in lanes["lane_rows"]:
        enabled_label = "활성" if lane["enabled"] else "비활성"
        managed_teams = ", ".join(lane.get("managed_team_slugs") or []) or "none"
        rows.append(
            f"""
            <div class="list-row">
              <div class="entity-row">
                <div class="entity-main">
                  <div class="section-head"><div class="entity-title">{html.escape(lane['label'])}</div><div class="mono">{html.escape(lane['provider_model'])}</div></div>
                <div class="entity-sub">{html.escape(_friendly_text(lane['notes']))}</div>
                  <div class="meta">관리 CLI={html.escape(lane['owning_cli'])} / 맡은 팀={html.escape(managed_teams)} / 결과 귀속={html.escape(lane['return_route'])}</div>
                  <div class="meta">adapter={html.escape(lane['adapter_type'])} / env={html.escape(lane['env_status'])} / approvals={html.escape(lane['approvals_policy'])}</div>
                </div>
                <div class="entity-meta">
                  <div class="chip-row">{_chip(enabled_label)}{_chip(lane['status'])}</div>
                  <div class="meta">provider={html.escape(lane['provider'])} / model={html.escape(lane['model'])}</div>
                  <div class="meta">timeout={html.escape(lane['timeout'])} / budget={html.escape(lane['budget'])} / schema={html.escape(lane['output_schema'])}</div>
                </div>
                <div class="entity-actions">{_link(lane['detail_href'], 'lane 상세 보기')}{_link(lane['editor_href'], 'lane 수정', subtle=True)}</div>
              </div>
            </div>
            """
        )
    body = f"""
    <div class="page">
      <section class="hero">
        <div class="kicker">VectorFL Paper</div>
        <div class="section-head"><h1>CLI / 어댑터</h1><div class="mono">도구 연결, 모델 선택, 실행 경로 관리</div></div>
        <div class="meta">여기는 단순 비교 탭이 아니라 Codex/Gemini 같은 CLI를 어떤 팀에 붙이고, 어떤 provider / model / payload 정책으로 돌릴지 정하는 실행면입니다.</div>
      </section>
      <div class="frame with-right">
        {_render_nav(data, 'lanes')}
        <main class="stack">
          <section class="panel">
            <div class="metric-strip">
              <div class="metric"><div class="kicker">lane 수</div><div class="metric-value">{len(lanes['lane_rows'])}</div><div class="meta">비교 가능한 실행 경로</div></div>
              <div class="metric"><div class="kicker">활성 lane</div><div class="metric-value">{sum(1 for lane in lanes['lane_rows'] if lane['enabled'])}</div><div class="meta">현재 켜진 lane</div></div>
              <div class="metric"><div class="kicker">공통 파이프라인</div><div class="metric-value" style="font-size:14px;">{html.escape(' / '.join(lanes['bottom_pipeline']))}</div><div class="meta">모든 lane이 같은 순서로 실행</div></div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">등록된 lane</div><h2>CLI 소유권과 모델 설정</h2></div><div class="mono">provider / model / team ownership</div></div>
            <div class="list-shell">{''.join(rows)}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">adapter manager</div><h2>어댑터 레지스트리와 환경 상태</h2></div><div class="mono">install / enable / reload / test</div></div>
            <div class="summary-grid">
              {''.join(
                  f'<div class="inspector-block"><div class="label">{html.escape(lane["label"])}</div><div class="body-copy">adapter={html.escape(lane["adapter_type"])} / env={html.escape(lane["env_status"])} / test={html.escape(lane["adapter_test"])}</div><div class="meta">{html.escape(lane["env_summary"])}</div></div>'
                  for lane in lanes["lane_rows"]
              )}
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">connection flow</div><h2>CLI 어댑터를 붙이는 순서</h2></div><div class="mono">select -> configure -> test -> launch</div></div>
            <div class="summary-grid">
              <div class="inspector-block"><div class="label">1. adapter 선택</div><div class="body-copy">Codex / Gemini / Claude 중 어떤 CLI를 어떤 팀에 붙일지 먼저 정합니다.</div></div>
              <div class="inspector-block"><div class="label">2. provider / model</div><div class="body-copy">각 lane의 provider와 model을 정하고, 같은 selection object를 공유하도록 고정합니다.</div></div>
              <div class="inspector-block"><div class="label">3. env / payload policy</div><div class="body-copy">승인 우회 여부, search 사용 여부, instructions/contract 경로를 확인합니다.</div></div>
              <div class="inspector-block"><div class="label">4. launch / return</div><div class="body-copy">launch 후 결과는 trace와 inbox로 돌아와 reopen 판단으로 이어집니다.</div></div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">launch queue</div><h2>지금 실행 대기 중인 요청</h2></div><div class="mono">payload preview first</div></div>
            {_render_worker_request_summary(data["worker_bridge"], title="현재 lane이 들고 가는 요청", compact=False)}
          </section>
        </main>
        <aside class="stack">
          <section class="panel soft">
            <div class="kicker">운용 원칙</div>
            <div class="body-copy">{html.escape(_friendly_text(lanes['top_note']))}</div>
          </section>
          <section class="panel soft">
            <div class="kicker">payload 정책</div>
            <div class="body-copy">{html.escape(_friendly_text(lanes['middle_note']))}</div>
            <div class="chip-row">{''.join(_chip(step) for step in lanes['bottom_pipeline'])}</div>
          </section>
          <section class="panel soft">
            <div class="kicker">다음으로 볼 곳</div>
            <div class="entity-actions">{_link('lane-runs.html', '실행 비교 보기')}{_link('case-routing.html', '업무 배정 보기', subtle=True)}</div>
          </section>
        </aside>
      </div>
    </div>"""
    return _base_html("VectorFL Operable Surfaces / Lanes", data, body)


def render_lane_runs_page(data: Dict[str, Any]) -> str:
    lane_runs = data["lane_runs"]
    supervisor_checkpoint = _render_supervisor_checkpoint(
        data,
        page_title="왜 lane 비교를 따로 보는가",
        page_reason="이 페이지는 여러 실행 결과를 병렬로 자랑하는 곳이 아니라, 같은 line과 같은 pipeline에서 무엇이 달라졌는지 비교해 지금 어떤 실행 경로를 채택하거나 보류해야 하는지 판단하는 비교면입니다.",
    )
    selection_impact_panel = _render_selection_impact(data, title="현재 선택이 lane compare에 미치는 영향", mode_label="lane compare")
    request_panel = _render_worker_request_summary(data["worker_bridge"], title="lane compare 옆에 유지되는 rewrite request", compact=True)
    evidence_bundle_cards = _render_evidence_bundle_cards(lane_runs.get("evidence_bundles") or [])
    run_trace_blocks = []
    for item in lane_runs.get("run_trace_rows") or []:
        bundle_text = ", ".join(item.get("bundle_ids") or []) or "none"
        payload_text = json.dumps(item.get("request_payload") or {}, ensure_ascii=False, indent=2)
        run_trace_blocks.append(
            f'<div class="audit-row"><div class="section-head"><div><div class="kicker">{html.escape(item.get("trace_kind") or "trace")}</div><h3>{html.escape(_friendly_text(item.get("summary") or "none"))}</h3></div><div class="pill {html.escape(item.get("status") or "")}">{html.escape(item.get("status") or "unknown")}</div></div><div class="meta">adapter={html.escape(str(item.get("adapter") or "unknown"))} / line={html.escape(str(item.get("selected_line") or "none"))}</div><div class="meta">bundles={html.escape(bundle_text)}</div><div class="code-block">{html.escape(payload_text)}</div><div class="body-copy">{html.escape(_friendly_text(item.get("return_text") or "none"))}</div></div>'
        )
    run_trace_rows = "".join(run_trace_blocks) or '<div class="audit-row"><strong>아직 남아 있는 run trace가 없습니다</strong></div>'
    lane_rows = []
    for lane in lane_runs["lanes"]:
        lane_rows.append(
            f"""
            <div class="list-row">
              <div class="section-head"><div><div class="kicker">{html.escape(lane['mode'])}</div><h3>{html.escape(lane['name'])}</h3></div><div class="mono">{html.escape(lane['status'])}</div></div>
              <div class="form-grid">
                <div class="inspector-block"><div class="label">읽기 결과</div><div class="body-copy">{html.escape(_friendly_text(lane['read_result']))}</div></div>
                <div class="inspector-block"><div class="label">적용 결과</div><div class="body-copy">{html.escape(_friendly_text(lane['apply_result']))}</div></div>
                <div class="inspector-block"><div class="label">검색 결과</div><div class="body-copy">{html.escape(_friendly_text(lane['search_result']))}</div></div>
                <div class="inspector-block"><div class="label">검증 결과</div><div class="body-copy">{html.escape(_friendly_text(lane['validate_result']))}</div></div>
              </div>
              <div class="inspector-block"><div class="label">보고 결과</div><div class="body-copy">{html.escape(_friendly_text(lane['report_result']))}</div></div>
              <div class="meta">다른 lane과의 차이: {html.escape(_friendly_text(lane.get('diff_note') or 'none'))}</div>
            </div>
            """
        )
    body = f"""
    <div class="page">
      <section class="hero">
        <div class="kicker">VectorFL Paper</div>
        <div class="section-head"><h1>실행 비교</h1><div class="mono">실행 경로를 나란히 보기</div></div>
        <div class="meta">같은 recall 기준과 같은 파이프라인 위에서 lane별 결과가 어떻게 달라지는지 비교하는 페이지입니다.</div>
      </section>
      <div class="frame with-right">
        {_render_nav(data, 'lane-runs')}
        <main class="stack">
          {supervisor_checkpoint}
          <section class="panel">
            <div class="section-head"><div><div class="kicker">1. 비교 기준</div><h2>{html.escape(lane_runs['selected_line'])}</h2></div><div class="mono">같은 실행 순서</div></div>
            <div class="chip-row">{''.join(_chip(item) for item in lane_runs['fixed_pipeline'])}</div>
            <div class="meta">{html.escape(lane_runs['lane_rule_note'])}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">2. lane별 결과</div><h2>Read / Apply / Search / Validate / Report</h2></div><div class="mono">{len(lane_runs['lanes'])} lanes</div></div>
            <div class="list-shell">{''.join(lane_rows)}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">3. 비교를 떠받치는 근거</div><h2>lane 비교가 왜 필요한지 보여주는 근거 묶음</h2></div><div class="mono">{len(lane_runs.get('evidence_bundles') or [])} bundles</div></div>
            <div class="bundle-grid">{evidence_bundle_cards}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">4. run trace</div><h2>lane 비교 요청과 회신</h2></div><div class="mono">{len(lane_runs.get('run_trace_rows') or [])} traces</div></div>
            <div class="list-shell">{run_trace_rows}</div>
          </section>
        </main>
        <aside class="stack">
          {selection_impact_panel}
          {request_panel}
          <section class="panel soft">
            <div class="kicker">비교 메모</div>
            <div class="body-copy">lane 비교는 독립된 장난감이 아니라 현재 selected line, bundle, compare target을 그대로 들고 가는 병렬 실행면입니다.</div>
          </section>
        </aside>
      </div>
    </div>"""
    return _base_html("VectorFL Operable Surfaces / Lane Runs", data, body)


def render_organs_page(data: Dict[str, Any]) -> str:
    function_process = _render_function_process(data)
    rows = []
    for organ in data["organs"]:
        state_bits = []
        if organ["current"]:
            state_bits.append("현재 팀")
        if organ["next_candidate"]:
            state_bits.append("다음 후보")
        if not state_bits:
            state_bits.append("사용 가능")
        rows.append(
            f"""
            <div class="list-row">
              <div class="entity-row">
                <div class="entity-main">
                  <div class="section-head"><div class="entity-title">{html.escape(organ['label'])}</div><div class="mono">{html.escape(organ['slug'])}</div></div>
                  <div class="entity-sub">{html.escape(organ['summary'] or 'no summary')}</div>
                  <div class="meta">lens={html.escape(organ['lens'])}</div>
                  <div class="meta">관리 CLI={html.escape(organ['managing_cli'])} / paired external={html.escape(organ['paired_external_team'])}</div>
                  <div class="meta">handoff={html.escape(' -> '.join(organ.get('handoff_targets') or ['none']))}</div>
                </div>
                <div class="entity-meta">
                  <div class="chip-row">{''.join(_chip(bit) for bit in state_bits)}</div>
                  <div class="meta">active_cases={organ['active_case_count']} / family={html.escape(str(organ.get('supported_family') or 'unknown'))} / gaps={html.escape(str(organ.get('supported_gap_count') or 0))}</div>
                </div>
                <div class="entity-actions">{_link(organ['detail_href'], '팀 보기')}{_link(organ['editor_href'], '팀 수정', subtle=True)}</div>
              </div>
            </div>
            """
        )
    body = f"""
    <div class="page">
      <section class="hero">
        <div class="kicker">VectorFL Paper</div>
        <div class="section-head"><h1>팀 / 운영 셀</h1><div class="mono">팀 선택, 역할 배정, handoff 구조 보기</div></div>
        <div class="meta">여기는 팀 이름 목록이 아니라 어떤 셀이 어떤 lens로 읽고, 어떤 CLI가 관리하고, 누구에게 넘기며, 어떤 외부 짝 셀을 갖는지 정하는 운영면입니다.</div>
      </section>
      <div class="frame">
        {_render_nav(data, 'organs')}
        <main class="stack">
          {function_process}
          <section class="panel">
            <div class="metric-strip">
              <div class="metric"><div class="kicker">팀 수</div><div class="metric-value">{len(data['organs'])}</div><div class="meta">현재 등록된 기능 팀</div></div>
              <div class="metric"><div class="kicker">현재 팀</div><div class="metric-value" style="font-size:14px;">{html.escape(next((o['label'] for o in data['organs'] if o['current']), 'none'))}</div><div class="meta">지금 맡고 있는 팀</div></div>
              <div class="metric"><div class="kicker">다음 후보</div><div class="metric-value" style="font-size:14px;">{html.escape(next((o['label'] for o in data['organs'] if o['next_candidate']), 'none'))}</div><div class="meta">다음으로 볼 수 있는 팀</div></div>
              <div class="metric"><div class="kicker">수정 bundle</div><div class="metric-value">4</div><div class="meta">ROLE / HANDOFF / CAUTION / RETURN</div></div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">1. 팀 목록</div><h2>지금 다루는 운영 셀</h2></div><div class="mono">lens / cli / handoff</div></div>
            <div class="list-shell">{''.join(rows)}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">2. 기능 수행 과정</div><h2>누가 위에 있느냐보다 무엇을 어떤 순서로 하느냐</h2></div><div class="mono">function process</div></div>
            <div class="summary-grid">
              <div class="inspector-block"><div class="label">intake</div><div class="body-copy">먼저 source를 확인하고 intake 방식과 bundle/reference 생성 여부를 고릅니다.</div></div>
              <div class="inspector-block"><div class="label">selection</div><div class="body-copy">그다음 selected line, bundle, compare target을 명시적으로 고정합니다.</div></div>
              <div class="inspector-block"><div class="label">interpretation / handoff</div><div class="body-copy">현재 organ은 이 선택을 어떤 읽기 단계에서 다룰지 결정하고 다음 후보를 정합니다.</div></div>
              <div class="inspector-block"><div class="label">worker / trace return</div><div class="body-copy">마지막으로 worker 요청을 payload로 만들고 결과를 trace와 return loop로 다시 surface 안에 귀속시킵니다.</div></div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">3. 확장 슬롯</div><h2>새 팀을 붙일 자리</h2></div><div class="mono">paired internal/external growth</div></div>
            <div class="entity-actions">{_link('organ-registry.html', '팀 관리 열기')}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">assignment grammar</div><h2>팀을 늘릴 때 같이 정해야 하는 것</h2></div><div class="mono">team != label</div></div>
            <div class="summary-grid">
              <div class="inspector-block"><div class="label">team lens</div><div class="body-copy">무엇을 우선 읽고 무엇을 일부러 덜 보는지</div></div>
              <div class="inspector-block"><div class="label">managing cli</div><div class="body-copy">Codex / Gemini 중 누가 이 팀을 관리하고 보고를 만드는지</div></div>
              <div class="inspector-block"><div class="label">handoff target</div><div class="body-copy">다음에 누구에게 넘기고 어떤 조건에서 넘기는지</div></div>
              <div class="inspector-block"><div class="label">human report</div><div class="body-copy">감독자가 바로 판단할 수 있는 보고 형식을 같이 고정합니다.</div></div>
            </div>
          </section>
        </main>
      </div>
    </div>"""
    return _base_html("VectorFL Operable Surfaces / Organs", data, body)


def render_organ_registry_page(data: Dict[str, Any]) -> str:
    registry = data["organ_registry"]
    worker_bridge = data["worker_bridge"]
    request = worker_bridge.get("current_request") or {}
    slot_rows = "".join(
        f'<div class="list-row"><div class="entity-row"><div class="entity-main"><div class="entity-title">{html.escape(slot["name"])}</div><div class="entity-sub">상태: {html.escape(slot["status"])}</div><div class="meta">새 팀은 md 계약, managing cli, handoff target, human report 형식을 같이 고정해야 합니다.</div></div><div class="entity-actions">{_link("organs.html", "팀 목록으로 돌아가기", subtle=True)}</div></div></div>'
        for slot in registry["available_extension_slots"]
    )
    organ_rows = "".join(
        f'<div class="check-row"><div><strong>{html.escape(organ["label"])}</strong><div class="meta">{html.escape(organ["slug"])} / cli={html.escape(organ["managing_cli"])} / handoff={html.escape(" -> ".join(organ.get("handoff_targets") or ["none"]))}</div></div><input type="checkbox" checked></div>'
        for organ in registry["organ_rows"]
    )
    body = f"""
    <div class="page">
      <section class="hero">
        <div class="kicker">VectorFL Paper</div>
        <div class="section-head"><h1>팀 계약 / 설정</h1><div class="mono">팀 계약, CLI ownership, 확장 슬롯</div></div>
        <div class="meta">통합 엔진으로 커지려면 팀을 켜고 끄는 수준이 아니라 md 계약, managing CLI, handoff target, paired external team을 함께 관리해야 합니다.</div>
      </section>
      <div class="frame with-right">
        {_render_nav(data, 'organ-registry')}
        <main class="stack">
          <section class="panel">
            <div class="section-head"><div><div class="kicker">1. 현재 켜진 팀</div><h2>지금 사용 중인 팀</h2></div><div class="mono">{len(registry['organ_rows'])} teams</div></div>
            <div class="check-list">{organ_rows}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">2. 빈 슬롯</div><h2>앞으로 붙일 팀과 역할</h2></div><div class="mono">표면에서 미리 계획</div></div>
            <div class="list-shell">{slot_rows}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">3. registry seam</div><h2>CLI와 팀 계약이 만나는 자리</h2></div><div class="mono">small seam first</div></div>
            <div class="summary-grid">
              <div class="inspector-block">
                <div class="label">current adapter seam</div>
                <strong>{html.escape(str(request.get('target_adapter') or 'none'))}</strong>
                <div class="body-copy">{html.escape(_friendly_text(request.get('intent') or ''))}</div>
              </div>
              <div class="inspector-block">
                <div class="label">why registry is small first</div>
                <div class="body-copy">처음부터 완전한 plugin framework를 만들지 않고, 팀 선택 -> managing cli -> payload -> trace -> return 귀속만 먼저 엽니다.</div>
              </div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">setup flow</div><h2>새 팀을 추가할 때 밟는 순서</h2></div><div class="mono">team -> cli -> contract -> issue loop</div></div>
            <div class="summary-grid">
              <div class="inspector-block"><div class="label">1. team 선택</div><div class="body-copy">어떤 lens와 어떤 내부 기능을 맡길 팀인지 먼저 정합니다.</div></div>
              <div class="inspector-block"><div class="label">2. managing cli 지정</div><div class="body-copy">Codex / Gemini 중 누가 이 팀을 실제로 관리할지 붙입니다.</div></div>
              <div class="inspector-block"><div class="label">3. md contract 연결</div><div class="body-copy">ROLE / HANDOFF / CAUTION / RETURN을 team contract로 고정합니다.</div></div>
              <div class="inspector-block"><div class="label">4. issue loop 연결</div><div class="body-copy">결과가 inbox, approvals, trace로 어떻게 돌아오는지까지 같이 정합니다.</div></div>
            </div>
          </section>
        </main>
        <aside class="stack">
          <section class="panel soft">
            <div class="kicker">공통 bundle 문법</div>
            <div class="chip-row">{''.join(_chip(mode) for mode in registry['bundle_modes'])}</div>
            <div class="meta">새 팀도 먼저 이 bundle 문법을 그대로 물려받아야 합니다.</div>
          </section>
          <section class="panel soft">
            <div class="kicker">실제 계약 작업공간</div>
            <div class="tool-row">
              {_link('contracts-workspace.html', '계약 작업공간 열기')}
              {_link('cli-setup.html', 'CLI 설정 보기', subtle=True)}
            </div>
            <div class="meta">설명만 보는 것이 아니라, 어떤 md 파일을 어떤 팀이 쓰는지 바로 이어서 볼 수 있게 분리합니다.</div>
          </section>
        </aside>
      </div>
    </div>"""
    return _base_html("VectorFL Operable Surfaces / Organ Registry", data, body)


def render_contracts_workspace_page(data: Dict[str, Any]) -> str:
    workspace = data["contracts_workspace"]
    engine_state_panel = _render_engine_state(data["engine_state"])
    current_selection_panel = _render_current_operating_selection(data["current_operating_selection"])
    selected_contract_path = (data.get("current_operating_selection") or {}).get("selected_contract_path")
    rows = "".join(
        f'<div class="list-row"><div class="entity-row"><div class="entity-main"><div class="entity-title">{html.escape(item["label"])}</div><div class="entity-sub">scope={html.escape(item["scope"])}</div><div class="meta">{html.escape(item["why"])}</div><div class="mono">{html.escape(item["path"])}</div></div><div class="entity-meta"><div class="chip-row">{_chip("current source") if item["path"] == selected_contract_path else ""}</div><div class="meta">used by</div><div class="chip-row">{"".join(_chip(team) for team in item.get("used_by") or [])}</div></div></div></div>'
        for item in workspace.get("contract_rows") or []
    ) or '<div class="list-row"><div class="entity-title">등록된 contract가 아직 없습니다</div></div>'
    draft_rows = "".join(
        f'<div class="list-row"><div class="entity-row"><div class="entity-main"><div class="entity-title">{html.escape(item["label"])}</div><div class="entity-sub">source={html.escape(item["source_contract"])} / team={html.escape(item.get("team_slug") or "unknown")}</div><div class="meta">{html.escape(item["purpose"])}</div><div class="mono">{html.escape(item["path"])}</div></div><div class="entity-meta"><div class="chip-row">{_chip("current draft") if item["path"] == selected_contract_path else ""}</div></div></div></div>'
        for item in workspace.get("draft_targets") or []
    ) or '<div class="list-row"><div class="entity-title">등록된 draft target이 아직 없습니다</div></div>'
    body = f"""
    <div class="page">
      <section class="hero">
        <div class="kicker">VectorFL Paper</div>
        <div class="section-head"><h1>계약 작업공간</h1><div class="mono">md contract paths / team usage / report rules</div></div>
        <div class="meta">이 페이지는 설명면이 아니라, 어떤 팀이 어떤 md 계약을 실제로 읽어야 하는지 고정하는 준비면입니다. 통합 운영은 여기서 contract path를 먼저 잡아야 시작됩니다.</div>
      </section>
      <div class="frame with-right">
        {_render_nav(data, 'contracts-workspace')}
        <main class="stack">
          {engine_state_panel}
          {current_selection_panel}
          <section class="panel">
            <div class="section-head"><div><div class="kicker">contract registry</div><h2>실제로 붙일 md 계약 파일</h2></div><div class="mono">{len(workspace.get('contract_rows') or [])} contracts</div></div>
            <div class="list-shell">{rows}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">workspace rules</div><h2>왜 여기서 먼저 계약을 잡아야 하는가</h2></div><div class="mono">contract before launch</div></div>
            <div class="summary-grid">
              {''.join(f'<div class="inspector-block"><div class="body-copy">{html.escape(rule)}</div></div>' for rule in workspace.get("workspace_rules") or [])}
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">draft targets</div><h2>바로 손대기 시작할 계약 draft slots</h2></div><div class="mono">runtime manifests</div></div>
            <div class="list-shell">{draft_rows}</div>
          </section>
        </main>
        <aside class="stack">
          <section class="panel soft">
            <div class="kicker">바로 이어서 보기</div>
            <div class="tool-row">
              {_link('organ-registry.html', '팀 계약 / 설정')}
              {_link('cli-setup.html', 'CLI 설정 작업공간', subtle=True)}
            </div>
          </section>
        </aside>
      </div>
    </div>"""
    return _base_html("VectorFL Operable Surfaces / Contracts Workspace", data, body)


def render_cli_setup_page(data: Dict[str, Any]) -> str:
    workspace = data["cli_setup_workspace"]
    engine_state_panel = _render_engine_state(data["engine_state"])
    current_selection_panel = _render_current_operating_selection(data["current_operating_selection"])
    selected_launch_path = (data.get("current_operating_selection") or {}).get("selected_launch_manifest_path")
    rows = "".join(
        f'<div class="list-row"><div class="entity-row"><div class="entity-main"><div class="entity-title">{html.escape(item["label"])}</div><div class="entity-sub">adapter={html.escape(item["adapter_type"])} / command={html.escape(item["command"])}</div><div class="meta">args={html.escape(item["args"])} / workdir={html.escape(item["working_directory"])}</div><div class="meta">contract={html.escape(item["contract_ref"])} / launch route={html.escape(item["launch_route"])}</div></div><div class="entity-meta"><div class="chip-row">{_chip(str(item.get("env_status") or "unknown"))}</div><div class="meta">managed teams</div><div class="chip-row">{"".join(_chip(team) for team in item.get("managed_teams") or [])}</div></div></div><div class="body-copy">{html.escape(item["env_summary"])}</div></div>'
        for item in workspace.get("tool_rows") or []
    ) or '<div class="list-row"><div class="entity-title">등록된 CLI tool이 아직 없습니다</div></div>'
    manifest_rows = "".join(
        f'<div class="list-row"><div class="entity-row"><div class="entity-main"><div class="entity-title">{html.escape(item["label"])}</div><div class="entity-sub">adapter={html.escape(item["adapter_type"])} / command={html.escape(item["command"])} / lane={html.escape(item.get("lane_slug") or "unknown")}</div><div class="meta">contract={html.escape(item["contract_ref"])}</div><div class="mono">{html.escape(item["path"])}</div></div><div class="entity-meta"><div class="chip-row">{_chip("current launch") if item["path"] == selected_launch_path else ""}</div></div></div></div>'
        for item in workspace.get("launch_manifests") or []
    ) or '<div class="list-row"><div class="entity-title">등록된 launch manifest가 아직 없습니다</div></div>'
    body = f"""
    <div class="page">
      <section class="hero">
        <div class="kicker">VectorFL Paper</div>
        <div class="section-head"><h1>CLI 설정 작업공간</h1><div class="mono">command / args / env / contract / launch</div></div>
        <div class="meta">이 페이지는 lane 설명면이 아니라, 어떤 CLI를 어떤 command와 args로 붙이고, 어느 workdir에서, 어떤 contract를 읽게 할지 준비하는 실제 setup 면입니다.</div>
      </section>
      <div class="frame with-right">
        {_render_nav(data, 'cli-setup')}
        <main class="stack">
          {engine_state_panel}
          {current_selection_panel}
          <section class="panel">
            <div class="section-head"><div><div class="kicker">tool registry</div><h2>실제로 붙일 CLI 도구</h2></div><div class="mono">{len(workspace.get('tool_rows') or [])} tools</div></div>
            <div class="list-shell">{rows}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">launch sequence</div><h2>실제 launch 전에 밟는 순서</h2></div><div class="mono">team -> contract -> env -> launch</div></div>
            <div class="chip-row">{''.join(_chip(step) for step in workspace.get("launch_sequence") or [])}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">workspace rules</div><h2>왜 이게 단순 lane 설명이 아니어야 하는가</h2></div><div class="mono">operable setup</div></div>
            <div class="summary-grid">
              {''.join(f'<div class="inspector-block"><div class="body-copy">{html.escape(rule)}</div></div>' for rule in workspace.get("workspace_rules") or [])}
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">launch manifests</div><h2>실제 실행 준비 파일 자리</h2></div><div class="mono">launch-ready artifacts</div></div>
            <div class="list-shell">{manifest_rows}</div>
          </section>
        </main>
        <aside class="stack">
          <section class="panel soft">
            <div class="kicker">바로 이어서 보기</div>
            <div class="tool-row">
              {_link('lanes.html', 'CLI / 어댑터')}
              {_link('contracts-workspace.html', '계약 작업공간', subtle=True)}
            </div>
          </section>
        </aside>
      </div>
    </div>"""
    return _base_html("VectorFL Operable Surfaces / CLI Setup Workspace", data, body)


def render_engine_overview_page(data: Dict[str, Any]) -> str:
    overview = data["engine_overview"]
    engine_state_panel = _render_engine_state(data["engine_state"])
    program_rows = "".join(
        f'<div class="list-row"><div class="entity-row"><div class="entity-main"><div class="entity-title">{html.escape(item["name"])}</div><div class="entity-sub">{html.escape(item["mission"])}</div><div class="meta">primary runtime={html.escape(item.get("primary_runtime") or "not fixed")}</div><div class="meta">output route={html.escape(item["output_route"])}</div></div><div class="entity-meta"><div class="chip-row">{_chip(item["status"])}</div><div class="meta">teams</div><div class="chip-row">{"".join(_chip(team) for team in item.get("teams") or [])}</div><div class="meta">cli</div><div class="chip-row">{"".join(_chip(cli) for cli in item.get("cli_stack") or [])}</div></div></div></div>'
        for item in overview.get("active_programs") or []
    ) or '<div class="list-row"><div class="entity-title">등록된 프로그램이 아직 없습니다</div></div>'
    body = f"""
    <div class="page">
      <section class="hero">
        <div class="kicker">VectorFL Paper</div>
        <div class="section-head"><h1>엔진 개요</h1><div class="mono">shared line supply / multi-program orchestration</div></div>
        <div class="meta">{html.escape(overview.get("mission") or "")}</div>
      </section>
      <div class="frame with-right">
        {_render_nav(data, 'engine-overview')}
        <main class="stack">
          {engine_state_panel}
          {_render_paper_proper_bridge_panel(data, mode='overview')}
          <section class="panel">
            <div class="section-head"><div><div class="kicker">core loop</div><h2>이 엔진이 반복해야 하는 기본 순서</h2></div><div class="mono">line -> teams -> cli -> return</div></div>
            <div class="chip-row">{''.join(_chip(step) for step in overview.get("core_loop") or [])}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">active programs</div><h2>지금 이 엔진 위에 올라갈 프로그램들</h2></div><div class="mono">{len(overview.get('active_programs') or [])} programs</div></div>
            <div class="list-shell">{program_rows}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">shared supply</div><h2>모든 프로그램이 같이 먹는 내부 공급원</h2></div><div class="mono">line-centered memory</div></div>
            <div class="chip-row">{''.join(_chip(item) for item in overview.get("shared_supply") or [])}</div>
          </section>
        </main>
        <aside class="stack">
          <section class="panel soft">
            <div class="kicker">감독 규칙</div>
            <div class="summary-grid">
              {''.join(f'<div class="inspector-block"><div class="body-copy">{html.escape(rule)}</div></div>' for rule in overview.get("supervisor_rules") or [])}
            </div>
          </section>
          <section class="panel soft">
            <div class="kicker">바로 이어서 보기</div>
            <div class="tool-row">
              {_link('program-workspaces.html', '프로그램 워크스페이스')}
              {_link('agent-mcp-control.html', '에이전트 / MCP 운용', subtle=True)}
            </div>
          </section>
        </aside>
      </div>
    </div>"""
    return _base_html("VectorFL Operable Surfaces / Engine Overview", data, body)


def render_program_workspaces_page(data: Dict[str, Any]) -> str:
    workspace = data["program_workspaces"]
    engine_state_panel = _render_engine_state(data["engine_state"])
    rows = "".join(
        f'<div class="list-row"><div class="entity-row"><div class="entity-main"><div class="entity-title">{html.escape(item["label"])}</div><div class="entity-sub">{html.escape(item["objective"])}</div><div class="meta">primary runtime={html.escape(item.get("primary_runtime") or "not fixed")}</div><div class="meta">line supply={html.escape(", ".join(item.get("line_supply") or []))}</div><div class="meta">artifacts={html.escape(", ".join(item.get("current_artifacts") or []))}</div></div><div class="entity-meta"><div class="chip-row">{_chip(item["status"])}</div><div class="meta">teams</div><div class="chip-row">{"".join(_chip(team) for team in item.get("team_stack") or [])}</div><div class="meta">cli</div><div class="chip-row">{"".join(_chip(cli) for cli in item.get("cli_stack") or [])}</div></div></div></div>'
        for item in workspace.get("workspace_rows") or []
    ) or '<div class="list-row"><div class="entity-title">등록된 워크스페이스가 아직 없습니다</div></div>'
    manifest_rows = "".join(
        f'<div class="list-row"><div class="entity-title">{html.escape(item["label"])}</div><div class="entity-sub">{html.escape(item["purpose"])}</div><div class="mono">{html.escape(item["path"])}</div></div>'
        for item in workspace.get("manifest_rows") or []
    ) or '<div class="list-row"><div class="entity-title">등록된 workspace manifest가 아직 없습니다</div></div>'
    body = f"""
    <div class="page">
      <section class="hero">
        <div class="kicker">VectorFL Paper</div>
        <div class="section-head"><h1>프로그램 워크스페이스</h1><div class="mono">one engine / many program loops</div></div>
        <div class="meta">이 페이지는 팀 목록이 아니라, 서로 다른 목적의 프로그램들이 같은 내부 line 공급원을 공유하면서 어떻게 병렬 운영될지를 보여주는 워크스페이스 면입니다.</div>
      </section>
      <div class="frame with-right">
        {_render_nav(data, 'program-workspaces')}
        <main class="stack">
          {engine_state_panel}
          <section class="panel">
            <div class="section-head"><div><div class="kicker">workspace registry</div><h2>프로그램 단위 운영 셀</h2></div><div class="mono">{len(workspace.get('workspace_rows') or [])} workspaces</div></div>
            <div class="list-shell">{rows}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">workspace rules</div><h2>왜 프로그램 단위 면이 따로 필요한가</h2></div><div class="mono">shared supply / different outputs</div></div>
            <div class="summary-grid">
              {''.join(f'<div class="inspector-block"><div class="body-copy">{html.escape(rule)}</div></div>' for rule in workspace.get("workspace_rules") or [])}
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">workspace manifests</div><h2>프로그램 단위 저장 파일 자리</h2></div><div class="mono">program runtime manifests</div></div>
            <div class="list-shell">{manifest_rows}</div>
          </section>
        </main>
        <aside class="stack">
          <section class="panel soft">
            <div class="kicker">바로 이어서 보기</div>
            <div class="tool-row">
              {_link('engine-overview.html', '엔진 개요')}
              {_link('organs.html', '팀 / 운영 셀', subtle=True)}
            </div>
          </section>
        </aside>
      </div>
    </div>"""
    return _base_html("VectorFL Operable Surfaces / Program Workspaces", data, body)


def render_agent_mcp_control_page(data: Dict[str, Any]) -> str:
    control = data["agent_mcp_control"]
    engine_state_panel = _render_engine_state(data["engine_state"])
    rows = "".join(
        f'<div class="list-row"><div class="entity-row"><div class="entity-main"><div class="entity-title">{html.escape(item["label"])}</div><div class="entity-sub">role={html.escape(item.get("role") or "unassigned")} / type={html.escape(item["type"])} / entry={html.escape(item["entry"])}</div><div class="meta">contract={html.escape(item["contract_link"])}</div><div class="meta">return route={html.escape(item["return_route"])}</div></div><div class="entity-meta"><div class="chip-row">{_chip(item["mode"])}</div><div class="meta">owns</div><div class="chip-row">{"".join(_chip(owner) for owner in item.get("owns") or [])}</div></div></div></div>'
        for item in control.get("runtime_rows") or []
    ) or '<div class="list-row"><div class="entity-title">등록된 runtime row가 아직 없습니다</div></div>'
    manifest_rows = "".join(
        f'<div class="list-row"><div class="entity-title">{html.escape(item["label"])}</div><div class="entity-sub">{html.escape(item["purpose"])}</div><div class="mono">{html.escape(item["path"])}</div></div>'
        for item in control.get("manifest_rows") or []
    ) or '<div class="list-row"><div class="entity-title">등록된 runtime binding이 아직 없습니다</div></div>'
    body = f"""
    <div class="page">
      <section class="hero">
        <div class="kicker">VectorFL Paper</div>
        <div class="section-head"><h1>에이전트 / MCP 운용</h1><div class="mono">runtime owners / connector intent / return routes</div></div>
        <div class="meta">에이전트와 MCP는 바깥 도구가 아니라, 프로그램 워크스페이스에 귀속된 실행층입니다. 여기서는 누가 어떤 프로그램을 맡고 무엇을 다시 공간에 돌려보내는지 봅니다.</div>
      </section>
      <div class="frame with-right">
        {_render_nav(data, 'agent-mcp-control')}
        <main class="stack">
          {engine_state_panel}
          {_render_paper_proper_bridge_panel(data, mode='assignment')}
          <section class="panel">
            <div class="section-head"><div><div class="kicker">runtime registry</div><h2>지금 이 엔진에서 다룰 실행층</h2></div><div class="mono">{len(control.get('runtime_rows') or [])} runtimes</div></div>
            <div class="list-shell">{rows}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">control rules</div><h2>왜 runtime owner가 따로 보여야 하는가</h2></div><div class="mono">runtime as controlled layer</div></div>
            <div class="summary-grid">
              {''.join(f'<div class="inspector-block"><div class="body-copy">{html.escape(rule)}</div></div>' for rule in control.get("control_rules") or [])}
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">runtime bindings</div><h2>에이전트 / MCP 저장 파일 자리</h2></div><div class="mono">runtime binding manifests</div></div>
            <div class="list-shell">{manifest_rows}</div>
          </section>
        </main>
        <aside class="stack">
          <section class="panel soft">
            <div class="kicker">바로 이어서 보기</div>
            <div class="tool-row">
              {_link('cli-setup.html', 'CLI 설정 작업공간')}
              {_link('program-workspaces.html', '프로그램 워크스페이스', subtle=True)}
            </div>
          </section>
        </aside>
      </div>
    </div>"""
    return _base_html("VectorFL Operable Surfaces / Agent MCP Control", data, body)


def render_lane_detail_page(data: Dict[str, Any], lane_slug: str) -> str:
    lane = next(item for item in data["lanes"]["lane_rows"] if item["slug"] == lane_slug)
    managed_teams = ", ".join(lane.get("managed_team_slugs") or []) or "none"
    body = f"""
    <div class="page">
      <section class="hero">
        <div class="kicker">VectorFL Paper</div>
        <div class="section-head"><h1>{html.escape(lane['label'])}</h1><div class="mono">CLI / lane 상세</div></div>
        <div class="meta">이 페이지는 이 lane이 어떤 CLI에 속하고, 어떤 모델을 쓰고, 어떤 팀을 맡고, 결과를 어디로 돌려보내는지 확인하는 운용면입니다.</div>
      </section>
      <div class="frame">
        {_render_nav(data, 'lanes')}
        <main class="stack">
          <section class="panel">
            <div class="section-head"><div><div class="kicker">1. lane 상태</div><h2>{html.escape(lane['label'])}</h2></div><div class="mono">{html.escape(lane['provider_model'])}</div></div>
            <div class="chip-row">{_chip('활성' if lane['enabled'] else '비활성')}{_chip(lane['status'])}{_chip(lane['output_schema'])}</div>
            <div class="meta">provider={html.escape(lane['provider'])} / model={html.escape(lane['model'])} / cli={html.escape(lane['owning_cli'])}</div>
            <div class="meta">timeout={html.escape(lane['timeout'])} / budget={html.escape(lane['budget'])} / 맡은 팀={html.escape(managed_teams)}</div>
            <div class="body-copy">{html.escape(lane['notes'])}</div>
            <div class="inspector-block"><div class="label">payload policy</div><div class="body-copy">{html.escape(lane['payload_policy'])}</div><div class="label">return route</div><div class="body-copy">{html.escape(lane['return_route'])}</div></div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">2. 이 lane의 묶음</div><h2>ROLE / TASK / CAUTION</h2></div><div class="mono">{html.escape(lane['contract_ref'])}</div></div>
            <div class="bundle-grid">
              <div class="bundle-card"><div class="label">ROLE</div><div class="body-copy">{html.escape(lane['role_md'])}</div></div>
              <div class="bundle-card"><div class="label">TASK</div><div class="body-copy">{html.escape(lane['task_md'])}</div></div>
              <div class="bundle-card"><div class="label">CAUTION</div><div class="body-copy">{html.escape(lane['caution_md'])}</div></div>
            </div>
          </section>
        </main>
      </div>
    </div>"""
    return _base_html(f"VectorFL Operable Surfaces / {lane['label']}", data, body)


def render_lane_editor_page(data: Dict[str, Any], lane_slug: str) -> str:
    lane = next(item for item in data["lanes"]["lane_rows"] if item["slug"] == lane_slug)
    managed_teams = ", ".join(lane.get("managed_team_slugs") or []) or "none"
    body = f"""
    <div class="page">
      <section class="hero">
        <div class="kicker">VectorFL Paper</div>
        <div class="section-head"><h1>{html.escape(lane['label'])} 수정</h1><div class="mono">CLI 연결 설정</div></div>
        <div class="meta">여기서는 provider, model, 관리 CLI, payload 정책, 팀 소유권을 읽고 조정합니다. 다만 공통 파이프라인 순서는 여기서 바꾸지 않습니다.</div>
      </section>
      <div class="frame with-right">
        {_render_nav(data, 'lanes')}
        <main class="stack">
          <section class="panel">
            <div class="section-head"><div><div class="kicker">1. lane 설정</div><h2>{html.escape(lane['label'])}</h2></div><div class="mono">{html.escape(lane['provider_model'])}</div></div>
            <div class="form-grid">
              <div class="field"><label>lane 이름</label><input value="{html.escape(lane['label'])}" readonly></div>
              <div class="field"><label>adapter type</label><input value="{html.escape(lane['adapter_type'])}" readonly></div>
              <div class="field"><label>provider / model</label><input value="{html.escape(lane['provider_model'])}" readonly></div>
              <div class="field"><label>관리 CLI</label><input value="{html.escape(lane['owning_cli'])}" readonly></div>
              <div class="field"><label>맡은 팀</label><input value="{html.escape(managed_teams)}" readonly></div>
              <div class="field"><label>timeout</label><input value="{html.escape(lane['timeout'])}" readonly></div>
              <div class="field"><label>budget</label><input value="{html.escape(lane['budget'])}" readonly></div>
              <div class="field"><label>enabled</label><input value="{html.escape('true' if lane['enabled'] else 'false')}" readonly></div>
              <div class="field"><label>출력 형식</label><input value="{html.escape(lane['output_schema'])}" readonly></div>
              <div class="field"><label>결과 귀속</label><input value="{html.escape(lane['return_route'])}" readonly></div>
              <div class="field"><label>command</label><input value="{html.escape(lane['command'])}" readonly></div>
              <div class="field"><label>args</label><input value="{html.escape(lane['args'])}" readonly></div>
              <div class="field"><label>working directory</label><input value="{html.escape(lane['working_directory'])}" readonly></div>
              <div class="field"><label>env status</label><input value="{html.escape(lane['env_status'])}" readonly></div>
              <div class="field"><label>adapter test</label><input value="{html.escape(lane['adapter_test'])}" readonly></div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">2. instruction blocks</div><h2>Role / Task / Caution</h2></div><div class="mono">수정 가능한 lane 설정</div></div>
            <div class="field"><label>Role MD</label><textarea readonly>{html.escape(lane['role_md'])}</textarea></div>
            <div class="field"><label>Task MD</label><textarea readonly>{html.escape(lane['task_md'])}</textarea></div>
            <div class="field"><label>Caution MD</label><textarea readonly>{html.escape(lane['caution_md'])}</textarea></div>
            <div class="field"><label>Payload Policy</label><textarea readonly>{html.escape(lane['payload_policy'])}</textarea></div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">3. runtime policy</div><h2>승인, 샌드박스, 검색 경계</h2></div><div class="mono">form-like runtime config</div></div>
            <div class="form-grid">
              <div class="field"><label>approvals policy</label><input value="{html.escape(lane['approvals_policy'])}" readonly></div>
              <div class="field"><label>sandbox policy</label><input value="{html.escape(lane['sandbox_policy'])}" readonly></div>
              <div class="field"><label>search policy</label><input value="{html.escape(lane['search_policy'])}" readonly></div>
              <div class="field"><label>contract ref</label><input value="{html.escape(lane['contract_ref'])}" readonly></div>
            </div>
            <label class="field"><span class="label">environment summary</span><textarea readonly>{html.escape(lane['env_summary'])}</textarea></label>
          </section>
        </main>
        <aside class="stack">
          <section class="panel soft">
            <div class="kicker">가능한 작업</div>
            <div class="entity-actions"><a class="button subtle" href="#">env test</a><a class="button subtle" href="#">reload adapter</a><a class="button subtle" href="#">lane 끄기</a></div>
          </section>
          <section class="panel soft">
            <div class="kicker">경계 규칙</div>
            <div class="body-copy">lane 수정은 provider, role, task, caution, budget를 바꿀 수 있지만, 상단 판단권과 고정된 하단 파이프라인 순서는 바꾸지 않습니다.</div>
          </section>
        </aside>
      </div>
    </div>"""
    return _base_html(f"VectorFL Operable Surfaces / {lane['label']} Editor", data, body)


def render_organ_detail_page(data: Dict[str, Any], organ_slug: str) -> str:
    organ = next(item for item in data["organs"] if item["slug"] == organ_slug)
    bundle = organ["bundle"]
    selected_line = data["case_detail"]["selected_line"]
    bundle_cards = []
    for key, label in [("role", "ROLE"), ("handoff", "HANDOFF"), ("caution", "CAUTION"), ("return", "RETURN")]:
        item = bundle[key]
        bundle_cards.append(
            f"""
            <div class="bundle-card">
              <div class="section-head"><div><div class="kicker">{label}</div><h3>{html.escape(item['title'])}</h3></div><div class="mono">{html.escape(item['path'])}</div></div>
              <div class="body-copy">{html.escape(item['summary'] or 'no summary')}</div>
              <div class="code-block">{html.escape(item['content'])}</div>
            </div>
            """
        )
    body = f"""
    <div class="page">
      <section class="hero">
        <div class="kicker">VectorFL Paper</div>
        <div class="section-head"><h1>{html.escape(organ['label'])}</h1><div class="mono">팀 상세</div></div>
        <div class="meta">이 페이지는 한 팀이 어떤 lens로 읽고, 어떤 CLI가 관리하고, 어떤 계약과 handoff로 움직이는지 확인하는 운영 셀 상세면입니다.</div>
      </section>
      <div class="frame">
        {_render_nav(data, 'organs')}
        <main class="stack">
          <section class="panel">
            <div class="section-head"><div><div class="kicker">1. 팀 상태</div><h2>{html.escape(organ['label'])}</h2></div><div class="mono">{html.escape(organ['slug'])}</div></div>
            <div class="chip-row">{_chip('현재 팀') if organ['current'] else ''}{_chip('다음 후보') if organ['next_candidate'] else ''}{_chip(f"활성 case={organ['active_case_count']}")}</div>
            <div class="body-copy">{html.escape(organ['summary'] or 'no summary')}</div>
            <div class="meta">supported_family={html.escape(str(organ.get('supported_family') or 'unknown'))} / supported_gap_count={html.escape(str(organ.get('supported_gap_count') or 0))}</div>
            <div class="inspector-block"><div class="label">team lens</div><div class="body-copy">{html.escape(organ['lens'])}</div><div class="label">managing cli / paired external</div><div class="body-copy">{html.escape(organ['managing_cli'])} / {html.escape(organ['paired_external_team'])}</div><div class="label">handoff target</div><div class="body-copy">{html.escape(' -> '.join(organ.get('handoff_targets') or ['none']))}</div><div class="label">human report format</div><div class="body-copy">{html.escape(organ['human_report_format'])}</div></div>
            <div class="inspector-block">
              <div class="label">지금 연결된 line</div>
              <div class="body-copy">{html.escape(selected_line['raw_value'])}</div>
              <div class="label">차용할 때의 말</div>
              <div class="body-copy">{html.escape(selected_line['adoption_form'])}</div>
            </div>
            <div class="entity-actions">{_link('organs.html', '팀 목록으로 돌아가기')}{_link(f"organ-editor-{organ['slug']}.html", 'bundle 수정', subtle=True)}{_link('case-detail.html', '작업 상세 보기', subtle=True)}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">2. instruction bundle</div><h2>Role / Handoff / Caution / Return</h2></div><div class="mono">md contract blocks</div></div>
            <div class="bundle-grid">{''.join(bundle_cards)}</div>
          </section>
        </main>
      </div>
    </div>"""
    return _base_html(f"VectorFL Operable Surfaces / {organ['label']}", data, body)


def render_organ_editor_page(data: Dict[str, Any], organ_slug: str) -> str:
    organ = next(item for item in data["organs"] if item["slug"] == organ_slug)
    bundle = organ["bundle"]
    selected_line = data["case_detail"]["selected_line"]
    routing = data["case_routing"]
    text_fields = []
    for key, label in [("role", "ROLE"), ("handoff", "HANDOFF"), ("caution", "CAUTION"), ("return", "RETURN")]:
        item = bundle[key]
        text_fields.append(
            f'<label class="field"><span class="label">{label}</span><textarea>{html.escape(item["content"])}</textarea></label>'
        )
    external_rows = """
      <div class="check-row"><div><strong>external-resource-team</strong><div class="meta">optional extension target</div></div><input type="checkbox"></div>
      <div class="check-row"><div><strong>external-program-team</strong><div class="meta">optional extension target</div></div><input type="checkbox"></div>
      <div class="check-row"><div><strong>comparison-team</strong><div class="meta">reserved slot</div></div><input type="checkbox"></div>
    """
    body = f"""
    <div class="page">
      <section class="hero">
        <div class="kicker">VectorFL Paper</div>
        <div class="section-head"><h1>{html.escape(organ['label'])} 수정</h1><div class="mono">팀 계약 / 역할 배정</div></div>
        <div class="meta">여기서는 역할 bundle뿐 아니라 managing CLI, handoff target, 외부 짝 팀, 보고 형식을 함께 다루는 편집면입니다.</div>
      </section>
      <div class="frame with-right">
        {_render_nav(data, 'organs')}
        <main class="stack">
          <section class="panel">
            <div class="section-head"><div><div class="kicker">1. bundle 수정</div><h2>ROLE / HANDOFF / CAUTION / RETURN</h2></div><div class="mono">{html.escape(organ['slug'])}</div></div>
            <div class="form-grid">{''.join(text_fields)}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">2. 운영 설정</div><h2>CLI ownership / handoff / report</h2></div><div class="mono">contract driven</div></div>
            <div class="form-grid">
              <div class="field"><label>관리 CLI</label><input value="{html.escape(organ['managing_cli'])}" readonly></div>
              <div class="field"><label>paired external team</label><input value="{html.escape(organ['paired_external_team'])}" readonly></div>
              <div class="field"><label>handoff target</label><input value="{html.escape(' -> '.join(organ.get('handoff_targets') or ['none']))}" readonly></div>
              <div class="field"><label>human report format</label><input value="{html.escape(organ['human_report_format'])}" readonly></div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">3. 연결 가능한 팀</div><h2>연결 가능한 팀 슬롯</h2></div><div class="mono">나중 확장 자리</div></div>
            <div class="check-list">{external_rows}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">3. 지금 맥락</div><h2>선택된 line / 넘김 기준</h2></div><div class="mono">현재 case와 함께 읽기</div></div>
            <div class="inspector-block">
              <div class="label">선택된 line</div>
              <div class="body-copy">{html.escape(selected_line['raw_value'])}</div>
              <div class="label">검색에 쓸 말</div>
              <div class="body-copy">{html.escape(selected_line['searchable_form'])}</div>
              <div class="label">현재 routing 기준</div>
              <div class="body-copy">{html.escape(str((routing.get('routing_basis') or {}).get('current_material_stage') or 'unknown'))}</div>
            </div>
          </section>
        </main>
        <aside class="stack">
          <section class="panel soft">
            <div class="kicker">현재 상태</div>
            <h3>{html.escape(organ['label'])}</h3>
            <div class="chip-row">{_chip('현재 팀') if organ['current'] else ''}{_chip('다음 후보') if organ['next_candidate'] else ''}{_chip(f"활성 case={organ['active_case_count']}")}</div>
            <div class="body-copy">{html.escape(organ['summary'] or 'no summary')}</div>
            <div class="meta">family={html.escape(str(organ.get('supported_family') or 'unknown'))} / gaps={html.escape(str(organ.get('supported_gap_count') or 0))}</div>
          </section>
          <section class="panel soft">
            <div class="kicker">바로 이어서 보기</div>
            <div class="tool-row">
              {_link(f"organ-detail-{organ['slug']}.html", '팀 상세 보기')}
              {_link('organ-registry.html', '팀 관리 보기', subtle=True)}
            </div>
            <div class="meta">아직 저장 연결은 없지만, 팀을 실제로 수정하는 페이지 클래스는 여기서 분리되어 있습니다.</div>
          </section>
        </aside>
      </div>
    </div>"""
    return _base_html(f"VectorFL Operable Surfaces / {organ['label']} Editor", data, body)


def render_trace_audit_page(data: Dict[str, Any]) -> str:
    worker_request_panel = _render_worker_request_summary(data["worker_bridge"], title="trace에 남는 현재 worker request")
    supervisor_checkpoint = _render_supervisor_checkpoint(
        data,
        page_title="왜 trace를 먼저 읽는가",
        page_reason="이 페이지는 로그를 보는 곳이 아니라, 실행 결과가 실제로 다시 내부로 돌아왔는지와 지금 어떤 reopen / hold 판단이 필요한지 읽는 감사면입니다.",
    )
    rows = []
    for item in data["trace_audit"]["trace_rows"]:
        artifact_href = item.get("artifact_href") or f"../vectorfl_page_shell/semi_live_trace_detail/{_slugify_trace_id(item.get('trace_id') or 'trace-unknown')}.html"
        extra_actions = ""
        current_request = (data.get("worker_bridge") or {}).get("current_request") or {}
        if item.get("trace_id") == current_request.get("request_id"):
            extra_actions = (
                _link(current_request.get("launch_href") or "#", "launch request", subtle=True)
                + _link(current_request.get("export_href") or "#", "payload export", subtle=True)
            )
        rows.append(
            f"""
            <div class="audit-row">
              <div class="section-head"><div><div class="kicker">{html.escape(item.get('trace_kind') or 'trace')}</div><h3>{html.escape(item.get('summary') or 'none')}</h3></div><div class="pill {html.escape(item.get('status') or '')}">{html.escape(item.get('status') or item.get('trace_id') or 'unknown')}</div></div>
              <div class="meta">남아 있는 흔적: {html.escape(_friendly_text(item.get('residue_note') or 'none'))}</div>
              <div class="meta">adapter={html.escape(str(item.get('adapter') or 'surface'))} / started={html.escape(str(item.get('started_at') or 'unknown'))} / ended={html.escape(str(item.get('ended_at') or 'unknown'))}</div>
              <div class="body-copy">{html.escape(_friendly_text(item.get('reentry_hint') or 'none'))}</div>
              <div class="entity-actions">{_link(artifact_href, 'trace 상세 보기')}{_link('external-resources.html', 'worker bridge 보기', subtle=True)}{extra_actions}</div>
            </div>
            """
        )
    issue_update_rows = "".join(
        f'<div class="list-row"><div class="entity-row"><div class="entity-main"><div class="entity-title">{html.escape(str(item.get("issue_title") or "issue"))}</div><div class="entity-sub">owner={html.escape(str(item.get("owner") or "unknown"))}</div><div class="entity-sub">next={html.escape(str(item.get("next_action") or "none"))}</div></div><div class="entity-meta"><div class="chip-row">{_chip(str(item.get("status") or "unknown"))}</div></div><div class="entity-actions">{_link(item.get("href") or "worker-inbox.html", "이슈 열기")}</div></div></div>'
        for item in data["trace_audit"].get("issue_updates") or []
    ) or '<div class="list-row"><div class="entity-title">이슈 업데이트가 아직 없습니다</div></div>'
    approval_cards = "".join(
        f'<div class="bundle-card"><div class="section-head"><div><div class="kicker">approval</div><h3>{html.escape(str(card.get("label") or "approval"))}</h3></div><div class="chip-row">{_chip(str(card.get("status") or "pending"))}</div></div><div class="body-copy">{html.escape(str(card.get("payload_summary") or ""))}</div><div class="meta">requested by {html.escape(str(card.get("requester") or "unknown"))}</div><div class="meta">note: {html.escape(str(card.get("decision_note") or ""))}</div><div class="tool-row">{_link("worker-inbox.html", "open return loop")}{_link("case-routing.html", "reroute", subtle=True)}</div></div>'
        for card in data["trace_audit"].get("approval_cards") or []
    ) or '<div class="bundle-card"><strong>승인 대기 카드가 아직 없습니다</strong></div>'
    body = f"""
    <div class="page">
      <section class="hero">
        <div class="kicker">VectorFL Paper</div>
        <div class="section-head"><h1>이슈 / 감사</h1><div class="mono">남겨진 기록과 판단 보기</div></div>
        <div class="meta">trace는 아래쪽에 잠깐 붙는 로그가 아니라, 무엇이 남았고 무엇을 다시 열어야 하는지 보는 전용 감사 면입니다. 즉 trace는 읽기의 부산물이 아니라, 읽기가 실제로 어떻게 흘렀는지 말해 주는 작업 입입니다.</div>
      </section>
      <div class="frame">
        {_render_nav(data, 'trace-audit')}
        <main class="stack">
          {supervisor_checkpoint}
          {_render_paper_proper_bridge_panel(data, mode='supervise')}
          <section class="panel">
            <div class="metric-strip">
              <div class="metric"><div class="kicker">trace 수</div><div class="metric-value">{len(data['trace_audit']['trace_rows'])}</div><div class="meta">지금 남아 있는 trace</div></div>
              <div class="metric"><div class="kicker">decision anchor</div><div class="metric-value" style="font-size:13px;">{html.escape(str(data['trace_audit'].get('decision_anchor') or 'none'))}</div><div class="meta">현재 기준 anchor</div></div>
              <div class="metric"><div class="kicker">다시 열 단서</div><div class="metric-value">{len(data['trace_audit'].get('reentry_cues') or [])}</div><div class="meta">나중에 다시 볼 신호</div></div>
              <div class="metric"><div class="kicker">남겨둔 residue</div><div class="metric-value">{len(data['trace_audit'].get('residue_emphasis') or [])}</div><div class="meta">아직 평평하게 만들지 않은 흔적</div></div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">issue updates</div><h2>실행과 회신이 만든 현재 이슈들</h2></div><div class="mono">live loop feed</div></div>
            <div class="list-shell">{issue_update_rows}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">approval gate</div><h2>지금 승인 / 보류 판단이 필요한 요청</h2></div><div class="mono">approve / reject / reopen</div></div>
            <div class="body-copy">Paperclip의 approvals처럼, 이 페이지는 단순 로그가 아니라 어떤 요청을 승인하고, 보류하고, 다시 열어야 하는지 판단하는 감사면입니다.</div>
            <div class="bundle-grid">{approval_cards}</div>
            <div class="tool-row">
              {_link('worker-inbox.html', '회신 / reopen 보기')}
              {_link('case-routing.html', '배정 다시 보기', subtle=True)}
            </div>
          </section>
          {worker_request_panel}
          <section class="panel">
            <div class="section-head"><div><div class="kicker">1. 남겨진 흔적</div><h2>append-only trace</h2></div><div class="mono">상세로 들어갈 수 있음</div></div>
            <div class="list-shell">{''.join(rows)}</div>
          </section>
        </main>
      </div>
    </div>"""
    return _base_html("VectorFL Operable Surfaces / Trace Audit", data, body)


def render_worker_inbox_page(data: Dict[str, Any]) -> str:
    inbox = (data.get("worker_bridge") or {}).get("inbox") or {}
    return_board = data.get("worker_return_board") or {}
    supervisor_checkpoint = _render_supervisor_checkpoint(
        data,
        page_title="왜 worker inbox를 따로 읽는가",
        page_reason="이 페이지는 결과를 쌓아두는 보관함이 아니라, request, return, reopen comment가 case를 덮어쓰지 않고 다시 감독 판단으로 돌아오게 만드는 귀속면입니다.",
    )
    worker_request_panel = _render_worker_request_summary(data["worker_bridge"], title="inbox에 귀속된 현재 request", compact=True)
    rows = "".join(
        f'<div class="list-row"><div class="section-head"><div><div class="kicker">{html.escape(str(item.get("target") or "worker"))}</div><h3>{html.escape(str(item.get("headline") or "message"))}</h3></div><div class="pill {html.escape(str(item.get("status") or ""))}">{html.escape(str(item.get("status") or "unknown"))}</div></div><div class="body-copy">{html.escape(_friendly_text(item.get("summary") or ""))}</div><div class="meta">{html.escape(_friendly_text(item.get("comment_hint") or ""))}</div><div class="tool-row">{_link("external-resources.html", "worker bridge로 돌아가기")}{_link("trace-audit.html", "trace 감사 보기", subtle=True)}</div></div>'
        for item in inbox.get("items") or []
    ) or '<div class="list-row"><div class="entity-title">아직 inbox item이 없습니다</div></div>'
    body = f"""
    <div class="page">
      <section class="hero">
        <div class="kicker">VectorFL Paper</div>
        <div class="section-head"><h1>결과 회신</h1><div class="mono">request / return / reopen</div></div>
        <div class="meta">worker 결과와 reopen comment는 case detail을 덮어쓰지 않고 이 inbox surface로 되돌아옵니다.</div>
      </section>
      <div class="frame">
        {_render_nav(data, 'worker-inbox')}
        <main class="stack">
          {supervisor_checkpoint}
          {_render_paper_proper_bridge_panel(data, mode='return')}
          <section class="panel">
            <div class="metric-strip">
              <div class="metric"><div class="kicker">current request</div><div class="metric-value" style="font-size:13px;">{html.escape(str(return_board.get("current_request_id") or "none"))}</div><div class="meta">현재 회신 루프 기준</div></div>
              <div class="metric"><div class="kicker">return route</div><div class="metric-value" style="font-size:13px;">worker return</div><div class="meta">{html.escape(str(return_board.get("return_route") or "none"))}</div></div>
              <div class="metric"><div class="kicker">pending comments</div><div class="metric-value">{html.escape(str(return_board.get("pending_comments") or 0))}</div><div class="meta">감독 판단으로 다시 올 comment 수</div></div>
            </div>
          </section>
          {worker_request_panel}
          <section class="panel">
            <div class="section-head"><div><div class="kicker">inbox</div><h2>{html.escape(str(inbox.get('title') or 'Worker Inbox'))}</h2></div><div class="mono">{len(inbox.get('items') or [])} items</div></div>
            <div class="list-shell">{rows}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">comment loop</div><h2>회신 뒤에 가능한 감독자 행동</h2></div><div class="mono">comment / reopen / redirect</div></div>
            <div class="summary-grid">
              <div class="inspector-block"><div class="label">comment</div><div class="body-copy">결과를 그대로 덮어쓰지 않고, 어떤 부분이 부족한지 코멘트를 남깁니다.</div></div>
              <div class="inspector-block"><div class="label">reopen</div><div class="body-copy">현재 결과가 부족하면 다시 열고 같은 request loop에 연결합니다.</div></div>
              <div class="inspector-block"><div class="label">redirect</div><div class="body-copy">다른 팀이나 다른 CLI에 다시 배정해야 하면 routing으로 돌립니다.</div></div>
              <div class="inspector-block"><div class="label">approve</div><div class="body-copy">충분하면 case detail과 trace에 귀속시키고 다음 단계로 넘깁니다.</div></div>
            </div>
          </section>
          <section class="panel soft">
            <div class="kicker">reopen policy</div>
            <div class="body-copy">{html.escape(_friendly_text(return_board.get("reopen_policy") or ""))}</div>
          </section>
        </main>
      </div>
    </div>"""
    return _base_html("VectorFL Operable Surfaces / Worker Inbox", data, body)


def render_evidence_bundle_detail_page(data: Dict[str, Any], bundle: Dict[str, Any]) -> str:
    source_rows = "".join(
        f'<div class="list-row"><div class="entity-title">{html.escape(str(source))}</div></div>'
        for source in (bundle.get("sources") or [])
    ) or '<div class="list-row"><div class="entity-title">연결된 source가 아직 없습니다</div></div>'
    confident_rows = "".join(_chip(item) for item in (bundle.get("confident_points") or []))
    open_rows = "".join(_chip(item) for item in (bundle.get("open_limits") or []))
    body = f"""
    <div class="page">
      <section class="hero">
        <div class="kicker">VectorFL Paper</div>
        <div class="section-head"><h1>근거 묶음 상세</h1><div class="mono">{html.escape(str(bundle.get('bundle_id') or 'bundle'))}</div></div>
        <div class="meta">이 페이지는 근거 묶음 하나가 어떤 source set에서 나왔고, 무엇을 확실히 말하게 해 주며, 아직 무엇이 비는지 따로 읽는 곳입니다. 즉 bundle도 단순 장식이 아니라 읽기 번역 단위입니다.</div>
      </section>
      <div class="frame with-right">
        {_render_nav(data, 'internal-recall')}
        <main class="stack">
          <section class="panel">
            <div class="section-head"><div><div class="kicker">1. 묶음 요약</div><h2>{html.escape(_friendly_text(bundle.get('theme') or '근거 묶음'))}</h2></div><div class="mono">{html.escape(str(bundle.get('recognition_level') or 'unknown'))}</div></div>
            <div class="inspector-block">
              <div class="label">왜 지금 이 근거를 붙였는가</div>
              <div class="body-copy">{html.escape(_friendly_text(bundle.get('why_it_is_here') or '현재 읽기와 직접 닿는 근거라서 같이 붙였습니다.'))}</div>
            </div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">2. source set</div><h2>이 묶음을 떠받치는 원본들</h2></div><div class="mono">{len(bundle.get('sources') or [])} sources</div></div>
            <div class="list-shell">{source_rows}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">3. 확실히 말할 수 있는 점</div><h2>현재까지 usable한 판단</h2></div><div class="mono">{len(bundle.get('confident_points') or [])} points</div></div>
            <div class="chip-row">{confident_rows}</div>
          </section>
          <section class="panel">
            <div class="section-head"><div><div class="kicker">4. 아직 비는 점</div><h2>더 읽거나 검증해야 하는 부분</h2></div><div class="mono">{len(bundle.get('open_limits') or [])} limits</div></div>
            <div class="chip-row">{open_rows}</div>
          </section>
        </main>
        <aside class="stack">
          <section class="panel soft">
            <div class="kicker">바로 이어서 보기</div>
            <div class="tool-row">
              {_link('internal-recall.html', '내부 자료 다시 보기')}
              {_link('case-inspector.html', 'line 들여다보기', subtle=True)}
              {_link('external-resources.html', '외부 자료 계획', subtle=True)}
            </div>
          </section>
          <section class="panel soft">
            <div class="kicker">메모</div>
            <div class="body-copy">이 묶음은 spec만이 아니라 generated artifact까지 함께 읽어서 만든 근거입니다. 따라서 보기 좋은 문장보다 evidence depth를 먼저 기준으로 봐야 합니다.</div>
          </section>
        </aside>
      </div>
    </div>"""
    return _base_html(f"VectorFL Operable Surfaces / {bundle.get('bundle_id') or 'Evidence Bundle'}", data, body)


def write_vectorfl_operable_surface_set(repo_root: Path, *, output_dir: Path | None = None) -> Dict[str, Any]:
    data = build_vectorfl_operable_surface_state(repo_root)
    root = output_dir or (repo_root / "runtime" / "views" / "vectorfl_operable_surface")
    manifest_root = repo_root / "runtime" / "manifests"
    root.mkdir(parents=True, exist_ok=True)
    manifest_root.mkdir(parents=True, exist_ok=True)

    pages: List[Tuple[str, str, Dict[str, Any]]] = [
        ("engine-overview.html", render_engine_overview_page(data), data),
        ("cases.html", render_cases_page(data), data),
        ("case-detail.html", render_case_detail_page(data), data),
        ("case-inspector.html", render_case_inspector_page(data), data),
        ("line-review.html", render_line_review_page(data), data),
        ("case-routing.html", render_case_routing_page(data), data),
        ("internal-recall.html", render_internal_recall_page(data), data),
        ("external-resources.html", render_external_resources_page(data), data),
        ("lanes.html", render_lanes_page(data), data),
        ("cli-setup.html", render_cli_setup_page(data), data),
        ("agent-mcp-control.html", render_agent_mcp_control_page(data), data),
        ("lane-runs.html", render_lane_runs_page(data), data),
        ("organs.html", render_organs_page(data), data),
        ("organ-registry.html", render_organ_registry_page(data), data),
        ("contracts-workspace.html", render_contracts_workspace_page(data), data),
        ("program-workspaces.html", render_program_workspaces_page(data), data),
        ("trace-audit.html", render_trace_audit_page(data), data),
        ("worker-inbox.html", render_worker_inbox_page(data), data),
    ]

    for idx, _line in enumerate(data["case_detail"]["generated_lines"][:6], start=1):
        pages.append((f"line-detail-{idx}.html", render_line_detail_page(data, idx - 1), data))

    bundle_map: Dict[str, Dict[str, Any]] = {}
    bundle_groups = [
        data["case_detail"].get("evidence_bundles") or [],
        data["case_inspector"].get("evidence_bundles") or [],
        data["case_routing"].get("evidence_bundles") or [],
        data["internal_recall"].get("evidence_bundles") or [],
        data["external_resources"].get("evidence_bundles") or [],
        data["lane_runs"].get("evidence_bundles") or [],
    ]
    for line in data["case_detail"]["generated_lines"][:6]:
        bundle_groups.append(line.get("evidence_bundles") or [])
    for group in bundle_groups:
        for bundle in group:
            bundle_id = str(bundle.get("bundle_id") or "")
            if bundle_id and bundle_id not in bundle_map:
                bundle_map[bundle_id] = bundle

    for bundle_id, bundle in bundle_map.items():
        pages.append((f"evidence-bundle-{bundle_id}.html", render_evidence_bundle_detail_page(data, bundle), {"bundle": bundle, "navigation": data["navigation"], "page_title": data["page_title"]}))

    outputs = []
    for name, markup, payload in pages:
        html_path = root / name
        json_path = root / name.replace(".html", ".json")
        html_path.write_text(markup, encoding="utf-8")
        json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        outputs.append({"name": name, "html_path": str(html_path), "json_path": str(json_path)})

    launch_json_path = root / "worker-request-launch.json"
    launch_json_path.write_text(
        json.dumps(data.get("worker_artifacts", {}).get("launch_request") or {}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    outputs.append({"name": "worker-request-launch.json", "html_path": "", "json_path": str(launch_json_path)})

    export_md_path = root / "worker-request-export.md"
    export_md_path.write_text(str(data.get("worker_artifacts", {}).get("export_packet_markdown") or ""), encoding="utf-8")
    outputs.append({"name": "worker-request-export.md", "html_path": str(export_md_path), "json_path": ""})

    current_selection = data.get("current_operating_selection") or {}
    current_selection_path = repo_root / str(current_selection.get("save_target_path") or "runtime/manifests/vectorfl_operable_surface_current_selection_v0.json")
    current_selection_path.parent.mkdir(parents=True, exist_ok=True)
    current_selection_path.write_text(
        json.dumps(current_selection, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    for item in (data.get("contracts_workspace") or {}).get("draft_targets") or []:
        draft_path = repo_root / str(item.get("path") or "")
        draft_path.parent.mkdir(parents=True, exist_ok=True)
        if not draft_path.exists():
            draft_path.write_text(
                "\n".join(
                    [
                        f"# {item.get('label')}",
                        "",
                        f"- source_contract: `{item.get('source_contract')}`",
                        f"- team_slug: `{item.get('team_slug')}`",
                        f"- purpose: {item.get('purpose')}",
                        "",
                        "## working draft",
                        "아직 수정 내용이 없습니다. 이 파일은 VectorFL Paper에서 실제 계약 초안을 준비하는 slot입니다.",
                    ]
                ),
                encoding="utf-8",
            )

    for item in (data.get("cli_setup_workspace") or {}).get("launch_manifests") or []:
        manifest_path = repo_root / str(item.get("path") or "")
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(
            json.dumps(
                {
                    "label": item.get("label"),
                    "adapter_type": item.get("adapter_type"),
                    "command": item.get("command"),
                    "args": item.get("args"),
                    "contract_ref": item.get("contract_ref"),
                    "lane_slug": item.get("lane_slug"),
                    "is_current_selection": current_selection.get("selected_launch_manifest_path") == item.get("path"),
                    "status": "draft",
                    "note": "This is a launch-ready placeholder manifest generated from the current VectorFL Paper CLI setup workspace.",
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )

    for item in (data.get("program_workspaces") or {}).get("manifest_rows") or []:
        manifest_path = repo_root / str(item.get("path") or "")
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        workspace_row = next(
            (row for row in (data.get("program_workspaces") or {}).get("workspace_rows") or [] if row.get("label") == item.get("label")),
            {},
        )
        manifest_path.write_text(
            json.dumps(
                {
                    "label": item.get("label"),
                    "purpose": item.get("purpose"),
                    "primary_runtime": workspace_row.get("primary_runtime"),
                    "cli_stack": workspace_row.get("cli_stack") or [],
                    "is_current_selection": current_selection.get("selected_program_label") == item.get("label"),
                    "status": "draft",
                    "note": "Program workspace manifest placeholder generated from VectorFL Paper.",
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )

    for item in (data.get("agent_mcp_control") or {}).get("manifest_rows") or []:
        manifest_path = repo_root / str(item.get("path") or "")
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        runtime_row = next(
            (row for row in (data.get("agent_mcp_control") or {}).get("runtime_rows") or [] if item.get("label", "").startswith(str(row.get("label", "")).split(" ")[0])),
            {},
        )
        manifest_path.write_text(
            json.dumps(
                {
                    "label": item.get("label"),
                    "purpose": item.get("purpose"),
                    "role": runtime_row.get("role"),
                    "owns": runtime_row.get("owns") or [],
                    "is_current_selection": current_selection.get("selected_runtime_label", "").startswith(str(runtime_row.get("label") or "").split(" ")[0]),
                    "status": "draft",
                    "note": "Agent/MCP runtime binding placeholder generated from VectorFL Paper.",
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )

    for organ in data["organs"]:
        name = f"organ-detail-{organ['slug']}.html"
        markup = render_organ_detail_page(data, organ["slug"])
        html_path = root / name
        json_path = root / name.replace(".html", ".json")
        detail_payload = {"organ": organ, "navigation": data["navigation"], "page_title": data["page_title"]}
        html_path.write_text(markup, encoding="utf-8")
        json_path.write_text(json.dumps(detail_payload, ensure_ascii=False, indent=2), encoding="utf-8")
        outputs.append({"name": name, "html_path": str(html_path), "json_path": str(json_path)})

    for lane in data["lanes"]["lane_rows"]:
        name = f"lane-detail-{lane['slug']}.html"
        markup = render_lane_detail_page(data, lane["slug"])
        html_path = root / name
        json_path = root / name.replace(".html", ".json")
        detail_payload = {"lane": lane, "navigation": data["navigation"], "page_title": data["page_title"]}
        html_path.write_text(markup, encoding="utf-8")
        json_path.write_text(json.dumps(detail_payload, ensure_ascii=False, indent=2), encoding="utf-8")
        outputs.append({"name": name, "html_path": str(html_path), "json_path": str(json_path)})

    for organ in data["organs"]:
        name = f"organ-editor-{organ['slug']}.html"
        markup = render_organ_editor_page(data, organ["slug"])
        html_path = root / name
        json_path = root / name.replace(".html", ".json")
        editor_payload = {"organ": organ, "navigation": data["navigation"], "page_title": data["page_title"], "mode": "editor"}
        html_path.write_text(markup, encoding="utf-8")
        json_path.write_text(json.dumps(editor_payload, ensure_ascii=False, indent=2), encoding="utf-8")
        outputs.append({"name": name, "html_path": str(html_path), "json_path": str(json_path)})

    for lane in data["lanes"]["lane_rows"]:
        name = f"lane-editor-{lane['slug']}.html"
        markup = render_lane_editor_page(data, lane["slug"])
        html_path = root / name
        json_path = root / name.replace(".html", ".json")
        editor_payload = {"lane": lane, "navigation": data["navigation"], "page_title": data["page_title"], "mode": "editor"}
        html_path.write_text(markup, encoding="utf-8")
        json_path.write_text(json.dumps(editor_payload, ensure_ascii=False, indent=2), encoding="utf-8")
        outputs.append({"name": name, "html_path": str(html_path), "json_path": str(json_path)})

    index_html = f"""<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>VectorFL Paper</title>
<style>:root{{--bg:#fff;--panel:#fff;--line:#e5e7eb;--ink:#111827;--muted:#6b7280}}*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font-family:ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}.page{{max-width:1120px;margin:0 auto;padding:16px;display:grid;gap:12px}}.panel{{background:var(--panel);border:1px solid var(--line);padding:14px;display:grid;gap:10px}}.list{{border:1px solid var(--line);background:#fff}}.row{{padding:10px 12px;border-bottom:1px solid var(--line);display:grid;gap:5px}}.row:last-child{{border-bottom:0}}.kicker{{color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:.08em;font-weight:600}}h1,h2{{margin:0}}h1{{font-size:18px}}h2{{font-size:14px}}.meta{{color:var(--muted);font-size:13px;line-height:1.5}}a{{color:inherit;text-decoration:none}}</style></head>
<body><div class="page"><section class="panel"><div class="kicker">VectorFL Paper</div><h1>페이지 묶음</h1><div class="meta">{html.escape(data['core_sentence'])}</div></section><section class="panel"><h2>주요 페이지</h2><div class="list">{''.join(f'<div class="row"><a href="{item["name"]}">{item["name"]}</a></div>' for item in outputs if not item["name"].startswith("organ-detail-") and not item["name"].startswith("organ-editor-") and not item["name"].startswith("lane-detail-") and not item["name"].startswith("lane-editor-") and not item["name"].startswith("line-detail-"))}</div></section><section class="panel"><h2>line 상세 페이지</h2><div class="list">{''.join(f'<div class="row"><a href="{item["name"]}">{item["name"]}</a></div>' for item in outputs if item["name"].startswith("line-detail-"))}</div></section><section class="panel"><h2>lane 상세 페이지</h2><div class="list">{''.join(f'<div class="row"><a href="{item["name"]}">{item["name"]}</a></div>' for item in outputs if item["name"].startswith("lane-detail-"))}</div></section><section class="panel"><h2>lane 수정 페이지</h2><div class="list">{''.join(f'<div class="row"><a href="{item["name"]}">{item["name"]}</a></div>' for item in outputs if item["name"].startswith("lane-editor-"))}</div></section><section class="panel"><h2>팀 상세 페이지</h2><div class="list">{''.join(f'<div class="row"><a href="{item["name"]}">{item["name"]}</a></div>' for item in outputs if item["name"].startswith("organ-detail-"))}</div></section><section class="panel"><h2>팀 수정 페이지</h2><div class="list">{''.join(f'<div class="row"><a href="{item["name"]}">{item["name"]}</a></div>' for item in outputs if item["name"].startswith("organ-editor-"))}</div></section></div></body></html>"""
    index_path = root / "index.html"
    index_path.write_text(index_html, encoding="utf-8")

    return {"output_dir": str(root), "index_path": str(index_path), "outputs": outputs}
