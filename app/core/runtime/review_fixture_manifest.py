from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List
import json


DEFAULT_MANIFEST_PATH = (
    Path(__file__).resolve().parents[2]
    / "work"
    / "processor_compare"
    / "reports"
    / "review_fixture_manifest_v0.json"
)


@dataclass(frozen=True)
class ReviewFixtureEntry:
    fixture_id: str
    fixture_kind: str
    left_local_space_id: str
    right_local_space_id: str
    expected_bridge_mode: str
    expected_review_state: str
    expected_lifecycle_temperature: str
    expected_lifecycle_stage: str
    allowed_drift: str
    mutable: bool
    description: str


def load_review_fixture_manifest(path: Path | None = None) -> Dict[str, object]:
    manifest_path = path or DEFAULT_MANIFEST_PATH
    with manifest_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_review_fixture_entries(path: Path | None = None) -> List[ReviewFixtureEntry]:
    manifest = load_review_fixture_manifest(path)
    rows: List[ReviewFixtureEntry] = []
    for item in list(manifest.get("fixtures", []) or []):
        rows.append(
            ReviewFixtureEntry(
                fixture_id=str(item.get("fixture_id", "")).strip(),
                fixture_kind=str(item.get("fixture_kind", "")).strip(),
                left_local_space_id=str(item.get("left_local_space_id", "")).strip(),
                right_local_space_id=str(item.get("right_local_space_id", "")).strip(),
                expected_bridge_mode=str(item.get("expected_bridge_mode", "")).strip(),
                expected_review_state=str(item.get("expected_review_state", "")).strip(),
                expected_lifecycle_temperature=str(item.get("expected_lifecycle_temperature", "")).strip(),
                expected_lifecycle_stage=str(item.get("expected_lifecycle_stage", "")).strip(),
                allowed_drift=str(item.get("allowed_drift", "")).strip(),
                mutable=bool(item.get("mutable")),
                description=str(item.get("description", "")).strip(),
            )
        )
    return rows


def split_fixture_entries(
    path: Path | None = None,
) -> Dict[str, List[ReviewFixtureEntry]]:
    entries = load_review_fixture_entries(path)
    return {
        "immutable_regression_fixture": [entry for entry in entries if not entry.mutable],
        "mutable_exploration_control": [entry for entry in entries if entry.mutable],
    }
