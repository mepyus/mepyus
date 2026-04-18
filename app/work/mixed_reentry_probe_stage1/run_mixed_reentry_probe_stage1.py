from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import json


REPO_ROOT = Path(__file__).resolve().parents[3]
CLOSE_ROOT = REPO_ROOT / "app" / "work" / "archive_review" / "transition_support" / "transition_mixed_close_reading" / "generated"
SURFACE_ROOT = REPO_ROOT / "app" / "work" / "archive_review" / "transition_support" / "transition_mixed_surface_refine" / "generated"
OUTPUT_ROOT = REPO_ROOT / "app" / "work" / "mixed_reentry_probe_stage1" / "generated"


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def summarize_bridge(bridges: list[dict[str, object]]) -> str:
    roles = [str(row.get("bridge_role", "")).strip() for row in bridges]
    counts = Counter(roles)
    return ", ".join(f"{k}:{v}" for k, v in counts.items())


def candidate_id(round_id: str, unit_id: str) -> str:
    return f"{round_id}::{unit_id}"


def build_candidates(index_rows: list[dict[str, object]], detail_rows: list[dict[str, object]], bridge_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    detail_map = {(row["round_id"], row["unit_id"]): row for row in detail_rows}
    bridge_map: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in bridge_rows:
        bridge_map[(row["round_id"], row["unit_id"])].append(row)
    out = []
    for row in index_rows:
        key = (row["round_id"], row["unit_id"])
        detail = detail_map[key]
        if not detail.get("good_mixed", False):
            continue
        out.append(
            {
                "candidate_id": candidate_id(row["round_id"], row["unit_id"]),
                "round_id": row["round_id"],
                "unit_id": row["unit_id"],
                "transition_from": detail["transition_from"],
                "transition_to": detail["transition_to"],
                "anchor_group": detail["dominant_anchor_group"],
                "bridge_summary": summarize_bridge(bridge_map[key]),
                "closure_gap": detail["closure_gap_point"],
                "mixed_quality": "good_hold",
                "readable_excerpt": row["readable_excerpt"],
            }
        )
    return out


def evaluate_match(src: dict[str, object], dst: dict[str, object]) -> dict[str, object] | None:
    if src["round_id"] == dst["round_id"]:
        return None
    anchor_overlap = src["anchor_group"] == dst["anchor_group"]
    transition_overlap = src["transition_from"] == dst["transition_from"]
    arrival_axis_overlap = src["transition_to"] == dst["transition_to"]
    bridge_support_found = "transition_bridge" in str(dst["bridge_summary"])
    if anchor_overlap and transition_overlap and arrival_axis_overlap and bridge_support_found:
        strength = "strong"
        match_type = ["anchor_reentry", "bridge_reentry", "arrival_axis_reentry", "closure_support_reentry"]
        closure_delta = "closure_partially_strengthened"
        note = "same corridor returns in the later transcript and reinforces the same arrival axis."
    elif transition_overlap and arrival_axis_overlap and bridge_support_found:
        strength = "meaningful"
        match_type = ["bridge_reentry", "arrival_axis_reentry"]
        closure_delta = "arrival_axis_clearer"
        note = "same transition corridor returns and keeps the destination axis alive, even if anchor labels differ."
    elif anchor_overlap and transition_overlap:
        strength = "weak"
        match_type = ["anchor_reentry"]
        closure_delta = "anchor_only_reinforced"
        note = "same anchor and transition family reappear, but the destination support is not as explicit."
    else:
        return None
    return {
        "candidate_id": src["candidate_id"],
        "matched_round_id": dst["round_id"],
        "matched_unit_id": dst["unit_id"],
        "match_type": match_type,
        "anchor_overlap": "same_anchor" if anchor_overlap else "different_anchor_family",
        "transition_overlap": "same_transition" if transition_overlap else "different_transition",
        "arrival_axis_overlap": "same_arrival_axis" if arrival_axis_overlap else "different_arrival_axis",
        "bridge_support_found": bridge_support_found,
        "reentry_strength": strength,
        "closure_delta": closure_delta,
        "note": note,
    }


def choose_best_matches(candidates: list[dict[str, object]]) -> list[dict[str, object]]:
    by_candidate: dict[str, list[dict[str, object]]] = defaultdict(list)
    for src in candidates:
        for dst in candidates:
            match = evaluate_match(src, dst)
            if match:
                by_candidate[src["candidate_id"]].append(match)
    rank = {"none": 0, "weak": 1, "meaningful": 2, "strong": 3}
    best = []
    for cid, rows in by_candidate.items():
        rows = sorted(rows, key=lambda r: (rank[r["reentry_strength"]], r["matched_round_id"], r["matched_unit_id"]), reverse=True)
        best.append(rows[0])
    return sorted(best, key=lambda r: r["candidate_id"])


def build_strength_delta(candidates: list[dict[str, object]], matches: list[dict[str, object]]) -> list[dict[str, object]]:
    candidate_map = {row["candidate_id"]: row for row in candidates}
    out = []
    for row in matches:
        cand = candidate_map[row["candidate_id"]]
        after_state = "mixed / confirmed_hold / " + (
            "arrival_axis_clearer" if row["closure_delta"] == "arrival_axis_clearer" else
            "closure_support_reinforced" if row["closure_delta"] == "closure_partially_strengthened" else
            "anchor_reentry_only"
        )
        out.append(
            {
                "candidate_id": row["candidate_id"],
                "before_state": "mixed / confirmed_hold / closure_spread",
                "after_support_state": after_state,
                "closure_delta": row["closure_delta"],
                "why_still_hold_or_why_strengthened": (
                    "support is stronger, but closure still depends on a transition corridor rather than a stable closed path"
                    if row["closure_delta"] in {"arrival_axis_clearer", "closure_partially_strengthened"}
                    else "the corridor reappears, but support increase is not enough to move beyond hold"
                ),
                "retention_value_confirmed": "yes" if row["reentry_strength"] in {"meaningful", "strong"} else "partial",
            }
        )
    return out


def build_cards(candidates: list[dict[str, object]], matches: list[dict[str, object]], deltas: list[dict[str, object]]) -> str:
    match_map = {row["candidate_id"]: row for row in matches}
    delta_map = {row["candidate_id"]: row for row in deltas}
    lines = ["# mixed reentry readable cards", ""]
    for cand in candidates:
        match = match_map.get(cand["candidate_id"])
        delta = delta_map.get(cand["candidate_id"])
        if not match or not delta:
            continue
        lines.extend(
            [
                f"## {cand['candidate_id']}",
                f"- original_mixed: `{cand['transition_from']} -> {cand['transition_to']}` / `{cand['closure_gap']}`",
                f"- excerpt: {cand['readable_excerpt']}",
                f"- reentry_found_in: `{match['matched_round_id']} / {match['matched_unit_id']}`",
                f"- what_reappeared: anchor=`{match['anchor_overlap']}`, transition=`{match['transition_overlap']}`, arrival=`{match['arrival_axis_overlap']}`",
                f"- bridge_reentry: `{ 'yes' if match['bridge_support_found'] else 'no' }` / strength=`{match['reentry_strength']}`",
                f"- closure_delta: `{delta['closure_delta']}`",
                f"- why_still_hold_or_strengthened: {delta['why_still_hold_or_why_strengthened']}",
                f"- hold_value: `{delta['retention_value_confirmed']}`",
                "",
            ]
        )
    return "\n".join(lines) + "\n"


def build_compare_board(candidates: list[dict[str, object]], matches: list[dict[str, object]], deltas: list[dict[str, object]]) -> str:
    strength_counts = Counter(row["reentry_strength"] for row in matches)
    delta_counts = Counter(row["closure_delta"] for row in deltas)
    transition_counts = Counter(f"{row['transition_from']}->{row['transition_to']}" for row in candidates)
    lines = [
        "# mixed reentry compare board",
        "",
        "## 1. 어떤 mixed들이 재진입 신호를 받았는가",
        f"- total candidates: `{len(candidates)}`",
        f"- matched candidates: `{len(matches)}`",
        f"- strength counts: `{dict(strength_counts)}`",
        "",
        "## 2. 어떤 transition corridor가 반복적으로 다시 붙는가",
    ]
    for key, count in transition_counts.items():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(
        [
            "",
            "## 3. 어떤 mixed는 재등장해도 거의 강화되지 않는가",
            "- `weak` reentry는 anchor family는 비슷하지만 arrival axis 보강이 부족한 경우다.",
            "",
            "## 4. good_hold의 실제 증거",
            "- reentry strength가 `meaningful` 또는 `strong` 이면 hold 가치가 사후적으로 확인된 것으로 본다.",
            "",
            "## 5. 보류의 가치가 증명된 경우 / 아직 보류만 된 경우",
            f"- retention confirmed yes: `{sum(1 for row in deltas if row['retention_value_confirmed'] == 'yes')}`",
            f"- retention confirmed partial: `{sum(1 for row in deltas if row['retention_value_confirmed'] == 'partial')}`",
            "",
            "## 6. canonical 승격 후보가 있는가",
            "- 이번 stage1에서는 `stable_closure_reached` 는 없음",
            "- 일부 corridor는 `closure_partially_strengthened` 까지는 갔지만 여전히 hold가 맞다",
            "",
            "## 7. 아직 승격하면 안 되는 이유",
            "- re-entry는 보였지만 stable closure reached 증거는 없다",
            "- 강화와 승격을 구분해야 한다",
        ]
    )
    return "\n".join(lines) + "\n"


def build_decision_note(matches: list[dict[str, object]], deltas: list[dict[str, object]]) -> str:
    strongish = [row for row in matches if row["reentry_strength"] in {"meaningful", "strong"}]
    lines = [
        "# mixed reentry decision note",
        "",
        "## A. hold는 생산적인가",
        "- 예. round 간 재등장으로 같은 corridor가 다시 붙는 경우가 반복적으로 보인다.",
        "",
        "## B. 어떤 mixed가 가장 재진입 가치가 큰가",
    ]
    for row in strongish[:3]:
        lines.append(f"- `{row['candidate_id']}` -> `{row['matched_round_id']}::{row['matched_unit_id']}` / `{row['reentry_strength']}`")
    lines.extend(
        [
            "",
            "## C. 지금 단계에서 승격 규칙을 만들면 안 되는 이유",
            "- re-entry는 support 강화이지 stable closure reached가 아니다",
            "- 지금은 hold 가치 확인 단계이지 승격 규칙 제정 단계가 아니다",
            "",
            "## D. 다음 턴이 observer 확장인지, 더 많은 input 검증인지",
            "- 다음은 더 많은 input 검증 쪽이 먼저다. 같은 corridor가 세 번째 입력에서도 다시 붙는지 봐야 한다.",
        ]
    )
    return "\n".join(lines) + "\n"


def build_boundary_contract() -> str:
    lines = [
        "# mixed reentry boundary contract",
        "",
        "## 1. 현단계에서 확정한 것",
        "- mixed hold corridor는 후속 transcript에서 다시 붙을 수 있다",
        "- hold는 단순 정지가 아니라 재진입 가능성이 있는 보류다",
        "",
        "## 2. 아직 확정하지 않은 것",
        "- re-entry가 곧 canonical 승격으로 이어지는지",
        "- 어떤 strength에서 승격 규칙을 만들 수 있는지",
        "",
        "## 3. observer/meaning layer에서만 다룰 것",
        "- re-entry strength 표시",
        "- closure delta 설명",
        "- retention value wording",
        "",
        "## 4. 코어 수정 금지 항목",
        "- mixed/canonical 판정 규칙 변경",
        "- hold trigger 변경",
        "- bridge admission 변경",
        "",
        "## 5. 다음 턴 진입 조건",
        "- 세 번째 입력에서도 같은 corridor의 re-entry가 반복되는지 볼 것",
        "- stable_closure_reached 사례가 실제로 나오는지 별도 확인할 것",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    index_rows = load_json(CLOSE_ROOT / "mixed_unit_index.json")
    detail_rows = load_json(CLOSE_ROOT / "mixed_transition_detail_packets.json")
    bridge_rows = load_json(CLOSE_ROOT / "mixed_transition_bridge_map.json")

    candidates = build_candidates(index_rows, detail_rows, bridge_rows)
    matches = choose_best_matches(candidates)
    deltas = build_strength_delta(candidates, matches)

    (OUTPUT_ROOT / "mixed_reentry_candidate_index.json").write_text(json.dumps(candidates, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUTPUT_ROOT / "mixed_reentry_match_report.json").write_text(json.dumps(matches, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUTPUT_ROOT / "mixed_reentry_strength_delta.json").write_text(json.dumps(deltas, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUTPUT_ROOT / "mixed_reentry_readable_cards.md").write_text(build_cards(candidates, matches, deltas), encoding="utf-8")
    (OUTPUT_ROOT / "mixed_reentry_compare_board.md").write_text(build_compare_board(candidates, matches, deltas), encoding="utf-8")
    (OUTPUT_ROOT / "mixed_reentry_decision_note.md").write_text(build_decision_note(matches, deltas), encoding="utf-8")
    (OUTPUT_ROOT / "mixed_reentry_boundary_contract.md").write_text(build_boundary_contract(), encoding="utf-8")
    print(
        json.dumps(
            {
                "candidate_count": len(candidates),
                "match_count": len(matches),
                "delta_count": len(deltas),
                "generated_dir": str(OUTPUT_ROOT),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
