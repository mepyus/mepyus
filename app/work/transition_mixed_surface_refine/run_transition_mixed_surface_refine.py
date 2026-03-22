from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import json


REPO_ROOT = Path(__file__).resolve().parents[3]
INPUT_ROOT = REPO_ROOT / "app" / "work" / "transition_mixed_close_reading" / "generated"
OUTPUT_ROOT = REPO_ROOT / "app" / "work" / "transition_mixed_surface_refine" / "generated"


def load_json(name: str) -> object:
    return json.loads((INPUT_ROOT / name).read_text(encoding="utf-8"))


def bridge_role_label(role: str) -> str:
    if role == "technical_anchor":
        return "기술 축을 붙잡는 시작점"
    if role == "transition_bridge":
        return "기술 축을 사업/조직 축으로 넘기는 문장"
    if role == "business_anchor":
        return "사업 축에 닿는 도착점"
    if role == "org_anchor":
        return "조직/운영 축에 닿는 도착점"
    return "약한 연결 흔적"


def build_cards_v2(index_rows: list[dict[str, object]], detail_rows: list[dict[str, object]], bridge_rows: list[dict[str, object]], gap_rows: list[dict[str, object]]) -> str:
    detail_map = {(row["round_id"], row["unit_id"]): row for row in detail_rows}
    bridge_map: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    gap_map: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in bridge_rows:
        bridge_map[(row["round_id"], row["unit_id"])].append(row)
    for row in gap_rows:
        gap_map[(next((d["round_id"] for d in detail_rows if d["unit_id"] == row["unit_id"]), "round1"), row["unit_id"])].append(row)

    lines = ["# transition mixed surface cards v2", ""]
    for row in index_rows:
        key = (row["round_id"], row["unit_id"])
        detail = detail_map[key]
        bridges = bridge_map[key]
        quality = "good_hold" if detail.get("good_mixed") else "unclear_hold"
        closure_bits = []
        for gap in gap_map[key]:
            if gap["gap_type"] in {"join_gap", "closure_spread"}:
                closure_bits.append(gap["gap_type"])
        closure_bits = sorted(set(closure_bits))
        lines.extend(
            [
                f"## {row['round_id']} / {row['unit_id']}",
                f"- transition_from: `{detail['transition_from']}`",
                f"- transition_to: `{detail['transition_to']}`",
                f"- hold_reason: `anchor_alive + bridge_alive + closure_spread`",
                f"- reading_status: `mixed / confirmed_hold`",
                f"- mixed_quality: `{quality}`",
                f"- excerpt: {row['readable_excerpt']}",
                f"- survived_anchor: `{detail['dominant_anchor_group']}` / repeated support `{detail['repeated_anchor_support']}`",
                "",
                "### bridge fragments",
            ]
        )
        for bridge in bridges:
            lines.append(
                f"- `{bridge['fragment_id']}` `{bridge['bridge_role']}`: {bridge_role_label(bridge['bridge_role'])} / {bridge['note']}"
            )
        lines.extend(
            [
                "",
                f"- closure_gap: `{ ' + '.join(closure_bits) if closure_bits else 'join_gap' }`",
                f"- why_not_canonical: repeated anchor는 충분하나 transition corridor가 stable local closure까지 응축되지 않음",
                f"- why_hold_is_valid: {detail['why_not_unreadable']}",
                f"- reread_point: 원문에서 bridge fragment 순서가 실제로 technical -> transition -> {detail['transition_to']} 로 읽히는지 확인",
                "",
            ]
        )
    return "\n".join(lines) + "\n"


def build_compare_board_v2(detail_rows: list[dict[str, object]], bridge_rows: list[dict[str, object]], gap_rows: list[dict[str, object]]) -> str:
    transition_counter = Counter(f"{row['transition_from']}->{row['transition_to']}" for row in detail_rows)
    bridge_counter = Counter(row["bridge_role"] for row in bridge_rows)
    gap_counter = Counter(row["gap_type"] for row in gap_rows)
    lines = [
        "# transition mixed compare board v2",
        "",
        "## 1. 반복된 transition pattern",
    ]
    for key, count in transition_counter.items():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(
        [
            "",
            "## 2. round1 / round2 공통 mixed 구조",
            "- repeated anchor는 충분하다",
            "- bridge fragment도 보인다",
            "- 하지만 closure는 transition-led라 spread된 상태로 남는다",
            "",
            "## 3. strongest surviving bridge 유형",
            f"- `{bridge_counter}`",
            "",
            "## 4. 반복 closure weakness 유형",
            f"- `{gap_counter}`",
            "",
            "## 5. canonical과 mixed의 경계 차이",
            "- canonical은 straight flow가 길고 bridge가 closure까지 닫힌다",
            "- mixed는 bridge가 있으나 closure가 hold 상태로 남는다",
            "",
            "## 6. 지금 손대도 되는 설명면 강화 항목",
            "- hold_reason을 카드 최상단에 고정",
            "- bridge fragment를 역할별로 바로 보이게 표기",
            "- closure_gap을 한 줄로 요약",
            "",
            "## 7. 아직 코어로 올리면 안 되는 항목",
            "- source_local_ref/translated handle 세분 원인을 mixed transcript 전체 규칙으로 일반화하는 것",
            "- mixed를 곧바로 재분류 규칙으로 바꾸는 것",
        ]
    )
    return "\n".join(lines) + "\n"


