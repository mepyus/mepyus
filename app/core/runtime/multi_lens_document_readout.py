from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal


ReadingStrength = Literal["strong", "weak", "caution", "absent"]
LineOperatingState = Literal["active", "parked", "candidate"]


@dataclass(frozen=True)
class SurfacedLineReadout:
    linked_segment_id: str
    source_id: str
    line_id: str
    line_name: str
    reading_strength: ReadingStrength
    reading_basis: str
    caution_reason: str | None
    operating_state: LineOperatingState
    is_primary_lens: bool
    provenance: Any


@dataclass(frozen=True)
class SurfacedDocumentReadout:
    source_id: str
    lens_ids_used: list[str]
    is_stable_lens_only: bool
    line_states: dict[str, LineOperatingState]
    readings: list[SurfacedLineReadout]


class MultiLensReadoutFormatter:
    """Surface adapter only; it must not perform operating decisions."""

    def __init__(self, line_definitions_by_id: dict[str, Any]) -> None:
        self.line_definitions_by_id = line_definitions_by_id

    def format(self, result: Any) -> SurfacedDocumentReadout:
        readings = [
            self._format_reading(reading)
            for reading in result.readings
        ]
        line_states = {
            line_id: self.line_definitions_by_id[line_id].operating_state
            for line_id in result.lens_ids_used
            if line_id in self.line_definitions_by_id
        }
        return SurfacedDocumentReadout(
            source_id=result.source_id,
            lens_ids_used=result.lens_ids_used,
            is_stable_lens_only=result.is_stable_lens_only,
            line_states=line_states,
            readings=readings,
        )

    def _format_reading(self, reading: Any) -> SurfacedLineReadout:
        line = self.line_definitions_by_id[reading.line_id]
        return SurfacedLineReadout(
            linked_segment_id=reading.linked_segment_id,
            source_id=reading.source_id,
            line_id=reading.line_id,
            line_name=reading.line_name,
            reading_strength=reading.reading_strength,
            reading_basis=reading.reading_basis,
            caution_reason=reading.caution_reason,
            operating_state=line.operating_state,
            is_primary_lens=line.is_primary,
            provenance=reading.provenance,
        )


def surface_readout(result: Any, line_definitions_by_id: dict[str, Any]) -> SurfacedDocumentReadout:
    formatter = MultiLensReadoutFormatter(line_definitions_by_id)
    return formatter.format(result)
