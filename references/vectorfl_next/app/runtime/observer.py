from pathlib import Path
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional

from app.runtime.file_store import JsonDirectoryStore, JsonlEventStore


def build_reactive_space_observation(runtime_root: Path) -> Dict[str, object]:
    return build_scoped_reactive_space_observation(runtime_root)


def build_scoped_reactive_space_observation(
    runtime_root: Path,
    recent_limit: Optional[int] = None,
    recent_seconds: Optional[int] = None,
    family_id: Optional[str] = None,
    session_id: Optional[str] = None,
) -> Dict[str, object]:
    events = JsonlEventStore(runtime_root / "events" / "formation_events.jsonl").read_all()
    cell_store = JsonDirectoryStore(runtime_root / "core" / "space_cells")
    local_space_store = JsonDirectoryStore(runtime_root / "core" / "local_spaces")
    bridge_store = JsonDirectoryStore(runtime_root / "core" / "bridge_traces")
    pressure_store = JsonDirectoryStore(runtime_root / "core" / "pressure_profiles")
    material_store = JsonDirectoryStore(runtime_root / "core" / "materials")

    scoped_cell_ids = _filter_cell_ids(cell_store, material_store, family_id, session_id)
    reaction_events = [
        event
        for event in events
        if event["event_type"] == "space_cell_reacted"
        and (not scoped_cell_ids or event["subject_id"] in scoped_cell_ids)
    ]
    if recent_seconds is not None:
        cutoff = datetime.now(timezone.utc) - timedelta(seconds=recent_seconds)
        reaction_events = [
            event
            for event in reaction_events
            if _parse_iso(event["occurred_at"]) >= cutoff
        ]
    if recent_limit is not None:
        reaction_events = reaction_events[-recent_limit:]

    branch_events = [
        event
        for event in events
        if event["event_type"] == "space_cell_branched"
        and (not scoped_cell_ids or event["subject_id"] in scoped_cell_ids)
    ]
    if recent_seconds is not None:
        cutoff = datetime.now(timezone.utc) - timedelta(seconds=recent_seconds)
        branch_events = [
            event
            for event in branch_events
            if _parse_iso(event["occurred_at"]) >= cutoff
        ]
    if recent_limit is not None:
        branch_events = branch_events[-recent_limit:]

    reaction_counts = {"thickening": 0, "split": 0, "relocation": 0}
    reactive_cells: Dict[str, List[str]] = {}
    for event in reaction_events:
        kind = event["payload"]["reaction_kind"]
        reaction_counts[kind] = reaction_counts.get(kind, 0) + 1
        reactive_cells.setdefault(kind, []).append(event["subject_id"])

    local_space_states: Dict[str, int] = {}
    local_space_maturation_signals: Dict[str, int] = {}
    local_space_coexistence_modes: Dict[str, int] = {}
    relevant_local_space_ids = {
        record["local_space_id"]
        for record in local_space_store.read_all()
        if not scoped_cell_ids or set(record.get("cell_refs", ())) & scoped_cell_ids
    }
    for record in local_space_store.read_all():
        if relevant_local_space_ids and record["local_space_id"] not in relevant_local_space_ids:
            continue
        state = record["state"]
        local_space_states[state] = local_space_states.get(state, 0) + 1
    space_manifest_store = JsonDirectoryStore(runtime_root / "manifests" / "reactive_spaces")
    space_manifests = [
        manifest
        for manifest in space_manifest_store.read_all()
        if not relevant_local_space_ids or manifest["local_space_id"] in relevant_local_space_ids
    ]
    for manifest in space_manifest_store.read_all():
        if relevant_local_space_ids and manifest["local_space_id"] not in relevant_local_space_ids:
            continue
        for signal in manifest.get("maturation_evidence", {}).get("signals", ()):
            local_space_maturation_signals[signal] = local_space_maturation_signals.get(signal, 0) + 1
        coexistence_mode = manifest.get("coexistence_mode")
        if coexistence_mode:
            local_space_coexistence_modes[coexistence_mode] = local_space_coexistence_modes.get(coexistence_mode, 0) + 1

    bridge_states: Dict[str, int] = {}
    bridge_maturation_signals: Dict[str, int] = {}
    bridge_manifests = [
        manifest
        for manifest in JsonDirectoryStore(runtime_root / "manifests" / "bridges").read_all()
        if not relevant_local_space_ids
        or (
            manifest["from_local_space_id"] in relevant_local_space_ids
            or manifest["to_local_space_id"] in relevant_local_space_ids
        )
    ]
    for record in bridge_store.read_all():
        if relevant_local_space_ids and not (
            record["from_local_space_id"] in relevant_local_space_ids
            or record["to_local_space_id"] in relevant_local_space_ids
        ):
            continue
        state = record["state"]
        bridge_states[state] = bridge_states.get(state, 0) + 1
    for manifest in bridge_manifests:
        for signal in manifest.get("maturation_evidence", {}).get("signals", ()):
            bridge_maturation_signals[signal] = bridge_maturation_signals.get(signal, 0) + 1

    reaction_sequence = []
    pressure_signatures: Dict[str, int] = {}
    pressure_axis_distribution: Dict[str, Dict[str, int]] = {}
    pressure_axis_combinations: Dict[str, int] = {}
    for event in reaction_events:
        pressure_profile_id = event["payload"].get("pressure_profile_id")
        signature = _pressure_signature(pressure_store.get(pressure_profile_id)) if pressure_profile_id else "none"
        profile = pressure_store.get(pressure_profile_id) if pressure_profile_id else None
        reaction_sequence.append(
            {
                "occurred_at": event["occurred_at"],
                "cell_id": event["subject_id"],
                "reaction_kind": event["payload"]["reaction_kind"],
                "pressure_signature": signature,
            }
        )
        pressure_signatures[signature] = pressure_signatures.get(signature, 0) + 1
        _accumulate_pressure_axes(pressure_axis_distribution, profile)
        combination = _pressure_axis_combination(profile)
        pressure_axis_combinations[combination] = pressure_axis_combinations.get(combination, 0) + 1

    pressure_transitions = _count_pressure_transitions(reaction_sequence)
    branch_reasons: Dict[str, int] = {}
    branch_cells: Dict[str, List[str]] = {}
    branch_sequence = []
    for event in branch_events:
        reason = event["payload"].get("reason", "unknown")
        branch_reasons[reason] = branch_reasons.get(reason, 0) + 1
        branch_cells.setdefault(reason, []).append(event["subject_id"])
        branch_sequence.append(
            {
                "occurred_at": event["occurred_at"],
                "cell_id": event["subject_id"],
                "reason": reason,
                "family_id": event["payload"].get("family_id"),
            }
        )
    process_summary = _build_process_summary(
        reaction_counts=reaction_counts,
        branch_reason_counts=branch_reasons,
        cell_count=len(scoped_cell_ids) if scoped_cell_ids else len(list(cell_store.list_ids())),
        local_space_states=local_space_states,
    )
    terrain_components = _build_terrain_components(
        local_space_records=local_space_store.read_all(),
        bridge_records=bridge_store.read_all(),
        space_manifests=space_manifests,
        bridge_manifests=bridge_manifests,
        relevant_local_space_ids=relevant_local_space_ids,
    )
    terrain_climate_modes: Dict[str, int] = {}
    terrain_climate_signals: Dict[str, int] = {}
    terrain_rhythm_modes: Dict[str, int] = {}
    terrain_rhythm_signals: Dict[str, int] = {}
    terrain_recurrence_modes: Dict[str, int] = {}
    terrain_recurrence_signals: Dict[str, int] = {}
    terrain_memory_modes: Dict[str, int] = {}
    terrain_memory_signals: Dict[str, int] = {}
    terrain_retention_modes: Dict[str, int] = {}
    terrain_retention_signals: Dict[str, int] = {}
    terrain_forgetting_modes: Dict[str, int] = {}
    terrain_forgetting_signals: Dict[str, int] = {}
    for component in terrain_components:
        climate_mode = component.get("climate_mode")
        if climate_mode:
            terrain_climate_modes[climate_mode] = terrain_climate_modes.get(climate_mode, 0) + 1
        for signal in component.get("climate_evidence", {}).get("signals", ()):
            terrain_climate_signals[signal] = terrain_climate_signals.get(signal, 0) + 1
        rhythm_mode = component.get("rhythm_mode")
        if rhythm_mode:
            terrain_rhythm_modes[rhythm_mode] = terrain_rhythm_modes.get(rhythm_mode, 0) + 1
        for signal in component.get("rhythm_evidence", {}).get("signals", ()):
            terrain_rhythm_signals[signal] = terrain_rhythm_signals.get(signal, 0) + 1
        recurrence_mode = component.get("recurrence_mode")
        if recurrence_mode:
            terrain_recurrence_modes[recurrence_mode] = terrain_recurrence_modes.get(recurrence_mode, 0) + 1
        for signal in component.get("recurrence_evidence", {}).get("signals", ()):
            terrain_recurrence_signals[signal] = terrain_recurrence_signals.get(signal, 0) + 1
        memory_mode = component.get("memory_mode")
        if memory_mode:
            terrain_memory_modes[memory_mode] = terrain_memory_modes.get(memory_mode, 0) + 1
        for signal in component.get("memory_evidence", {}).get("signals", ()):
            terrain_memory_signals[signal] = terrain_memory_signals.get(signal, 0) + 1
        retention_mode = component.get("retention_mode")
        if retention_mode:
            terrain_retention_modes[retention_mode] = terrain_retention_modes.get(retention_mode, 0) + 1
        for signal in component.get("retention_evidence", {}).get("signals", ()):
            terrain_retention_signals[signal] = terrain_retention_signals.get(signal, 0) + 1
        forgetting_mode = component.get("forgetting_mode")
        if forgetting_mode:
            terrain_forgetting_modes[forgetting_mode] = terrain_forgetting_modes.get(forgetting_mode, 0) + 1
        for signal in component.get("forgetting_evidence", {}).get("signals", ()):
            terrain_forgetting_signals[signal] = terrain_forgetting_signals.get(signal, 0) + 1

    return {
        "reaction_counts": reaction_counts,
        "reactive_cell_ids": {key: sorted(set(value)) for key, value in reactive_cells.items()},
        "branch_reason_counts": branch_reasons,
        "branched_cell_ids": {key: sorted(set(value)) for key, value in branch_cells.items()},
        "branch_sequence": branch_sequence,
        "process_summary": process_summary,
        "terrain_components": terrain_components,
        "terrain_climate_modes": terrain_climate_modes,
        "terrain_climate_signals": terrain_climate_signals,
        "terrain_rhythm_modes": terrain_rhythm_modes,
        "terrain_rhythm_signals": terrain_rhythm_signals,
        "terrain_recurrence_modes": terrain_recurrence_modes,
        "terrain_recurrence_signals": terrain_recurrence_signals,
        "terrain_memory_modes": terrain_memory_modes,
        "terrain_memory_signals": terrain_memory_signals,
        "terrain_retention_modes": terrain_retention_modes,
        "terrain_retention_signals": terrain_retention_signals,
        "terrain_forgetting_modes": terrain_forgetting_modes,
        "terrain_forgetting_signals": terrain_forgetting_signals,
        "cell_count": len(scoped_cell_ids) if scoped_cell_ids else len(list(cell_store.list_ids())),
        "local_space_states": local_space_states,
        "local_space_maturation_signals": local_space_maturation_signals,
        "local_space_coexistence_modes": local_space_coexistence_modes,
        "bridge_states": bridge_states,
        "bridge_maturation_signals": bridge_maturation_signals,
        "reaction_sequence": reaction_sequence,
        "pressure_signatures": pressure_signatures,
        "pressure_axis_distribution": pressure_axis_distribution,
        "pressure_axis_combinations": pressure_axis_combinations,
        "pressure_transitions": pressure_transitions,
        "scope": {
            "recent_limit": recent_limit,
            "recent_seconds": recent_seconds,
            "family_id": family_id,
            "session_id": session_id,
        },
    }