def build_legend() -> str:
    lines = [
        "# transition mixed reading legend",
        "",
        "- `transition_from`: 이 mixed가 출발한 축. 보통 `technical`, `tool`, `product` 중 하나로 읽는다.",
        "- `transition_to`: 이 mixed가 도달하려던 축. 보통 `business`, `organization`, `startup_thesis` 중 하나다.",
        "- `anchor_alive`: 반복 앵커가 살아 있어서 unreadable로 버리면 손실이 큰 상태다.",
        "- `bridge_alive`: 전환을 이어주는 fragment가 실제로 보이는 상태다.",
        "- `closure_spread`: 전환은 존재하지만 stable local closure로 응축되지 못한 상태다.",
        "- `join_gap`: join closure가 gap_dominant로 남은 상태다.",
        "- `good_hold`: hold 가치가 분명한 mixed다. anchor와 bridge가 살아 있다.",
        "- `why_not_canonical`: 왜 stable_reading으로 바로 닫히지 않았는지 읽는 문장이다.",
    ]
    return "\n".join(lines) + "\n"


def build_operator_summary(detail_rows: list[dict[str, object]], gap_rows: list[dict[str, object]]) -> str:
    transition_counter = Counter(f"{row['transition_from']}->{row['transition_to']}" for row in detail_rows)
    good_hold_count = sum(1 for row in detail_rows if row.get("good_mixed"))
    lines = [
        "# transition mixed operator summary",
        "",
        "## A. 전체 진단",
        "- 지금 mixed의 핵심은 anchor 부족이 아니라 `transition-led closure weakness` 입니다.",
        "",
        "## B. 가장 자주 반복된 전환",
    ]
    for key, count in transition_counter.items():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(
        [
            "",
            "## C. mixed가 되는 직접 이유",
            "- anchor는 살아 있음",
            "- bridge도 있음",
            "- stable closure가 spread됨",
            "",
            "## D. 지금 먼저 개선할 surface",
            "- hold 이유 표기",
            "- bridge fragment 표기",
            "- closure gap 한 줄 요약",
            "",
            "## E. 아직 코어 수정으로 가면 안 되는 이유",
            "- 반복 mixed는 보이지만 source 규칙 붕괴로 단정할 수준은 아님",
            "- 현재 부족한 것은 판독 실패보다 readable surface 해상도임",
            "",
            "## F. 한 줄 결론",
            f"- readable surface 강화가 지금 우선순위이며, 현재 mixed `{good_hold_count}`개는 대부분 `good_hold`로 읽힌다.",
        ]
    )
    return "\n".join(lines) + "\n"


def build_fix_boundary_v2() -> str:
    lines = [
        "# transition mixed fix boundary note v2",
        "",
        "## 1. 지금 바로 반영할 표현면 개선",
        "- 카드 최상단에 transition_from / transition_to / hold_reason / reading_status 고정",
        "- bridge fragments 역할별 표기",
        "- closure_gap 한 줄 요약",
        "",
        "## 2. 다음 관찰 후 판단할 것",
        "- good_hold와 unclear_hold가 실제로 갈라지는지",
        "- transition_to를 더 세분화할 필요가 있는지",
        "",
        "## 3. 코어 수정 금지 영역",
        "- mixed 판정 규칙 변경",
        "- source_local_ref / translated_handles 생성 규칙 변경",
        "- bridge admission 로직 변경",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    index_rows = load_json("mixed_unit_index.json")
    detail_rows = load_json("mixed_transition_detail_packets.json")
    bridge_rows = load_json("mixed_transition_bridge_map.json")
    gap_rows = load_json("mixed_transition_gap_ledger.json")

    (OUTPUT_ROOT / "transition_mixed_surface_cards_v2.md").write_text(
        build_cards_v2(index_rows, detail_rows, bridge_rows, gap_rows),
        encoding="utf-8",
    )
    (OUTPUT_ROOT / "transition_mixed_compare_board_v2.md").write_text(
        build_compare_board_v2(detail_rows, bridge_rows, gap_rows),
        encoding="utf-8",
    )
    (OUTPUT_ROOT / "transition_mixed_reading_legend.md").write_text(
        build_legend(),
        encoding="utf-8",
    )
    (OUTPUT_ROOT / "transition_mixed_operator_summary.md").write_text(
        build_operator_summary(detail_rows, gap_rows),
        encoding="utf-8",
    )
    (OUTPUT_ROOT / "transition_mixed_fix_boundary_note_v2.md").write_text(
        build_fix_boundary_v2(),
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "surface_card_units": len(index_rows),
                "generated_dir": str(OUTPUT_ROOT),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
