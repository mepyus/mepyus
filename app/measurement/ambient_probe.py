from __future__ import annotations

import hashlib
from typing import Dict, List

from app.fragment.schema import FragmentRecord
from app.measurement.schema import MeasurementRecord
from app.measurement.seed_bank import AnchorSeed


PROBE_VERSION = "v0.1"


def build_ambient_anchor_probe(
    fragment: FragmentRecord,
    *,
    seeds: List[AnchorSeed],
    ingest_batch_id: str,
    ingest_session_id: str,
    seed_bank_version: str,
    source_mode: str = "internal_seed_only",
) -> MeasurementRecord | None:
    candidates = []
    lowered_text = fragment.raw_text.lower()
    current_anchor_keys = [anchor.key for anchor in fragment.anchors]

    for seed in seeds:
        if seed.status != "active":
            continue
        matches = _match_seed(seed, lowered_text, current_anchor_keys)
        if not matches:
            continue
        strength = min(0.95, seed.confidence_hint * (0.45 + (0.12 * len(matches["matched_phrases"]))))
        candidates.append(
            {
                "handle": seed.handle,
                "seed_id": seed.seed_id,
                "seed_stage": seed.stage,
                "source_kind": seed.source_kind,
                "match_mode": matches["match_mode"],
                "strength": round(strength, 3),
                "evidence": {
                    "matched_phrases": matches["matched_phrases"],
                    "nearby_handles": matches["nearby_handles"],
                    "fragment_excerpt": " ".join(fragment.raw_text.split())[:180],
                },
                "co_signals": matches["nearby_handles"],
                "promotion_blocked": True,
                "remarks": "ambient only, no primary impact",
            }
        )

    if not candidates:
        return None

    candidates.sort(key=lambda row: (-float(row["strength"]), row["handle"]))
    top = candidates[0]
    measurement_id = _measurement_id(fragment.fragment_id, ingest_batch_id, top["handle"])
    return MeasurementRecord(
        measurement_id=measurement_id,
        fragment_id=fragment.fragment_id,
        measurement_type="ambient_anchor_probe",
        column_key="ambient_anchor_probe",
        value={
            "probe_version": PROBE_VERSION,
            "seed_bank_version": seed_bank_version,
            "source_mode": source_mode,
            "candidates": candidates,
            "summary": {
                "candidate_count": len(candidates),
                "top_handle": top["handle"],
                "top_strength": top["strength"],
                "primary_anchor_changed": False,
            },
            "revision_of": None,
        },
        basis="seed-bank ambient probe",
        evidence_text=top["evidence"]["fragment_excerpt"],
        confidence=float(top["strength"]),
        origin="seed_bank_probe",
        status="active",
        provisional=True,
        related_source_path=fragment.source_path,
        related_material_id=fragment.metadata.get("projected_material_id", ""),
        metadata={
            "probe_version": PROBE_VERSION,
            "seed_bank_version": seed_bank_version,
            "ingest_batch_id": ingest_batch_id,
            "ingest_session_id": ingest_session_id,
            "source_mode": source_mode,
            "candidate_count": len(candidates),
        },
    )


def _match_seed(seed: AnchorSeed, lowered_text: str, current_anchor_keys: List[str]) -> Dict[str, object] | None:
    matched_phrases = []
    for pattern in seed.evidence_patterns:
        if pattern and pattern.lower() in lowered_text:
            matched_phrases.append(pattern)
    nearby_handles = [key for key in current_anchor_keys if seed.family and key.startswith(seed.family)]
    if matched_phrases:
        match_mode = "exact_phrase"
    elif nearby_handles:
        match_mode = "family_match"
    else:
        aliases = [alias for alias in seed.aliases if alias.lower() in lowered_text]
        if aliases:
            matched_phrases.extend(aliases[:2])
            match_mode = "alias_match"
        else:
            return None
    return {
        "matched_phrases": matched_phrases[:4],
        "nearby_handles": nearby_handles[:4],
        "match_mode": match_mode,
    }


def _measurement_id(fragment_id: str, ingest_batch_id: str, handle: str) -> str:
    digest = hashlib.sha1(f"{fragment_id}|ambient_anchor_probe|{ingest_batch_id}|{handle}".encode("utf-8")).hexdigest()
    return f"msr_{digest[:16]}"