def build_session_timeline(runtime_root: Path, session_id: str) -> Dict[str, object]:
    scoped = build_scoped_reactive_space_observation(runtime_root, session_id=session_id)
    timeline = []
    for item in scoped["reaction_sequence"]:
        timeline.append(
            {
                "occurred_at": item["occurred_at"],
                "cell_id": item["cell_id"],
                "reaction_kind": item["reaction_kind"],
                "pressure_signature": item["pressure_signature"],
            }
        )
    return {
        "session_id": session_id,
        "event_count": len(timeline),
        "timeline": timeline,
        "phases": _compress_reaction_phases(timeline),
        "reaction_counts": scoped["reaction_counts"],
        "pressure_signatures": scoped["pressure_signatures"],
    }


def _pressure_signature(profile: Dict[str, object]) -> str:
    if not profile:
        return "none"
    axes = []
    for axis in profile.get("axes", []):
        axes.append("%s:%s" % (axis["axis"], _strength_bucket(axis["strength_hint"])))
    return "|".join(sorted(axes)) if axes else "none"


def _strength_bucket(strength_hint: float) -> str:
    if strength_hint < 0.4:
        return "low"
    if strength_hint < 0.75:
        return "mid"
    return "high"


def _parse_iso(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _accumulate_pressure_axes(
    distribution: Dict[str, Dict[str, int]],
    profile: Optional[Dict[str, object]],
) -> None:
    if not profile:
        distribution.setdefault("none", {}).setdefault("none", 0)
        distribution["none"]["none"] += 1
        return
    for axis in profile.get("axes", []):
        axis_name = axis["axis"]
        bucket = _strength_bucket(axis["strength_hint"])
        distribution.setdefault(axis_name, {}).setdefault(bucket, 0)
        distribution[axis_name][bucket] += 1


def _pressure_axis_combination(profile: Optional[Dict[str, object]]) -> str:
    if not profile:
        return "none"
    axes = sorted(axis["axis"] for axis in profile.get("axes", []))
    return "+".join(axes) if axes else "none"


def _filter_cell_ids(
    cell_store: JsonDirectoryStore,
    material_store: JsonDirectoryStore,
    family_id: Optional[str],
    session_id: Optional[str],
) -> List[str]:
    if family_id is None and session_id is None:
        return []
    matching_material_ids = {
        record["material_id"]
        for record in material_store.read_all()
        if (family_id is None or record.get("family_id") == family_id)
        and (session_id is None or record.get("session_id") == session_id)
    }
    if not matching_material_ids:
        return []
    matching_cell_ids = []
    for record in cell_store.read_all():
        if set(record.get("material_refs", ())) & matching_material_ids:
            matching_cell_ids.append(record["cell_id"])
    return matching_cell_ids


def _compress_reaction_phases(timeline: List[Dict[str, str]]) -> List[Dict[str, object]]:
    if not timeline:
        return []
    phases: List[Dict[str, object]] = []
    current = {
        "reaction_kind": timeline[0]["reaction_kind"],
        "pressure_signature": timeline[0]["pressure_signature"],
        "start_at": timeline[0]["occurred_at"],
        "end_at": timeline[0]["occurred_at"],
        "event_count": 1,
        "cell_ids": [timeline[0]["cell_id"]],
    }
    for item in timeline[1:]:
        if (
            item["reaction_kind"] == current["reaction_kind"]
            and item["pressure_signature"] == current["pressure_signature"]
        ):
            current["end_at"] = item["occurred_at"]
            current["event_count"] += 1
            current["cell_ids"].append(item["cell_id"])
            continue
        current["cell_ids"] = sorted(set(current["cell_ids"]))
        phases.append(current)
        current = {
            "reaction_kind": item["reaction_kind"],
            "pressure_signature": item["pressure_signature"],
            "start_at": item["occurred_at"],
            "end_at": item["occurred_at"],
            "event_count": 1,
            "cell_ids": [item["cell_id"]],
        }
    current["cell_ids"] = sorted(set(current["cell_ids"]))
    phases.append(current)
    return phases


def _count_pressure_transitions(timeline: List[Dict[str, str]]) -> Dict[str, int]:
    transitions: Dict[str, int] = {}
    if len(timeline) < 2:
        return transitions
    previous = timeline[0]["pressure_signature"]
    for item in timeline[1:]:
        current = item["pressure_signature"]
        key = "%s -> %s" % (previous, current)
        transitions[key] = transitions.get(key, 0) + 1
        previous = current
    return transitions


def _build_process_summary(
    reaction_counts: Dict[str, int],
    branch_reason_counts: Dict[str, int],
    cell_count: int,
    local_space_states: Dict[str, int],
) -> Dict[str, object]:
    continuity_count = reaction_counts.get("thickening", 0)
    split_count = reaction_counts.get("split", 0)
    relocation_count = reaction_counts.get("relocation", 0)
    mismatch_count = branch_reason_counts.get("pressure_signature_mismatch_or_absent", 0)

    phase_tags: List[str] = []
    if continuity_count:
        phase_tags.append("continuity")
    if mismatch_count:
        phase_tags.append("mismatch_branching")
    if split_count:
        phase_tags.append("split_pressure")
    if relocation_count:
        phase_tags.append("relocation_pressure")
    if local_space_states:
        phase_tags.append("space_formation_visible")
    if not phase_tags:
        phase_tags.append("sparse_process")

    if continuity_count and mismatch_count:
        dominant_mode = "mixed_process"
    elif continuity_count:
        dominant_mode = "continuity_process"
    elif mismatch_count:
        dominant_mode = "branching_process"
    elif split_count or relocation_count:
        dominant_mode = "reactive_process"
    else:
        dominant_mode = "sparse_process"

    summary_line = (
        "mode=%s continuity=%s mismatch=%s split=%s relocation=%s cells=%s"
        % (
            dominant_mode,
            continuity_count,
            mismatch_count,
            split_count,
            relocation_count,
            cell_count,
        )
    )
    return {
        "dominant_mode": dominant_mode,
        "phase_tags": phase_tags,
        "summary_line": summary_line,
    }


def _build_terrain_components(
    local_space_records: List[Dict[str, object]],
    bridge_records: List[Dict[str, object]],
    space_manifests: List[Dict[str, object]],
    bridge_manifests: List[Dict[str, object]],
    relevant_local_space_ids: set,
) -> List[Dict[str, object]]:
    records = [
        record
        for record in local_space_records
        if not relevant_local_space_ids or record["local_space_id"] in relevant_local_space_ids
    ]
    if not records:
        return []

    adjacency: Dict[str, set] = {record["local_space_id"]: set() for record in records}
    for bridge in bridge_records:
        left = bridge["from_local_space_id"]
        right = bridge["to_local_space_id"]
        if left not in adjacency or right not in adjacency:
            continue
        adjacency[left].add(right)
        adjacency[right].add(left)

    components: List[Dict[str, object]] = []
    seen = set()
    by_id = {record["local_space_id"]: record for record in records}
    manifest_by_id = {manifest["local_space_id"]: manifest for manifest in space_manifests}
    bridge_manifests_by_pair: Dict[tuple, List[Dict[str, object]]] = {}
    for manifest in bridge_manifests:
        pair = tuple(sorted((manifest["from_local_space_id"], manifest["to_local_space_id"])))
        bridge_manifests_by_pair.setdefault(pair, []).append(manifest)
    for local_space_id in sorted(adjacency):
        if local_space_id in seen:
            continue
        stack = [local_space_id]
        component_ids = []
        bridge_state_counts: Dict[str, int] = {}
        while stack:
            current = stack.pop()
            if current in seen:
                continue
            seen.add(current)
            component_ids.append(current)
            for neighbor in adjacency[current]:
                stack.append(neighbor)
        component_set = set(component_ids)
        for bridge in bridge_records:
            if (
                bridge["from_local_space_id"] in component_set
                and bridge["to_local_space_id"] in component_set
            ):
                state = bridge["state"]
                bridge_state_counts[state] = bridge_state_counts.get(state, 0) + 1
        component_manifests = [
            manifest_by_id[item]
            for item in component_ids
            if item in manifest_by_id
        ]
        component_bridge_manifests = []
        for bridge in bridge_records:
            pair = tuple(sorted((bridge["from_local_space_id"], bridge["to_local_space_id"])))
            if (
                bridge["from_local_space_id"] in component_set
                and bridge["to_local_space_id"] in component_set
                and pair in bridge_manifests_by_pair
            ):
                component_bridge_manifests.extend(bridge_manifests_by_pair[pair])
        climate_summary = _summarize_component_climate(
            component_manifests,
            component_bridge_manifests,
            bridge_state_counts,
        )
        rhythm_summary = _summarize_component_rhythm(
            component_manifests,
            component_bridge_manifests,
            climate_summary["shared_pressure_axes"],
        )
        recurrence_summary = _summarize_component_recurrence(
            component_manifests,
            component_bridge_manifests,
            rhythm_summary["rhythm_evidence"],
        )
        memory_summary = _summarize_component_memory(
            component_manifests,
            component_bridge_manifests,
            recurrence_summary["recurrence_evidence"],
        )
        retention_summary = _summarize_component_retention(memory_summary["memory_evidence"])
        forgetting_summary = _summarize_component_forgetting(
            memory_summary["memory_evidence"],
            retention_summary["retention_evidence"],
        )
        components.append(
            {
                "local_space_ids": sorted(component_ids),
                "local_space_count": len(component_ids),
                "states": [by_id[item]["state"] for item in component_ids],
                "bridge_state_counts": bridge_state_counts,
                "climate_mode": climate_summary["climate_mode"],
                "shared_pressure_axes": climate_summary["shared_pressure_axes"],
                "union_pressure_axes": climate_summary["union_pressure_axes"],
                "climate_evidence": climate_summary["climate_evidence"],
                "rhythm_mode": rhythm_summary["rhythm_mode"],
                "rhythm_evidence": rhythm_summary["rhythm_evidence"],
                "recurrence_mode": recurrence_summary["recurrence_mode"],
                "recurrence_evidence": recurrence_summary["recurrence_evidence"],
                "memory_mode": memory_summary["memory_mode"],
                "memory_evidence": memory_summary["memory_evidence"],
                "retention_mode": retention_summary["retention_mode"],
                "retention_evidence": retention_summary["retention_evidence"],
                "forgetting_mode": forgetting_summary["forgetting_mode"],
                "forgetting_evidence": forgetting_summary["forgetting_evidence"],
            }
        )
    components.sort(key=lambda item: (item["local_space_count"], len(item["bridge_state_counts"])), reverse=True)
    return components


def _summarize_component_climate(
    component_manifests: List[Dict[str, object]],
    component_bridge_manifests: List[Dict[str, object]],
    bridge_state_counts: Dict[str, int],
) -> Dict[str, object]:
    if not component_manifests:
        return {
            "climate_mode": "unknown_climate",
            "shared_pressure_axes": [],
            "union_pressure_axes": [],
            "climate_evidence": {"signals": []},
        }
    axis_sets = [
        set(manifest.get("terrain_pressure_axes", ()))
        for manifest in component_manifests
    ]
    union_axes = sorted(set().union(*axis_sets)) if axis_sets else []
    shared_axes = sorted(set.intersection(*axis_sets)) if axis_sets else []
    coexistence_modes = {manifest.get("coexistence_mode", "isolated_local") for manifest in component_manifests}
    local_signals = [
        set(manifest.get("maturation_evidence", {}).get("signals", ()))
        for manifest in component_manifests
    ]
    bridge_signals = [
        set(manifest.get("maturation_evidence", {}).get("signals", ()))
        for manifest in component_bridge_manifests
    ]

    if len(component_manifests) == 1:
        climate_mode = "single_local_climate"
    elif shared_axes and (
        "terrain_shared" in coexistence_modes or "pressure_adjacent" in coexistence_modes
    ):
        climate_mode = "shared_climate"
    elif shared_axes or "terrain_resonant" in coexistence_modes or "pressure_resonant" in coexistence_modes:
        climate_mode = "resonant_climate"
    elif bridge_state_counts:
        climate_mode = "bridge_climate"
    else:
        climate_mode = "scattered_climate"

    evidence_signals = []
    if len(component_manifests) > 1:
        evidence_signals.append("multi_local_climate")
    if shared_axes:
        evidence_signals.append("shared_axis_climate")
    elif union_axes:
        evidence_signals.append("distributed_axis_climate")
    if local_signals and all("boundary_aged" in signals for signals in local_signals):
        evidence_signals.append("boundary_supported_climate")
    if any("bridge_aged" in signals for signals in local_signals):
        evidence_signals.append("bridge_exposed_climate")
    if bridge_signals and any("time_aged" in signals for signals in bridge_signals):
        evidence_signals.append("time_aged_climate")
    if bridge_signals and any("durably_held" in signals for signals in bridge_signals):
        evidence_signals.append("durably_held_climate")

    return {
        "climate_mode": climate_mode,
        "shared_pressure_axes": shared_axes,
        "union_pressure_axes": union_axes,
        "climate_evidence": {"signals": evidence_signals},
    }


def _summarize_component_rhythm(
    component_manifests: List[Dict[str, object]],
    component_bridge_manifests: List[Dict[str, object]],
    shared_axes: List[str],
) -> Dict[str, object]:
    reaction_total = 0
    thickening_total = 0
    relocation_total = 0
    for manifest in component_manifests:
        reaction_counts = manifest.get("reaction_counts", {})
        reaction_total += sum(reaction_counts.values())
        thickening_total += reaction_counts.get("thickening", 0)
        relocation_total += reaction_counts.get("relocation", 0)

    support_round_total = 0
    repeated_support = False
    time_aged_bridge = False
    for manifest in component_bridge_manifests:
        support_round_total += manifest.get("support_round_count", 0)
        bridge_signals = set(manifest.get("maturation_evidence", {}).get("signals", ()))
        if "repeated_support" in bridge_signals:
            repeated_support = True
        if "time_aged" in bridge_signals:
            time_aged_bridge = True

    rhythm_signals = []
    if reaction_total >= 2:
        rhythm_signals.append("reaction_recurrent")
    if thickening_total >= 2:
        rhythm_signals.append("thickening_recurrent")
    if relocation_total >= 2:
        rhythm_signals.append("relocation_recurrent")
    if shared_axes:
        rhythm_signals.append("axis_continuous")
    if repeated_support or support_round_total >= 2:
        rhythm_signals.append("bridge_pulsed")
    if time_aged_bridge:
        rhythm_signals.append("time_spaced_rhythm")

    if "time_spaced_rhythm" in rhythm_signals and "bridge_pulsed" in rhythm_signals:
        rhythm_mode = "persistent_rhythm"
    elif "reaction_recurrent" in rhythm_signals or "bridge_pulsed" in rhythm_signals:
        rhythm_mode = "recurrent_rhythm"
    elif shared_axes:
        rhythm_mode = "steady_rhythm"
    else:
        rhythm_mode = "sparse_rhythm"

    return {
        "rhythm_mode": rhythm_mode,
        "rhythm_evidence": {
            "signals": rhythm_signals,
            "reaction_total": reaction_total,
            "support_round_total": support_round_total,
        },
    }


def _summarize_component_recurrence(
    component_manifests: List[Dict[str, object]],
    component_bridge_manifests: List[Dict[str, object]],
    rhythm_evidence: Dict[str, object],
) -> Dict[str, object]:
    local_recurrence = 0
    local_thickening_presence = 0
    for manifest in component_manifests:
        reaction_counts = manifest.get("reaction_counts", {})
        local_recurrence += reaction_counts.get("thickening", 0) + reaction_counts.get("relocation", 0)
        if reaction_counts.get("thickening", 0) > 0:
            local_thickening_presence += 1

    bridge_round_total = 0
    time_aged_count = 0
    durable_count = 0
    for manifest in component_bridge_manifests:
        bridge_round_total += manifest.get("support_round_count", 0)
        signals = set(manifest.get("maturation_evidence", {}).get("signals", ()))
        if "time_aged" in signals:
            time_aged_count += 1
        if "durably_held" in signals:
            durable_count += 1

    recurrence_signals = []
    if local_recurrence >= 2:
        recurrence_signals.append("local_returning")
    if local_thickening_presence >= 2:
        recurrence_signals.append("multi_space_thickening")
    if bridge_round_total >= 2:
        recurrence_signals.append("bridge_returning")
    if time_aged_count >= 1:
        recurrence_signals.append("time_spaced_return")
    if durable_count >= 1:
        recurrence_signals.append("durable_return")
    if "axis_continuous" in rhythm_evidence.get("signals", ()):
        recurrence_signals.append("axis_recurrent")

    if "durable_return" in recurrence_signals and "time_spaced_return" in recurrence_signals:
        recurrence_mode = "cadenced_recurrence"
    elif "bridge_returning" in recurrence_signals or "local_returning" in recurrence_signals:
        recurrence_mode = "returning_recurrence"
    elif "axis_recurrent" in recurrence_signals:
        recurrence_mode = "lingering_recurrence"
    else:
        recurrence_mode = "sparse_recurrence"

    return {
        "recurrence_mode": recurrence_mode,
        "recurrence_evidence": {
            "signals": recurrence_signals,
            "local_recurrence": local_recurrence,
            "bridge_round_total": bridge_round_total,
        },
    }


def _summarize_component_memory(
    component_manifests: List[Dict[str, object]],
    component_bridge_manifests: List[Dict[str, object]],
    recurrence_evidence: Dict[str, object],
) -> Dict[str, object]:
    local_memory_count = 0
    bridge_memory_count = 0
    for manifest in component_manifests:
        signals = set(manifest.get("maturation_evidence", {}).get("signals", ()))
        if "boundary_aged" in signals or "reentry_aged" in signals:
            local_memory_count += 1
    for manifest in component_bridge_manifests:
        signals = set(manifest.get("maturation_evidence", {}).get("signals", ()))
        if "bridge_exposed" in signals or "time_aged" in signals or "durably_held" in signals:
            bridge_memory_count += 1

    recurrence_signals = set(recurrence_evidence.get("signals", ()))
    memory_signals = []
    if local_memory_count >= 1:
        memory_signals.append("local_memory_present")
    if local_memory_count >= 2:
        memory_signals.append("multi_local_memory")
    if bridge_memory_count >= 1:
        memory_signals.append("bridge_memory_present")
    if bridge_memory_count >= 2:
        memory_signals.append("persistent_bridge_memory")
    if "durable_return" in recurrence_signals:
        memory_signals.append("durable_return_memory")
    if "time_spaced_return" in recurrence_signals:
        memory_signals.append("time_spaced_memory")
    if "axis_recurrent" in recurrence_signals:
        memory_signals.append("axis_memory")

    if "durable_return_memory" in memory_signals and "persistent_bridge_memory" in memory_signals:
        memory_mode = "persistent_memory"
    elif "bridge_memory_present" in memory_signals or "local_memory_present" in memory_signals:
        memory_mode = "retained_memory"
    elif "axis_memory" in memory_signals:
        memory_mode = "lingering_memory"
    else:
        memory_mode = "sparse_memory"

    return {
        "memory_mode": memory_mode,
        "memory_evidence": {
            "signals": memory_signals,
            "local_memory_count": local_memory_count,
            "bridge_memory_count": bridge_memory_count,
        },
    }


def _summarize_component_retention(memory_evidence: Dict[str, object]) -> Dict[str, object]:
    memory_signals = set(memory_evidence.get("signals", ()))
    retention_signals = []
    if "local_memory_present" in memory_signals or "bridge_memory_present" in memory_signals:
        retention_signals.append("memory_retained")
    if "persistent_bridge_memory" in memory_signals or "durable_return_memory" in memory_signals:
        retention_signals.append("durably_retained")
    if "time_spaced_memory" in memory_signals and "durably_retained" not in retention_signals:
        retention_signals.append("slowly_fading")
    if "axis_memory" in memory_signals and "memory_retained" in retention_signals:
        retention_signals.append("axis_lingering")
    if not retention_signals and memory_signals:
        retention_signals.append("weakly_retained")

    if "durably_retained" in retention_signals:
        retention_mode = "retained_terrain"
    elif "slowly_fading" in retention_signals or "axis_lingering" in retention_signals:
        retention_mode = "fading_terrain"
    elif "memory_retained" in retention_signals:
        retention_mode = "held_terrain"
    else:
        retention_mode = "sparse_retention"

    return {
        "retention_mode": retention_mode,
        "retention_evidence": {
            "signals": retention_signals,
        },
    }


def _summarize_component_forgetting(
    memory_evidence: Dict[str, object],
    retention_evidence: Dict[str, object],
) -> Dict[str, object]:
    memory_signals = set(memory_evidence.get("signals", ()))
    retention_signals = set(retention_evidence.get("signals", ()))
    forgetting_signals = []

    if (
        "time_spaced_memory" in memory_signals
        or (
            "bridge_memory_present" in memory_signals
            and "persistent_bridge_memory" not in memory_signals
            and "durable_return_memory" not in memory_signals
        )
    ) and "durably_retained" not in retention_signals:
        forgetting_signals.append("forgetting_trace")
    if "axis_memory" in memory_signals and "persistent_bridge_memory" not in memory_signals:
        forgetting_signals.append("lingering_without_hold")
    if "weakly_retained" in retention_signals or "slowly_fading" in retention_signals:
        forgetting_signals.append("fading_hold")

    if "fading_hold" in forgetting_signals and "forgetting_trace" in forgetting_signals:
        forgetting_mode = "active_fading"
    elif forgetting_signals:
        forgetting_mode = "light_forgetting"
    else:
        forgetting_mode = "held_memory"

    return {
        "forgetting_mode": forgetting_mode,
        "forgetting_evidence": {
            "signals": forgetting_signals,
        },
    }
