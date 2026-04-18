from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple
from uuid import uuid4

from app.core.runtime.file_store import JsonlEventStore


CONTROL_FILES = {
    "space_kernel": Path("control/space_kernel.json"),
    "turn_router": Path("control/turn_router.json"),
    "drift_guard": Path("control/drift_guard.json"),
    "current_phase": Path("runtime/current_phase.json"),
}

WATCH_RULE_FILE = Path("runtime/manifests/second_candidate_watch_rules.json")
LATENT_LINE_REGISTRY_FILE = Path("runtime/manifests/latent_line_registry_v1.json")
PHASE_DECISION_LOG_FILE = Path("runtime/manifests/phase_decision_log.jsonl")

MODE_GROUPS: Dict[str, Dict[str, Any]] = {
    "space_reading": {
        "group_key": "raw_external_cases",
        "artifact_roots": ["inputs/external_cases", "source_assets/external_case_inputs"],
        "guard_actions": [
            "read raw source before derived surfaces",
            "keep raw / first-pass / report separate",
        ],
        "drift_risks": [
            "raw import -> summary shortcut",
            "derived report treated as raw source",
        ],
        "why_selected": "raw materials should be read before promotion into reports or downstream structures",
        "sample_refs": [
            "inputs/external_cases/README.md",
            "inputs/external_cases/saltlux_ai.txt",
            "source_assets/external_case_inputs/folder_status.md",
            "source_assets/external_case_inputs/external_case_first_pass_saltlux_ai_input_v1.md",
        ],
    },
    "reflection": {
        "group_key": "report_trace_surfaces",
        "artifact_roots": ["docs/reports", "runtime/breadcrumbs.jsonl", "runtime/current_phase.json"],
        "guard_actions": [
            "read trace layers before implementation",
            "keep reading path explicit",
        ],
        "drift_risks": [
            "reflection -> implementation jump",
            "trace reading -> summary only",
        ],
        "why_selected": "the current task is to inspect traces, records, and rereadable surfaces before thickening interpretation",
        "sample_refs": [
            "docs/reports/today_handoff_index_v1.md",
            "docs/reports/control_plane_breadcrumbs_internal_structure_reading_check_v1.md",
            "runtime/breadcrumbs.jsonl",
        ],
    },
    "problem_solving": {
        "group_key": "runtime_engine_surfaces",
        "artifact_roots": ["app/runtime", "app/core/runtime", "runtime/manifests"],
        "guard_actions": [
            "use the smallest bounded fix",
            "separate binding from fidelity",
        ],
        "drift_risks": [
            "space reading -> immediate solution",
            "problem solving expanded beyond the existing frame",
        ],
        "why_selected": "this mode is for bounded technical issues inside the existing runtime frame",
        "sample_refs": [
            "app/runtime/user_page_shell.py",
            "app/runtime/runtime_preflight.py",
            "runtime/manifests/document_routing_alias_map_v1.json",
        ],
    },
    "implementation": {
        "group_key": "implementation_surfaces",
        "artifact_roots": ["app/runtime", "app/core", "scripts", "control"],
        "guard_actions": [
            "keep edits minimal and explicit",
            "write the smallest record that preserves the reasoning path",
        ],
        "drift_risks": [
            "implementation jump from reading",
            "broadening scope because the structure seems obvious",
        ],
        "why_selected": "this mode is for bounded file changes, preflight gating, and runtime plumbing",
        "sample_refs": [
            "control/space_kernel.json",
            "control/turn_router.json",
            "app/runtime/user_page_shell.py",
            "scripts/run_runtime_preflight.py",
        ],
    },
}


