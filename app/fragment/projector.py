from __future__ import annotations

from pathlib import Path
from typing import Dict, Optional

from app.core.formation_service import FormationService
from app.fragment.schema import FragmentRecord


SOURCE_ROLE_MAP = {
    "memo": "memo_material",
    "paper": "paper_material",
    "review": "review_material",
    "conversation": "review_material",
    "dialogue": "review_material",
    "code": "code_material",
    "log": "log_material",
    "bullet": "bullet_material",
}


def project_fragment_to_material(
    runtime_root: Path,
    fragment: FragmentRecord,
    *,
    actor_id: str = "replica_user",
    session_id: str = "replica_session",
    project_id: str = "vectorfl-replica",
    family_id: Optional[str] = None,
) -> Dict[str, object]:
    service = FormationService(runtime_root)
    material = service.ingest_material_with_role(
        raw_payload=fragment.raw_text,
        actor_id=actor_id,
        session_id=session_id,
        project_id=project_id,
        source_type=fragment.source_type,
        source_ref=fragment.source_path,
        formation_role=SOURCE_ROLE_MAP.get(fragment.source_type, "memo_material"),
        family_id=family_id,
        lineage_refs=(),
    )

    persisted = service.materials.get(material.material_id) or {}
    metadata = dict(persisted.get("metadata", {}))
    fragment_record = fragment.to_record()
    metadata.update(
        {
            "fragment_id": fragment.fragment_id,
            "source_id": fragment.source_id,
            "source_range": fragment_record["source_range"],
            "page_ref": fragment_record["page_ref"],
            "paragraph_index": fragment.paragraph_index,
            "unit_scale": fragment.unit_scale,
            "anchor": fragment_record["anchor"],
            "anchors": fragment_record["anchors"],
            "D": fragment.D,
            "I": fragment.I,
            "S": fragment.S,
            "scene": fragment.scene,
            "flow": fragment.flow,
            "time_in": fragment.time,
            "confidence": fragment.confidence,
            "provenance_log": fragment_record["provenance_log"],
            "fragment_metadata": fragment.metadata,
        }
    )
    metadata["projected_material_id"] = material.material_id
    persisted["metadata"] = metadata
    service.materials.put(material.material_id, persisted)
    return persisted
