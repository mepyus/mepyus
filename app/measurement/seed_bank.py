from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass(frozen=True)
class AnchorSeed:
    seed_id: str
    handle: str
    family: str
    layer: str
    stage: str
    source_kind: str
    source_ref: str
    label: str
    aliases: List[str]
    description: str
    evidence_patterns: List[str]
    confidence_hint: float
    first_seen_at: str
    last_seen_at: str
    occurrence_count: int
    promotion_score: float
    status: str
    notes: str


def load_anchor_seed_bank(runtime_root: Path) -> List[AnchorSeed]:
    path = runtime_root / "config" / "anchor_seed_bank.jsonl"
    if not path.exists():
        return []
    seeds: List[AnchorSeed] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        row = json.loads(line)
        seeds.append(
            AnchorSeed(
                seed_id=row["seed_id"],
                handle=row["handle"],
                family=row.get("family", ""),
                layer=row.get("layer", ""),
                stage=row.get("stage", "shadow"),
                source_kind=row.get("source_kind", ""),
                source_ref=row.get("source_ref", ""),
                label=row.get("label", row["handle"]),
                aliases=list(row.get("aliases", [])),
                description=row.get("description", ""),
                evidence_patterns=list(row.get("evidence_patterns", [])),
                confidence_hint=float(row.get("confidence_hint", 0.0)),
                first_seen_at=row.get("first_seen_at", ""),
                last_seen_at=row.get("last_seen_at", ""),
                occurrence_count=int(row.get("occurrence_count", 0)),
                promotion_score=float(row.get("promotion_score", 0.0)),
                status=row.get("status", "active"),
                notes=row.get("notes", ""),
            )
        )
    return seeds
