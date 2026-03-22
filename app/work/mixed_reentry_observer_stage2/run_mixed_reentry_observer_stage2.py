from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import json
import re


REPO_ROOT = Path(__file__).resolve().parents[3]
STAGE1_ROOT = REPO_ROOT / "app" / "work" / "mixed_reentry_probe_stage1" / "generated"
OUTPUT_ROOT = REPO_ROOT / "app" / "work" / "mixed_reentry_observer_stage2" / "generated"

OBSERVER_INPUTS = [
    {
        "input_id": "observer_exam",
        "path": REPO_ROOT / "references" / "vectorfl_next_gemini_session" / "youtube_exam.md",
        "kind": "paragraph",
        "window_size": 4,
        "overlap": 1,
    },
    {
        "input_id": "observer_session",
        "path": REPO_ROOT / "runtime" / "logs" / "work_sessions" / "session_20260318_180251.md",
        "kind": "section",
        "window_size": 5,
        "overlap": 2,
    },
]

ANCHOR_GROUPS = {
    "ai_business": [
        "ai",
        "비즈니스",
        "사업",
        "산업",
        "회사",
        "시장",
        "가치",
        "비용",
        "roi",
        "monetization",
        "platform shift",
        "future of work",
        "future_of_work",
        "playbook",
        "advantage",
    ],
    "harness_agent": [
        "openclaw",
        "하네스",
        "workflow",
        "워크플로우",
        "에이전트",
        "agent",
        "claude code",
        "codex",
        "backend.ai",
        "backend.ai:go",
        "router",
        "fragment",
        "source fragment",
        "source view",
        "observer layer",
    ],
    "model_compute": [
        "모델",
        "model",
        "tensorflow",
        "딥러닝",
        "머신러닝",
        "compute",
        "computation",
        "rlvr",
        "cua",
        "frontier",
        "gpu",
        "토큰",
        "token",
        "architecture",
        "moe",
        "dense",
        "deepseek",
        "alphago",
        "cnn",
        "mnist",
        "softmax",
    ],
    "organization_ax": [
        "조직",
        "업무",
        "인재",
        "talent",
        "효율",
        "efficiency",
        "entrepreneur",
        "startup",
        "스타트업",
        "복제",
        "적응",
        "observer",
        "deferred",
        "rejected",
        "promotion",
        "comparison",
    ],
    "security_isolation": ["보안", "prompt injection", "injection", "격리", "vm", "credential", "2fa", "dgx"],
}

TECH_GROUPS = {"harness_agent", "model_compute", "security_isolation"}
TRANSITION_MARKERS = [
    "그래서",
    "결국",
    "근데",
    "하지만",
    "그러면",
    "그러면서",
    "전환",
    "this makes",
    "the next useful step",
    "intended workflow",
]


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def corridor_id(transition_from: str, transition_to: str, anchor_group: str) -> str:
    return f"{transition_from}->{transition_to}::{anchor_group}"


def parse_units(path: Path, kind: str) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    units: list[dict[str, str]] = []
    if kind == "section" and "## " in text:
        current_title = ""
        current_lines: list[str] = []
        index = 0
        for line in text.splitlines():
            if line.startswith("## "):
                if current_title:
                    index += 1
                    units.append(
                        {
                            "unit_id": f"u{index:02d}",
                            "title": current_title,
                            "text": " ".join(current_lines).strip(),
                        }
                    )
                current_title = line[3:].strip()
                current_lines = []
            elif line.strip():
                current_lines.append(line.strip())
        if current_title:
            index += 1
            units.append(
                {
                    "unit_id": f"u{index:02d}",
                    "title": current_title,
                    "text": " ".join(current_lines).strip(),
                }
            )
    else:
        paragraphs = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]
        for index, paragraph in enumerate(paragraphs, start=1):
            units.append({"unit_id": f"u{index:02d}", "title": f"para{index:02d}", "text": paragraph})
    return units


def build_windows(input_id: str, units: list[dict[str, str]], window_size: int, overlap: int) -> list[dict[str, object]]:
    step = max(1, window_size - overlap)
    windows: list[dict[str, object]] = []
    for start in range(0, len(units), step):
        chunk = units[start : start + window_size]
        if not chunk:
            continue
        windows.append(
            {
                "input_id": input_id,
                "window_id": f"{input_id}::w{start // step + 1:02d}",
                "unit_ids": [row["unit_id"] for row in chunk],
                "titles": [row["title"] for row in chunk],
                "text": " ".join(f"{row['title']} {row['text']}" for row in chunk).strip(),
                "excerpt": " / ".join(f"[{row['title']}] {row['text'][:120]}" for row in chunk[:3]),
            }
        )
        if start + window_size >= len(units):
            break
    return windows


