from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Set, Tuple
from uuid import uuid4

from app.core.states import BridgeState, CellState, LocalSpaceState, SeedState
from app.events.schema import EventRecord, to_record as event_to_record, utc_now_iso
from app.models.entities import (
    BridgeTrace,
    LocalSpace,
    Material,
    PointSeed,
    PressureAxis,
    PressureProfile,
    SpaceBoundary,
    SpaceCell,
    SupportRef,
    Trace,
    to_record,
)
from app.runtime.bootstrap import bootstrap_runtime_layout
from app.runtime.file_store import JsonDirectoryStore, JsonlEventStore


class FormationService:
    def __init__(self, runtime_root: Path) -> None:
        self.runtime_root = runtime_root
        bootstrap_runtime_layout(runtime_root)
        self.materials = JsonDirectoryStore(runtime_root / "core" / "materials")
        self.traces = JsonDirectoryStore(runtime_root / "core" / "traces")
        self.pressures = JsonDirectoryStore(runtime_root / "core" / "pressure_profiles")
        self.seeds = JsonDirectoryStore(runtime_root / "core" / "point_seeds")
        self.cells = JsonDirectoryStore(runtime_root / "core" / "space_cells")
        self.local_spaces = JsonDirectoryStore(runtime_root / "core" / "local_spaces")
        self.bridges = JsonDirectoryStore(runtime_root / "core" / "bridge_traces")
        self.space_manifests = JsonDirectoryStore(runtime_root / "manifests" / "reactive_spaces")
        self.cell_manifests = JsonDirectoryStore(runtime_root / "manifests" / "reactive_cells")
        self.bridge_manifests = JsonDirectoryStore(runtime_root / "manifests" / "bridges")
        self.events = JsonlEventStore(runtime_root / "events" / "formation_events.jsonl")

    def ingest_material(
        self,
        raw_payload: str,
        actor_id: str,
        session_id: str,
        project_id: str,
        source_type: str,
        source_ref: str,
        family_id: str = None,
        lineage_refs: Sequence[str] = (),
    ) -> Material:
        return self.ingest_material_with_role(
            raw_payload=raw_payload,
            actor_id=actor_id,
            session_id=session_id,
            project_id=project_id,
            source_type=source_type,
            source_ref=source_ref,
            formation_role=None,
            family_id=family_id,
            lineage_refs=lineage_refs,
        )

    def ingest_material_with_role(
        self,
        raw_payload: str,
        actor_id: str,
        session_id: str,
        project_id: str,
        source_type: str,
        source_ref: str,
        formation_role: Optional[str],
        family_id: str = None,
        lineage_refs: Sequence[str] = (),
    ) -> Material:
        metadata = {}
        if formation_role is not None:
            metadata["formation_role"] = formation_role
        material = Material(
            material_id=self._next_id("mat"),
            raw_payload=raw_payload,
            created_at=utc_now_iso(),
            actor_id=actor_id,
            session_id=session_id,
            project_id=project_id,
            source_type=source_type,
            source_ref=source_ref,
            family_id=family_id,
            lineage_refs=tuple(lineage_refs),
            metadata=metadata,
        )
        self.materials.put(material.material_id, to_record(material))
        self._append_event(
            "material_ingested",
            "material",
            material.material_id,
            {"source_ref": source_ref, "formation_role": formation_role},
        )
        return material

    def register_trace(
        self,
        material_refs: Sequence[str],
        evidence_kind: str,
        support_refs: Sequence[SupportRef],
        note: str = None,
    ) -> Trace:
        trace = Trace(
            trace_id=self._next_id("trc"),
            material_refs=tuple(material_refs),
            evidence_kind=evidence_kind,
            support_refs=tuple(support_refs),
            note=note,
        )
        self.traces.put(trace.trace_id, to_record(trace))
        self._append_event("trace_registered", "trace", trace.trace_id, {"evidence_kind": evidence_kind})
        return trace

    def create_pressure_profile(
        self,
        axes: Sequence[PressureAxis],
        support_refs: Sequence[SupportRef] = (),
    ) -> PressureProfile:
        profile = PressureProfile(
            profile_id=self._next_id("prs"),
            axes=tuple(axes),
            created_at=utc_now_iso(),
            support_refs=tuple(support_refs),
        )
        self.pressures.put(profile.profile_id, to_record(profile))
        self._append_event("pressure_profile_created", "pressure_profile", profile.profile_id, {"axis_count": len(profile.axes)})
        return profile

    def create_point_seed_candidate(
        self,
        material_refs: Sequence[str],
        trace_refs: Sequence[str],
        pressure_profile_id: str,
        reentering: bool = False,
    ) -> PointSeed:
        state = SeedState.REENTERING if reentering else SeedState.FORMING
        seed = PointSeed(
            seed_id=self._next_id("sed"),
            material_refs=tuple(material_refs),
            trace_refs=tuple(trace_refs),
            pressure_profile_id=pressure_profile_id,
            state=state,
            created_at=utc_now_iso(),
        )
        self.seeds.put(seed.seed_id, to_record(seed))
        self._append_event("point_seed_created", "point_seed", seed.seed_id, {"state": seed.state.value})
        return seed

    def create_reentry_seed_for_family(
        self,
        family_id: str,
        material_refs: Sequence[str],
        trace_refs: Sequence[str],
        pressure_profile_id: str,
    ) -> PointSeed:
        prior_seed_ids = tuple(self._find_seed_ids_for_family(family_id))
        seed = PointSeed(
            seed_id=self._next_id("sed"),
            material_refs=tuple(material_refs),
            trace_refs=tuple(trace_refs),
            pressure_profile_id=pressure_profile_id,
            state=SeedState.REENTERING,
            created_at=utc_now_iso(),
            lineage_refs=prior_seed_ids,
        )
        self.seeds.put(seed.seed_id, to_record(seed))
        self._append_event(
            "point_seed_reentered",
            "point_seed",
            seed.seed_id,
            {"family_id": family_id, "prior_seed_ids": list(prior_seed_ids)},
        )
        return seed

    def create_space_cell_candidate(
        self,
        material_refs: Sequence[str],
        trace_refs: Sequence[str],
        seed_refs: Sequence[str],
        pressure_profile_id: str,
        interior_refs: Sequence[str],
        exterior_refs: Sequence[str],
        cohesion_note: str = None,
    ) -> SpaceCell:
        boundary = SpaceBoundary(
            interior_refs=tuple(interior_refs),
            exterior_refs=tuple(exterior_refs),
            permeability_hint=0.5,
        )
        cell = SpaceCell(
            cell_id=self._next_id("cel"),
            material_refs=tuple(material_refs),
            trace_refs=tuple(trace_refs),
            seed_refs=tuple(seed_refs),
            pressure_profile_id=pressure_profile_id,
            boundary=boundary,
            state=CellState.CANDIDATE,
            cohesion_note=cohesion_note,
            created_at=utc_now_iso(),
        )
        self.cells.put(cell.cell_id, to_record(cell))
        self._append_event("space_cell_created", "space_cell", cell.cell_id, {"state": cell.state.value})
        self._bind_seeds_to_cell(seed_refs)
        self._write_cell_manifest(cell.cell_id)
        return cell

    def create_or_branch_space_cell_for_family(
        self,
        family_id: str,
        material_refs: Sequence[str],
        trace_refs: Sequence[str],
        seed_refs: Sequence[str],
        pressure_profile_id: str,
        interior_refs: Sequence[str],
        exterior_refs: Sequence[str],
        cohesion_note: str = None,
    ) -> SpaceCell:
        family_material_ids = self._find_material_ids_for_family(family_id)
        matching_cell = self._find_matching_family_cell(family_material_ids, pressure_profile_id)
        if matching_cell is None:
            cell = self.create_space_cell_candidate(
                material_refs=material_refs,
                trace_refs=trace_refs,
                seed_refs=seed_refs,
                pressure_profile_id=pressure_profile_id,
                interior_refs=interior_refs,
                exterior_refs=exterior_refs,
                cohesion_note=cohesion_note,
            )
            self._append_event(
                "space_cell_branched",
                "space_cell",
                cell.cell_id,
                {"family_id": family_id, "reason": "pressure_signature_mismatch_or_absent"},
            )
            return cell

        merged_material_refs = tuple(sorted(set(matching_cell["material_refs"]) | set(material_refs)))
        merged_trace_refs = tuple(sorted(set(matching_cell["trace_refs"]) | set(trace_refs)))
        merged_seed_refs = tuple(sorted(set(matching_cell["seed_refs"]) | set(seed_refs)))
        merged_interior_refs = tuple(
            sorted(set(matching_cell["boundary"]["interior_refs"]) | set(interior_refs))
        )
        merged_exterior_refs = tuple(
            sorted(set(matching_cell["boundary"]["exterior_refs"]) | set(exterior_refs))
        )
        merged_state = CellState.HELD if len(merged_seed_refs) > 1 else matching_cell["state"]
        updated_record = {
            "cell_id": matching_cell["cell_id"],
            "material_refs": list(merged_material_refs),
            "trace_refs": list(merged_trace_refs),
            "seed_refs": list(merged_seed_refs),
            "pressure_profile_id": matching_cell["pressure_profile_id"],
            "boundary": {
                "interior_refs": list(merged_interior_refs),
                "exterior_refs": list(merged_exterior_refs),
                "permeability_hint": matching_cell["boundary"]["permeability_hint"],
            },
            "state": merged_state.value if isinstance(merged_state, CellState) else merged_state,
            "cohesion_note": cohesion_note or matching_cell.get("cohesion_note"),
            "created_at": matching_cell["created_at"],
        }
        self.cells.put(matching_cell["cell_id"], updated_record)
        self._bind_seeds_to_cell(seed_refs)
        self._append_event(
            "space_cell_extended",
            "space_cell",
            matching_cell["cell_id"],
            {"family_id": family_id, "added_seed_ids": list(seed_refs)},
        )
        self._write_cell_manifest(matching_cell["cell_id"])
        return SpaceCell(
            cell_id=updated_record["cell_id"],
            material_refs=tuple(updated_record["material_refs"]),
            trace_refs=tuple(updated_record["trace_refs"]),
            seed_refs=tuple(updated_record["seed_refs"]),
            pressure_profile_id=updated_record["pressure_profile_id"],
            boundary=SpaceBoundary(
                interior_refs=tuple(updated_record["boundary"]["interior_refs"]),
                exterior_refs=tuple(updated_record["boundary"]["exterior_refs"]),
                permeability_hint=updated_record["boundary"]["permeability_hint"],
            ),
            state=CellState(updated_record["state"]),
            cohesion_note=updated_record["cohesion_note"],
            created_at=updated_record["created_at"],
        )

    def form_local_space(self, cell_refs: Sequence[str], pressure_profile_id: str = None) -> LocalSpace:
        state = self._derive_local_space_state(cell_refs)
        bridge_trace_refs = self._collect_bridge_refs_for_cells(cell_refs)
        local_space = LocalSpace(
            local_space_id=self._next_id("lsp"),
            cell_refs=tuple(cell_refs),
            pressure_profile_id=pressure_profile_id,
            state=state,
            created_at=utc_now_iso(),
            bridge_trace_refs=tuple(bridge_trace_refs),
        )
        self.local_spaces.put(local_space.local_space_id, to_record(local_space))
        self._append_event("local_space_formed", "local_space", local_space.local_space_id, {"cell_count": len(cell_refs)})
        self._write_local_space_manifest(local_space.local_space_id)
        self._refresh_all_local_space_manifests()
        return local_space

    def reactivate_space_cell(
        self,
        cell_id: str,
        reaction_kind: str,
        pressure_profile_id: Optional[str] = None,
        note: str = None,
        triggered_by_seed_ids: Sequence[str] = (),
    ) -> Dict[str, object]:
        if reaction_kind not in {"thickening", "split", "relocation"}:
            raise ValueError("unsupported reaction_kind: %s" % reaction_kind)

        cell_record = self.cells.get(cell_id)
        if not cell_record:
            raise ValueError("unknown cell_id: %s" % cell_id)

        updated_record = dict(cell_record)
        updated_record["state"] = self._next_cell_state_for_reaction(reaction_kind).value
        if pressure_profile_id is not None:
            updated_record["pressure_profile_id"] = pressure_profile_id
        if note:
            existing_note = updated_record.get("cohesion_note")
            updated_record["cohesion_note"] = note if not existing_note else "%s | %s" % (existing_note, note)
        self.cells.put(cell_id, updated_record)
        self._append_event(
            "space_cell_reacted",
            "space_cell",
            cell_id,
            {
                "reaction_kind": reaction_kind,
                "pressure_profile_id": pressure_profile_id,
                "triggered_by_seed_ids": list(triggered_by_seed_ids),
                "note": note,
            },
        )
        self._write_cell_manifest(cell_id)
        return updated_record

    def derive_bridge_trace_from_cells(
        self,
        from_local_space_id: str,
        to_local_space_id: str,
        via_cell_ids: Sequence[str],
        note: str = None,
    ) -> Optional[BridgeTrace]:
        relocation_events = [
            event
            for event in self.events.read_all()
            if event["event_type"] == "space_cell_reacted"
            and event["subject_id"] in via_cell_ids
            and event["payload"]["reaction_kind"] == "relocation"
        ]
        if not relocation_events:
            return None

        shared_boundary_strength = self._boundary_overlap_strength(via_cell_ids)
        support_round_count = self._bridge_support_round_count(
            from_local_space_id=from_local_space_id,
            to_local_space_id=to_local_space_id,
        ) + 1
        temporal_spacing_ok = self._bridge_temporal_spacing_satisfied(
            from_local_space_id=from_local_space_id,
            to_local_space_id=to_local_space_id,
        )
        state = (
            BridgeState.HELD
            if (
                shared_boundary_strength >= 1
                and len(relocation_events) >= 2
                and support_round_count >= 2
                and temporal_spacing_ok
            )
            else BridgeState.OBSERVED
        )
        bridge = BridgeTrace(
            bridge_id=self._next_id("brg"),
            from_local_space_id=from_local_space_id,
            to_local_space_id=to_local_space_id,
            trace_refs=tuple(event["event_id"] for event in relocation_events),
            state=state,
            created_at=utc_now_iso(),
            note=note,
        )
        self.bridges.put(bridge.bridge_id, to_record(bridge))
        self._append_event(
            "bridge_trace_derived",
            "bridge_trace",
            bridge.bridge_id,
            {
                "state": bridge.state.value,
                "via_cell_ids": list(via_cell_ids),
                "relocation_event_count": len(relocation_events),
                "support_round_count": support_round_count,
                "temporal_spacing_ok": temporal_spacing_ok,
                "durability_mode": self._bridge_durability_mode(bridge.state),
            },
        )
        self._attach_bridge_to_local_space(from_local_space_id, bridge.bridge_id)
        self._attach_bridge_to_local_space(to_local_space_id, bridge.bridge_id)
        self._write_bridge_manifest(bridge.bridge_id)
        return bridge

    def derive_bridge_trace_from_local_spaces(
        self,
        from_local_space_id: str,
        to_local_space_id: str,
        note: str = None,
    ) -> Optional[BridgeTrace]:
        from_space = self.local_spaces.get(from_local_space_id)
        to_space = self.local_spaces.get(to_local_space_id)
        if not from_space or not to_space:
            return None
        via_cell_ids = tuple(
            sorted(
                set(from_space.get("cell_refs", ())) | set(to_space.get("cell_refs", ()))
            )
        )
        if not via_cell_ids:
            return None
        return self.derive_bridge_trace_from_cells(
            from_local_space_id=from_local_space_id,
            to_local_space_id=to_local_space_id,
            via_cell_ids=via_cell_ids,
            note=note,
        )

    def register_bridge_trace(
        self,
        from_local_space_id: str,
        to_local_space_id: str,
        trace_refs: Sequence[str],
        note: str = None,
    ) -> BridgeTrace:
        bridge = BridgeTrace(
            bridge_id=self._next_id("brg"),
            from_local_space_id=from_local_space_id,
            to_local_space_id=to_local_space_id,
            trace_refs=tuple(trace_refs),
            state=BridgeState.CANDIDATE,
            created_at=utc_now_iso(),
            note=note,
        )
        self.bridges.put(bridge.bridge_id, to_record(bridge))
        self._append_event("bridge_trace_registered", "bridge_trace", bridge.bridge_id, {"state": bridge.state.value})
        self._attach_bridge_to_local_space(from_local_space_id, bridge.bridge_id)
        self._attach_bridge_to_local_space(to_local_space_id, bridge.bridge_id)
        self._write_bridge_manifest(bridge.bridge_id)
        return bridge

    def _bind_seeds_to_cell(self, seed_refs: Sequence[str]) -> None:
        for seed_id in seed_refs:
            seed_record = self.seeds.get(seed_id)
            if not seed_record:
                continue
            seed_record["state"] = SeedState.CELL_BOUND.value
            self.seeds.put(seed_id, seed_record)
            self._append_event("point_seed_state_changed", "point_seed", seed_id, {"state": SeedState.CELL_BOUND.value})

    def _attach_bridge_to_local_space(self, local_space_id: str, bridge_id: str) -> None:
        local_space = self.local_spaces.get(local_space_id)
        if not local_space:
            return
        bridge_refs = sorted(set(local_space.get("bridge_trace_refs", ())) | {bridge_id})
        local_space["bridge_trace_refs"] = bridge_refs
        if local_space.get("state") != LocalSpaceState.BOUNDARY_HEAVY.value:
            local_space["state"] = LocalSpaceState.BRIDGE_EXPOSED.value
        self.local_spaces.put(local_space_id, local_space)
        self._append_event(
            "local_space_bridge_attached",
            "local_space",
            local_space_id,
            {"bridge_id": bridge_id, "state": local_space["state"]},
        )
        self._write_local_space_manifest(local_space_id)
        self._refresh_all_local_space_manifests()

    def _refresh_all_local_space_manifests(self) -> None:
        for local_space_id in self.local_spaces.list_ids():
            self._write_local_space_manifest(local_space_id)

    def _find_seed_ids_for_family(self, family_id: str) -> List[str]:
        family_material_ids = self._find_material_ids_for_family(family_id)
        if not family_material_ids:
            return []
        prior_seed_ids: List[str] = []
        for record in self.seeds.read_all():
            material_refs = set(record.get("material_refs", ()))
            if material_refs & family_material_ids:
                prior_seed_ids.append(record["seed_id"])
        return prior_seed_ids

    def _find_material_ids_for_family(self, family_id: str) -> Set[str]:
        return {
            record["material_id"]
            for record in self.materials.read_all()
            if record.get("family_id") == family_id
        }

    def _find_matching_family_cell(
        self,
        family_material_ids: Set[str],
        pressure_profile_id: str,
    ) -> Dict[str, object]:
        target_signature = self._pressure_signature(pressure_profile_id)
        for record in self.cells.read_all():
            material_refs = set(record.get("material_refs", ()))
            if not (material_refs & family_material_ids):
                continue
            if self._pressure_signature(record["pressure_profile_id"]) == target_signature:
                return record
        return None

    def _pressure_signature(self, profile_id: str) -> Tuple[str, ...]:
        profile = self.pressures.get(profile_id)
        if not profile:
            return ()
        signature = []
        for axis in profile.get("axes", []):
            signature.append("%s:%s" % (axis["axis"], self._strength_bucket(axis["strength_hint"])))
        return tuple(sorted(signature))

    def _derive_local_space_state(self, cell_refs: Sequence[str]) -> LocalSpaceState:
        if not cell_refs:
            return LocalSpaceState.SPARSE
        if len(cell_refs) == 1:
            return LocalSpaceState.FORMING

        cell_records = [self.cells.get(cell_id) for cell_id in cell_refs]
        cell_records = [record for record in cell_records if record is not None]
        reaction_events = [
            event
            for event in self.events.read_all()
            if event["event_type"] == "space_cell_reacted" and event["subject_id"] in cell_refs
        ]
        if any(event["payload"]["reaction_kind"] == "relocation" for event in reaction_events):
            return LocalSpaceState.BRIDGE_EXPOSED
        if any(event["payload"]["reaction_kind"] == "split" for event in reaction_events):
            return LocalSpaceState.BOUNDARY_HEAVY
        if self._is_stable_local_candidate(cell_records, reaction_events):
            return LocalSpaceState.STABLE_LOCAL
        if self._has_shared_boundary_tendency(cell_records):
            return LocalSpaceState.FORMING
        return LocalSpaceState.SPARSE

    def _has_shared_boundary_tendency(self, cell_records: Sequence[Dict[str, object]]) -> bool:
        if len(cell_records) < 2:
            return False
        boundary_sets = [
            set(record["boundary"]["exterior_refs"]) | set(record["boundary"]["interior_refs"])
            for record in cell_records
        ]
        shared_refs = set.intersection(*boundary_sets) if boundary_sets else set()
        return bool(shared_refs)

    def _is_stable_local_candidate(
        self,
        cell_records: Sequence[Dict[str, object]],
        reaction_events: Sequence[Dict[str, object]],
    ) -> bool:
        if not self._has_shared_boundary_tendency(cell_records):
            return False
        if not reaction_events:
            return False
        if not all(record["state"] == CellState.HELD.value for record in cell_records):
            return False
        if self._has_branch_mismatch(cell_records):
            return False
        pressure_ids = {record["pressure_profile_id"] for record in cell_records}
        if len({self._pressure_signature(profile_id) for profile_id in pressure_ids}) != 1:
            return False
        boundary_durability = self._boundary_durability_score(cell_records)
        if boundary_durability < len(cell_records):
            return False
        thickening_count = sum(
            1 for event in reaction_events if event["payload"]["reaction_kind"] == "thickening"
        )
        return thickening_count >= 1

    def _has_branch_mismatch(self, cell_records: Sequence[Dict[str, object]]) -> bool:
        cell_ids = {record["cell_id"] for record in cell_records}
        for event in self.events.read_all():
            if event["event_type"] != "space_cell_branched":
                continue
            if event["subject_id"] not in cell_ids:
                continue
            if event["payload"].get("reason") == "pressure_signature_mismatch_or_absent":
                return True
        return False

    def _boundary_durability_score(self, cell_records: Sequence[Dict[str, object]]) -> int:
        if len(cell_records) < 2:
            return 0
        shared_strength = self._boundary_overlap_strength(
            [record["cell_id"] for record in cell_records]
        )
        held_count = sum(1 for record in cell_records if record["state"] == CellState.HELD.value)
        return shared_strength * held_count

    def _collect_bridge_refs_for_cells(self, cell_refs: Sequence[str]) -> List[str]:
        bridge_refs: List[str] = []
        for bridge in self.bridges.read_all():
            trace_refs = set(bridge.get("trace_refs", ()))
            matching_reaction_event_ids = {
                event["event_id"]
                for event in self.events.read_all()
                if event["event_type"] == "space_cell_reacted"
                and event["subject_id"] in cell_refs
                and event["payload"]["reaction_kind"] == "relocation"
            }
            if trace_refs & matching_reaction_event_ids:
                bridge_refs.append(bridge["bridge_id"])
        return bridge_refs

    def _write_local_space_manifest(self, local_space_id: str) -> None:
        local_space = self.local_spaces.get(local_space_id)
        if not local_space:
            return
        cell_records = [self.cells.get(cell_id) for cell_id in local_space.get("cell_refs", ())]
        cell_records = [record for record in cell_records if record is not None]
        reaction_events = [
            event
            for event in self.events.read_all()
            if event["event_type"] == "space_cell_reacted" and event["subject_id"] in local_space.get("cell_refs", ())
        ]
        manifest = {
            "manifest_id": "space_manifest_%s" % local_space_id,
            "local_space_id": local_space_id,
            "state": local_space["state"],
            "cell_ids": list(local_space.get("cell_refs", ())),
            "bridge_trace_refs": list(local_space.get("bridge_trace_refs", ())),
            "pressure_profile_id": local_space.get("pressure_profile_id"),
            "shared_boundary_strength": self._boundary_overlap_strength(local_space.get("cell_refs", ())),
            "boundary_durability_score": self._boundary_durability_score(cell_records),
            "reaction_counts": self._count_reaction_kinds(reaction_events),
            "has_branch_mismatch": self._has_branch_mismatch(cell_records),
            "cell_states": [record["state"] for record in cell_records],
            "maturation_evidence": self._local_space_maturation_evidence(local_space, cell_records, reaction_events),
            "terrain_pressure_signature": self._pressure_signature(local_space.get("pressure_profile_id")),
            "terrain_pressure_axes": sorted(self._pressure_axis_names(local_space.get("pressure_profile_id"))),
            "adjacent_local_space_ids": self._adjacent_local_space_ids(local_space_id),
            "coexistence_mode": self._local_space_coexistence_mode(local_space_id),
            "generated_at": utc_now_iso(),
        }
        self.space_manifests.put(local_space_id, manifest)

    def _write_cell_manifest(self, cell_id: str) -> None:
        cell = self.cells.get(cell_id)
        if not cell:
            return
        reaction_events = [
            event
            for event in self.events.read_all()
            if event["event_type"] == "space_cell_reacted" and event["subject_id"] == cell_id
        ]
        manifest = {
            "manifest_id": "cell_manifest_%s" % cell_id,
            "cell_id": cell_id,
            "state": cell["state"],
            "pressure_profile_id": cell["pressure_profile_id"],
            "material_count": len(cell.get("material_refs", ())),
            "trace_count": len(cell.get("trace_refs", ())),
            "seed_count": len(cell.get("seed_refs", ())),
            "boundary_strength": len(
                set(cell["boundary"]["interior_refs"]) & set(cell["boundary"]["exterior_refs"])
            ),
            "reaction_counts": self._count_reaction_kinds(reaction_events),
            "cohesion_note": cell.get("cohesion_note"),
            "generated_at": utc_now_iso(),
        }
        self.cell_manifests.put(cell_id, manifest)

    def _write_bridge_manifest(self, bridge_id: str) -> None:
        bridge = self.bridges.get(bridge_id)
        if not bridge:
            return
        support_round_count = self._bridge_support_round_count(
            from_local_space_id=bridge["from_local_space_id"],
            to_local_space_id=bridge["to_local_space_id"],
        )
        temporal_spacing_ok = self._bridge_temporal_spacing_satisfied(
            from_local_space_id=bridge["from_local_space_id"],
            to_local_space_id=bridge["to_local_space_id"],
            reference_created_at=bridge["created_at"],
            exclude_bridge_id=bridge_id,
        )
        manifest = {
            "manifest_id": "bridge_manifest_%s" % bridge_id,
            "bridge_id": bridge_id,
            "state": bridge["state"],
            "from_local_space_id": bridge["from_local_space_id"],
            "to_local_space_id": bridge["to_local_space_id"],
            "trace_ref_count": len(bridge.get("trace_refs", ())),
            "support_round_count": support_round_count,
            "temporal_spacing_ok": temporal_spacing_ok,
            "durability_mode": self._bridge_durability_mode(BridgeState(bridge["state"])),
            "maturation_evidence": self._bridge_maturation_evidence(
                support_round_count=support_round_count,
                temporal_spacing_ok=temporal_spacing_ok,
                state=BridgeState(bridge["state"]),
            ),
            "note": bridge.get("note"),
            "generated_at": utc_now_iso(),
        }
        self.bridge_manifests.put(bridge_id, manifest)

    @staticmethod
    def _count_reaction_kinds(reaction_events: Sequence[Dict[str, object]]) -> Dict[str, int]:
        counts = {"thickening": 0, "split": 0, "relocation": 0}
        for event in reaction_events:
            kind = event["payload"]["reaction_kind"]
            counts[kind] = counts.get(kind, 0) + 1
        return counts

    def _boundary_overlap_strength(self, cell_ids: Sequence[str]) -> int:
        cell_records = [self.cells.get(cell_id) for cell_id in cell_ids]
        cell_records = [record for record in cell_records if record is not None]
        if len(cell_records) < 2:
            return 0
        boundary_sets = [
            set(record["boundary"]["interior_refs"]) | set(record["boundary"]["exterior_refs"])
            for record in cell_records
        ]
        shared_refs = set.intersection(*boundary_sets) if boundary_sets else set()
        return len(shared_refs)

    def _bridge_support_round_count(self, from_local_space_id: str, to_local_space_id: str) -> int:
        normalized_pair = tuple(sorted((from_local_space_id, to_local_space_id)))
        count = 0
        for bridge in self.bridges.read_all():
            bridge_pair = tuple(
                sorted((bridge["from_local_space_id"], bridge["to_local_space_id"]))
            )
            if bridge_pair == normalized_pair:
                count += 1
        return count

    def _bridge_temporal_spacing_satisfied(
        self,
        from_local_space_id: str,
        to_local_space_id: str,
        reference_created_at: Optional[str] = None,
        exclude_bridge_id: Optional[str] = None,
    ) -> bool:
        normalized_pair = tuple(sorted((from_local_space_id, to_local_space_id)))
        prior_created_at: List[datetime] = []
        for bridge in self.bridges.read_all():
            if exclude_bridge_id is not None and bridge.get("bridge_id") == exclude_bridge_id:
                continue
            bridge_pair = tuple(
                sorted((bridge["from_local_space_id"], bridge["to_local_space_id"]))
            )
            if bridge_pair != normalized_pair:
                continue
            created_at = bridge.get("created_at")
            if created_at:
                prior_created_at.append(datetime.fromisoformat(created_at.replace("Z", "+00:00")))
        if not prior_created_at:
            return False
        reference_time = (
            datetime.fromisoformat(reference_created_at.replace("Z", "+00:00"))
            if reference_created_at
            else datetime.now(timezone.utc)
        )
        latest_prior = max(prior_created_at)
        return (reference_time - latest_prior).total_seconds() >= 60

    @staticmethod
    def _bridge_durability_mode(state: BridgeState) -> str:
        if state == BridgeState.HELD:
            return "durable_holding"
        if state == BridgeState.OBSERVED:
            return "exposed_adjacency"
        return "candidate_exposure"

    def _local_space_maturation_evidence(
        self,
        local_space: Dict[str, object],
        cell_records: Sequence[Dict[str, object]],
        reaction_events: Sequence[Dict[str, object]],
    ) -> Dict[str, object]:
        boundary_durability = self._boundary_durability_score(cell_records)
        bridge_ref_count = len(local_space.get("bridge_trace_refs", ()))
        thickening_count = sum(
            1 for event in reaction_events if event["payload"]["reaction_kind"] == "thickening"
        )
        maturation_signals = []
        if boundary_durability >= len(cell_records) and cell_records:
            maturation_signals.append("boundary_aged")
        if len({record["cell_id"] for record in cell_records for _ in record.get("seed_refs", [])}) >= 2:
            maturation_signals.append("reentry_aged")
        if bridge_ref_count > 0:
            maturation_signals.append("bridge_aged")
        if thickening_count > 0:
            maturation_signals.append("thickening_present")
        return {
            "signals": maturation_signals,
            "boundary_durability_score": boundary_durability,
            "bridge_ref_count": bridge_ref_count,
            "thickening_count": thickening_count,
        }

    def _adjacent_local_space_ids(self, local_space_id: str) -> List[str]:
        adjacent_ids = set()
        for bridge in self.bridges.read_all():
            if bridge["from_local_space_id"] == local_space_id:
                adjacent_ids.add(bridge["to_local_space_id"])
            if bridge["to_local_space_id"] == local_space_id:
                adjacent_ids.add(bridge["from_local_space_id"])
        return sorted(adjacent_ids)

    def _local_space_coexistence_mode(self, local_space_id: str) -> str:
        local_space = self.local_spaces.get(local_space_id)
        if not local_space:
            return "isolated_local"
        current_signature = self._pressure_signature(local_space.get("pressure_profile_id"))
        current_axes = self._pressure_axis_names(local_space.get("pressure_profile_id"))
        adjacent_ids = self._adjacent_local_space_ids(local_space_id)
        pressure_adjacent = False
        pressure_resonant = False
        for record in self.local_spaces.read_all():
            if record["local_space_id"] == local_space_id:
                continue
            other_signature = self._pressure_signature(record.get("pressure_profile_id"))
            other_axes = self._pressure_axis_names(record.get("pressure_profile_id"))
            if other_signature == current_signature:
                pressure_adjacent = True
            elif current_axes and other_axes and current_axes & other_axes:
                pressure_resonant = True
        if adjacent_ids and pressure_adjacent:
            return "terrain_shared"
        if adjacent_ids and pressure_resonant:
            return "terrain_resonant"
        if adjacent_ids:
            return "bridge_adjacent"
        if pressure_adjacent:
            return "pressure_adjacent"
        if pressure_resonant:
            return "pressure_resonant"
        return "isolated_local"

    def _pressure_axis_names(self, pressure_profile_id: Optional[str]) -> Set[str]:
        profile = self.pressures.get(pressure_profile_id) if pressure_profile_id else None
        if not profile:
            return set()
        return {axis["axis"] for axis in profile.get("axes", ())}

    @staticmethod
    def _bridge_maturation_evidence(
        support_round_count: int,
        temporal_spacing_ok: bool,
        state: BridgeState,
    ) -> Dict[str, object]:
        signals = []
        if support_round_count >= 1:
            signals.append("bridge_exposed")
        if support_round_count >= 2:
            signals.append("repeated_support")
        if temporal_spacing_ok:
            signals.append("time_aged")
        if state == BridgeState.HELD:
            signals.append("durably_held")
        return {
            "signals": signals,
            "support_round_count": support_round_count,
            "temporal_spacing_ok": temporal_spacing_ok,
        }

    @staticmethod
    def _next_cell_state_for_reaction(reaction_kind: str) -> CellState:
        if reaction_kind == "thickening":
            return CellState.HELD
        if reaction_kind == "split":
            return CellState.UNSTABLE
        return CellState.REENTERING

    @staticmethod
    def _strength_bucket(strength_hint: float) -> str:
        if strength_hint < 0.4:
            return "low"
        if strength_hint < 0.75:
            return "mid"
        return "high"

    def _append_event(self, event_type: str, subject_kind: str, subject_id: str, payload: dict) -> None:
        event = EventRecord(
            event_id=self._next_id("evt"),
            event_type=event_type,
            subject_kind=subject_kind,
            subject_id=subject_id,
            payload=payload,
        )
        self.events.append(event_to_record(event))

    @staticmethod
    def _next_id(prefix: str) -> str:
        return "%s_%s" % (prefix, uuid4().hex[:12])
