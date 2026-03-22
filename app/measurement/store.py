from __future__ import annotations

from pathlib import Path
from typing import List, Optional

from app.core.runtime.file_store import JsonDirectoryStore
from app.measurement.schema import MeasurementRecord


class MeasurementStore:
    def __init__(self, runtime_root: Path) -> None:
        self.runtime_root = runtime_root
        self.store = JsonDirectoryStore(runtime_root / "measurements")

    def put(self, measurement: MeasurementRecord) -> Path:
        return self.store.put(measurement.measurement_id, measurement.to_record())

    def get(self, measurement_id: str) -> Optional[MeasurementRecord]:
        record = self.store.get(measurement_id)
        if record is None:
            return None
        return MeasurementRecord(**record)

    def read_all(self) -> List[MeasurementRecord]:
        return [MeasurementRecord(**record) for record in self.store.read_all()]