def anchor_counts(text: str) -> Counter[str]:
    lowered = text.lower()
    counts: Counter[str] = Counter()
    for group, aliases in ANCHOR_GROUPS.items():
        for alias in aliases:
            if alias.lower() in lowered:
                counts[group] += 1
    return counts


def build_bridge_fragments(window: dict[str, object], units_by_id: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for unit_id in list(window["unit_ids"]):
        unit = units_by_id[unit_id]
        text = f"{unit['title']} {unit['text']}"
        counts = anchor_counts(text)
        lowered = text.lower()
        tech_present = any(group in TECH_GROUPS for group in counts)
        org_present = counts["organization_ax"] > 0
        business_present = counts["ai_business"] > 0
        bridge_like = any(marker.lower() in lowered for marker in TRANSITION_MARKERS) or (tech_present and (org_present or business_present))
        if not bridge_like:
            continue
        if tech_present and business_present and counts["ai_business"] >= counts["organization_ax"]:
            role = "transition_bridge"
        elif tech_present and org_present:
            role = "transition_bridge"
        elif tech_present:
            role = "technical_anchor"
        elif business_present:
            role = "business_anchor"
        else:
            role = "org_anchor"
        rows.append({"unit_id": unit_id, "title": unit["title"], "bridge_role": role, "text_excerpt": unit["text"][:160]})
    return rows


def classify_window(window: dict[str, object], units_by_id: dict[str, dict[str, str]]) -> dict[str, object] | None:
    counts = anchor_counts(str(window["text"]))
    tech_present = any(group in TECH_GROUPS for group in counts)
    org_score = counts["organization_ax"]
    business_score = counts["ai_business"]
    if not tech_present or (org_score == 0 and business_score == 0):
        return None
    transition_to = "organization" if org_score >= business_score and org_score > 0 else "business"
    anchor_group = max(
        ["harness_agent", "ai_business", "model_compute"],
        key=lambda group: (counts[group], group == "harness_agent", group == "ai_business"),
    )
    if counts[anchor_group] == 0:
        return None
    bridge_fragments = build_bridge_fragments(window, units_by_id)
    repeated_anchor_support = sum(1 for value in counts.values() if value >= 2)
    bridge_support_found = bool(bridge_fragments) or repeated_anchor_support >= 2
    return {
        "input_id": window["input_id"],
        "window_id": window["window_id"],
        "transition_from": "technical",
        "transition_to": transition_to,
        "anchor_group": anchor_group,
        "repeated_anchor_support": repeated_anchor_support,
        "bridge_support_found": bridge_support_found,
        "bridge_fragments": bridge_fragments,
        "excerpt": window["excerpt"],
        "titles": list(window["titles"]),
    }


def build_stage1_corridors(candidates: list[dict[str, object]], matches: list[dict[str, object]]) -> tuple[list[dict[str, object]], dict[str, str]]:
    candidate_to_corridor: dict[str, str] = {}
    grouped: dict[str, dict[str, object]] = {}
    for row in candidates:
        cid = corridor_id(str(row["transition_from"]), str(row["transition_to"]), str(row["anchor_group"]))
        candidate_to_corridor[row["candidate_id"]] = cid
        grouped.setdefault(
            cid,
            {
                "corridor_id": cid,
                "origin_round": str(row["round_id"]),
                "transition_from": str(row["transition_from"]),
                "transition_to": str(row["transition_to"]),
                "anchor_group": str(row["anchor_group"]),
                "initial_hold_reason": str(row["closure_gap"]),
                "readable_excerpt": [str(row["readable_excerpt"])],
                "stage1_match_rows": [],
            },
        )
        grouped[cid]["readable_excerpt"].append(str(row["readable_excerpt"]))
        if grouped[cid]["origin_round"] != str(row["round_id"]):
            grouped[cid]["origin_round"] = "round1+round2"
    for row in matches:
        cid = candidate_to_corridor[row["candidate_id"]]
        grouped[cid]["stage1_match_rows"].append(row)
    out = []
    for row in grouped.values():
        row["readable_excerpt"] = row["readable_excerpt"][0]
        out.append(row)
    return sorted(out, key=lambda row: row["corridor_id"]), candidate_to_corridor


def evaluate_corridor_reentry(corridor: dict[str, object], observer_window: dict[str, object]) -> dict[str, object] | None:
    if str(corridor["transition_from"]) != str(observer_window["transition_from"]):
        return None
    arrival_same = str(corridor["transition_to"]) == str(observer_window["transition_to"])
    anchor_same = str(corridor["anchor_group"]) == str(observer_window["anchor_group"])
    bridge_support = bool(observer_window["bridge_support_found"])
    repeated = int(observer_window["repeated_anchor_support"])
    if arrival_same and anchor_same and bridge_support and repeated >= 2:
        strength = "strong"
        closure_delta = "closure_partially_strengthened"
    elif arrival_same and bridge_support and repeated >= 2:
        strength = "meaningful"
        closure_delta = "arrival_axis_clearer"
    elif arrival_same and bridge_support:
        strength = "weak"
        closure_delta = "anchor_only_reinforced"
    elif anchor_same:
        strength = "weak"
        closure_delta = "anchor_only_reinforced"
    else:
        return None
    match_type = []
    if anchor_same:
        match_type.append("anchor_reentry")
    if bridge_support:
        match_type.append("bridge_reentry")
    if arrival_same:
        match_type.append("arrival_axis_reentry")
    if closure_delta == "closure_partially_strengthened":
        match_type.append("closure_support_reentry")
    return {
        "corridor_id": corridor["corridor_id"],
        "matched_input_id": str(observer_window["window_id"]),
        "anchor_overlap": "same_anchor" if anchor_same else "different_anchor_family",
        "bridge_support": "yes" if bridge_support else "no",
        "arrival_axis_reinforcement": "same_arrival_axis" if arrival_same else "different_arrival_axis",
        "closure_delta": closure_delta,
        "reentry_strength": strength,
        "retention_value_confirmed": "yes" if strength in {"meaningful", "strong"} else "partial",
        "bridge_fragment_count": len(list(observer_window["bridge_fragments"])),
        "excerpt": str(observer_window["excerpt"]),
        "titles": list(observer_window["titles"]),
        "match_type": match_type,
    }


def choose_best_observer_matches(corridors: list[dict[str, object]], observer_windows: list[dict[str, object]]) -> list[dict[str, object]]:
    by_key: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for corridor in corridors:
        for window in observer_windows:
            match = evaluate_corridor_reentry(corridor, window)
            if match:
                by_key[(corridor["corridor_id"], window["window_id"].split("::", 1)[0])].append(match)
    rank = {"none": 0, "weak": 1, "meaningful": 2, "strong": 3}
    chosen: list[dict[str, object]] = []
    for _, rows in by_key.items():
        rows = sorted(
            rows,
            key=lambda row: (
                rank[str(row["reentry_strength"])],
                int(row["bridge_fragment_count"]),
                len(str(row["excerpt"])),
            ),
            reverse=True,
        )
        chosen.append(rows[0])
    return sorted(chosen, key=lambda row: (row["corridor_id"], row["matched_input_id"]))


def build_ledger(
    corridors: list[dict[str, object]],
    stage1_matches: list[dict[str, object]],
    observer_matches: list[dict[str, object]],
    candidate_to_corridor: dict[str, str],
) -> list[dict[str, object]]:
    stage1_by_corridor: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in stage1_matches:
        stage1_by_corridor[candidate_to_corridor[row["candidate_id"]]].append(row)
    observer_by_corridor: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in observer_matches:
        observer_by_corridor[row["corridor_id"]].append(row)
    rank = {"none": 0, "weak": 1, "meaningful": 2, "strong": 3}
    rows = []
    for corridor in corridors:
        cid = corridor["corridor_id"]
        s1 = stage1_by_corridor.get(cid, [])
        obs = observer_by_corridor.get(cid, [])
        strengths = [row["reentry_strength"] for row in s1] + [row["reentry_strength"] for row in obs]
        strongest = max(strengths, key=lambda item: rank[item]) if strengths else "none"
        if any(row["closure_delta"] == "closure_partially_strengthened" for row in obs):
            latest_closure_state = "closure_partially_strengthened"
        elif any(row["closure_delta"] == "arrival_axis_clearer" for row in obs):
            latest_closure_state = "arrival_axis_clearer"
        elif any(row["closure_delta"] == "anchor_only_reinforced" for row in obs):
            latest_closure_state = "anchor_only_reinforced"
        else:
            latest_closure_state = "no_change"
        matched_inputs = [f"{row['matched_round_id']}::{row['matched_unit_id']}" for row in s1] + [row["matched_input_id"] for row in obs]
        if obs and all(row["retention_value_confirmed"] == "yes" for row in obs):
            note = "observer-stage reentry keeps reinforcing this hold corridor, but still does not close it."
        elif obs:
            note = "observer-stage reentry exists, but reinforcement is uneven and still mostly explanatory."
        else:
            note = "so far this corridor is mostly backed by round1/round2 reentry only."
        rows.append(
            {
                "corridor_id": cid,
                "origin_round": corridor["origin_round"],
                "transition_from": corridor["transition_from"],
                "transition_to": corridor["transition_to"],
                "anchor_group": corridor["anchor_group"],
                "initial_hold_reason": corridor["initial_hold_reason"],
                "reentry_count": len(matched_inputs),
                "matched_inputs": matched_inputs,
                "strongest_reentry_strength": strongest,
                "latest_closure_state": latest_closure_state,
                "stable_closure_reached": False,
                "note": note,
            }
        )
    return rows


def build_trend_report(ledger: list[dict[str, object]], observer_matches: list[dict[str, object]]) -> list[dict[str, object]]:
    by_corridor: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in observer_matches:
        by_corridor[row["corridor_id"]].append(row)
    rows = []
    for item in ledger:
        cid = item["corridor_id"]
        obs = by_corridor.get(cid, [])
        strengths = [row["reentry_strength"] for row in obs]
        if any(strength == "strong" for strength in strengths):
            trend = "strong_reentry_but_still_hold"
        elif any(strength == "meaningful" for strength in strengths):
            trend = "meaningfully_accumulating"
        elif any(strength == "weak" for strength in strengths):
            trend = "weakly_accumulating"
        else:
            trend = "flat"
        rows.append(
            {
                "corridor_id": cid,
                "trend": trend,
                "observer_match_count": len(obs),
                "observer_strengths": strengths,
                "latest_closure_state": item["latest_closure_state"],
                "stable_closure_reached": False,
            }
        )
    return rows


def build_survivor_cards(ledger: list[dict[str, object]], observer_matches: list[dict[str, object]]) -> str:
    by_corridor: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in observer_matches:
        by_corridor[row["corridor_id"]].append(row)
    lines = ["# corridor survivor cards", ""]
    for row in ledger:
        obs = sorted(
            by_corridor.get(row["corridor_id"], []),
            key=lambda item: {"weak": 1, "meaningful": 2, "strong": 3}[item["reentry_strength"]],
            reverse=True,
        )
        if not obs or obs[0]["reentry_strength"] not in {"meaningful", "strong"}:
            continue
        best = obs[0]
        lines.extend(
            [
                f"## {row['corridor_id']}",
                f"- why_hold_mattered: `{row['initial_hold_reason']}`",
                f"- strongest_reentry: `{best['matched_input_id']}` / `{best['reentry_strength']}`",
                f"- what_got_reinforced: anchor=`{best['anchor_overlap']}`, arrival=`{best['arrival_axis_reinforcement']}`, closure=`{best['closure_delta']}`",
                f"- why_still_not_canonical: stable closure is still not reached even after the later support comes back",
                f"- retention_value: `{best['retention_value_confirmed']}`",
                f"- excerpt: {best['excerpt']}",
                "",
            ]
        )
    return "\n".join(lines) + "\n"


def build_nonreinforced_cards(ledger: list[dict[str, object]], observer_matches: list[dict[str, object]]) -> str:
    lines = ["# corridor nonreinforced cards", ""]
    weak_rows = [row for row in observer_matches if row["reentry_strength"] == "weak"]
    if not weak_rows:
        lines.extend(["- no weak observer-stage reentry cases were found in this pass.", ""])
        return "\n".join(lines) + "\n"
    for row in weak_rows:
        lines.extend(
            [
                f"## {row['corridor_id']} / {row['matched_input_id']}",
                "- strongest_observer_signal: `weak`",
                "- why_not_reinforced: the corridor family returns, but anchor or arrival-axis support is still too thin for meaningful accumulation.",
                f"- closure_delta: `{row['closure_delta']}`",
                f"- note: {row['excerpt']}",
                "",
            ]
        )
    return "\n".join(lines) + "\n"


def build_observer_board(ledger: list[dict[str, object]], trends: list[dict[str, object]], observer_matches: list[dict[str, object]]) -> str:
    strengths = Counter(row["strongest_reentry_strength"] for row in ledger)
    trend_counts = Counter(row["trend"] for row in trends)
    transition_counts = Counter(f"{row['transition_from']}->{row['transition_to']}" for row in ledger)
    weak_inputs = [row for row in observer_matches if row["reentry_strength"] == "weak"]
    lines = [
        "# corridor observer board",
        "",
        "## 1. 가장 자주 재강화되는 corridor",
    ]
    for row in sorted(ledger, key=lambda item: (item["strongest_reentry_strength"], item["reentry_count"]), reverse=True):
        if row["strongest_reentry_strength"] in {"strong", "meaningful"}:
            lines.append(f"- `{row['corridor_id']}` / strongest=`{row['strongest_reentry_strength']}` / latest=`{row['latest_closure_state']}`")
    lines.extend(
        [
            "",
            "## 2. 거의 강화되지 않는 corridor",
        ]
    )
    if weak_inputs:
        for row in weak_inputs:
            lines.append(f"- weak observer input: `{row['corridor_id']}` <- `{row['matched_input_id']}`")
    else:
        lines.append("- no weak observer-only cases in this pass")
    lines.extend(
        [
            "",
            "## 3. technical->organization vs technical->business 누적 비교",
        ]
    )
    for key, count in transition_counts.items():
        lines.append(f"- `{key}` corridors: `{count}`")
    lines.extend(
        [
            f"- strongest strength counts: `{dict(strengths)}`",
            f"- trend counts: `{dict(trend_counts)}`",
            "",
            "## 4. stable_closure_reached 유무",
            "- 이번 stage2에서도 `stable_closure_reached` 는 없음",
            "",
            "## 5. 지금 당장 promotion rule을 만들면 안 되는 이유",
            "- reentry accumulation is real, but it still reinforces hold rather than finishing closure.",
            "- observer evidence should remain observer evidence until stable closure repeats across more inputs.",
        ]
    )
    return "\n".join(lines) + "\n"


def build_boundary_note(ledger: list[dict[str, object]], trends: list[dict[str, object]]) -> str:
    strongish = [row for row in ledger if row["strongest_reentry_strength"] in {"meaningful", "strong"}]
    lines = [
        "# corridor boundary note stage2",
        "",
        "## 1. 현단계에서 확정한 것",
        "- some mixed corridors keep getting reentry support across more than two inputs.",
        "- reentry accumulation thickens observer evidence, but does not by itself create stable closure.",
        "",
        "## 2. 아직 확정하지 않은 것",
        "- whether repeated observer reinforcement should ever trigger canonical promotion",
        "- whether technical->organization should be treated differently from technical->business in promotion terms",
        "",
        "## 3. observer/meaning layer에서만 다룰 것",
        "- corridor trend labels",
        "- retention value wording",
        "- arrival axis clarity commentary",
        "",
        "## 4. 코어 수정 금지 항목",
        "- no promotion rule",
        "- no automatic mixed upgrade",
        "- no change to mixed/canonical boundary grammar",
        "",
        "## 5. 다음 턴 진입 조건",
        f"- add another similar input and see whether the current strongish corridors `{len(strongish)}` keep reinforcing",
        "- keep checking whether any corridor ever reaches stable_closure_reached under the same observer discipline",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

    candidates = load_json(STAGE1_ROOT / "mixed_reentry_candidate_index.json")
    stage1_matches = load_json(STAGE1_ROOT / "mixed_reentry_match_report.json")

    corridors, candidate_to_corridor = build_stage1_corridors(candidates, stage1_matches)

    observer_windows: list[dict[str, object]] = []
    for spec in OBSERVER_INPUTS:
        units = parse_units(Path(spec["path"]), str(spec["kind"]))
        units_by_id = {row["unit_id"]: row for row in units}
        windows = build_windows(str(spec["input_id"]), units, int(spec["window_size"]), int(spec["overlap"]))
        for window in windows:
            classified = classify_window(window, units_by_id)
            if classified is not None:
                observer_windows.append(classified)

    observer_matches = choose_best_observer_matches(corridors, observer_windows)
    ledger = build_ledger(corridors, stage1_matches, observer_matches, candidate_to_corridor)
    trends = build_trend_report(ledger, observer_matches)

    (OUTPUT_ROOT / "corridor_ledger_stage2.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUTPUT_ROOT / "corridor_reentry_accumulation_report.json").write_text(json.dumps(observer_matches, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUTPUT_ROOT / "corridor_strength_trend_report.json").write_text(json.dumps(trends, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUTPUT_ROOT / "corridor_survivor_cards.md").write_text(build_survivor_cards(ledger, observer_matches), encoding="utf-8")
    (OUTPUT_ROOT / "corridor_nonreinforced_cards.md").write_text(build_nonreinforced_cards(ledger, observer_matches), encoding="utf-8")
    (OUTPUT_ROOT / "corridor_observer_board.md").write_text(build_observer_board(ledger, trends, observer_matches), encoding="utf-8")
    (OUTPUT_ROOT / "corridor_boundary_note_stage2.md").write_text(build_boundary_note(ledger, trends), encoding="utf-8")

    print(
        json.dumps(
            {
                "corridor_count": len(ledger),
                "observer_match_count": len(observer_matches),
                "trend_count": len(trends),
                "generated_dir": str(OUTPUT_ROOT),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