def build_runtime_preflight(
    runtime_root: Path,
    *,
    requested_mode: Optional[str] = None,
    requested_artifact_ref: Optional[str] = None,
    page_key: Optional[str] = None,
    purpose: Optional[str] = None,
) -> Dict[str, Any]:
    control = _load_control_plane(runtime_root)
    selected_mode, mode_source = _resolve_mode(
        requested_mode=requested_mode,
        page_key=page_key,
        requested_artifact_ref=requested_artifact_ref,
        turn_router=control.get("turn_router") or {},
        current_phase=control.get("current_phase") or {},
    )
    group = MODE_GROUPS.get(selected_mode, MODE_GROUPS["space_reading"])
    selected_artifact_refs = _resolve_artifact_refs(
        runtime_root,
        group.get("sample_refs") or [],
        requested_artifact_ref=requested_artifact_ref,
    )
    phase_snapshot = control.get("current_phase") or {}
    drift_risks = _merge_unique(
        list((control.get("drift_guard") or {}).get("drifts") or []),
        list(group.get("drift_risks") or []),
    )
    guard_actions = _merge_unique(
        list((control.get("drift_guard") or {}).get("repairs") or []),
        list(group.get("guard_actions") or []),
    )
    preflight_id = _preflight_id()
    latent_lines = _load_latent_line_registry(runtime_root)
    phase_transition = _evaluate_phase_transition(
        runtime_root,
        decision_context={
            "preflight_id": preflight_id,
            "selected_mode": selected_mode,
            "selected_artifact_group": {
                "group_key": group.get("group_key") or selected_mode,
                "artifact_roots": list(group.get("artifact_roots") or []),
                "selected_artifacts": selected_artifact_refs,
            },
            "requested_artifact_ref": requested_artifact_ref or "",
            "first_read_ref": selected_artifact_refs[0] if selected_artifact_refs else "",
            "mode_source": mode_source,
        },
        latent_lines=latent_lines,
    )
    why_selected = _build_why_selected(
        selected_mode=selected_mode,
        mode_source=mode_source,
        page_key=page_key,
        requested_artifact_ref=requested_artifact_ref,
        purpose=purpose,
        group=group,
    )
    decision = {
        "preflight_id": preflight_id,
        "selected_mode": selected_mode,
        "mode_source": mode_source,
        "phase_snapshot": phase_snapshot,
        "selected_artifact_group": {
            "group_key": group.get("group_key") or selected_mode,
            "artifact_roots": list(group.get("artifact_roots") or []),
            "selected_artifacts": selected_artifact_refs,
        },
        "why_selected": why_selected,
        "drift_risks": drift_risks,
        "guard_actions": guard_actions,
        "requested_mode": requested_mode or "",
        "requested_artifact_ref": requested_artifact_ref or "",
        "page_key": page_key or "",
        "purpose": purpose or "",
        "selected_artifact_root_hint": (group.get("artifact_roots") or [""])[0] if group.get("artifact_roots") else "",
        "first_read_ref": selected_artifact_refs[0] if selected_artifact_refs else "",
        "selected_at": _now_iso(),
        "phase_transition": phase_transition,
    }
    return decision


def write_preflight_snapshot(runtime_root: Path, decision: Dict[str, Any]) -> Path:
    path = runtime_root / "preflight_last_decision.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(decision, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def append_preflight_breadcrumb(runtime_root: Path, decision: Dict[str, Any]) -> Dict[str, Any]:
    store = JsonlEventStore(runtime_root / "breadcrumbs.jsonl")
    crumb = {
        "crumb_id": _next_crumb_id(runtime_root),
        "source_ref": "control/space_kernel.json > control/turn_router.json > control/drift_guard.json > runtime/current_phase.json > runtime/preflight_last_decision.json",
        "why_this_was_read": "run the control plane before the next read begins, so mode and drift are decided first",
        "what_was_seen": (
            f"selected_mode={decision.get('selected_mode')} / "
            f"group={((decision.get('selected_artifact_group') or {}).get('group_key') or '')} / "
            f"first_read_ref={decision.get('first_read_ref') or ''}"
        ),
        "shift_in_understanding": (
            "the control plane now acts as a pre-read gate rather than a post-read description"
        ),
        "next_hop": decision.get("first_read_ref") or "",
        "drift_risk": ", ".join(decision.get("drift_risks") or []),
        "repair_signal": ", ".join(decision.get("guard_actions") or []),
        "mode_at_time": decision.get("selected_mode") or "space_reading",
    }
    store.append(crumb)
    return crumb


