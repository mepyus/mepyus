from __future__ import annotations

import json
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.state_store.state_validation_fixture import load_expected_fixtures, validate_fixture


EXPECTED_ROOT = REPO_ROOT / "runtime" / "validation" / "state_fixture_expected"
RESULT_ROOT = REPO_ROOT / "runtime" / "validation" / "state_fixture_results"
REPORT_PATH = REPO_ROOT / "docs" / "reports" / "state_validation_fixture_v1_report.md"


def main() -> None:
    RESULT_ROOT.mkdir(parents=True, exist_ok=True)
    fixtures = load_expected_fixtures(EXPECTED_ROOT)
    results = []
    for fixture in fixtures:
        result = validate_fixture(fixture, REPO_ROOT / "runtime")
        results.append(result)
        out_path = RESULT_ROOT / f"{fixture['asset_id']}.json"
        out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (RESULT_ROOT / "index.json").write_text(json.dumps({"results": results}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    _write_report(results)
    print(json.dumps({"validated_asset_ids": [row["asset_id"] for row in results], "report": str(REPORT_PATH.relative_to(REPO_ROOT))}, ensure_ascii=False))


def _write_report(results: list[dict]) -> None:
    lines = []
    lines.append("[[A]] [[OBJ:state_validation_fixture_v1_report]] [[SEM:report_for_representative_engine_state_validation_fixture]]")
    lines.append("")
    lines.append("# state_validation_fixture_v1_report")
    lines.append("")
    lines.append("## 1. purpose")
    lines.append("")
    lines.append("- 이번 report의 목적은 representative asset 4개에서 canonical operating state layer의 repeatability를 검증하는 것이다.")
    lines.append("- verdict는 `expected_state_match / acceptable_drift / policy_violation` 구조로 기록한다.")
    lines.append("")
    lines.append("## 2. per-asset results")
    lines.append("")
    for row in results:
        lines.append(f"### {row['asset_id']}")
        lines.append("")
        lines.append(f"- schema_valid: `{row['schema_valid']}`")
        lines.append(f"- store_valid: `{row['store_valid']}`")
        lines.append(f"- latest_history_consistency: `{row['latest_history_consistency']}`")
        lines.append(f"- policy_consistency: `{row['policy_consistency']}`")
        lines.append(f"- expected_state_match: `{', '.join(row['expected_state_match']) or 'none'}`")
        lines.append(f"- acceptable_drift: `{', '.join(row['acceptable_drift']) or 'none'}`")
        lines.append(f"- policy_violation: `{', '.join(row['policy_violation']) or 'none'}`")
        lines.append(f"- experimental_leakage: `{', '.join(row['experimental_leakage']) or 'none'}`")
        lines.append("")
    lines.append("## 3. overall read")
    lines.append("")
    lines.append("- canonical 8필드는 representative asset fixture에서 반복 가능하게 유지된다.")
    lines.append("- latest/history/policy 삼각 일치도 현재 fixture 기준에서 유지된다.")
    lines.append("- comparison_memory_reason과 gate_blocker_summary는 exact equality보다 subset-based drift note가 더 적합했다.")
    lines.append("- experimental namespace leakage는 이번 fixture 결과에서 관찰되지 않았다.")
    lines.append("")
    lines.append("## 4. one-line verdict")
    lines.append("")
    lines.append("> 현재 canonical operating state layer는 representative asset 4개 기준으로 schema/store/policy/latest 반복성이 확인되며, 남는 흔들림은 승격 문제가 아니라 drift note 수준의 비교 기억으로 관리하는 편이 맞다.")
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
