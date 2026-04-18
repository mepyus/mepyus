from __future__ import annotations

from pathlib import Path
import json
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.work.operating_ui.operating_ui_payload_adapter import (
    adapt_process_console_payload_to_operating_ui_model,
)


FIXTURE_ROOT = Path(__file__).resolve().parent / "fixtures"
CASES = ["a", "b", "c", "d"]


def main() -> int:
    results = []
    for case in CASES:
        raw = _load_json(FIXTURE_ROOT / f"process_console_payload_case_{case}.json")
        expected = _load_json(FIXTURE_ROOT / f"operating_ui_model_case_{case}.json")
        actual = adapt_process_console_payload_to_operating_ui_model(raw)
        errors: list[str] = []
        _assert_subset(expected, actual, path="$", errors=errors)
        results.append(
            {
                "case": case.upper(),
                "ok": not errors,
                "errors": errors,
            }
        )

    print(json.dumps({"results": results}, ensure_ascii=False, indent=2))
    return 0 if all(item["ok"] for item in results) else 1


def _load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _assert_subset(expected, actual, *, path: str, errors: list[str]) -> None:
    if isinstance(expected, dict):
        if not isinstance(actual, dict):
            errors.append(f"{path}: expected object, got {type(actual).__name__}")
            return
        for key, expected_value in expected.items():
            if key not in actual:
                errors.append(f"{path}.{key}: missing key")
                continue
            _assert_subset(expected_value, actual[key], path=f"{path}.{key}", errors=errors)
        return

    if isinstance(expected, list):
        if not isinstance(actual, list):
            errors.append(f"{path}: expected list, got {type(actual).__name__}")
            return
        if len(actual) < len(expected):
            errors.append(f"{path}: expected at least {len(expected)} items, got {len(actual)}")
            return
        for index, expected_item in enumerate(expected):
            _assert_subset(expected_item, actual[index], path=f"{path}[{index}]", errors=errors)
        return

    if expected != actual:
        errors.append(f"{path}: expected {expected!r}, got {actual!r}")


if __name__ == "__main__":
    sys.exit(main())