def write_current_phase_snapshot(runtime_root: Path, decision: Dict[str, Any]) -> Path:
    path = runtime_root / "current_phase.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(decision, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def append_phase_decision_log(runtime_root: Path, decision: Dict[str, Any]) -> Dict[str, Any]:
    store = JsonlEventStore(runtime_root / "manifests" / "phase_decision_log.jsonl")
    store.append(decision)
    return decision


def append_pipeline_observation(
    runtime_root: Path,
    *,
    decision: Dict[str, Any],
    candidate_name: str,
    repeated_on: Iterable[str],
    not_promoted_reason: str,
    boundary_note: Optional[str] = None,
) -> Dict[str, Any]:
    store = JsonlEventStore(runtime_root / "manifests" / "pipeline_observation_registry.jsonl")
    existing = store.read_all()
    observations = [row for row in existing if str(row.get("candidate_name") or "") == candidate_name]
    requested_ref = str(decision.get("requested_artifact_ref") or "")
    first_read_ref = str(decision.get("first_read_ref") or "")
    family = _derive_family(requested_ref) or _derive_family(first_read_ref)
    watch = _evaluate_second_candidate_watch(
        runtime_root,
        decision=decision,
        candidate_name=candidate_name,
        family=family,
        requested_ref=requested_ref,
        existing=observations,
        boundary_note=boundary_note,
    )
    record = {
        "candidate_name": candidate_name,
        "family": family,
        "mode": str(decision.get("selected_mode") or ""),
        "first_read_ref": first_read_ref,
        "selected_artifact_group": decision.get("selected_artifact_group") or {},
        "next_hop": first_read_ref,
        "drift_risk_present": bool(decision.get("drift_risks")),
        "guard_action_present": bool(decision.get("guard_actions")),
        "observation_source": f"runtime_preflight:{decision.get('preflight_id') or ''}",
        "observation_timestamp": _now_iso(),
        "promotion_status": "observation",
        "not_promoted_reason": not_promoted_reason,
        "watch_rule_evaluated": bool(watch),
        "watch_result": watch.get("watch_result") if watch else "second_seed_not_triggered",
        "collapse_target": watch.get("collapse_target") if watch else candidate_name,
        "triggered_seed_name": watch.get("triggered_seed_name") if watch else None,
        "watch_reason": watch.get("watch_reason") if watch else "watch rule unavailable",
    }
    if boundary_note:
        record["boundary_note"] = boundary_note
    if requested_ref:
        record["requested_artifact_ref"] = requested_ref
    record["repeated_on"] = list(repeated_on)
    record["observation_count"] = len(observations) + 1
    store.append(record)
    return record


def _load_latent_line_registry(runtime_root: Path) -> Dict[str, Any]:
    path = runtime_root.parent / LATENT_LINE_REGISTRY_FILE
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def _select_active_latent_lines(
    latent_registry: Dict[str, Any],
    *,
    selected_mode: str,
    limit: int = 2,
) -> List[Dict[str, Any]]:
    lines = list(latent_registry.get("lines") or [])
    alive = [line for line in lines if str(line.get("status") or "") == "alive"]
    preferred_order = {
        "space_reading": [
            "pre_read_eye",
            "raw_return_preservation",
            "transition_over_surface",
            "input_to_reading_organ",
        ],
        "reflection": [
            "transition_over_surface",
            "input_to_reading_organ",
            "pre_read_eye",
            "raw_return_preservation",
        ],
        "implementation": [
            "harness_over_model",
            "work_absorption_harness",
            "alignment_before_autonomy",
            "pre_read_eye",
        ],
        "problem_solving": [
            "input_to_reading_organ",
            "harness_over_model",
            "raw_return_preservation",
            "pre_read_eye",
        ],
    }.get(selected_mode, [
        "pre_read_eye",
        "raw_return_preservation",
        "transition_over_surface",
        "input_to_reading_organ",
    ])
    preferred_index = {name: idx for idx, name in enumerate(preferred_order)}

    def _sort_key(line: Dict[str, Any]) -> Tuple[int, int, str]:
        name = str(line.get("latent_line_name") or "")
        return (
            preferred_index.get(name, len(preferred_order)),
            _strength_rank(str(line.get("strength") or "")),
            name,
        )

    alive.sort(key=_sort_key)
    return alive[:limit]


