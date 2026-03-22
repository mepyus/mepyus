import tempfile
import unittest
from pathlib import Path
import subprocess
import json

from app.core.formation_service import FormationService
from app.core.states import BridgeState, CellState, LocalSpaceState, SeedState
from app.runtime.bootstrap import bootstrap_runtime_layout, find_legacy_runtime_directories
from app.runtime.dust_field import build_dust_field_data, render_dust_field_html, write_dust_field_view
from app.runtime.observer import (
    build_reactive_space_observation,
    build_scoped_reactive_space_observation,
    build_session_timeline,
)
from app.runtime.reread_audit import build_reread_audit
from app.runtime.reporting import should_issue_workspace_report
from app.runtime.reactive_space_report import write_reactive_space_report
from app.runtime.graph_view import render_space_graph_view_html, write_space_graph_view
from app.runtime.live_input import ingest_live_input
from app.runtime.stage0_handoff import build_handoff_materials, run_stage0_handoff
from app.runtime.scale_review import build_first_scale_review
from app.runtime.workspace_report import write_workspace_report
from app.runtime.workspace_manifest import build_workspace_manifest, write_workspace_manifest
from app.models.entities import PressureAxis, SupportRef


class FormationServiceTest(unittest.TestCase):
    def test_material_to_local_space_flow_preserves_append_only_events(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            service = FormationService(Path(tmpdir))

            material = service.ingest_material(
                raw_payload="material stays raw",
                actor_id="actor-1",
                session_id="session-1",
                project_id="project-1",
                source_type="note",
                source_ref="note-1",
                family_id="fam-1",
            )
            trace = service.register_trace(
                material_refs=[material.material_id],
                evidence_kind="recurrence",
                support_refs=[SupportRef(ref_kind="material", ref_id=material.material_id)],
            )
            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="temporal_pressure", strength_hint=0.7)]
            )
            seed = service.create_point_seed_candidate(
                material_refs=[material.material_id],
                trace_refs=[trace.trace_id],
                pressure_profile_id=pressure.profile_id,
            )
            cell = service.create_space_cell_candidate(
                material_refs=[material.material_id],
                trace_refs=[trace.trace_id],
                seed_refs=[seed.seed_id],
                pressure_profile_id=pressure.profile_id,
                interior_refs=[material.material_id, seed.seed_id],
                exterior_refs=["outside-context"],
                cohesion_note="weak but held",
            )
            local_space = service.form_local_space(
                cell_refs=[cell.cell_id],
                pressure_profile_id=pressure.profile_id,
            )

            self.assertEqual(material.raw_payload, "material stays raw")
            self.assertEqual(seed.state, SeedState.FORMING)
            self.assertEqual(cell.state, CellState.CANDIDATE)
            self.assertEqual(local_space.state, LocalSpaceState.FORMING)

            persisted_seed = service.seeds.get(seed.seed_id)
            cell_manifest = service.cell_manifests.get(cell.cell_id)
            self.assertEqual(persisted_seed["state"], SeedState.CELL_BOUND.value)
            self.assertEqual(cell_manifest["state"], CellState.CANDIDATE.value)

            event_rows = service.events.read_all()
            self.assertGreaterEqual(len(event_rows), 6)
            self.assertEqual(event_rows[0]["event_type"], "material_ingested")
            self.assertEqual(event_rows[-1]["event_type"], "local_space_formed")

    def test_material_ingest_helper_can_record_formation_role_without_changing_source_type(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            service = FormationService(Path(tmpdir))

            material = service.ingest_material_with_role(
                raw_payload="observer report payload",
                actor_id="actor-1",
                session_id="session-1",
                project_id="project-1",
                source_type="report",
                source_ref="report-1",
                formation_role="observer_material",
            )

            persisted = service.materials.get(material.material_id)
            event_rows = service.events.read_all()

            self.assertEqual(persisted["source_type"], "report")
            self.assertEqual(persisted["metadata"]["formation_role"], "observer_material")
            self.assertEqual(event_rows[-1]["payload"]["formation_role"], "observer_material")

    def test_family_reentry_opens_new_seed_path_without_overwriting_prior_seed(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            service = FormationService(Path(tmpdir))

            first_material = service.ingest_material(
                raw_payload="same family, first pass",
                actor_id="actor-1",
                session_id="session-1",
                project_id="project-1",
                source_type="note",
                source_ref="note-1",
                family_id="family-a",
            )
            second_material = service.ingest_material(
                raw_payload="same family, later pass",
                actor_id="actor-1",
                session_id="session-2",
                project_id="project-1",
                source_type="note",
                source_ref="note-2",
                family_id="family-a",
                lineage_refs=[first_material.material_id],
            )
            first_trace = service.register_trace(
                material_refs=[first_material.material_id],
                evidence_kind="co_occurrence",
                support_refs=[SupportRef(ref_kind="material", ref_id=first_material.material_id)],
            )
            second_trace = service.register_trace(
                material_refs=[second_material.material_id],
                evidence_kind="temporal_reentry",
                support_refs=[
                    SupportRef(ref_kind="material", ref_id=first_material.material_id),
                    SupportRef(ref_kind="material", ref_id=second_material.material_id),
                ],
            )
            first_pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="session_pressure", strength_hint=0.3)]
            )
            second_pressure = service.create_pressure_profile(
                axes=[
                    PressureAxis(axis="session_pressure", strength_hint=0.9),
                    PressureAxis(axis="recurrence_pressure", strength_hint=0.8),
                ]
            )

            first_seed = service.create_point_seed_candidate(
                material_refs=[first_material.material_id],
                trace_refs=[first_trace.trace_id],
                pressure_profile_id=first_pressure.profile_id,
            )
            reentry_seed = service.create_reentry_seed_for_family(
                family_id="family-a",
                material_refs=[second_material.material_id],
                trace_refs=[second_trace.trace_id],
                pressure_profile_id=second_pressure.profile_id,
            )

            persisted_first_seed = service.seeds.get(first_seed.seed_id)
            persisted_reentry_seed = service.seeds.get(reentry_seed.seed_id)
            event_rows = service.events.read_all()

            self.assertEqual(persisted_first_seed["state"], SeedState.FORMING.value)
            self.assertEqual(persisted_reentry_seed["state"], SeedState.REENTERING.value)
            self.assertEqual(persisted_reentry_seed["lineage_refs"], [first_seed.seed_id])
            self.assertEqual(len(list(service.seeds.list_ids())), 2)
            self.assertEqual(event_rows[-1]["event_type"], "point_seed_reentered")
            self.assertEqual(event_rows[-1]["payload"]["family_id"], "family-a")

    def test_bridge_trace_does_not_merge_spaces(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            service = FormationService(Path(tmpdir))
            left = service.form_local_space(cell_refs=["cell-a", "cell-b"])
            right = service.form_local_space(cell_refs=["cell-c", "cell-d"])

            bridge = service.register_bridge_trace(
                from_local_space_id=left.local_space_id,
                to_local_space_id=right.local_space_id,
                trace_refs=["trace-1"],
                note="possible relation only",
            )

            self.assertEqual(bridge.from_local_space_id, left.local_space_id)
            self.assertEqual(bridge.to_local_space_id, right.local_space_id)
            self.assertEqual(
                set(service.local_spaces.list_ids()),
                {left.local_space_id, right.local_space_id},
            )
            persisted_left = service.local_spaces.get(left.local_space_id)
            persisted_right = service.local_spaces.get(right.local_space_id)
            self.assertEqual(persisted_left["state"], LocalSpaceState.BRIDGE_EXPOSED.value)
            self.assertEqual(persisted_right["state"], LocalSpaceState.BRIDGE_EXPOSED.value)
            self.assertIn(bridge.bridge_id, persisted_left["bridge_trace_refs"])
            self.assertIn(bridge.bridge_id, persisted_right["bridge_trace_refs"])

    def test_matching_pressure_reuses_family_cell_but_shifted_pressure_branches_new_cell(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            service = FormationService(Path(tmpdir))

            first_material = service.ingest_material(
                raw_payload="family b first",
                actor_id="actor-1",
                session_id="session-1",
                project_id="project-1",
                source_type="note",
                source_ref="family-b-1",
                family_id="family-b",
            )
            second_material = service.ingest_material(
                raw_payload="family b second similar pressure",
                actor_id="actor-1",
                session_id="session-2",
                project_id="project-1",
                source_type="note",
                source_ref="family-b-2",
                family_id="family-b",
            )
            third_material = service.ingest_material(
                raw_payload="family b third shifted pressure",
                actor_id="actor-1",
                session_id="session-3",
                project_id="project-1",
                source_type="note",
                source_ref="family-b-3",
                family_id="family-b",
            )

            trace_one = service.register_trace(
                material_refs=[first_material.material_id],
                evidence_kind="recurrence",
                support_refs=[SupportRef(ref_kind="material", ref_id=first_material.material_id)],
            )
            trace_two = service.register_trace(
                material_refs=[second_material.material_id],
                evidence_kind="recurrence",
                support_refs=[SupportRef(ref_kind="material", ref_id=second_material.material_id)],
            )
            trace_three = service.register_trace(
                material_refs=[third_material.material_id],
                evidence_kind="contrast",
                support_refs=[SupportRef(ref_kind="material", ref_id=third_material.material_id)],
            )

            pressure_low = service.create_pressure_profile(
                axes=[PressureAxis(axis="session_pressure", strength_hint=0.3)]
            )
            pressure_low_again = service.create_pressure_profile(
                axes=[PressureAxis(axis="session_pressure", strength_hint=0.35)]
            )
            pressure_shifted = service.create_pressure_profile(
                axes=[
                    PressureAxis(axis="session_pressure", strength_hint=0.9),
                    PressureAxis(axis="tone_pressure", strength_hint=0.85),
                ]
            )

            seed_one = service.create_point_seed_candidate(
                material_refs=[first_material.material_id],
                trace_refs=[trace_one.trace_id],
                pressure_profile_id=pressure_low.profile_id,
            )
            seed_two = service.create_reentry_seed_for_family(
                family_id="family-b",
                material_refs=[second_material.material_id],
                trace_refs=[trace_two.trace_id],
                pressure_profile_id=pressure_low_again.profile_id,
            )
            seed_three = service.create_reentry_seed_for_family(
                family_id="family-b",
                material_refs=[third_material.material_id],
                trace_refs=[trace_three.trace_id],
                pressure_profile_id=pressure_shifted.profile_id,
            )

            first_cell = service.create_or_branch_space_cell_for_family(
                family_id="family-b",
                material_refs=[first_material.material_id],
                trace_refs=[trace_one.trace_id],
                seed_refs=[seed_one.seed_id],
                pressure_profile_id=pressure_low.profile_id,
                interior_refs=[first_material.material_id, seed_one.seed_id],
                exterior_refs=["outer-a"],
                cohesion_note="first hold",
            )
            reused_cell = service.create_or_branch_space_cell_for_family(
                family_id="family-b",
                material_refs=[second_material.material_id],
                trace_refs=[trace_two.trace_id],
                seed_refs=[seed_two.seed_id],
                pressure_profile_id=pressure_low_again.profile_id,
                interior_refs=[second_material.material_id, seed_two.seed_id],
                exterior_refs=["outer-b"],
                cohesion_note="second hold",
            )
            branched_cell = service.create_or_branch_space_cell_for_family(
                family_id="family-b",
                material_refs=[third_material.material_id],
                trace_refs=[trace_three.trace_id],
                seed_refs=[seed_three.seed_id],
                pressure_profile_id=pressure_shifted.profile_id,
                interior_refs=[third_material.material_id, seed_three.seed_id],
                exterior_refs=["outer-c"],
                cohesion_note="pressure shifted",
            )

            persisted_first_cell = service.cells.get(first_cell.cell_id)
            persisted_branched_cell = service.cells.get(branched_cell.cell_id)
            event_rows = service.events.read_all()

            self.assertEqual(first_cell.cell_id, reused_cell.cell_id)
            self.assertNotEqual(first_cell.cell_id, branched_cell.cell_id)
            self.assertEqual(set(persisted_first_cell["material_refs"]), {first_material.material_id, second_material.material_id})
            self.assertEqual(set(persisted_first_cell["seed_refs"]), {seed_one.seed_id, seed_two.seed_id})
            self.assertEqual(persisted_first_cell["state"], CellState.HELD.value)
            self.assertEqual(persisted_branched_cell["pressure_profile_id"], pressure_shifted.profile_id)
            self.assertEqual(len(list(service.cells.list_ids())), 2)
            self.assertIn(event_rows[-1]["event_type"], {"space_cell_branched", "space_cell_extended"})

    def test_cell_reactions_are_logged_and_drive_local_space_state(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            service = FormationService(Path(tmpdir))

            pressure_shared = service.create_pressure_profile(
                axes=[PressureAxis(axis="session_pressure", strength_hint=0.6)]
            )
            pressure_shifted = service.create_pressure_profile(
                axes=[PressureAxis(axis="tone_pressure", strength_hint=0.95)]
            )

            cell_one = service.create_space_cell_candidate(
                material_refs=["mat-1"],
                trace_refs=["trc-1"],
                seed_refs=["sed-1"],
                pressure_profile_id=pressure_shared.profile_id,
                interior_refs=["anchor-a", "shared-boundary"],
                exterior_refs=["shared-boundary", "outer-1"],
                cohesion_note="seeded",
            )
            cell_two = service.create_space_cell_candidate(
                material_refs=["mat-2"],
                trace_refs=["trc-2"],
                seed_refs=["sed-2"],
                pressure_profile_id=pressure_shared.profile_id,
                interior_refs=["anchor-b", "shared-boundary"],
                exterior_refs=["shared-boundary", "outer-2"],
                cohesion_note="seeded",
            )
            cell_three = service.create_space_cell_candidate(
                material_refs=["mat-3"],
                trace_refs=["trc-3"],
                seed_refs=["sed-3"],
                pressure_profile_id=pressure_shifted.profile_id,
                interior_refs=["anchor-c", "shared-boundary"],
                exterior_refs=["shared-boundary", "outer-3"],
                cohesion_note="seeded",
            )

            service.reactivate_space_cell(
                cell_id=cell_one.cell_id,
                reaction_kind="thickening",
                pressure_profile_id=pressure_shared.profile_id,
                note="recurrence thickened boundary",
                triggered_by_seed_ids=["sed-r1"],
            )
            service.reactivate_space_cell(
                cell_id=cell_two.cell_id,
                reaction_kind="split",
                pressure_profile_id=pressure_shared.profile_id,
                note="internal tension increased",
                triggered_by_seed_ids=["sed-r2"],
            )
            service.reactivate_space_cell(
                cell_id=cell_three.cell_id,
                reaction_kind="relocation",
                pressure_profile_id=pressure_shifted.profile_id,
                note="practical departure from prior cohesion",
                triggered_by_seed_ids=["sed-r3"],
            )

            boundary_heavy_space = service.form_local_space(
                cell_refs=[cell_one.cell_id, cell_two.cell_id],
                pressure_profile_id=pressure_shared.profile_id,
            )
            bridge_exposed_space = service.form_local_space(
                cell_refs=[cell_one.cell_id, cell_three.cell_id],
                pressure_profile_id=pressure_shared.profile_id,
            )

            reacted_cell_one = service.cells.get(cell_one.cell_id)
            reacted_cell_two = service.cells.get(cell_two.cell_id)
            reacted_cell_three = service.cells.get(cell_three.cell_id)
            event_rows = service.events.read_all()

            self.assertEqual(reacted_cell_one["state"], CellState.HELD.value)
            self.assertEqual(reacted_cell_two["state"], CellState.UNSTABLE.value)
            self.assertEqual(reacted_cell_three["state"], CellState.REENTERING.value)
            self.assertEqual(boundary_heavy_space.state, LocalSpaceState.BOUNDARY_HEAVY)
            self.assertEqual(bridge_exposed_space.state, LocalSpaceState.BRIDGE_EXPOSED)
            self.assertGreaterEqual(
                len([row for row in event_rows if row["event_type"] == "space_cell_reacted"]),
                3,
            )
            self.assertEqual(service.cell_manifests.get(cell_three.cell_id)["reaction_counts"]["relocation"], 1)

    def test_stable_local_requires_boundary_durability_and_thickening_presence(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            service = FormationService(Path(tmpdir))

            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="recurrence_pressure", strength_hint=0.8)]
            )
            cell_one = service.create_space_cell_candidate(
                material_refs=["mat-a"],
                trace_refs=["trc-a"],
                seed_refs=["sed-a"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["shared", "a"],
                exterior_refs=["outer-a", "shared"],
                cohesion_note="seeded",
            )
            cell_two = service.create_space_cell_candidate(
                material_refs=["mat-b"],
                trace_refs=["trc-b"],
                seed_refs=["sed-b"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["shared", "b"],
                exterior_refs=["outer-b", "shared"],
                cohesion_note="seeded",
            )

            service.reactivate_space_cell(cell_one.cell_id, "thickening", pressure.profile_id, "held-1")
            service.reactivate_space_cell(cell_two.cell_id, "thickening", pressure.profile_id, "held-2")

            local_space = service.form_local_space(
                cell_refs=[cell_one.cell_id, cell_two.cell_id],
                pressure_profile_id=pressure.profile_id,
            )

            self.assertEqual(local_space.state, LocalSpaceState.STABLE_LOCAL)
            manifest = service.space_manifests.get(local_space.local_space_id)
            self.assertEqual(manifest["state"], LocalSpaceState.STABLE_LOCAL.value)
            self.assertGreaterEqual(manifest["boundary_durability_score"], 2)
            self.assertEqual(manifest["reaction_counts"]["thickening"], 2)
            self.assertFalse(manifest["has_branch_mismatch"])
            self.assertIn("boundary_aged", manifest["maturation_evidence"]["signals"])
            self.assertIn("thickening_present", manifest["maturation_evidence"]["signals"])
            self.assertEqual(manifest["coexistence_mode"], "isolated_local")

    def test_local_space_without_boundary_durability_does_not_mature_to_stable_local(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            service = FormationService(Path(tmpdir))

            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="recurrence_pressure", strength_hint=0.8)]
            )
            cell_one = service.create_space_cell_candidate(
                material_refs=["mat-da"],
                trace_refs=["trc-da"],
                seed_refs=["sed-da"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["inside-a"],
                exterior_refs=["outer-a"],
                cohesion_note="seeded",
            )
            cell_two = service.create_space_cell_candidate(
                material_refs=["mat-db"],
                trace_refs=["trc-db"],
                seed_refs=["sed-db"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["inside-b"],
                exterior_refs=["outer-b"],
                cohesion_note="seeded",
            )

            service.reactivate_space_cell(cell_one.cell_id, "thickening", pressure.profile_id, "held-1")
            service.reactivate_space_cell(cell_two.cell_id, "thickening", pressure.profile_id, "held-2")

            local_space = service.form_local_space(
                cell_refs=[cell_one.cell_id, cell_two.cell_id],
                pressure_profile_id=pressure.profile_id,
            )

            self.assertEqual(local_space.state, LocalSpaceState.SPARSE)
            manifest = service.space_manifests.get(local_space.local_space_id)
            self.assertEqual(manifest["boundary_durability_score"], 0)

    def test_local_space_with_branch_mismatch_does_not_mature_to_stable_local(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            service = FormationService(Path(tmpdir))

            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="recurrence_pressure", strength_hint=0.8)]
            )
            cell_one = service.create_space_cell_candidate(
                material_refs=["mat-ba"],
                trace_refs=["trc-ba"],
                seed_refs=["sed-ba"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["shared-mismatch", "a"],
                exterior_refs=["outer-a", "shared-mismatch"],
                cohesion_note="seeded",
            )
            cell_two = service.create_space_cell_candidate(
                material_refs=["mat-bb"],
                trace_refs=["trc-bb"],
                seed_refs=["sed-bb"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["shared-mismatch", "b"],
                exterior_refs=["outer-b", "shared-mismatch"],
                cohesion_note="seeded",
            )

            service.reactivate_space_cell(cell_one.cell_id, "thickening", pressure.profile_id, "held-1")
            service.reactivate_space_cell(cell_two.cell_id, "thickening", pressure.profile_id, "held-2")
            service._append_event(
                "space_cell_branched",
                "space_cell",
                cell_two.cell_id,
                {"family_id": "family-mismatch", "reason": "pressure_signature_mismatch_or_absent"},
            )

            local_space = service.form_local_space(
                cell_refs=[cell_one.cell_id, cell_two.cell_id],
                pressure_profile_id=pressure.profile_id,
            )

            self.assertEqual(local_space.state, LocalSpaceState.FORMING)
            manifest = service.space_manifests.get(local_space.local_space_id)
            self.assertTrue(manifest["has_branch_mismatch"])

    def test_relocation_can_derive_bridge_trace_from_reactive_history(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            service = FormationService(Path(tmpdir))

            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="tone_pressure", strength_hint=0.9)]
            )
            cell_one = service.create_space_cell_candidate(
                material_refs=["mat-x"],
                trace_refs=["trc-x"],
                seed_refs=["sed-x"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["shared-bridge", "x"],
                exterior_refs=["shared-bridge", "outer-x"],
                cohesion_note="seeded",
            )
            cell_two = service.create_space_cell_candidate(
                material_refs=["mat-y"],
                trace_refs=["trc-y"],
                seed_refs=["sed-y"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["shared-bridge", "y"],
                exterior_refs=["shared-bridge", "outer-y"],
                cohesion_note="seeded",
            )

            left_space = service.form_local_space([cell_one.cell_id], pressure.profile_id)
            right_space = service.form_local_space([cell_two.cell_id], pressure.profile_id)

            service.reactivate_space_cell(
                cell_id=cell_one.cell_id,
                reaction_kind="relocation",
                pressure_profile_id=pressure.profile_id,
                note="shifted out of prior cohesion",
                triggered_by_seed_ids=["sed-rx"],
            )
            service.reactivate_space_cell(
                cell_id=cell_two.cell_id,
                reaction_kind="relocation",
                pressure_profile_id=pressure.profile_id,
                note="shifted toward adjacent space",
                triggered_by_seed_ids=["sed-ry"],
            )

            bridge = service.derive_bridge_trace_from_cells(
                from_local_space_id=left_space.local_space_id,
                to_local_space_id=right_space.local_space_id,
                via_cell_ids=[cell_one.cell_id, cell_two.cell_id],
                note="derived from paired relocation",
            )

            self.assertIsNotNone(bridge)
            self.assertEqual(bridge.state, BridgeState.OBSERVED)
            self.assertEqual(len(bridge.trace_refs), 2)
            persisted_bridge = service.bridges.get(bridge.bridge_id)
            self.assertEqual(persisted_bridge["state"], BridgeState.OBSERVED.value)
            bridge_manifest = service.bridge_manifests.get(bridge.bridge_id)
            self.assertEqual(bridge_manifest["state"], BridgeState.OBSERVED.value)
            self.assertEqual(bridge_manifest["trace_ref_count"], 2)
            self.assertEqual(bridge_manifest["support_round_count"], 1)
            self.assertFalse(bridge_manifest["temporal_spacing_ok"])
            self.assertEqual(bridge_manifest["durability_mode"], "exposed_adjacency")
            self.assertIn("bridge_exposed", bridge_manifest["maturation_evidence"]["signals"])
            persisted_left = service.local_spaces.get(left_space.local_space_id)
            persisted_right = service.local_spaces.get(right_space.local_space_id)
            self.assertEqual(persisted_left["state"], LocalSpaceState.BRIDGE_EXPOSED.value)
            self.assertEqual(persisted_right["state"], LocalSpaceState.BRIDGE_EXPOSED.value)

    def test_bridge_can_be_derived_from_local_spaces(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            service = FormationService(Path(tmpdir))

            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="tone_pressure", strength_hint=0.9)]
            )
            cell_one = service.create_space_cell_candidate(
                material_refs=["mat-lx"],
                trace_refs=["trc-lx"],
                seed_refs=["sed-lx"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["shared-local-bridge", "lx"],
                exterior_refs=["shared-local-bridge", "outer-lx"],
                cohesion_note="seeded",
            )
            cell_two = service.create_space_cell_candidate(
                material_refs=["mat-ly"],
                trace_refs=["trc-ly"],
                seed_refs=["sed-ly"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["shared-local-bridge", "ly"],
                exterior_refs=["shared-local-bridge", "outer-ly"],
                cohesion_note="seeded",
            )

            left_space = service.form_local_space([cell_one.cell_id], pressure.profile_id)
            right_space = service.form_local_space([cell_two.cell_id], pressure.profile_id)
            service.reactivate_space_cell(cell_one.cell_id, "relocation", pressure.profile_id, "move-left")
            service.reactivate_space_cell(cell_two.cell_id, "relocation", pressure.profile_id, "move-right")

            bridge = service.derive_bridge_trace_from_local_spaces(
                from_local_space_id=left_space.local_space_id,
                to_local_space_id=right_space.local_space_id,
                note="local-space-derived bridge",
            )

            self.assertIsNotNone(bridge)
            self.assertEqual(bridge.state, BridgeState.OBSERVED)
            persisted_left = service.local_spaces.get(left_space.local_space_id)
            persisted_right = service.local_spaces.get(right_space.local_space_id)
            self.assertIn(bridge.bridge_id, persisted_left["bridge_trace_refs"])
            self.assertIn(bridge.bridge_id, persisted_right["bridge_trace_refs"])
            self.assertEqual(persisted_left["state"], LocalSpaceState.BRIDGE_EXPOSED.value)
            self.assertEqual(persisted_right["state"], LocalSpaceState.BRIDGE_EXPOSED.value)

    def test_repeated_bridge_derivation_can_mature_to_durable_holding(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            service = FormationService(Path(tmpdir))

            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="tone_pressure", strength_hint=0.9)]
            )
            cell_one = service.create_space_cell_candidate(
                material_refs=["mat-hx"],
                trace_refs=["trc-hx"],
                seed_refs=["sed-hx"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["shared-held-bridge", "hx"],
                exterior_refs=["shared-held-bridge", "outer-hx"],
                cohesion_note="seeded",
            )
            cell_two = service.create_space_cell_candidate(
                material_refs=["mat-hy"],
                trace_refs=["trc-hy"],
                seed_refs=["sed-hy"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["shared-held-bridge", "hy"],
                exterior_refs=["shared-held-bridge", "outer-hy"],
                cohesion_note="seeded",
            )
            left_space = service.form_local_space([cell_one.cell_id], pressure.profile_id)
            right_space = service.form_local_space([cell_two.cell_id], pressure.profile_id)
            service.reactivate_space_cell(cell_one.cell_id, "relocation", pressure.profile_id, "move-left")
            service.reactivate_space_cell(cell_two.cell_id, "relocation", pressure.profile_id, "move-right")

            first_bridge = service.derive_bridge_trace_from_local_spaces(
                from_local_space_id=left_space.local_space_id,
                to_local_space_id=right_space.local_space_id,
                note="first exposure",
            )
            first_record = service.bridges.get(first_bridge.bridge_id)
            first_record["created_at"] = "2026-03-16T00:00:00+00:00"
            service.bridges.put(first_bridge.bridge_id, first_record)
            second_bridge = service.derive_bridge_trace_from_local_spaces(
                from_local_space_id=left_space.local_space_id,
                to_local_space_id=right_space.local_space_id,
                note="durable revisit",
            )

            self.assertEqual(first_bridge.state, BridgeState.OBSERVED)
            self.assertEqual(second_bridge.state, BridgeState.HELD)
            second_manifest = service.bridge_manifests.get(second_bridge.bridge_id)
            self.assertEqual(second_manifest["support_round_count"], 2)
            self.assertTrue(second_manifest["temporal_spacing_ok"])
            self.assertEqual(second_manifest["durability_mode"], "durable_holding")
            self.assertIn("time_aged", second_manifest["maturation_evidence"]["signals"])
            self.assertIn("durably_held", second_manifest["maturation_evidence"]["signals"])

    def test_runtime_bootstrap_creates_contract_aligned_directories_and_detects_legacy_paths(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            (runtime_root / "spaces" / "reference_center").mkdir(parents=True, exist_ok=True)
            (runtime_root / "bridges" / "traces").mkdir(parents=True, exist_ok=True)

            created_paths = bootstrap_runtime_layout(runtime_root)
            legacy_paths = find_legacy_runtime_directories(runtime_root)

            self.assertIn(runtime_root / "core" / "space_cells", created_paths)
            self.assertIn(runtime_root / "manifests" / "reactive_cells", created_paths)
            self.assertIn(runtime_root / "spaces" / "reference_center", legacy_paths)
            self.assertIn(runtime_root / "bridges" / "traces", legacy_paths)

    def test_workspace_manifest_summarizes_core_and_legacy_coexistence(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            service = FormationService(runtime_root)
            (runtime_root / "spaces" / "reference_center").mkdir(parents=True, exist_ok=True)

            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="session_pressure", strength_hint=0.5)]
            )
            cell = service.create_space_cell_candidate(
                material_refs=["mat-1"],
                trace_refs=["trc-1"],
                seed_refs=["sed-1"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["inner", "shared"],
                exterior_refs=["outer", "shared"],
                cohesion_note="manifested",
            )
            local_space = service.form_local_space([cell.cell_id], pressure.profile_id)

            manifest = build_workspace_manifest(runtime_root)
            manifest_path = write_workspace_manifest(runtime_root)

            self.assertEqual(manifest["coexistence_status"], "hybrid")
            self.assertEqual(manifest["core_counts"]["space_cells"], 1)
            self.assertEqual(manifest["manifest_counts"]["reactive_spaces"], 1)
            self.assertIn("spaces/reference_center", manifest["legacy_paths"])
            self.assertIn("process_summary", manifest)
            self.assertIn("local_space_maturation_signals", manifest)
            self.assertIn("bridge_maturation_signals", manifest)
            self.assertTrue(manifest_path.exists())

    def test_workspace_report_is_written_for_human_reading(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            service = FormationService(runtime_root)
            (runtime_root / "bridges" / "traces").mkdir(parents=True, exist_ok=True)

            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="recurrence_pressure", strength_hint=0.8)]
            )
            cell = service.create_space_cell_candidate(
                material_refs=["mat-r"],
                trace_refs=["trc-r"],
                seed_refs=["sed-r"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["shared", "inner"],
                exterior_refs=["shared", "outer"],
                cohesion_note="reportable",
            )
            service.form_local_space([cell.cell_id], pressure.profile_id)

            report_path = write_workspace_report(runtime_root)
            report_text = report_path.read_text(encoding="utf-8")

            self.assertTrue(report_path.exists())
            self.assertIn("# Workspace Report", report_text)
            self.assertIn("status: hybrid", report_text)
            self.assertIn("process_mode:", report_text)
            self.assertIn("process_summary:", report_text)
            self.assertIn("Maturation Signals", report_text)
            self.assertIn("space_cells: 1", report_text)
            self.assertIn("bridges/traces", report_text)

    def test_reactive_space_report_is_written_for_space_scale_reread(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            service = FormationService(runtime_root)

            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="recurrence_pressure", strength_hint=0.8)]
            )
            cell_one = service.create_space_cell_candidate(
                material_refs=["mat-r1"],
                trace_refs=["trc-r1"],
                seed_refs=["sed-r1"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["shared-r", "inner-r1"],
                exterior_refs=["shared-r", "outer-r1"],
                cohesion_note="report-r1",
            )
            cell_two = service.create_space_cell_candidate(
                material_refs=["mat-r2"],
                trace_refs=["trc-r2"],
                seed_refs=["sed-r2"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["shared-r", "inner-r2"],
                exterior_refs=["shared-r", "outer-r2"],
                cohesion_note="report-r2",
            )
            service.reactivate_space_cell(cell_one.cell_id, "thickening", pressure.profile_id, "held-r1")
            service.reactivate_space_cell(cell_two.cell_id, "thickening", pressure.profile_id, "held-r2")
            local_space = service.form_local_space([cell_one.cell_id, cell_two.cell_id], pressure.profile_id)

            report_path = write_reactive_space_report(runtime_root)
            report_text = report_path.read_text(encoding="utf-8")

            self.assertTrue(report_path.exists())
            self.assertIn("# Reactive Space Report", report_text)
            self.assertIn("mode:", report_text)
            self.assertIn("Terrain Climate", report_text)
            self.assertIn("Terrain Climate Signals", report_text)
            self.assertIn("Terrain Rhythm", report_text)
            self.assertIn("Terrain Rhythm Signals", report_text)
            self.assertIn("Terrain Recurrence", report_text)
            self.assertIn("Terrain Recurrence Signals", report_text)
            self.assertIn("Terrain Memory", report_text)
            self.assertIn("Terrain Memory Signals", report_text)
            self.assertIn("Terrain Retention", report_text)
            self.assertIn("Terrain Retention Signals", report_text)
            self.assertIn("Terrain Forgetting", report_text)
            self.assertIn("Terrain Forgetting Signals", report_text)
            self.assertIn("Terrain Components", report_text)
            self.assertIn("Local Space Coexistence", report_text)
            self.assertIn("Local Spaces", report_text)
            self.assertIn(local_space.local_space_id, report_text)

    def test_reactive_observer_builds_terrain_components_from_local_spaces_and_bridges(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            service = FormationService(runtime_root)

            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="tone_pressure", strength_hint=0.9)]
            )
            cell_one = service.create_space_cell_candidate(
                material_refs=["mat-t1"],
                trace_refs=["trc-t1"],
                seed_refs=["sed-t1"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["shared-terrain", "t1"],
                exterior_refs=["shared-terrain", "outer-t1"],
                cohesion_note="terrain-1",
            )
            cell_two = service.create_space_cell_candidate(
                material_refs=["mat-t2"],
                trace_refs=["trc-t2"],
                seed_refs=["sed-t2"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["shared-terrain", "t2"],
                exterior_refs=["shared-terrain", "outer-t2"],
                cohesion_note="terrain-2",
            )
            left_space = service.form_local_space([cell_one.cell_id], pressure.profile_id)
            right_space = service.form_local_space([cell_two.cell_id], pressure.profile_id)
            service.reactivate_space_cell(cell_one.cell_id, "relocation", pressure.profile_id, "move-left")
            service.reactivate_space_cell(cell_two.cell_id, "relocation", pressure.profile_id, "move-right")
            service.derive_bridge_trace_from_local_spaces(
                from_local_space_id=left_space.local_space_id,
                to_local_space_id=right_space.local_space_id,
                note="terrain-link",
            )

            observation = build_reactive_space_observation(runtime_root)

            self.assertEqual(len(observation["terrain_components"]), 1)
            component = observation["terrain_components"][0]
            self.assertEqual(component["local_space_count"], 2)
            self.assertEqual(set(component["local_space_ids"]), {left_space.local_space_id, right_space.local_space_id})

    def test_reactive_observer_reads_resonant_shared_climate_without_collapse(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            service = FormationService(runtime_root)

            left_pressure = service.create_pressure_profile(
                axes=[
                    PressureAxis(axis="session_pressure", strength_hint=0.5),
                    PressureAxis(axis="tone_pressure", strength_hint=0.9),
                ]
            )
            right_pressure = service.create_pressure_profile(
                axes=[
                    PressureAxis(axis="session_pressure", strength_hint=0.85),
                    PressureAxis(axis="recurrence_pressure", strength_hint=0.7),
                ]
            )
            left_cell = service.create_space_cell_candidate(
                material_refs=["mat-cl1"],
                trace_refs=["trc-cl1"],
                seed_refs=["sed-cl1"],
                pressure_profile_id=left_pressure.profile_id,
                interior_refs=["shared-climate", "inner-cl1"],
                exterior_refs=["shared-climate", "outer-cl1"],
                cohesion_note="climate-left",
            )
            right_cell = service.create_space_cell_candidate(
                material_refs=["mat-cl2"],
                trace_refs=["trc-cl2"],
                seed_refs=["sed-cl2"],
                pressure_profile_id=right_pressure.profile_id,
                interior_refs=["shared-climate", "inner-cl2"],
                exterior_refs=["shared-climate", "outer-cl2"],
                cohesion_note="climate-right",
            )
            left_space = service.form_local_space([left_cell.cell_id], left_pressure.profile_id)
            right_space = service.form_local_space([right_cell.cell_id], right_pressure.profile_id)
            service.register_bridge_trace(
                from_local_space_id=left_space.local_space_id,
                to_local_space_id=right_space.local_space_id,
                trace_refs=["trace-climate"],
                note="shared climate without collapse",
            )

            observation = build_reactive_space_observation(runtime_root)

            self.assertEqual(observation["terrain_climate_modes"]["resonant_climate"], 1)
            component = observation["terrain_components"][0]
            self.assertEqual(component["climate_mode"], "resonant_climate")
            self.assertEqual(component["shared_pressure_axes"], ["session_pressure"])
            self.assertEqual(
                set(component["union_pressure_axes"]),
                {"session_pressure", "tone_pressure", "recurrence_pressure"},
            )
            self.assertIn("multi_local_climate", component["climate_evidence"]["signals"])
            self.assertIn("shared_axis_climate", component["climate_evidence"]["signals"])

    def test_reactive_observer_reads_time_aged_terrain_climate_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            service = FormationService(runtime_root)

            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="tone_pressure", strength_hint=0.9)]
            )
            left_cell = service.create_space_cell_candidate(
                material_refs=["mat-tc1"],
                trace_refs=["trc-tc1"],
                seed_refs=["sed-tc1"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["shared-time-climate", "tc1"],
                exterior_refs=["shared-time-climate", "outer-tc1"],
                cohesion_note="time-climate-left",
            )
            right_cell = service.create_space_cell_candidate(
                material_refs=["mat-tc2"],
                trace_refs=["trc-tc2"],
                seed_refs=["sed-tc2"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["shared-time-climate", "tc2"],
                exterior_refs=["shared-time-climate", "outer-tc2"],
                cohesion_note="time-climate-right",
            )
            service.reactivate_space_cell(left_cell.cell_id, "thickening", pressure.profile_id, "held-tc1")
            service.reactivate_space_cell(right_cell.cell_id, "thickening", pressure.profile_id, "held-tc2")
            left_space = service.form_local_space([left_cell.cell_id], pressure.profile_id)
            right_space = service.form_local_space([right_cell.cell_id], pressure.profile_id)
            service.reactivate_space_cell(left_cell.cell_id, "relocation", pressure.profile_id, "move-tc1")
            service.reactivate_space_cell(right_cell.cell_id, "relocation", pressure.profile_id, "move-tc2")

            first_bridge = service.derive_bridge_trace_from_local_spaces(
                from_local_space_id=left_space.local_space_id,
                to_local_space_id=right_space.local_space_id,
                note="first climate exposure",
            )
            first_record = service.bridges.get(first_bridge.bridge_id)
            first_record["created_at"] = "2026-03-16T00:00:00+00:00"
            service.bridges.put(first_bridge.bridge_id, first_record)
            service.derive_bridge_trace_from_local_spaces(
                from_local_space_id=left_space.local_space_id,
                to_local_space_id=right_space.local_space_id,
                note="climate revisit",
            )

            observation = build_reactive_space_observation(runtime_root)

            self.assertEqual(observation["terrain_climate_modes"]["shared_climate"], 1)
            self.assertGreaterEqual(observation["terrain_climate_signals"]["time_aged_climate"], 1)
            self.assertGreaterEqual(observation["terrain_climate_signals"]["durably_held_climate"], 1)
            self.assertGreaterEqual(observation["terrain_rhythm_modes"]["persistent_rhythm"], 1)
            self.assertGreaterEqual(observation["terrain_rhythm_signals"]["bridge_pulsed"], 1)
            self.assertGreaterEqual(observation["terrain_rhythm_signals"]["time_spaced_rhythm"], 1)
            self.assertGreaterEqual(observation["terrain_recurrence_modes"]["cadenced_recurrence"], 1)
            self.assertGreaterEqual(observation["terrain_recurrence_signals"]["bridge_returning"], 1)
            self.assertGreaterEqual(observation["terrain_recurrence_signals"]["time_spaced_return"], 1)
            self.assertGreaterEqual(observation["terrain_memory_modes"]["persistent_memory"], 1)
            self.assertGreaterEqual(observation["terrain_memory_signals"]["persistent_bridge_memory"], 1)
            self.assertGreaterEqual(observation["terrain_memory_signals"]["durable_return_memory"], 1)
            self.assertGreaterEqual(observation["terrain_retention_modes"]["retained_terrain"], 1)
            self.assertGreaterEqual(observation["terrain_retention_signals"]["durably_retained"], 1)
            component = observation["terrain_components"][0]
            self.assertIn("shared_axis_climate", component["climate_evidence"]["signals"])
            self.assertIn("time_aged_climate", component["climate_evidence"]["signals"])
            self.assertIn("durably_held_climate", component["climate_evidence"]["signals"])
            self.assertEqual(component["rhythm_mode"], "persistent_rhythm")
            self.assertIn("bridge_pulsed", component["rhythm_evidence"]["signals"])
            self.assertIn("time_spaced_rhythm", component["rhythm_evidence"]["signals"])
            self.assertEqual(component["recurrence_mode"], "cadenced_recurrence")
            self.assertIn("bridge_returning", component["recurrence_evidence"]["signals"])
            self.assertIn("time_spaced_return", component["recurrence_evidence"]["signals"])
            self.assertEqual(component["memory_mode"], "persistent_memory")
            self.assertIn("persistent_bridge_memory", component["memory_evidence"]["signals"])
            self.assertIn("durable_return_memory", component["memory_evidence"]["signals"])
            self.assertEqual(component["retention_mode"], "retained_terrain")
            self.assertIn("durably_retained", component["retention_evidence"]["signals"])

    def test_reactive_observer_reads_fading_forgetting_without_durable_return(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            service = FormationService(runtime_root)

            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="session_pressure", strength_hint=0.7)]
            )
            left_cell = service.create_space_cell_candidate(
                material_refs=["mat-fg1"],
                trace_refs=["trc-fg1"],
                seed_refs=["sed-fg1"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["shared-fade", "fg1"],
                exterior_refs=["shared-fade", "outer-fg1"],
                cohesion_note="fade-left",
            )
            right_cell = service.create_space_cell_candidate(
                material_refs=["mat-fg2"],
                trace_refs=["trc-fg2"],
                seed_refs=["sed-fg2"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["shared-fade", "fg2"],
                exterior_refs=["shared-fade", "outer-fg2"],
                cohesion_note="fade-right",
            )
            left_space = service.form_local_space([left_cell.cell_id], pressure.profile_id)
            right_space = service.form_local_space([right_cell.cell_id], pressure.profile_id)
            service.reactivate_space_cell(left_cell.cell_id, "relocation", pressure.profile_id, "fade-move-left")
            service.reactivate_space_cell(right_cell.cell_id, "relocation", pressure.profile_id, "fade-move-right")

            first_bridge = service.derive_bridge_trace_from_local_spaces(
                from_local_space_id=left_space.local_space_id,
                to_local_space_id=right_space.local_space_id,
                note="fading-first",
            )
            first_record = service.bridges.get(first_bridge.bridge_id)
            first_record["created_at"] = "2026-03-16T00:00:00+00:00"
            service.bridges.put(first_bridge.bridge_id, first_record)

            observation = build_reactive_space_observation(runtime_root)

            self.assertGreaterEqual(observation["terrain_forgetting_modes"]["light_forgetting"], 1)
            self.assertGreaterEqual(observation["terrain_forgetting_signals"]["forgetting_trace"], 1)
            component = observation["terrain_components"][0]
            self.assertEqual(component["retention_mode"], "fading_terrain")
            self.assertEqual(component["forgetting_mode"], "light_forgetting")
            self.assertIn("forgetting_trace", component["forgetting_evidence"]["signals"])

    def test_local_space_manifest_reads_pressure_adjacent_and_terrain_shared_modes(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            service = FormationService(Path(tmpdir))

            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="session_pressure", strength_hint=0.6)]
            )
            cell_one = service.create_space_cell_candidate(
                material_refs=["mat-ca"],
                trace_refs=["trc-ca"],
                seed_refs=["sed-ca"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["inner-ca"],
                exterior_refs=["outer-ca"],
                cohesion_note="coexist-a",
            )
            cell_two = service.create_space_cell_candidate(
                material_refs=["mat-cb"],
                trace_refs=["trc-cb"],
                seed_refs=["sed-cb"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["inner-cb"],
                exterior_refs=["outer-cb"],
                cohesion_note="coexist-b",
            )

            left_space = service.form_local_space([cell_one.cell_id], pressure.profile_id)
            right_space = service.form_local_space([cell_two.cell_id], pressure.profile_id)
            left_manifest = service.space_manifests.get(left_space.local_space_id)
            right_manifest = service.space_manifests.get(right_space.local_space_id)
            self.assertEqual(left_manifest["coexistence_mode"], "pressure_adjacent")
            self.assertEqual(right_manifest["coexistence_mode"], "pressure_adjacent")

            service.register_bridge_trace(
                from_local_space_id=left_space.local_space_id,
                to_local_space_id=right_space.local_space_id,
                trace_refs=["trace-coexist"],
                note="terrain adjacency only",
            )

            updated_left = service.space_manifests.get(left_space.local_space_id)
            updated_right = service.space_manifests.get(right_space.local_space_id)
            self.assertEqual(updated_left["coexistence_mode"], "terrain_shared")
            self.assertEqual(updated_right["coexistence_mode"], "terrain_shared")

    def test_local_space_manifest_reads_pressure_resonant_and_terrain_resonant_modes(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            service = FormationService(Path(tmpdir))

            left_pressure = service.create_pressure_profile(
                axes=[
                    PressureAxis(axis="session_pressure", strength_hint=0.6),
                    PressureAxis(axis="tone_pressure", strength_hint=0.4),
                ]
            )
            right_pressure = service.create_pressure_profile(
                axes=[
                    PressureAxis(axis="session_pressure", strength_hint=0.85),
                    PressureAxis(axis="recurrence_pressure", strength_hint=0.7),
                ]
            )
            cell_one = service.create_space_cell_candidate(
                material_refs=["mat-ra"],
                trace_refs=["trc-ra"],
                seed_refs=["sed-ra"],
                pressure_profile_id=left_pressure.profile_id,
                interior_refs=["inner-ra"],
                exterior_refs=["outer-ra"],
                cohesion_note="resonance-a",
            )
            cell_two = service.create_space_cell_candidate(
                material_refs=["mat-rb"],
                trace_refs=["trc-rb"],
                seed_refs=["sed-rb"],
                pressure_profile_id=right_pressure.profile_id,
                interior_refs=["inner-rb"],
                exterior_refs=["outer-rb"],
                cohesion_note="resonance-b",
            )

            left_space = service.form_local_space([cell_one.cell_id], left_pressure.profile_id)
            right_space = service.form_local_space([cell_two.cell_id], right_pressure.profile_id)
            left_manifest = service.space_manifests.get(left_space.local_space_id)
            right_manifest = service.space_manifests.get(right_space.local_space_id)
            self.assertEqual(left_manifest["coexistence_mode"], "pressure_resonant")
            self.assertEqual(right_manifest["coexistence_mode"], "pressure_resonant")
            self.assertEqual(set(left_manifest["terrain_pressure_axes"]), {"session_pressure", "tone_pressure"})
            self.assertEqual(set(right_manifest["terrain_pressure_axes"]), {"session_pressure", "recurrence_pressure"})

            service.register_bridge_trace(
                from_local_space_id=left_space.local_space_id,
                to_local_space_id=right_space.local_space_id,
                trace_refs=["trace-resonance"],
                note="terrain resonance only",
            )

            updated_left = service.space_manifests.get(left_space.local_space_id)
            updated_right = service.space_manifests.get(right_space.local_space_id)
            self.assertEqual(updated_left["coexistence_mode"], "terrain_resonant")
            self.assertEqual(updated_right["coexistence_mode"], "terrain_resonant")

    def test_report_issuance_policy_marks_hybrid_runtime_as_reportable(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            service = FormationService(runtime_root)
            (runtime_root / "spaces" / "reference_center").mkdir(parents=True, exist_ok=True)
            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="session_pressure", strength_hint=0.4)]
            )
            service.create_space_cell_candidate(
                material_refs=["mat-i"],
                trace_refs=["trc-i"],
                seed_refs=["sed-i"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["shared"],
                exterior_refs=["outer"],
                cohesion_note="issuable",
            )

            decision = should_issue_workspace_report(runtime_root)

            self.assertTrue(decision["issue_report"])
            self.assertEqual(decision["coexistence_status"], "hybrid")
            self.assertGreaterEqual(len(decision["reasons"]), 2)

    def test_observe_runtime_script_prints_summary(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            service = FormationService(runtime_root)
            (runtime_root / "bridges" / "traces").mkdir(parents=True, exist_ok=True)
            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="recurrence_pressure", strength_hint=0.6)]
            )
            service.create_space_cell_candidate(
                material_refs=["mat-o"],
                trace_refs=["trc-o"],
                seed_refs=["sed-o"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["inside"],
                exterior_refs=["outside"],
                cohesion_note="observable",
            )

            result = subprocess.run(
                ["python3", "scripts/observe_runtime.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            self.assertIn("coexistence_status: hybrid", result.stdout)
            self.assertIn("issue_report: True", result.stdout)
            self.assertIn("reactive_report_path:", result.stdout)

    def test_seed_initial_materials_script_creates_three_seeded_materials(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            result = subprocess.run(
                ["python3", "scripts/seed_initial_materials.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            material_ids = list(service.materials.list_ids())
            persisted = [service.materials.get(material_id) for material_id in material_ids]
            role_set = {row["metadata"].get("formation_role") for row in persisted}
            source_type_set = {row["source_type"] for row in persisted}

            self.assertIn("seeded_materials: 3", result.stdout)
            self.assertEqual(len(material_ids), 3)
            self.assertEqual(
                role_set,
                {"fresh_material", "engine_self_material", "observer_material"},
            )
            self.assertEqual(source_type_set, {"note", "worklog", "observer_output"})

    def test_trace_initial_relation_script_links_engine_self_and_observer_materials(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            subprocess.run(
                ["python3", "scripts/seed_initial_materials.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )
            result = subprocess.run(
                ["python3", "scripts/trace_initial_relation.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            trace_ids = list(service.traces.list_ids())
            self.assertEqual(len(trace_ids), 1)

            persisted = service.traces.get(trace_ids[0])
            self.assertIn("trace_id:", result.stdout)
            self.assertEqual(persisted["evidence_kind"], "observer_reflection")
            self.assertEqual(len(persisted["material_refs"]), 2)

    def test_seed_fresh_pressure_input_script_opens_seed_without_cell_escalation(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            subprocess.run(
                ["python3", "scripts/seed_initial_materials.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )
            result = subprocess.run(
                ["python3", "scripts/seed_fresh_pressure_input.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            trace_ids = list(service.traces.list_ids())
            pressure_ids = list(service.pressures.list_ids())
            seed_ids = list(service.seeds.list_ids())
            cell_ids = list(service.cells.list_ids())

            self.assertIn("seed_state: forming", result.stdout)
            self.assertEqual(len(trace_ids), 1)
            self.assertEqual(len(pressure_ids), 1)
            self.assertEqual(len(seed_ids), 1)
            self.assertEqual(len(cell_ids), 0)

    def test_second_material_wave_script_expands_runtime_into_multi_local_terrain(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_second_material_wave.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            cell_ids = list(service.cells.list_ids())
            local_space_ids = list(service.local_spaces.list_ids())
            bridge_ids = list(service.bridges.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("second_cell_id:", result.stdout)
            self.assertGreaterEqual(len(cell_ids), 2)
            self.assertGreaterEqual(len(local_space_ids), 2)
            self.assertGreaterEqual(len(bridge_ids), 1)
            self.assertTrue(observation["terrain_components"])
            self.assertIn(
                "bridge_exposed",
                observation["local_space_states"],
            )

    def test_third_material_wave_script_opens_distinct_third_terrain(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_third_material_wave.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("third_local_space_id:", result.stdout)
            self.assertGreaterEqual(len(local_space_ids), 3)
            self.assertEqual(len(observation["terrain_components"]), 2)

    def test_fourth_material_wave_script_thickens_third_terrain_without_new_bridge(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_fourth_material_wave.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("cell_state: held", result.stdout)
            self.assertEqual(len(bridge_ids), 1)
            self.assertGreaterEqual(observation["reaction_counts"]["thickening"], 2)
            self.assertEqual(len(observation["terrain_components"]), 2)

    def test_fifth_material_wave_script_adds_repeated_thickening_to_third_terrain(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_fifth_material_wave.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("cell_state: held", result.stdout)
            self.assertGreaterEqual(observation["reaction_counts"]["thickening"], 3)
            self.assertEqual(len(observation["terrain_components"]), 2)

    def test_sixth_material_wave_script_adds_repeated_thickening_to_observer_facing_terrain(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_sixth_material_wave.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("cell_state: held", result.stdout)
            self.assertEqual(len(bridge_ids), 1)
            self.assertGreaterEqual(observation["reaction_counts"]["thickening"], 4)
            self.assertEqual(len(observation["terrain_components"]), 2)

    def test_seventh_material_wave_script_opens_fourth_local_terrain_without_new_bridge(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_seventh_material_wave.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("seventh_local_space_id:", result.stdout)
            self.assertEqual(len(bridge_ids), 1)
            self.assertGreaterEqual(len(local_space_ids), 4)
            self.assertEqual(len(observation["terrain_components"]), 3)

    def test_eighth_material_wave_script_thickens_reflective_terrain_without_new_bridge(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_eighth_material_wave.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("cell_state: held", result.stdout)
            self.assertEqual(len(bridge_ids), 1)
            self.assertGreaterEqual(observation["reaction_counts"]["thickening"], 5)
            self.assertEqual(len(observation["terrain_components"]), 3)

    def test_ninth_material_wave_script_adds_another_reflective_thickening_without_new_bridge(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_ninth_material_wave.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("cell_state: held", result.stdout)
            self.assertEqual(len(bridge_ids), 1)
            self.assertGreaterEqual(observation["reaction_counts"]["thickening"], 6)
            self.assertEqual(len(observation["terrain_components"]), 3)

    def test_tenth_material_wave_script_adds_temporal_project_thickening_without_new_bridge(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_tenth_material_wave.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("cell_state: held", result.stdout)
            self.assertEqual(len(bridge_ids), 1)
            self.assertGreaterEqual(observation["reaction_counts"]["thickening"], 7)
            self.assertEqual(len(observation["terrain_components"]), 3)

    def test_eleventh_material_wave_script_opens_constraint_band_without_new_bridge(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_eleventh_material_wave.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("eleventh_local_space_id:", result.stdout)
            self.assertEqual(len(bridge_ids), 1)
            self.assertGreaterEqual(len(local_space_ids), 5)
            self.assertEqual(len(observation["terrain_components"]), 4)

    def test_twelfth_material_wave_script_thickens_constraint_band_without_new_bridge(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_twelfth_material_wave.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("cell_state: held", result.stdout)
            self.assertEqual(len(bridge_ids), 1)
            self.assertGreaterEqual(observation["reaction_counts"]["thickening"], 8)
            self.assertEqual(len(observation["terrain_components"]), 4)

    def test_thirteenth_material_wave_script_opens_drift_band_without_new_bridge(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_thirteenth_material_wave.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("thirteenth_local_space_id:", result.stdout)
            self.assertEqual(len(bridge_ids), 1)
            self.assertGreaterEqual(len(local_space_ids), 6)
            self.assertEqual(len(observation["terrain_components"]), 5)

    def test_fourteenth_material_wave_script_thickens_drift_band_without_new_bridge(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_fourteenth_material_wave.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("cell_state: held", result.stdout)
            self.assertEqual(len(bridge_ids), 1)
            self.assertGreaterEqual(observation["reaction_counts"]["thickening"], 9)
            self.assertEqual(len(observation["terrain_components"]), 5)

    def test_fifteenth_bridge_exposure_script_opens_observed_exposure_between_mature_terrains(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_fifteenth_bridge_exposure.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("bridge_state: observed", result.stdout)
            self.assertEqual(len(bridge_ids), 2)
            self.assertEqual(len(observation["terrain_components"]), 3)

    def test_sixteenth_material_pulse_script_opens_small_pulse_terrain_and_two_weak_exposures(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_fifteenth_bridge_exposure.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_sixteenth_material_pulse.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("pulse_local_space_id:", result.stdout)
            self.assertEqual(len(bridge_ids), 4)
            self.assertGreaterEqual(len(local_space_ids), 6)
            self.assertEqual(len(observation["terrain_components"]), 3)

    def test_seventeenth_material_pulse_script_opens_small_pulse_between_constraint_and_drift(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
                "scripts/seed_fourteenth_material_wave.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_seventeenth_material_pulse.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("pulse_local_space_id:", result.stdout)
            self.assertEqual(len(bridge_ids), 3)
            self.assertGreaterEqual(len(local_space_ids), 7)
            self.assertEqual(len(observation["terrain_components"]), 4)

    def test_eighteenth_material_pulse_script_opens_small_pulse_between_observer_and_temporal(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
                "scripts/seed_fourteenth_material_wave.py",
                "scripts/seed_seventeenth_material_pulse.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_eighteenth_material_pulse.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("pulse_local_space_id:", result.stdout)
            self.assertEqual(len(bridge_ids), 5)
            self.assertEqual(len(local_space_ids), 8)
            self.assertEqual(len(observation["terrain_components"]), 3)

    def test_nineteenth_material_pulse_script_rethreads_internal_resonant_flow(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
                "scripts/seed_fourteenth_material_wave.py",
                "scripts/seed_seventeenth_material_pulse.py",
                "scripts/seed_eighteenth_material_pulse.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_nineteenth_material_pulse.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("pulse_local_space_id:", result.stdout)
            self.assertEqual(len(bridge_ids), 7)
            self.assertEqual(len(local_space_ids), 9)
            self.assertEqual(len(observation["terrain_components"]), 2)

    def test_twentieth_material_pulse_script_reaches_outer_drift_terrain(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
                "scripts/seed_fourteenth_material_wave.py",
                "scripts/seed_seventeenth_material_pulse.py",
                "scripts/seed_eighteenth_material_pulse.py",
                "scripts/seed_nineteenth_material_pulse.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_twentieth_material_pulse.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("pulse_local_space_id:", result.stdout)
            self.assertEqual(len(bridge_ids), 9)
            self.assertEqual(len(local_space_ids), 10)
            self.assertEqual(len(observation["terrain_components"]), 1)

    def test_twentyfirst_scale_bundle_script_adds_three_independent_local_spaces_without_new_bridges(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
                "scripts/seed_fourteenth_material_wave.py",
                "scripts/seed_seventeenth_material_pulse.py",
                "scripts/seed_eighteenth_material_pulse.py",
                "scripts/seed_nineteenth_material_pulse.py",
                "scripts/seed_twentieth_material_pulse.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_twentyfirst_scale_bundle.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("sparse_local_space_id:", result.stdout)
            self.assertIn("reflux_local_space_id:", result.stdout)
            self.assertIn("reading_local_space_id:", result.stdout)
            self.assertEqual(len(bridge_ids), 9)
            self.assertEqual(len(local_space_ids), 13)
            self.assertEqual(len(observation["terrain_components"]), 4)

    def test_twentysecond_scale_bundle_script_adds_four_more_quiet_local_spaces_without_new_bridges(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
                "scripts/seed_fourteenth_material_wave.py",
                "scripts/seed_seventeenth_material_pulse.py",
                "scripts/seed_eighteenth_material_pulse.py",
                "scripts/seed_nineteenth_material_pulse.py",
                "scripts/seed_twentieth_material_pulse.py",
                "scripts/seed_twentyfirst_scale_bundle.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_twentysecond_scale_bundle.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("agent_log_local_space_id:", result.stdout)
            self.assertIn("failure_local_space_id:", result.stdout)
            self.assertIn("book_local_space_id:", result.stdout)
            self.assertIn("unknown_local_space_id:", result.stdout)
            self.assertEqual(len(bridge_ids), 9)
            self.assertEqual(len(local_space_ids), 17)
            self.assertEqual(len(observation["terrain_components"]), 8)

    def test_twentythird_scale_bundle_script_adds_external_world_quiet_spaces_without_new_bridges(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
                "scripts/seed_fourteenth_material_wave.py",
                "scripts/seed_seventeenth_material_pulse.py",
                "scripts/seed_eighteenth_material_pulse.py",
                "scripts/seed_nineteenth_material_pulse.py",
                "scripts/seed_twentieth_material_pulse.py",
                "scripts/seed_twentyfirst_scale_bundle.py",
                "scripts/seed_twentysecond_scale_bundle.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_twentythird_scale_bundle.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("web_chatgpt_local_space_id:", result.stdout)
            self.assertIn("gemini_cli_local_space_id:", result.stdout)
            self.assertIn("claude_code_local_space_id:", result.stdout)
            self.assertIn("youtube_note_local_space_id:", result.stdout)
            self.assertEqual(len(bridge_ids), 9)
            self.assertEqual(len(local_space_ids), 21)
            self.assertEqual(len(observation["terrain_components"]), 12)

    def test_sparse_presence_review_script_reads_quiet_space_counts_descriptively(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
                "scripts/seed_fourteenth_material_wave.py",
                "scripts/seed_seventeenth_material_pulse.py",
                "scripts/seed_eighteenth_material_pulse.py",
                "scripts/seed_nineteenth_material_pulse.py",
                "scripts/seed_twentieth_material_pulse.py",
                "scripts/seed_twentyfirst_scale_bundle.py",
                "scripts/seed_twentysecond_scale_bundle.py",
                "scripts/seed_twentythird_scale_bundle.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/review_sparse_presence.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            self.assertIn("quiet_local_spaces: 21", result.stdout)
            self.assertIn("forming_local_spaces: 11", result.stdout)
            self.assertIn("bridge_exposed_local_spaces: 10", result.stdout)

    def test_twentyfourth_scale_bundle_script_adds_four_more_quiet_spaces_without_new_bridges(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
                "scripts/seed_fourteenth_material_wave.py",
                "scripts/seed_seventeenth_material_pulse.py",
                "scripts/seed_eighteenth_material_pulse.py",
                "scripts/seed_nineteenth_material_pulse.py",
                "scripts/seed_twentieth_material_pulse.py",
                "scripts/seed_twentyfirst_scale_bundle.py",
                "scripts/seed_twentysecond_scale_bundle.py",
                "scripts/seed_twentythird_scale_bundle.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_twentyfourth_scale_bundle.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("mcp_local_space_id:", result.stdout)
            self.assertIn("agent_local_space_id:", result.stdout)
            self.assertIn("human_note_local_space_id:", result.stdout)
            self.assertIn("reserve_local_space_id:", result.stdout)
            self.assertEqual(len(bridge_ids), 9)
            self.assertEqual(len(local_space_ids), 25)
            self.assertEqual(len(observation["terrain_components"]), 16)

    def test_twentyfifth_scale_bundle_script_adds_four_more_quiet_spaces_without_new_bridges(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
                "scripts/seed_fourteenth_material_wave.py",
                "scripts/seed_seventeenth_material_pulse.py",
                "scripts/seed_eighteenth_material_pulse.py",
                "scripts/seed_nineteenth_material_pulse.py",
                "scripts/seed_twentieth_material_pulse.py",
                "scripts/seed_twentyfirst_scale_bundle.py",
                "scripts/seed_twentysecond_scale_bundle.py",
                "scripts/seed_twentythird_scale_bundle.py",
                "scripts/seed_twentyfourth_scale_bundle.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_twentyfifth_scale_bundle.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("policy_local_space_id:", result.stdout)
            self.assertIn("experiment_local_space_id:", result.stdout)
            self.assertIn("book_highlight_local_space_id:", result.stdout)
            self.assertIn("codex_return_local_space_id:", result.stdout)
            self.assertEqual(len(bridge_ids), 9)
            self.assertEqual(len(local_space_ids), 29)
            self.assertEqual(len(observation["terrain_components"]), 20)

    def test_twentysixth_scale_bundle_script_adds_four_more_quiet_spaces_without_new_bridges(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
                "scripts/seed_fourteenth_material_wave.py",
                "scripts/seed_seventeenth_material_pulse.py",
                "scripts/seed_eighteenth_material_pulse.py",
                "scripts/seed_nineteenth_material_pulse.py",
                "scripts/seed_twentieth_material_pulse.py",
                "scripts/seed_twentyfirst_scale_bundle.py",
                "scripts/seed_twentysecond_scale_bundle.py",
                "scripts/seed_twentythird_scale_bundle.py",
                "scripts/seed_twentyfourth_scale_bundle.py",
                "scripts/seed_twentyfifth_scale_bundle.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_twentysixth_scale_bundle.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("handoff_local_space_id:", result.stdout)
            self.assertIn("tool_error_local_space_id:", result.stdout)
            self.assertIn("unread_quote_local_space_id:", result.stdout)
            self.assertIn("question_local_space_id:", result.stdout)
            self.assertEqual(len(bridge_ids), 9)
            self.assertEqual(len(local_space_ids), 33)
            self.assertEqual(len(observation["terrain_components"]), 24)

    def test_first_scale_review_script_reads_five_review_axes_descriptively(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
                "scripts/seed_fourteenth_material_wave.py",
                "scripts/seed_seventeenth_material_pulse.py",
                "scripts/seed_eighteenth_material_pulse.py",
                "scripts/seed_nineteenth_material_pulse.py",
                "scripts/seed_twentieth_material_pulse.py",
                "scripts/seed_twentyfirst_scale_bundle.py",
                "scripts/seed_twentysecond_scale_bundle.py",
                "scripts/seed_twentythird_scale_bundle.py",
                "scripts/seed_twentyfourth_scale_bundle.py",
                "scripts/seed_twentyfifth_scale_bundle.py",
                "scripts/seed_twentysixth_scale_bundle.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/run_first_scale_review.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )
            review = build_first_scale_review(runtime_root)

            self.assertIn("quiet_persistence:", result.stdout)
            self.assertIn("multi_speed_coexistence:", result.stdout)
            self.assertIn("reflux_effect:", result.stdout)
            self.assertIn("perspective_invariance:", result.stdout)
            self.assertIn("non_purpose_survival:", result.stdout)
            self.assertEqual(review["local_space_count"], 33)
            self.assertEqual(review["bridge_count"], 9)
            self.assertEqual(review["terrain_component_count"], 24)
            self.assertTrue(
                review["axes"]["perspective_invariance"]["service_local_space_count"]
                == review["axes"]["perspective_invariance"]["observer_local_space_state_total"]
            )

    def test_twentyseventh_scale_bundle_script_adds_four_more_quiet_spaces_without_new_bridges(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
                "scripts/seed_fourteenth_material_wave.py",
                "scripts/seed_seventeenth_material_pulse.py",
                "scripts/seed_eighteenth_material_pulse.py",
                "scripts/seed_nineteenth_material_pulse.py",
                "scripts/seed_twentieth_material_pulse.py",
                "scripts/seed_twentyfirst_scale_bundle.py",
                "scripts/seed_twentysecond_scale_bundle.py",
                "scripts/seed_twentythird_scale_bundle.py",
                "scripts/seed_twentyfourth_scale_bundle.py",
                "scripts/seed_twentyfifth_scale_bundle.py",
                "scripts/seed_twentysixth_scale_bundle.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_twentyseventh_scale_bundle.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("pipeline_local_space_id:", result.stdout)
            self.assertIn("meeting_local_space_id:", result.stdout)
            self.assertIn("diff_local_space_id:", result.stdout)
            self.assertIn("voice_local_space_id:", result.stdout)
            self.assertEqual(len(bridge_ids), 9)
            self.assertEqual(len(local_space_ids), 37)
            self.assertEqual(len(observation["terrain_components"]), 28)

    def test_twentyeighth_scale_bundle_script_adds_four_more_quiet_spaces_without_new_bridges(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
                "scripts/seed_fourteenth_material_wave.py",
                "scripts/seed_seventeenth_material_pulse.py",
                "scripts/seed_eighteenth_material_pulse.py",
                "scripts/seed_nineteenth_material_pulse.py",
                "scripts/seed_twentieth_material_pulse.py",
                "scripts/seed_twentyfirst_scale_bundle.py",
                "scripts/seed_twentysecond_scale_bundle.py",
                "scripts/seed_twentythird_scale_bundle.py",
                "scripts/seed_twentyfourth_scale_bundle.py",
                "scripts/seed_twentyfifth_scale_bundle.py",
                "scripts/seed_twentysixth_scale_bundle.py",
                "scripts/seed_twentyseventh_scale_bundle.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_twentyeighth_scale_bundle.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("browser_local_space_id:", result.stdout)
            self.assertIn("shell_local_space_id:", result.stdout)
            self.assertIn("disagreement_local_space_id:", result.stdout)
            self.assertIn("test_report_local_space_id:", result.stdout)
            self.assertEqual(len(bridge_ids), 9)
            self.assertEqual(len(local_space_ids), 41)
            self.assertEqual(len(observation["terrain_components"]), 32)

    def test_twentyninth_scale_bundle_script_adds_four_more_quiet_spaces_without_new_bridges(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
                "scripts/seed_fourteenth_material_wave.py",
                "scripts/seed_seventeenth_material_pulse.py",
                "scripts/seed_eighteenth_material_pulse.py",
                "scripts/seed_nineteenth_material_pulse.py",
                "scripts/seed_twentieth_material_pulse.py",
                "scripts/seed_twentyfirst_scale_bundle.py",
                "scripts/seed_twentysecond_scale_bundle.py",
                "scripts/seed_twentythird_scale_bundle.py",
                "scripts/seed_twentyfourth_scale_bundle.py",
                "scripts/seed_twentyfifth_scale_bundle.py",
                "scripts/seed_twentysixth_scale_bundle.py",
                "scripts/seed_twentyseventh_scale_bundle.py",
                "scripts/seed_twentyeighth_scale_bundle.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_twentyninth_scale_bundle.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            bridge_ids = list(service.bridges.list_ids())
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("archive_local_space_id:", result.stdout)
            self.assertIn("changelog_local_space_id:", result.stdout)
            self.assertIn("sketch_local_space_id:", result.stdout)
            self.assertIn("transcript_local_space_id:", result.stdout)
            self.assertEqual(len(bridge_ids), 9)
            self.assertEqual(len(local_space_ids), 45)
            self.assertEqual(len(observation["terrain_components"]), 36)

    def test_space_graph_view_is_written_with_local_space_and_bridge_counts(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
                "scripts/seed_fourteenth_material_wave.py",
                "scripts/seed_seventeenth_material_pulse.py",
                "scripts/seed_eighteenth_material_pulse.py",
                "scripts/seed_nineteenth_material_pulse.py",
                "scripts/seed_twentieth_material_pulse.py",
                "scripts/seed_twentyfirst_scale_bundle.py",
                "scripts/seed_twentysecond_scale_bundle.py",
                "scripts/seed_twentythird_scale_bundle.py",
                "scripts/seed_twentyfourth_scale_bundle.py",
                "scripts/seed_twentyfifth_scale_bundle.py",
                "scripts/seed_twentysixth_scale_bundle.py",
                "scripts/seed_twentyseventh_scale_bundle.py",
                "scripts/seed_twentyeighth_scale_bundle.py",
                "scripts/seed_twentyninth_scale_bundle.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            paths = write_space_graph_view(runtime_root)
            graph_json = json.loads(paths["json_path"].read_text(encoding="utf-8"))
            graph_html = paths["html_path"].read_text(encoding="utf-8")

            self.assertEqual(graph_json["summary"]["local_space_count"], 45)
            self.assertEqual(graph_json["summary"]["bridge_count"], 9)
            self.assertEqual(graph_json["summary"]["terrain_component_count"], 36)
            self.assertTrue(graph_json["nodes"][0]["materials"])
            self.assertIn("trace_details", graph_json["nodes"][0])
            self.assertIn("structure", graph_json["nodes"][0])
            self.assertIn("interpretation", graph_json["nodes"][0])
            self.assertIn("material_summary", graph_json["nodes"][0]["interpretation"])
            self.assertIn("raw_payload", graph_json["nodes"][0]["materials"][0])
            self.assertIn("latest_intake", graph_json)
            self.assertIn("latest_traces", graph_json)
            self.assertIn("공간 뷰어", graph_html)
            self.assertIn("브리지 선은 병합선이 아니라 노출 흔적", graph_html)
            self.assertIn("modal-backdrop", graph_html)
            self.assertIn("공간 상세", graph_html)
            self.assertIn("여기 있는 것:", graph_html)
            self.assertIn("space 카메라", graph_html)
            self.assertIn("material 카메라", graph_html)
            self.assertIn("물질단 카메라", graph_html)
            self.assertIn("원문", graph_html)
            self.assertIn("최근 유입", graph_html)
            self.assertIn("Stage0 provenance", graph_html)
            self.assertIn("신규 물질", graph_html)
            self.assertIn("mode-traces", graph_html)
            self.assertIn("trace 없음", render_space_graph_view_html(
                {
                    "summary": {
                        "local_space_count": 0,
                        "bridge_count": 0,
                        "terrain_component_count": 0,
                        "quiet_local_space_count": 0,
                        "bridge_exposed_local_space_count": 0,
                        "forming_local_space_count": 0,
                    },
                    "latest_intake": {},
                    "latest_materials": [],
                    "latest_traces": [],
                    "process_summary": {"summary_line": "empty-runtime"},
                    "components": [],
                    "nodes": [],
                    "edges": [],
                }
            ))

    def test_render_space_graph_view_html_can_include_live_intake_form(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            bootstrap_runtime_layout(runtime_root)

            html = render_space_graph_view_html(
                {
                    "summary": {
                        "local_space_count": 0,
                        "bridge_count": 0,
                        "terrain_component_count": 0,
                        "quiet_local_space_count": 0,
                        "bridge_exposed_local_space_count": 0,
                        "forming_local_space_count": 0,
                    },
                    "process_summary": {"summary_line": "empty-runtime"},
                    "components": [],
                    "nodes": [],
                    "edges": [],
                },
                interactive=True,
            )

            self.assertIn("입력 투입", html)
            self.assertIn("id=\"open-intake\"", html)
            self.assertIn("id=\"intake-form\"", html)
            self.assertIn("/api/ingest", html)
            self.assertIn("유형과 내용만 넣으면 제목은 자동으로 생성됩니다.", html)

    def test_dust_field_view_can_rebuild_existing_materials_into_dust_and_links(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            service = FormationService(runtime_root)
            service.ingest_material_with_role(
                raw_payload="하네스 설계와 AI 에이전트 운영은 큰 코드베이스에서 중요하다.",
                actor_id="actor-1",
                session_id="session-1",
                project_id="project-1",
                source_type="memo",
                source_ref="memo-dust-1",
                formation_role="memo_material",
            )
            service.ingest_material_with_role(
                raw_payload="큰 코드베이스 운영과 하네스 설계 패턴을 다시 읽는다.",
                actor_id="actor-1",
                session_id="session-2",
                project_id="project-1",
                source_type="memo",
                source_ref="memo-dust-2",
                formation_role="memo_material",
            )

            data = build_dust_field_data(runtime_root)
            html = render_dust_field_html(data)
            paths = write_dust_field_view(runtime_root)

            self.assertEqual(data["summary"]["material_count"], 2)
            self.assertEqual(data["summary"]["dust_count"], 2)
            self.assertGreaterEqual(data["summary"]["edge_count"], 1)
            self.assertIn("먼지 그래프", html)
            self.assertIn("Obsidian-like Dust Space", html)
            self.assertTrue(paths["json_path"].exists())
            self.assertTrue(paths["html_path"].exists())

    def test_live_input_emits_labeled_dust_and_relation_records_from_server_payload(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            result = ingest_live_input(
                runtime_root,
                {
                    "source_type": "paper",
                    "source_ref": "paper-note-1",
                    "family_id": "family-paper-1",
                    "raw_payload": "A paper excerpt enters the space through the local server.",
                },
            )

            service = FormationService(runtime_root)
            material_ids = list(service.materials.list_ids())
            trace_ids = list(service.traces.list_ids())
            seed_ids = list(service.seeds.list_ids())
            first_material = service.materials.get(material_ids[0])

            self.assertGreaterEqual(result["dust_count"], 1)
            self.assertEqual(result["material_count"], len(material_ids))
            self.assertEqual(result["trace_count"], len(trace_ids))
            self.assertEqual(len(result["local_space_ids"]), 0)
            self.assertEqual(len(result["bridge_ids"]), 0)
            self.assertEqual(first_material["source_type"], "paper")
            self.assertEqual(first_material["metadata"]["formation_role"], "paper_material")
            self.assertIn("scene", first_material["metadata"])
            self.assertIn("flow", first_material["metadata"])
            self.assertIn("anchors", first_material["metadata"])
            self.assertEqual(len(seed_ids), len(trace_ids))

    def test_stage0_handoff_decomposes_input_into_multiple_candidates(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            stage0_output = run_stage0_handoff(
                runtime_root,
                {
                    "source_type": "memo",
                    "raw_payload": (
                        "시간은 배경 축이 아니라 행동 특성일 수 있다.\n\n"
                        "어떤 존재는 빠르게 나타나 사라진다.\n\n"
                        "어떤 존재는 오랫동안 quiet하게 버틴다."
                    ),
                },
            )

            self.assertEqual(stage0_output["manifest"]["counts"]["fragment"], 3)
            self.assertEqual(stage0_output["manifest"]["counts"]["candidate"], 3)
            self.assertEqual(len(stage0_output["candidates"]), 3)
            self.assertEqual(stage0_output["manifest"]["decomposition_kind"], "axis_stage0_bridge_handoff")
            self.assertEqual(stage0_output["fragments"][0]["axes"]["time"], "unspecified")
            self.assertEqual(stage0_output["fragments"][1]["axes"]["time"], "rapid")
            self.assertEqual(stage0_output["fragments"][2]["axes"]["stability"], "stable")
            self.assertTrue((stage0_output["run_dir"] / "bridges.json").exists())

            handoff_bundle = build_handoff_materials(
                runtime_root,
                {
                    "source_type": "memo",
                    "raw_payload": (
                        "시간은 배경 축이 아니라 행동 특성일 수 있다.\n\n"
                        "어떤 존재는 빠르게 나타나 사라진다.\n\n"
                        "어떤 존재는 오랫동안 quiet하게 버틴다."
                    ),
                },
            )
            handoff_materials = handoff_bundle["handoff_materials"]

            self.assertEqual(len(handoff_materials), 3)
            self.assertTrue(handoff_materials[0]["candidate_id"].startswith("cand_"))
            self.assertTrue(handoff_materials[0]["bridge_id"].startswith("bridge_"))
            self.assertIn("axes", handoff_materials[0])
            self.assertIn("connectivity_keys", handoff_materials[0])

    def test_live_input_uses_stage0_handoff_and_creates_multiple_materials(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            result = ingest_live_input(
                runtime_root,
                {
                    "source_type": "memo",
                    "raw_payload": (
                        "시간은 배경 축이 아니라 행동 특성일 수 있다.\n\n"
                        "어떤 존재는 빠르게 나타나 사라진다.\n\n"
                        "어떤 존재는 오랫동안 quiet하게 버틴다."
                    ),
                },
            )

            service = FormationService(runtime_root)
            materials = service.materials.read_all()
            traces = service.traces.read_all()

            self.assertEqual(result["material_count"], 3)
            self.assertEqual(len(result["material_ids"]), 3)
            self.assertEqual(len(result["local_space_ids"]), 3)
            self.assertEqual(len(materials), 3)
            self.assertEqual(len(traces), 3)
            self.assertTrue(all(row["metadata"]["decomposition_kind"] == "axis_stage0_bridge_handoff" for row in materials))
            self.assertTrue(all("candidate_id" in row["metadata"] for row in materials))
            self.assertTrue(all("bridge_id" in row["metadata"] for row in materials))
            self.assertTrue(all("axes" in row["metadata"] for row in materials))
            self.assertTrue(all("connectivity_keys" in row["metadata"] for row in materials))
            self.assertEqual(sorted(row["metadata"]["scene_index"] for row in materials), [1, 2, 3])
            self.assertTrue(all(trace["evidence_kind"] == "memo_scene_flow_trace" for trace in traces))
            self.assertTrue(any(len(trace["material_refs"]) == 3 for trace in traces))
            self.assertTrue(any(any(ref["note"] == "flow_prev" for ref in trace["support_refs"]) for trace in traces))
            self.assertTrue(any(any(ref["note"] == "flow_next" for ref in trace["support_refs"]) for trace in traces))
            self.assertTrue(result["stage0_run_dir"].endswith(result["stage0_run_id"]))

    def test_live_input_adds_cross_context_trace_refs_for_related_recent_memos(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            first = ingest_live_input(
                runtime_root,
                {
                    "source_type": "memo",
                    "source_ref": "memo-cross-1",
                    "session_id": "live-session-shared",
                    "raw_payload": (
                        "AI 에이전트가 큰 코드베이스를 다룰 때 하네스 엔지니어링이 중요하다. "
                        "긴 코드베이스와 AI 협업 패턴은 설계와 운영을 함께 요구한다."
                    ),
                },
            )
            second = ingest_live_input(
                runtime_root,
                {
                    "source_type": "memo",
                    "source_ref": "memo-cross-2",
                    "session_id": "live-session-shared",
                    "raw_payload": (
                        "하네스 엔지니어링은 AI 에이전트가 긴 코드베이스를 다루도록 돕는다. "
                        "설계와 운영 패턴이 함께 보여야 큰 코드베이스 협업이 안정된다."
                    ),
                },
            )

            service = FormationService(runtime_root)
            traces = service.traces.read_all()
            second_material_ids = set(second["material_ids"])
            first_material_ids = set(first["material_ids"])
            related_second_traces = [
                trace for trace in traces if second_material_ids & set(trace.get("material_refs", ()))
            ]

            self.assertTrue(related_second_traces)
            self.assertTrue(
                any(first_material_ids & set(trace.get("material_refs", ())) for trace in related_second_traces)
            )
            self.assertTrue(
                any(
                    any(ref["note"] == "cross_context" for ref in trace.get("support_refs", ()))
                    for trace in related_second_traces
                )
            )

    def test_live_input_adds_global_field_refs_from_existing_runtime_materials(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            earlier = ingest_live_input(
                runtime_root,
                {
                    "source_type": "memo",
                    "source_ref": "memo-global-1",
                    "session_id": "older-session",
                    "raw_payload": (
                        "하네스 엔지니어링은 AI 에이전트가 큰 코드베이스를 다룰 때 중요하다. "
                        "코드베이스 운영 패턴과 설계 흐름이 함께 보여야 한다."
                    ),
                },
            )
            later = ingest_live_input(
                runtime_root,
                {
                    "source_type": "memo",
                    "source_ref": "memo-global-2",
                    "session_id": "newer-session",
                    "raw_payload": (
                        "AI 에이전트의 하네스 설계는 큰 코드베이스 운영에서 중요하다. "
                        "설계 흐름과 운영 패턴을 동시에 읽어야 한다."
                    ),
                },
            )

            service = FormationService(runtime_root)
            traces = service.traces.read_all()
            later_material_ids = set(later["material_ids"])
            earlier_material_ids = set(earlier["material_ids"])
            related_later_traces = [
                trace for trace in traces if later_material_ids & set(trace.get("material_refs", ()))
            ]

            self.assertTrue(related_later_traces)
            self.assertTrue(
                any(earlier_material_ids & set(trace.get("material_refs", ())) for trace in related_later_traces)
            )
            self.assertTrue(
                any(
                    any(ref["note"] == "global_field" for ref in trace.get("support_refs", ()))
                    for trace in related_later_traces
                )
            )
            self.assertFalse(later["bridge_ids"])

            third = ingest_live_input(
                runtime_root,
                {
                    "source_type": "memo",
                    "source_ref": "memo-global-3",
                    "session_id": "newer-session-2",
                    "raw_payload": (
                        "AI 에이전트 하네스 설계는 큰 코드베이스 운영에서 반복적으로 중요하다. "
                        "운영 패턴과 설계 흐름을 함께 읽어야 한다."
                    ),
                },
            )
            self.assertTrue(third["bridge_ids"])
            bridges = service.bridges.read_all()
            self.assertTrue(
                any(bridge["bridge_id"] in third["bridge_ids"] for bridge in bridges)
            )
            self.assertTrue(
                any(bridge["note"] == "recursive_stage_progression_from_trace" for bridge in bridges)
            )

    def test_live_input_limits_external_trace_amplification(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for index in range(1, 5):
                ingest_live_input(
                    runtime_root,
                    {
                        "source_type": "memo",
                        "source_ref": f"memo-saturation-{index}",
                        "session_id": f"session-{index}",
                        "raw_payload": (
                            "AI 에이전트와 하네스 설계는 큰 코드베이스 운영에서 중요하다. "
                            f"운영 패턴과 설계 흐름을 함께 본다 {index}."
                        ),
                    },
                )

            result = ingest_live_input(
                runtime_root,
                {
                    "source_type": "memo",
                    "source_ref": "memo-saturation-final",
                    "session_id": "session-final",
                    "raw_payload": (
                        "하네스 설계와 AI 에이전트 운영은 큰 코드베이스에서 중요하다. "
                        "설계 흐름과 운영 패턴을 함께 본다."
                    ),
                },
            )

            service = FormationService(runtime_root)
            traces = service.traces.read_all()
            result_material_ids = set(result["material_ids"])
            related_traces = [trace for trace in traces if result_material_ids & set(trace.get("material_refs", ()))]

            self.assertTrue(related_traces)
            for trace in related_traces:
                source_refs = set()
                for material_id in trace.get("material_refs", ()):
                    material = service.materials.get(material_id)
                    if material:
                        source_refs.add(material.get("source_ref"))
                self.assertLessEqual(len(source_refs), 3)
                external_notes = [
                    ref["note"]
                    for ref in trace.get("support_refs", ())
                    if ref["note"] in {"cross_context", "global_field"}
                ]
                self.assertLessEqual(len(external_notes), 2)

    def test_phase2_real_data_bundle_uses_actual_files_under_same_physics(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
                "scripts/seed_fourteenth_material_wave.py",
                "scripts/seed_seventeenth_material_pulse.py",
                "scripts/seed_eighteenth_material_pulse.py",
                "scripts/seed_nineteenth_material_pulse.py",
                "scripts/seed_twentieth_material_pulse.py",
                "scripts/seed_twentyfirst_scale_bundle.py",
                "scripts/seed_twentysecond_scale_bundle.py",
                "scripts/seed_twentythird_scale_bundle.py",
                "scripts/seed_twentyfourth_scale_bundle.py",
                "scripts/seed_twentyfifth_scale_bundle.py",
                "scripts/seed_twentysixth_scale_bundle.py",
                "scripts/seed_twentyseventh_scale_bundle.py",
                "scripts/seed_twentyeighth_scale_bundle.py",
                "scripts/seed_twentyninth_scale_bundle.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_phase2_real_data_bundle.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("worklog_local_space_id:", result.stdout)
            self.assertIn("space_report_local_space_id:", result.stdout)
            self.assertIn("readme_local_space_id:", result.stdout)
            self.assertIn("actual_relation_local_space_id:", result.stdout)
            self.assertEqual(len(local_space_ids), 49)
            self.assertEqual(len(observation["terrain_components"]), 40)

    def test_phase2_memo_bundle_uses_actual_memo_files_under_same_physics(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
                "scripts/seed_fourteenth_material_wave.py",
                "scripts/seed_seventeenth_material_pulse.py",
                "scripts/seed_eighteenth_material_pulse.py",
                "scripts/seed_nineteenth_material_pulse.py",
                "scripts/seed_twentieth_material_pulse.py",
                "scripts/seed_twentyfirst_scale_bundle.py",
                "scripts/seed_twentysecond_scale_bundle.py",
                "scripts/seed_twentythird_scale_bundle.py",
                "scripts/seed_twentyfourth_scale_bundle.py",
                "scripts/seed_twentyfifth_scale_bundle.py",
                "scripts/seed_twentysixth_scale_bundle.py",
                "scripts/seed_twentyseventh_scale_bundle.py",
                "scripts/seed_twentyeighth_scale_bundle.py",
                "scripts/seed_twentyninth_scale_bundle.py",
                "scripts/seed_phase2_real_data_bundle.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_phase2_memo_bundle.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("memo1_local_space_id:", result.stdout)
            self.assertIn("memo2_local_space_id:", result.stdout)
            self.assertIn("memo_relation_local_space_id:", result.stdout)
            self.assertEqual(len(local_space_ids), 52)
            self.assertEqual(len(observation["terrain_components"]), 43)

    def test_phase2_memo3_bundle_uses_actual_memo3_under_same_physics(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
                "scripts/seed_fourteenth_material_wave.py",
                "scripts/seed_seventeenth_material_pulse.py",
                "scripts/seed_eighteenth_material_pulse.py",
                "scripts/seed_nineteenth_material_pulse.py",
                "scripts/seed_twentieth_material_pulse.py",
                "scripts/seed_twentyfirst_scale_bundle.py",
                "scripts/seed_twentysecond_scale_bundle.py",
                "scripts/seed_twentythird_scale_bundle.py",
                "scripts/seed_twentyfourth_scale_bundle.py",
                "scripts/seed_twentyfifth_scale_bundle.py",
                "scripts/seed_twentysixth_scale_bundle.py",
                "scripts/seed_twentyseventh_scale_bundle.py",
                "scripts/seed_twentyeighth_scale_bundle.py",
                "scripts/seed_twentyninth_scale_bundle.py",
                "scripts/seed_phase2_real_data_bundle.py",
                "scripts/seed_phase2_memo_bundle.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_phase2_memo3_bundle.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("memo3_local_space_id:", result.stdout)
            self.assertIn("memo23_relation_local_space_id:", result.stdout)
            self.assertEqual(len(local_space_ids), 54)
            self.assertGreaterEqual(len(observation["terrain_components"]), 44)

    def test_phase2_memo4_bundle_uses_actual_memo4_under_same_physics(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
                "scripts/seed_fourteenth_material_wave.py",
                "scripts/seed_seventeenth_material_pulse.py",
                "scripts/seed_eighteenth_material_pulse.py",
                "scripts/seed_nineteenth_material_pulse.py",
                "scripts/seed_twentieth_material_pulse.py",
                "scripts/seed_twentyfirst_scale_bundle.py",
                "scripts/seed_twentysecond_scale_bundle.py",
                "scripts/seed_twentythird_scale_bundle.py",
                "scripts/seed_twentyfourth_scale_bundle.py",
                "scripts/seed_twentyfifth_scale_bundle.py",
                "scripts/seed_twentysixth_scale_bundle.py",
                "scripts/seed_twentyseventh_scale_bundle.py",
                "scripts/seed_twentyeighth_scale_bundle.py",
                "scripts/seed_twentyninth_scale_bundle.py",
                "scripts/seed_phase2_real_data_bundle.py",
                "scripts/seed_phase2_memo_bundle.py",
                "scripts/seed_phase2_memo3_bundle.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_phase2_memo4_bundle.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("memo4_local_space_id:", result.stdout)
            self.assertIn("memo34_relation_local_space_id:", result.stdout)
            self.assertEqual(len(local_space_ids), 56)
            self.assertGreaterEqual(len(observation["terrain_components"]), 46)

    def test_phase2_memo5_bundle_uses_actual_memo5_under_same_physics(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
                "scripts/seed_fourteenth_material_wave.py",
                "scripts/seed_seventeenth_material_pulse.py",
                "scripts/seed_eighteenth_material_pulse.py",
                "scripts/seed_nineteenth_material_pulse.py",
                "scripts/seed_twentieth_material_pulse.py",
                "scripts/seed_twentyfirst_scale_bundle.py",
                "scripts/seed_twentysecond_scale_bundle.py",
                "scripts/seed_twentythird_scale_bundle.py",
                "scripts/seed_twentyfourth_scale_bundle.py",
                "scripts/seed_twentyfifth_scale_bundle.py",
                "scripts/seed_twentysixth_scale_bundle.py",
                "scripts/seed_twentyseventh_scale_bundle.py",
                "scripts/seed_twentyeighth_scale_bundle.py",
                "scripts/seed_twentyninth_scale_bundle.py",
                "scripts/seed_phase2_real_data_bundle.py",
                "scripts/seed_phase2_memo_bundle.py",
                "scripts/seed_phase2_memo3_bundle.py",
                "scripts/seed_phase2_memo4_bundle.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_phase2_memo5_bundle.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("memo5_local_space_id:", result.stdout)
            self.assertIn("memo45_relation_local_space_id:", result.stdout)
            self.assertEqual(len(local_space_ids), 58)
            self.assertGreaterEqual(len(observation["terrain_components"]), 48)

    def test_phase2_memo6_bundle_uses_actual_memo6_under_same_physics(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
                "scripts/seed_fourteenth_material_wave.py",
                "scripts/seed_seventeenth_material_pulse.py",
                "scripts/seed_eighteenth_material_pulse.py",
                "scripts/seed_nineteenth_material_pulse.py",
                "scripts/seed_twentieth_material_pulse.py",
                "scripts/seed_twentyfirst_scale_bundle.py",
                "scripts/seed_twentysecond_scale_bundle.py",
                "scripts/seed_twentythird_scale_bundle.py",
                "scripts/seed_twentyfourth_scale_bundle.py",
                "scripts/seed_twentyfifth_scale_bundle.py",
                "scripts/seed_twentysixth_scale_bundle.py",
                "scripts/seed_twentyseventh_scale_bundle.py",
                "scripts/seed_twentyeighth_scale_bundle.py",
                "scripts/seed_twentyninth_scale_bundle.py",
                "scripts/seed_phase2_real_data_bundle.py",
                "scripts/seed_phase2_memo_bundle.py",
                "scripts/seed_phase2_memo3_bundle.py",
                "scripts/seed_phase2_memo4_bundle.py",
                "scripts/seed_phase2_memo5_bundle.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_phase2_memo6_bundle.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("memo6_local_space_id:", result.stdout)
            self.assertIn("memo56_relation_local_space_id:", result.stdout)
            self.assertEqual(len(local_space_ids), 60)
            self.assertGreaterEqual(len(observation["terrain_components"]), 50)

    def test_phase2_memo7_bundle_uses_actual_memo7_under_same_physics(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
                "scripts/seed_fourteenth_material_wave.py",
                "scripts/seed_seventeenth_material_pulse.py",
                "scripts/seed_eighteenth_material_pulse.py",
                "scripts/seed_nineteenth_material_pulse.py",
                "scripts/seed_twentieth_material_pulse.py",
                "scripts/seed_twentyfirst_scale_bundle.py",
                "scripts/seed_twentysecond_scale_bundle.py",
                "scripts/seed_twentythird_scale_bundle.py",
                "scripts/seed_twentyfourth_scale_bundle.py",
                "scripts/seed_twentyfifth_scale_bundle.py",
                "scripts/seed_twentysixth_scale_bundle.py",
                "scripts/seed_twentyseventh_scale_bundle.py",
                "scripts/seed_twentyeighth_scale_bundle.py",
                "scripts/seed_twentyninth_scale_bundle.py",
                "scripts/seed_phase2_real_data_bundle.py",
                "scripts/seed_phase2_memo_bundle.py",
                "scripts/seed_phase2_memo3_bundle.py",
                "scripts/seed_phase2_memo4_bundle.py",
                "scripts/seed_phase2_memo5_bundle.py",
                "scripts/seed_phase2_memo6_bundle.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_phase2_memo7_bundle.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("memo7_local_space_id:", result.stdout)
            self.assertIn("memo67_relation_local_space_id:", result.stdout)
            self.assertEqual(len(local_space_ids), 62)
            self.assertGreaterEqual(len(observation["terrain_components"]), 52)

    def test_phase2_memo8_bundle_uses_actual_memo8_under_same_physics(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
                "scripts/seed_third_material_wave.py",
                "scripts/seed_fourth_material_wave.py",
                "scripts/seed_fifth_material_wave.py",
                "scripts/seed_sixth_material_wave.py",
                "scripts/seed_seventh_material_wave.py",
                "scripts/seed_eighth_material_wave.py",
                "scripts/seed_ninth_material_wave.py",
                "scripts/seed_tenth_material_wave.py",
                "scripts/seed_eleventh_material_wave.py",
                "scripts/seed_twelfth_material_wave.py",
                "scripts/seed_thirteenth_material_wave.py",
                "scripts/seed_fourteenth_material_wave.py",
                "scripts/seed_seventeenth_material_pulse.py",
                "scripts/seed_eighteenth_material_pulse.py",
                "scripts/seed_nineteenth_material_pulse.py",
                "scripts/seed_twentieth_material_pulse.py",
                "scripts/seed_twentyfirst_scale_bundle.py",
                "scripts/seed_twentysecond_scale_bundle.py",
                "scripts/seed_twentythird_scale_bundle.py",
                "scripts/seed_twentyfourth_scale_bundle.py",
                "scripts/seed_twentyfifth_scale_bundle.py",
                "scripts/seed_twentysixth_scale_bundle.py",
                "scripts/seed_twentyseventh_scale_bundle.py",
                "scripts/seed_twentyeighth_scale_bundle.py",
                "scripts/seed_twentyninth_scale_bundle.py",
                "scripts/seed_phase2_real_data_bundle.py",
                "scripts/seed_phase2_memo_bundle.py",
                "scripts/seed_phase2_memo3_bundle.py",
                "scripts/seed_phase2_memo4_bundle.py",
                "scripts/seed_phase2_memo5_bundle.py",
                "scripts/seed_phase2_memo6_bundle.py",
                "scripts/seed_phase2_memo7_bundle.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/seed_phase2_memo8_bundle.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            local_space_ids = list(service.local_spaces.list_ids())
            observation = build_reactive_space_observation(runtime_root)

            self.assertIn("memo8_local_space_id:", result.stdout)
            self.assertIn("memo78_relation_local_space_id:", result.stdout)
            self.assertEqual(len(local_space_ids), 64)
            self.assertGreaterEqual(len(observation["terrain_components"]), 54)

    def test_reread_audit_warns_when_reread_stack_outpaces_runtime_scale(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
                "scripts/reactivate_initial_cell.py",
                "scripts/seed_second_material_wave.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            audit = build_reread_audit(runtime_root)

            self.assertEqual(audit["posture"], "reread_heavy")
            self.assertIn("reread_stack_is_deep", audit["risks"])
            self.assertIn("reread_density_exceeds_runtime_scale", audit["risks"])

    def test_converge_initial_space_cell_script_creates_one_candidate_cell_without_local_space(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/converge_initial_space_cell.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            cell_ids = list(service.cells.list_ids())
            local_space_ids = list(service.local_spaces.list_ids())
            seed_ids = list(service.seeds.list_ids())
            seed_record = service.seeds.get(seed_ids[0])
            cell_record = service.cells.get(cell_ids[0])

            self.assertIn("cell_state: candidate", result.stdout)
            self.assertEqual(len(cell_ids), 1)
            self.assertEqual(len(local_space_ids), 0)
            self.assertEqual(seed_record["state"], SeedState.CELL_BOUND.value)
            self.assertEqual(len(cell_record["trace_refs"]), 2)
            self.assertEqual(len(cell_record["boundary"]["exterior_refs"]), 2)

    def test_reactivate_initial_cell_script_thickens_candidate_without_local_space(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"

            for script_name in [
                "scripts/seed_initial_materials.py",
                "scripts/trace_initial_relation.py",
                "scripts/seed_fresh_pressure_input.py",
                "scripts/converge_initial_space_cell.py",
            ]:
                subprocess.run(
                    ["python3", script_name, str(runtime_root)],
                    cwd="/Users/sungsookim/universe/vectorfl_next",
                    capture_output=True,
                    text=True,
                    check=True,
                )

            result = subprocess.run(
                ["python3", "scripts/reactivate_initial_cell.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            service = FormationService(runtime_root)
            cell_ids = list(service.cells.list_ids())
            local_space_ids = list(service.local_spaces.list_ids())
            event_rows = service.events.read_all()
            reacted_events = [row for row in event_rows if row["event_type"] == "space_cell_reacted"]
            cell_record = service.cells.get(cell_ids[0])

            self.assertIn("cell_state: held", result.stdout)
            self.assertEqual(len(cell_ids), 1)
            self.assertEqual(len(local_space_ids), 0)
            self.assertEqual(cell_record["state"], CellState.HELD.value)
            self.assertEqual(reacted_events[-1]["payload"]["reaction_kind"], "thickening")

    def test_reactive_space_observer_summarizes_reaction_distribution(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            service = FormationService(runtime_root)
            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="recurrence_pressure", strength_hint=0.7)]
            )
            cell_one = service.create_space_cell_candidate(
                material_refs=["mat-1"],
                trace_refs=["trc-1"],
                seed_refs=["sed-1"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["shared-a"],
                exterior_refs=["outer-a"],
                cohesion_note="observer-1",
            )
            cell_two = service.create_space_cell_candidate(
                material_refs=["mat-2"],
                trace_refs=["trc-2"],
                seed_refs=["sed-2"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["shared-b"],
                exterior_refs=["outer-b"],
                cohesion_note="observer-2",
            )
            service.reactivate_space_cell(cell_one.cell_id, "thickening", pressure.profile_id, "thick")
            service.reactivate_space_cell(cell_two.cell_id, "relocation", pressure.profile_id, "move")
            local_space = service.form_local_space([cell_one.cell_id, cell_two.cell_id], pressure.profile_id)
            service.derive_bridge_trace_from_cells(
                from_local_space_id=local_space.local_space_id,
                to_local_space_id="lsp_other",
                via_cell_ids=[cell_one.cell_id, cell_two.cell_id],
                note="observer-bridge",
            )

            observation = build_reactive_space_observation(runtime_root)

            self.assertEqual(observation["reaction_counts"]["thickening"], 1)
            self.assertEqual(observation["reaction_counts"]["relocation"], 1)
            self.assertFalse(observation["branch_reason_counts"])
            self.assertEqual(observation["process_summary"]["dominant_mode"], "continuity_process")
            self.assertEqual(observation["local_space_states"][LocalSpaceState.BRIDGE_EXPOSED.value], 1)
            self.assertTrue(observation["local_space_maturation_signals"])
            self.assertTrue(observation["bridge_maturation_signals"])
            self.assertTrue(observation["terrain_components"])
            self.assertTrue(observation["bridge_states"])
            self.assertEqual(len(observation["reaction_sequence"]), 2)
            self.assertTrue(observation["pressure_signatures"])
            self.assertTrue(observation["pressure_axis_distribution"])
            self.assertTrue(observation["pressure_axis_combinations"])

    def test_reactive_space_observer_reads_branch_reasons(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            service = FormationService(runtime_root)

            first_material = service.ingest_material(
                raw_payload="family branch first",
                actor_id="actor-1",
                session_id="session-1",
                project_id="project-1",
                source_type="note",
                source_ref="branch-1",
                family_id="family-branch",
            )
            second_material = service.ingest_material(
                raw_payload="family branch second",
                actor_id="actor-1",
                session_id="session-2",
                project_id="project-1",
                source_type="note",
                source_ref="branch-2",
                family_id="family-branch",
            )
            trace_one = service.register_trace(
                material_refs=[first_material.material_id],
                evidence_kind="branch-a",
                support_refs=[SupportRef(ref_kind="material", ref_id=first_material.material_id)],
            )
            trace_two = service.register_trace(
                material_refs=[second_material.material_id],
                evidence_kind="branch-b",
                support_refs=[SupportRef(ref_kind="material", ref_id=second_material.material_id)],
            )
            pressure_one = service.create_pressure_profile(
                axes=[PressureAxis(axis="session_pressure", strength_hint=0.3)]
            )
            pressure_two = service.create_pressure_profile(
                axes=[PressureAxis(axis="session_pressure", strength_hint=0.9)]
            )
            seed_one = service.create_point_seed_candidate(
                material_refs=[first_material.material_id],
                trace_refs=[trace_one.trace_id],
                pressure_profile_id=pressure_one.profile_id,
            )
            seed_two = service.create_reentry_seed_for_family(
                family_id="family-branch",
                material_refs=[second_material.material_id],
                trace_refs=[trace_two.trace_id],
                pressure_profile_id=pressure_two.profile_id,
            )

            service.create_or_branch_space_cell_for_family(
                family_id="family-branch",
                material_refs=[first_material.material_id],
                trace_refs=[trace_one.trace_id],
                seed_refs=[seed_one.seed_id],
                pressure_profile_id=pressure_one.profile_id,
                interior_refs=[first_material.material_id],
                exterior_refs=["outer-1"],
            )
            service.create_or_branch_space_cell_for_family(
                family_id="family-branch",
                material_refs=[second_material.material_id],
                trace_refs=[trace_two.trace_id],
                seed_refs=[seed_two.seed_id],
                pressure_profile_id=pressure_two.profile_id,
                interior_refs=[second_material.material_id],
                exterior_refs=["outer-2"],
            )

            observation = build_reactive_space_observation(runtime_root)

            self.assertEqual(
                observation["branch_reason_counts"]["pressure_signature_mismatch_or_absent"],
                2,
            )
            self.assertTrue(observation["branch_sequence"])
            self.assertTrue(observation["branched_cell_ids"]["pressure_signature_mismatch_or_absent"])
            self.assertEqual(observation["process_summary"]["dominant_mode"], "branching_process")

    def test_reactive_space_observer_marks_mixed_process_when_thickening_and_branching_coexist(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            service = FormationService(runtime_root)

            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="session_pressure", strength_hint=0.5)]
            )
            cell = service.create_space_cell_candidate(
                material_refs=["mat-mix-a"],
                trace_refs=["trc-mix-a"],
                seed_refs=["sed-mix-a"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["inside-mix-a"],
                exterior_refs=["outside-mix-a"],
                cohesion_note="mixed-a",
            )
            service.reactivate_space_cell(cell.cell_id, "thickening", pressure.profile_id, "held")
            service._append_event(
                "space_cell_branched",
                "space_cell",
                cell.cell_id,
                {"family_id": "family-mix", "reason": "pressure_signature_mismatch_or_absent"},
            )

            observation = build_reactive_space_observation(runtime_root)

            self.assertEqual(observation["process_summary"]["dominant_mode"], "mixed_process")
            self.assertIn("continuity", observation["process_summary"]["phase_tags"])
            self.assertIn("mismatch_branching", observation["process_summary"]["phase_tags"])

    def test_observe_reactive_space_script_prints_reaction_summary(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            service = FormationService(runtime_root)
            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="tone_pressure", strength_hint=0.8)]
            )
            cell = service.create_space_cell_candidate(
                material_refs=["mat-rs"],
                trace_refs=["trc-rs"],
                seed_refs=["sed-rs"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["inside-rs"],
                exterior_refs=["outside-rs"],
                cohesion_note="reactive-script",
            )
            service.reactivate_space_cell(cell.cell_id, "split", pressure.profile_id, "split-now")

            result = subprocess.run(
                ["python3", "scripts/observe_reactive_space.py", str(runtime_root)],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            self.assertIn("reaction_counts:", result.stdout)
            self.assertIn("process_mode:", result.stdout)
            self.assertIn("process_summary:", result.stdout)
            self.assertIn("- split: 1", result.stdout)
            self.assertIn("pressure_signatures:", result.stdout)
            self.assertIn("pressure_axes:", result.stdout)
            self.assertIn("pressure_axis_combinations:", result.stdout)
            self.assertIn("pressure_transitions:", result.stdout)
            self.assertIn("branch_reasons:", result.stdout)
            self.assertIn("branch_sequence:", result.stdout)
            self.assertIn("reaction_sequence:", result.stdout)

    def test_scoped_reactive_observation_can_filter_by_recent_limit_and_family(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            service = FormationService(runtime_root)
            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="session_pressure", strength_hint=0.6)]
            )
            material_a = service.ingest_material(
                raw_payload="family scoped a",
                actor_id="actor-1",
                session_id="session-a",
                project_id="project-1",
                source_type="note",
                source_ref="note-a",
                family_id="family-scope",
            )
            material_b = service.ingest_material(
                raw_payload="family scoped b",
                actor_id="actor-1",
                session_id="session-b",
                project_id="project-1",
                source_type="note",
                source_ref="note-b",
                family_id="family-other",
            )
            cell_a = service.create_space_cell_candidate(
                material_refs=[material_a.material_id],
                trace_refs=["trc-a"],
                seed_refs=["sed-a"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["inner-a"],
                exterior_refs=["outer-a"],
                cohesion_note="scope-a",
            )
            cell_b = service.create_space_cell_candidate(
                material_refs=[material_b.material_id],
                trace_refs=["trc-b"],
                seed_refs=["sed-b"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["inner-b"],
                exterior_refs=["outer-b"],
                cohesion_note="scope-b",
            )
            service.reactivate_space_cell(cell_a.cell_id, "thickening", pressure.profile_id, "a-1")
            service.reactivate_space_cell(cell_b.cell_id, "split", pressure.profile_id, "b-1")
            service.reactivate_space_cell(cell_a.cell_id, "relocation", pressure.profile_id, "a-2")

            recent_observation = build_scoped_reactive_space_observation(runtime_root, recent_limit=1)
            family_observation = build_scoped_reactive_space_observation(runtime_root, family_id="family-scope")

            self.assertEqual(sum(recent_observation["reaction_counts"].values()), 1)
            self.assertEqual(recent_observation["reaction_counts"]["relocation"], 1)
            self.assertEqual(family_observation["reaction_counts"]["thickening"], 1)
            self.assertEqual(family_observation["reaction_counts"]["relocation"], 1)
            self.assertEqual(family_observation["reaction_counts"]["split"], 0)

    def test_scoped_reactive_observation_can_filter_by_recent_seconds(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            service = FormationService(runtime_root)
            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="session_pressure", strength_hint=0.6)]
            )
            material = service.ingest_material(
                raw_payload="recent seconds",
                actor_id="actor-1",
                session_id="session-rs",
                project_id="project-1",
                source_type="note",
                source_ref="note-rs",
                family_id="family-rs",
            )
            cell = service.create_space_cell_candidate(
                material_refs=[material.material_id],
                trace_refs=["trc-rs"],
                seed_refs=["sed-rs"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["in-rs"],
                exterior_refs=["out-rs"],
                cohesion_note="recent-seconds",
            )
            service.reactivate_space_cell(cell.cell_id, "thickening", pressure.profile_id, "old")
            service.reactivate_space_cell(cell.cell_id, "relocation", pressure.profile_id, "new")

            event_path = runtime_root / "events" / "formation_events.jsonl"
            rows = []
            with event_path.open("r", encoding="utf-8") as handle:
                for line in handle:
                    if line.strip():
                        rows.append(json.loads(line))
            changed_old = False
            for row in rows:
                if row["event_type"] == "space_cell_reacted" and row["payload"]["reaction_kind"] == "thickening" and not changed_old:
                    row["occurred_at"] = "2000-01-01T00:00:00+00:00"
                    changed_old = True
            with event_path.open("w", encoding="utf-8") as handle:
                for row in rows:
                    handle.write(json.dumps(row, ensure_ascii=True) + "\n")

            recent_seconds_observation = build_scoped_reactive_space_observation(
                runtime_root,
                recent_seconds=60,
            )

            self.assertEqual(recent_seconds_observation["reaction_counts"]["thickening"], 0)
            self.assertEqual(recent_seconds_observation["reaction_counts"]["relocation"], 1)

    def test_scoped_reactive_observation_can_filter_by_session(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            service = FormationService(runtime_root)
            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="session_pressure", strength_hint=0.7)]
            )
            material_a = service.ingest_material(
                raw_payload="session scoped a",
                actor_id="actor-1",
                session_id="session-x",
                project_id="project-1",
                source_type="note",
                source_ref="note-x",
                family_id="family-x",
            )
            material_b = service.ingest_material(
                raw_payload="session scoped b",
                actor_id="actor-1",
                session_id="session-y",
                project_id="project-1",
                source_type="note",
                source_ref="note-y",
                family_id="family-y",
            )
            cell_a = service.create_space_cell_candidate(
                material_refs=[material_a.material_id],
                trace_refs=["trc-x"],
                seed_refs=["sed-x"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["inner-x"],
                exterior_refs=["outer-x"],
                cohesion_note="session-x",
            )
            cell_b = service.create_space_cell_candidate(
                material_refs=[material_b.material_id],
                trace_refs=["trc-y"],
                seed_refs=["sed-y"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["inner-y"],
                exterior_refs=["outer-y"],
                cohesion_note="session-y",
            )
            service.reactivate_space_cell(cell_a.cell_id, "thickening", pressure.profile_id, "x-1")
            service.reactivate_space_cell(cell_b.cell_id, "split", pressure.profile_id, "y-1")

            session_observation = build_scoped_reactive_space_observation(
                runtime_root,
                session_id="session-x",
            )

            self.assertEqual(session_observation["reaction_counts"]["thickening"], 1)
            self.assertEqual(session_observation["reaction_counts"]["split"], 0)
            self.assertEqual(session_observation["scope"]["session_id"], "session-x")

    def test_session_timeline_compacts_reaction_flow_for_one_session(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            service = FormationService(runtime_root)
            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="session_pressure", strength_hint=0.65)]
            )
            pressure_shifted = service.create_pressure_profile(
                axes=[PressureAxis(axis="session_pressure", strength_hint=0.95)]
            )
            material = service.ingest_material(
                raw_payload="timeline session",
                actor_id="actor-1",
                session_id="session-timeline",
                project_id="project-1",
                source_type="note",
                source_ref="note-timeline",
                family_id="family-timeline",
            )
            cell = service.create_space_cell_candidate(
                material_refs=[material.material_id],
                trace_refs=["trc-tl"],
                seed_refs=["sed-tl"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["in-tl"],
                exterior_refs=["out-tl"],
                cohesion_note="timeline",
            )
            service.reactivate_space_cell(cell.cell_id, "thickening", pressure.profile_id, "tl-1")
            service.reactivate_space_cell(cell.cell_id, "thickening", pressure_shifted.profile_id, "tl-1b")
            service.reactivate_space_cell(cell.cell_id, "relocation", pressure_shifted.profile_id, "tl-2")

            timeline = build_session_timeline(runtime_root, "session-timeline")

            self.assertEqual(timeline["session_id"], "session-timeline")
            self.assertEqual(timeline["event_count"], 3)
            self.assertEqual(timeline["reaction_counts"]["thickening"], 2)
            self.assertEqual(timeline["reaction_counts"]["relocation"], 1)
            self.assertEqual(len(timeline["phases"]), 3)
            self.assertEqual(timeline["phases"][0]["reaction_kind"], "thickening")
            self.assertEqual(timeline["phases"][0]["event_count"], 1)
            self.assertNotEqual(
                timeline["phases"][0]["pressure_signature"],
                timeline["phases"][1]["pressure_signature"],
            )

    def test_pressure_transition_frequency_is_observed(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            service = FormationService(runtime_root)
            pressure_a = service.create_pressure_profile(
                axes=[PressureAxis(axis="session_pressure", strength_hint=0.3)]
            )
            pressure_b = service.create_pressure_profile(
                axes=[PressureAxis(axis="session_pressure", strength_hint=0.9)]
            )
            material = service.ingest_material(
                raw_payload="pressure transition",
                actor_id="actor-1",
                session_id="session-pt",
                project_id="project-1",
                source_type="note",
                source_ref="note-pt",
                family_id="family-pt",
            )
            cell = service.create_space_cell_candidate(
                material_refs=[material.material_id],
                trace_refs=["trc-pt"],
                seed_refs=["sed-pt"],
                pressure_profile_id=pressure_a.profile_id,
                interior_refs=["in-pt"],
                exterior_refs=["out-pt"],
                cohesion_note="pressure-transition",
            )
            service.reactivate_space_cell(cell.cell_id, "thickening", pressure_a.profile_id, "pt-1")
            service.reactivate_space_cell(cell.cell_id, "thickening", pressure_b.profile_id, "pt-2")
            service.reactivate_space_cell(cell.cell_id, "relocation", pressure_b.profile_id, "pt-3")

            observation = build_reactive_space_observation(runtime_root)

            self.assertTrue(observation["pressure_transitions"])
            keys = list(observation["pressure_transitions"].keys())
            self.assertTrue(any("session_pressure:low -> session_pressure:high" in key for key in keys))

    def test_observe_reactive_space_script_accepts_scope_flags(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            service = FormationService(runtime_root)
            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="tone_pressure", strength_hint=0.8)]
            )
            material = service.ingest_material(
                raw_payload="family flagged",
                actor_id="actor-1",
                session_id="session-flag",
                project_id="project-1",
                source_type="note",
                source_ref="note-flag",
                family_id="family-flag",
            )
            cell = service.create_space_cell_candidate(
                material_refs=[material.material_id],
                trace_refs=["trc-f"],
                seed_refs=["sed-f"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["in-f"],
                exterior_refs=["out-f"],
                cohesion_note="flagged",
            )
            service.reactivate_space_cell(cell.cell_id, "thickening", pressure.profile_id, "flag")

            result = subprocess.run(
                [
                    "python3",
                    "scripts/observe_reactive_space.py",
                    str(runtime_root),
                    "--recent",
                    "1",
                    "--family",
                    "family-flag",
                ],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            self.assertIn("scope_recent_limit: 1", result.stdout)
            self.assertIn("scope_family_id: family-flag", result.stdout)

    def test_observe_reactive_space_script_accepts_recent_seconds(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            service = FormationService(runtime_root)
            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="tone_pressure", strength_hint=0.8)]
            )
            material = service.ingest_material(
                raw_payload="recent seconds flagged",
                actor_id="actor-1",
                session_id="session-rs-flag",
                project_id="project-1",
                source_type="note",
                source_ref="note-rs-flag",
                family_id="family-rs-flag",
            )
            cell = service.create_space_cell_candidate(
                material_refs=[material.material_id],
                trace_refs=["trc-rsf"],
                seed_refs=["sed-rsf"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["in-rsf"],
                exterior_refs=["out-rsf"],
                cohesion_note="rs-flag",
            )
            service.reactivate_space_cell(cell.cell_id, "thickening", pressure.profile_id, "flag")

            result = subprocess.run(
                [
                    "python3",
                    "scripts/observe_reactive_space.py",
                    str(runtime_root),
                    "--recent-seconds",
                    "60",
                ],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            self.assertIn("scope_recent_seconds: 60", result.stdout)

    def test_observe_reactive_space_script_accepts_session_scope(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            runtime_root = Path(tmpdir) / "runtime"
            service = FormationService(runtime_root)
            pressure = service.create_pressure_profile(
                axes=[PressureAxis(axis="tone_pressure", strength_hint=0.8)]
            )
            material = service.ingest_material(
                raw_payload="session flagged",
                actor_id="actor-1",
                session_id="session-flagged",
                project_id="project-1",
                source_type="note",
                source_ref="note-session",
                family_id="family-session",
            )
            cell = service.create_space_cell_candidate(
                material_refs=[material.material_id],
                trace_refs=["trc-s"],
                seed_refs=["sed-s"],
                pressure_profile_id=pressure.profile_id,
                interior_refs=["in-s"],
                exterior_refs=["out-s"],
                cohesion_note="session-flagged",
            )
            service.reactivate_space_cell(cell.cell_id, "thickening", pressure.profile_id, "session")

            result = subprocess.run(
                [
                    "python3",
                    "scripts/observe_reactive_space.py",
                    str(runtime_root),
                    "--session",
                    "session-flagged",
                ],
                cwd="/Users/sungsookim/universe/vectorfl_next",
                capture_output=True,
                text=True,
                check=True,
            )

            self.assertIn("scope_session_id: session-flagged", result.stdout)
            self.assertIn("session_timeline:", result.stdout)
            self.assertIn("session_phases:", result.stdout)


if __name__ == "__main__":
    unittest.main()