def _strength_rank(value: str) -> int:
    order = {
        "strong": 0,
        "medium": 1,
        "weak": 2,
        "unknown": 3,
    }
    return order.get(value, 99)


def _load_jsonl_rows(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    store = JsonlEventStore(path)
    return store.read_all()


def _evaluate_phase_transition(
    runtime_root: Path,
    *,
    decision_context: Dict[str, Any],
    latent_lines: Dict[str, Any],
) -> Dict[str, Any]:
    selected_mode = str(decision_context.get("selected_mode") or "")
    selected_group = decision_context.get("selected_artifact_group") or {}
    selected_group_key = str(selected_group.get("group_key") or "")
    first_read_ref = str(decision_context.get("first_read_ref") or "")
    requested_artifact_ref = str(decision_context.get("requested_artifact_ref") or "")
    preflight_id = str(decision_context.get("preflight_id") or "")

    active_latent_lines = _select_active_latent_lines(latent_lines, selected_mode=selected_mode, limit=2)
    active_latent_line_names = [str(line.get("latent_line_name") or "") for line in active_latent_lines]
    strong_line_names = [name for name in active_latent_line_names if name]

    observation_rows = _load_jsonl_rows(runtime_root / "manifests" / "pipeline_observation_registry.jsonl")
    candidate_rows = [row for row in observation_rows if str(row.get("candidate_name") or "") == "raw_to_first_pass_to_report"]
    boundary_rows = [row for row in candidate_rows if row.get("boundary_note")]
    watch_triggered_rows = [row for row in candidate_rows if row.get("watch_result") == "second_seed_triggered"]

    continuity = "high" if "pre_read_eye" in strong_line_names and selected_mode in {"space_reading", "reflection"} else "medium"
    residue = "medium"
    if watch_triggered_rows:
        residue = "high"
    elif boundary_rows or candidate_rows:
        residue = "medium"
    tension = "low"
    if watch_triggered_rows and boundary_rows:
        tension = "high"
    sufficiency = "medium"
    if selected_group_key == "raw_external_cases" and selected_mode == "space_reading":
        sufficiency = "medium"
    if selected_mode == "reflection" and "report_trace_surfaces" in selected_group_key:
        sufficiency = "medium"
    if watch_triggered_rows:
        sufficiency = "high"

    phase = "hold"
    decision_reason = "signals remain unresolved; defaulting to hold"
    blocked_by: List[str] = []
    next_check_trigger: List[str] = []

    if tension == "high":
        phase = "hold"
        decision_reason = "tension between boundary or latent lines remains unresolved"
        blocked_by = ["latent_line_tension"]
        next_check_trigger = [
            "same tension repeats in next reread",
            "tension_map rule added",
            "new evidence clarifies priority",
        ]
    elif continuity == "high" and residue in {"low", "medium"} and tension == "low" and sufficiency in {"low", "medium"}:
        phase = "thickening"
        decision_reason = "existing latent lines and pre-read gate are stable, but the path is still not closure-ready"
        next_check_trigger = [
            "same latent line repeats in a future reread",
            "residue becomes high because a new path cannot be collapsed",
            "sufficiency moves to high and closure can be reviewed",
        ]
    elif residue == "high" and continuity in {"low", "medium"} and sufficiency == "low":
        phase = "widening"
        decision_reason = "existing structure does not absorb the current input cleanly; widening is needed"
        next_check_trigger = [
            "new latent line appears",
            "boundary note cannot explain the residue",
            "existing candidate scope no longer absorbs the input",
        ]
        blocked_by = ["low_continuity"]
    elif continuity == "high" and sufficiency == "high" and tension == "low" and residue in {"low", "medium"}:
        phase = "closure"
        decision_reason = "current observation is sufficiently absorbed and can be handoff-ready"
        next_check_trigger = [
            "new evidence reopens the loop",
            "boundary or residue rises again",
            "new candidate or latent line interrupts closure",
        ]
    else:
        phase = "hold"
        decision_reason = "the current signal mix is not yet stable enough for a phase switch"
        blocked_by = ["insufficient_phase_signal"]
        next_check_trigger = [
            "signals repeat with higher consistency",
            "residue or tension becomes better explained",
            "continuity strengthens without introducing new conflict",
        ]

    phase_record = {
        "phase": phase,
        "status": "active",
        "last_updated": _now_iso(),
        "reading_frame": "binding_closed -> semantic_fidelity -> output-worthiness -> meaning_context_sufficiency -> detector -> widening_trigger",
        "evaluated_from": "turn_preflight",
        "phase_source_turn": preflight_id,
        "decision_scope": "mode_scoped",
        "active_latent_lines": strong_line_names,
        "signals": {
            "continuity": continuity,
            "residue": residue,
            "tension": tension,
            "sufficiency": sufficiency,
        },
        "decision": phase,
        "decision_reason": decision_reason,
        "blocked_by": blocked_by,
        "next_check_trigger": next_check_trigger,
        "phase_confidence": "medium" if phase != "hold" else "high",
        "related_candidate_ids": ["raw_to_first_pass_to_report"] if candidate_rows else [],
        "related_watch_rules": ["second_candidate_emergence_watch"] if candidate_rows else [],
        "related_breadcrumb_refs": [str((runtime_root / "breadcrumbs.jsonl").as_posix())],
        "reopen_hint": [
            "if residue becomes high with same line repeated twice",
            "if a new observation cannot collapse back to the current candidate",
        ],
        "notes": {
            "selected_mode": selected_mode,
            "first_read_ref": first_read_ref,
            "requested_artifact_ref": requested_artifact_ref,
        },
    }
    return phase_record


def _evaluate_second_candidate_watch(
    runtime_root: Path,
    *,
    decision: Dict[str, Any],
    candidate_name: str,
    family: str,
    requested_ref: str,
    existing: List[Dict[str, Any]],
    boundary_note: Optional[str],
) -> Optional[Dict[str, Any]]:
    path = runtime_root.parent / WATCH_RULE_FILE
    if not path.exists():
        return None
    try:
        watch = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None

    current_candidates = list(watch.get("current_clear_candidates") or [])
    if not current_candidates:
        return None
    clear_candidate = str(current_candidates[0])
    selected_mode = str(decision.get("selected_mode") or "")
    result = "second_seed_not_triggered"
    reason = "watch rule active but no new seed criteria met"
    collapse_target = clear_candidate
    triggered_seed_name: Optional[str] = None

    if candidate_name in current_candidates:
        if selected_mode == "space_reading":
            result = "collapse_to_existing_candidate"
            reason = "same clear candidate under space reading"
        elif boundary_note or selected_mode == "reflection":
            result = "boundary_only_variation"
            reason = boundary_note or "same candidate under reflection boundary"
        else:
            result = "second_seed_not_triggered"
            reason = "same candidate without distinct path evidence"
    else:
        result = "second_seed_triggered"
        triggered_seed_name = candidate_name
        reason = "distinct repeated path not collapsible to existing candidate"
        collapse_target = ""

    if family and candidate_name in current_candidates and selected_mode == "reflection":
        reason = f"{reason}; family={family}"

    return {
        "watch_rule_evaluated": True,
        "watch_result": result,
        "collapse_target": collapse_target,
        "triggered_seed_name": triggered_seed_name,
        "watch_reason": reason,
    }


def _load_control_plane(runtime_root: Path) -> Dict[str, Any]:
    payload: Dict[str, Any] = {}
    for key, relative in CONTROL_FILES.items():
        path = runtime_root.parent / relative if relative.is_absolute() else runtime_root.parent / relative
        if not path.exists():
            payload[key] = {}
            continue
        try:
            payload[key] = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            payload[key] = {}
    return payload


def _resolve_mode(
    *,
    requested_mode: Optional[str],
    page_key: Optional[str],
    requested_artifact_ref: Optional[str],
    turn_router: Dict[str, Any],
    current_phase: Dict[str, Any],
) -> Tuple[str, str]:
    valid_modes = set(str(mode) for mode in (turn_router.get("modes") or []))
    if requested_mode and requested_mode in valid_modes:
        return requested_mode, "requested_mode"
    if page_key in {"memory", "similar"}:
        return "reflection", "page_key"
    if page_key in {"implementation"}:
        return "implementation", "page_key"
    if page_key in {"problem_solving"}:
        return "problem_solving", "page_key"
    if requested_artifact_ref:
        lowered = requested_artifact_ref.lower()
        if lowered.startswith(("docs/", "runtime/")):
            if lowered.startswith("docs/reports") or lowered.startswith("runtime/breadcrumbs"):
                return "reflection", "artifact_ref"
            if lowered.startswith("app/") or lowered.startswith("scripts/") or lowered.startswith("control/"):
                return "implementation", "artifact_ref"
        if lowered.startswith(("inputs/external_cases", "source_assets/external_case_inputs")):
            return "space_reading", "artifact_ref"
    phase_name = str(current_phase.get("phase") or "").strip().lower()
    if "bootstrap" in phase_name or "reading" in phase_name:
        return "space_reading", "current_phase"
    default_modes = list(turn_router.get("default_order") or [])
    if default_modes:
        return str(default_modes[0]), "default_order"
    return "space_reading", "fallback"


def _resolve_artifact_refs(
    runtime_root: Path,
    sample_refs: List[str],
    *,
    requested_artifact_ref: Optional[str],
) -> List[str]:
    refs: List[str] = []
    if requested_artifact_ref:
        candidate = _normalize_ref(requested_artifact_ref)
        if _ref_exists(runtime_root, candidate):
            refs.append(candidate)
    for ref in sample_refs:
        normalized = _normalize_ref(ref)
        if normalized not in refs and _ref_exists(runtime_root, normalized):
            refs.append(normalized)
    return refs[:4]


def _build_why_selected(
    *,
    selected_mode: str,
    mode_source: str,
    page_key: Optional[str],
    requested_artifact_ref: Optional[str],
    purpose: Optional[str],
    group: Dict[str, Any],
) -> str:
    bits = [
        f"mode={selected_mode}",
        f"mode_source={mode_source}",
        f"group={group.get('group_key')}",
    ]
    if page_key:
        bits.append(f"page={page_key}")
    if requested_artifact_ref:
        bits.append(f"requested={requested_artifact_ref}")
    if purpose:
        bits.append(f"purpose={purpose}")
    bits.append(str(group.get("why_selected") or ""))
    return " / ".join(bit for bit in bits if bit)


def _ref_exists(runtime_root: Path, ref: str) -> bool:
    path = _resolve_ref_path(runtime_root, ref)
    return path.exists()


def _resolve_ref_path(runtime_root: Path, ref: str) -> Path:
    path = Path(ref)
    if path.is_absolute():
        return path
    return (runtime_root.parent / path).resolve()


def _normalize_ref(value: str) -> str:
    return str(value or "").strip().replace("\\", "/")


def _derive_family(ref: str) -> str:
    normalized = _normalize_ref(ref)
    for prefix in ("inputs/external_cases/", "source_assets/external_case_inputs/"):
        if normalized.startswith(prefix):
            tail = normalized[len(prefix) :]
            return Path(tail).stem
    return ""


def _merge_unique(*values: Iterable[str]) -> List[str]:
    merged: List[str] = []
    seen = set()
    for seq in values:
        for item in seq:
            text = str(item).strip()
            if not text or text in seen:
                continue
            seen.add(text)
            merged.append(text)
    return merged


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _preflight_id() -> str:
    return "preflight_" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%f") + "_" + uuid4().hex[:6]


def _next_crumb_id(runtime_root: Path) -> str:
    store = JsonlEventStore(runtime_root / "breadcrumbs.jsonl")
    rows = store.read_all()
    max_num = 0
    for row in rows:
        crumb_id = str(row.get("crumb_id") or "")
        if not crumb_id.startswith("crumb_"):
            continue
        suffix = crumb_id.rsplit("_", 1)[-1]
        if suffix.isdigit():
            max_num = max(max_num, int(suffix))
    return f"crumb_{max_num + 1:04d}_{uuid4().hex[:4]}"
