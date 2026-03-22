from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import json


REPO_ROOT = Path(__file__).resolve().parents[3]
STAGE2_ROOT = REPO_ROOT / "app" / "work" / "mixed_reentry_observer_stage2" / "generated"
OUTPUT_ROOT = REPO_ROOT / "app" / "work" / "mixed_corridor_boundary_probe_stage3" / "generated"

INPUT_REGISTRY = [
    {
        "input_id": "reinforce_session_log",
        "source_path": "runtime/logs/work_sessions/session_20260318_180251.md",
        "probe_group": "reinforcing",
        "why_grouped_here": "observer/fragment/workflow log repeatedly converts technical implementation into organization/process interpretation.",
        "expected_corridor_family": ["technical->organization::harness_agent", "technical->organization::ai_business"],
        "caution_note": "same ecosystem language may inflate anchor overlap.",
        "kind": "section",
        "window_size": 5,
        "overlap": 2,
    },
    {
        "input_id": "reinforce_basic3",
        "source_path": "basic3.md",
        "probe_group": "reinforcing",
        "why_grouped_here": "platform shift and future-of-work discussion is close to technical->business and technical->organization corridors.",
        "expected_corridor_family": ["technical->business::ai_business", "technical->organization::ai_business"],
        "caution_note": "more reflective than operational, so closure may stay partial.",
        "kind": "paragraph",
        "window_size": 4,
        "overlap": 1,
    },
    {
        "input_id": "adjacent_basic4",
        "source_path": "basic4.md",
        "probe_group": "adjacent",
        "why_grouped_here": "AI trend and frontier pressure are nearby topics, but organization/business arrival axis is less direct.",
        "expected_corridor_family": ["technical->business::ai_business"],
        "caution_note": "may show topic resonance without corridor closure.",
        "kind": "paragraph",
        "window_size": 4,
        "overlap": 1,
    },
    {
        "input_id": "adjacent_youtube_exam",
        "source_path": "references/vectorfl_next_gemini_session/youtube_exam.md",
        "probe_group": "adjacent",
        "why_grouped_here": "AI/model history commentary touches business significance, but the arrival axis is shallow and inconsistent.",
        "expected_corridor_family": ["technical->business::ai_business"],
        "caution_note": "short excerpt may produce bridge-like echoes without durable closure.",
        "kind": "paragraph",
        "window_size": 4,
        "overlap": 1,
    },
    {
        "input_id": "offaxis_basic5",
        "source_path": "basic5.md",
        "probe_group": "off_axis",
        "why_grouped_here": "dense vs MoE is strongly technical and should mostly stay inside architecture explanation rather than organization/business transition.",
        "expected_corridor_family": [],
        "caution_note": "model/compute anchors may still echo topic-level resonance.",
        "kind": "paragraph",
        "window_size": 4,
        "overlap": 1,
    },
    {
        "input_id": "offaxis_codex1",
        "source_path": "references/vectorfl_next_gemini_session/codex1.md",
        "probe_group": "off_axis",
        "why_grouped_here": "segmentation and dust annotation of a related transcript should trigger annotation-format resonance more than transition-corridor reinforcement.",
        "expected_corridor_family": [],
        "caution_note": "same source family can create false positive anchor echoes.",
        "kind": "paragraph",
        "window_size": 6,
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
        "startup",
        "스타트업",
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
        "dust",
        "flow",
        "scene",
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
        "sparsity",
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
        "work",
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
                    units.append({"unit_id": f"u{index:02d}", "title": current_title, "text": " ".join(current_lines).strip()})
                current_title = line[3:].strip()
                current_lines = []
            elif line.strip():
                current_lines.append(line.strip())
        if current_title:
            index += 1
            units.append({"unit_id": f"u{index:02d}", "title": current_title, "text": " ".join(current_lines).strip()})
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


def classify_window(window: dict[str, object]) -> dict[str, object] | None:
    counts = anchor_counts(str(window["text"]))
    tech_present = any(group in TECH_GROUPS for group in counts)
    org_score = counts["organization_ax"]
    business_score = counts["ai_business"]
    arrival_axis = None
    if tech_present and org_score >= business_score and org_score > 0:
        arrival_axis = "organization"
    elif tech_present and business_score > 0:
        arrival_axis = "business"
    repeated = sum(1 for value in counts.values() if value >= 2)
    bridge_support = any(marker.lower() in str(window["text"]).lower() for marker in TRANSITION_MARKERS) or repeated >= 2
    dominant_anchor = max(
        ["harness_agent", "ai_business", "model_compute", "organization_ax"],
        key=lambda group: (counts[group], group == "harness_agent", group == "ai_business"),
    )
    return {
        "input_id": str(window["input_id"]),
        "window_id": str(window["window_id"]),
        "arrival_axis": arrival_axis,
        "anchor_counts": dict(counts),
        "bridge_support": bridge_support,
        "repeated_anchor_support": repeated,
        "dominant_anchor": dominant_anchor,
        "excerpt": str(window["excerpt"]),
        "titles": list(window["titles"]),
        "tech_present": tech_present,
    }


def match_against_corridor(corridor: dict[str, object], group: str, classified: dict[str, object]) -> dict[str, object]:
    arrival_same = corridor["transition_to"] == classified["arrival_axis"]
    anchor_same = corridor["anchor_group"] == classified["dominant_anchor"]
    bridge_support = bool(classified["bridge_support"])
    repeated = int(classified["repeated_anchor_support"])
    tech_present = bool(classified["tech_present"])
    anchor_overlap = "same_anchor" if anchor_same else ("adjacent_anchor" if classified["anchor_counts"].get(corridor["anchor_group"], 0) > 0 else "different_anchor")
    arrival_axis_overlap = "same_arrival_axis" if arrival_same else ("missing_arrival_axis" if classified["arrival_axis"] is None else "different_arrival_axis")

    if arrival_same and anchor_same and bridge_support and repeated >= 2:
        match_type = "corridor_specific_reentry"
        strength = "strong" if group == "reinforcing" else "meaningful"
        specificity = "specific"
    elif arrival_same and bridge_support and repeated >= 1:
        match_type = "arrival_axis_match"
        strength = "meaningful" if group != "off_axis" else "weak"
        specificity = "specific" if group == "reinforcing" else "unclear"
    elif tech_present and classified["anchor_counts"].get(corridor["anchor_group"], 0) > 0 and bridge_support:
        match_type = "bridge_partial_echo"
        strength = "weak"
        specificity = "broad_but_noisy" if group == "off_axis" else "unclear"
    elif classified["anchor_counts"].get(corridor["anchor_group"], 0) > 0:
        match_type = "anchor_only_echo"
        strength = "weak" if group != "off_axis" else "none"
        specificity = "topic_only"
    else:
        match_type = "no_meaningful_match"
        strength = "none"
        specificity = "topic_only" if any(classified["anchor_counts"].values()) else "unclear"

    note = (
        f"arrival={arrival_axis_overlap}, anchor={anchor_overlap}, repeated={repeated}, bridge={'yes' if bridge_support else 'no'}"
    )
    return {
        "corridor_id": corridor["corridor_id"],
        "input_id": classified["input_id"],
        "window_id": classified["window_id"],
        "probe_group": group,
        "anchor_overlap": anchor_overlap,
        "bridge_support": "yes" if bridge_support else "no",
        "arrival_axis_overlap": arrival_axis_overlap,
        "match_type": match_type,
        "reentry_strength": strength,
        "specificity_judgment": specificity,
        "note": note,
        "excerpt": classified["excerpt"],
        "titles": classified["titles"],
    }


def choose_best(rows: list[dict[str, object]]) -> dict[str, object]:
    rank = {"none": 0, "weak": 1, "meaningful": 2, "strong": 3}
    type_rank = {
        "no_meaningful_match": 0,
        "anchor_only_echo": 1,
        "bridge_partial_echo": 2,
        "arrival_axis_match": 3,
        "corridor_specific_reentry": 4,
    }
    return sorted(
        rows,
        key=lambda row: (
            rank[str(row["reentry_strength"])],
            type_rank[str(row["match_type"])],
            1 if row["bridge_support"] == "yes" else 0,
        ),
        reverse=True,
    )[0]


def trend_summary(rows: list[dict[str, object]]) -> str:
    best = choose_best(rows)
    return f"{best['reentry_strength']} / {best['match_type']} / {best['specificity_judgment']}"


def build_group_comparison(best_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    by_group: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in best_rows:
        by_group[str(row["probe_group"])].append(row)
    rows = []
    for group in ["reinforcing", "adjacent", "off_axis"]:
        items = by_group.get(group, [])
        strength_counts = Counter(str(row["reentry_strength"]) for row in items)
        match_counts = Counter(str(row["match_type"]) for row in items)
        spec_counts = Counter(str(row["specificity_judgment"]) for row in items)
        dominant_match = max(match_counts, key=match_counts.get) if match_counts else "no_meaningful_match"
        dominant_spec = max(spec_counts, key=spec_counts.get) if spec_counts else "unclear"
        rows.append(
            {
                "group_name": group,
                "tested_count": len(items),
                "strong_count": strength_counts["strong"],
                "meaningful_count": strength_counts["meaningful"],
                "weak_count": strength_counts["weak"],
                "none_count": strength_counts["none"],
                "dominant_match_type": dominant_match,
                "dominant_specificity_judgment": dominant_spec,
                "summary": f"{group} inputs mostly read as {dominant_match} / {dominant_spec}",
            }
        )
    return rows


def build_specificity_ledger(corridors: list[dict[str, object]], best_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    by_corridor: dict[str, dict[str, list[dict[str, object]]]] = defaultdict(lambda: defaultdict(list))
    for row in best_rows:
        by_corridor[str(row["corridor_id"])][str(row["probe_group"])].append(row)
    rows = []
    for corridor in corridors:
        cid = str(corridor["corridor_id"])
        rein_rows = by_corridor[cid].get("reinforcing", [])
        adj_rows = by_corridor[cid].get("adjacent", [])
        off_rows = by_corridor[cid].get("off_axis", [])
        rein = choose_best(rein_rows) if rein_rows else None
        adj = choose_best(adj_rows) if adj_rows else None
        off = choose_best(off_rows) if off_rows else None
        reinforcing_response = trend_summary([rein]) if rein else "none"
        adjacent_response = trend_summary([adj]) if adj else "none"
        off_axis_response = trend_summary([off]) if off else "none"
        if rein and rein["reentry_strength"] == "strong" and adj and adj["reentry_strength"] in {"weak", "meaningful"} and off and off["reentry_strength"] in {"none", "weak"}:
            specificity = "specific"
            false_positive_risk = "low"
        elif rein and rein["reentry_strength"] in {"meaningful", "strong"} and off and off["reentry_strength"] == "none":
            specificity = "moderately_specific"
            false_positive_risk = "medium"
        elif off and off["reentry_strength"] in {"meaningful", "strong"}:
            specificity = "broad_but_noisy"
            false_positive_risk = "high"
        else:
            specificity = "unclear"
            false_positive_risk = "medium"
        rows.append(
            {
                "corridor_id": cid,
                "reinforcing_response": reinforcing_response,
                "adjacent_response": adjacent_response,
                "off_axis_response": off_axis_response,
                "current_specificity_reading": specificity,
                "false_positive_risk": false_positive_risk,
                "promotion_readiness": "far_from_ready" if specificity != "specific" else "still_observe",
                "note": "specificity must stay observer-only until stable closure repeats under boundary challenge.",
            }
        )
    return rows


def build_survivor_cards(ledger: list[dict[str, object]]) -> str:
    lines = ["# boundary survivor cards", ""]
    for row in ledger:
        if row["current_specificity_reading"] not in {"specific", "moderately_specific"}:
            continue
        lines.extend(
            [
                f"## {row['corridor_id']}",
                "- why_it_matters: this corridor already had productive hold value and now also survives boundary challenge better than nearby inputs.",
                f"- reinforcing: `{row['reinforcing_response']}`",
                f"- adjacent: `{row['adjacent_response']}`",
                f"- off_axis: `{row['off_axis_response']}`",
                f"- specificity_reading: `{row['current_specificity_reading']}`",
                "- why_still_not_canonical: even specific corridors are still support-thickened holds, not stable closures.",
                "",
            ]
        )
    return "\n".join(lines) + "\n"


def build_false_positive_watch(best_rows: list[dict[str, object]], ledger: list[dict[str, object]]) -> str:
    lines = ["# boundary false positive watch", ""]
    off_axis_hits = [row for row in best_rows if row["probe_group"] == "off_axis" and row["reentry_strength"] != "none"]
    for row in off_axis_hits:
        lines.extend(
            [
                f"## {row['corridor_id']} / {row['input_id']}",
                f"- observed_as: `{row['match_type']}` / `{row['reentry_strength']}`",
                "- warning: off-axis input still produced some resonance, so topic overlap must not be mistaken for corridor closure.",
                f"- note: {row['note']}",
                "",
            ]
        )
    noisy = [row for row in ledger if row["current_specificity_reading"] in {"broad_but_noisy", "unclear"}]
    if not off_axis_hits and not noisy:
        lines.extend(["- no major false-positive corridor was found in this pass, but off-axis echoes still need continued monitoring.", ""])
    return "\n".join(lines) + "\n"


def build_probe_board(group_comparison: list[dict[str, object]], ledger: list[dict[str, object]]) -> str:
    spec_counts = Counter(row["current_specificity_reading"] for row in ledger)
    org_rows = [row for row in ledger if "technical->organization" in row["corridor_id"]]
    biz_rows = [row for row in ledger if "technical->business" in row["corridor_id"]]
    lines = [
        "# boundary probe board",
        "",
        "## 1. 현재 strongest corridor family",
    ]
    for row in ledger:
        if row["current_specificity_reading"] in {"specific", "moderately_specific"}:
            lines.append(f"- `{row['corridor_id']}` / `{row['current_specificity_reading']}`")
    lines.extend(["", "## 2. reinforcing / adjacent / off-axis 그룹 비교표"])
    for row in group_comparison:
        lines.append(
            f"- `{row['group_name']}`: strong=`{row['strong_count']}`, meaningful=`{row['meaningful_count']}`, weak=`{row['weak_count']}`, none=`{row['none_count']}` / dominant=`{row['dominant_match_type']}`"
        )
    lines.extend(
        [
            "",
            "## 3. technical->organization vs technical->business specificity 비교",
            f"- technical->organization corridors: `{len(org_rows)}` / readings=`{[row['current_specificity_reading'] for row in org_rows]}`",
            f"- technical->business corridors: `{len(biz_rows)}` / readings=`{[row['current_specificity_reading'] for row in biz_rows]}`",
            "",
            "## 4. false positive risk 요약",
            f"- specificity counts: `{dict(spec_counts)}`",
            "",
            "## 5. stable_closure_reached 여부",
            "- 이번 stage3에서도 `stable_closure_reached` 는 없음",
            "",
            "## 6. promotion rule을 아직 만들면 안 되는 이유",
            "- boundary challenge passes still measure observer specificity, not stable closure.",
            "- off-axis resonance remains possible on topic-heavy technical text.",
            "",
            "## 7. 다음 턴 추천",
            "- add more off-axis negative controls or a second reinforcing business transcript before any promotion discussion.",
        ]
    )
    return "\n".join(lines) + "\n"


def build_decision_note(ledger: list[dict[str, object]]) -> str:
    specific = [row["corridor_id"] for row in ledger if row["current_specificity_reading"] == "specific"]
    broad = [row["corridor_id"] for row in ledger if row["current_specificity_reading"] in {"broad_but_noisy", "unclear"}]
    lines = [
        "# boundary probe decision note",
        "",
        "## A. corridor specificity는 확인됐는가",
        f"- 부분적으로 예. `{len(specific)}` corridor는 reinforcing/adjacent/off-axis 차이가 비교적 선명하게 갈린다.",
        "",
        "## B. 어떤 corridor는 진짜 specific해 보이는가",
    ]
    for cid in specific:
        lines.append(f"- `{cid}`")
    lines.extend(
        [
            "",
            "## C. 어떤 corridor는 broad resonance 가능성이 남는가",
        ]
    )
    if broad:
        for cid in broad:
            lines.append(f"- `{cid}`")
    else:
        lines.append("- major broad-but-noisy corridor was not dominant in this pass, but off-axis echoes still exist.")
    lines.extend(
        [
            "",
            "## D. 다음 단계가 더 많은 negative-control인지, 다른 축 확장인지",
            "- 다음은 negative-control을 조금 더 늘리는 쪽이 먼저다. specificity를 더 보수적으로 눌러봐야 한다.",
            "",
            "## E. 왜 아직 canonical promotion은 아닌가",
            "- specificity is not closure.",
            "- stable_closure_reached 증거가 없고, observer boundary pass는 still-observe 단계다.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    corridors = load_json(STAGE2_ROOT / "corridor_ledger_stage2.json")

    registry_rows = []
    best_rows = []
    for spec in INPUT_REGISTRY:
        registry_rows.append(
            {
                "input_id": spec["input_id"],
                "source_path": spec["source_path"],
                "probe_group": spec["probe_group"],
                "why_grouped_here": spec["why_grouped_here"],
                "expected_corridor_family": spec["expected_corridor_family"],
                "caution_note": spec["caution_note"],
            }
        )
        units = parse_units(REPO_ROOT / spec["source_path"], spec["kind"])
        windows = build_windows(spec["input_id"], units, spec["window_size"], spec["overlap"])
        classified = [classify_window(window) for window in windows]
        classified = [row for row in classified if row is not None]
        for corridor in corridors:
            rows = [match_against_corridor(corridor, spec["probe_group"], row) for row in classified]
            best_rows.append(choose_best(rows) if rows else {
                "corridor_id": corridor["corridor_id"],
                "input_id": spec["input_id"],
                "window_id": "",
                "probe_group": spec["probe_group"],
                "anchor_overlap": "different_anchor",
                "bridge_support": "no",
                "arrival_axis_overlap": "missing_arrival_axis",
                "match_type": "no_meaningful_match",
                "reentry_strength": "none",
                "specificity_judgment": "unclear",
                "note": "no relevant window found under current grouping",
                "excerpt": "",
                "titles": [],
            })

    group_comparison = build_group_comparison(best_rows)
    specificity_ledger = build_specificity_ledger(corridors, best_rows)

    (OUTPUT_ROOT / "boundary_input_registry.json").write_text(json.dumps(registry_rows, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUTPUT_ROOT / "boundary_probe_match_report.json").write_text(json.dumps(best_rows, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUTPUT_ROOT / "boundary_probe_group_comparison.json").write_text(json.dumps(group_comparison, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUTPUT_ROOT / "boundary_corridor_specificity_ledger.json").write_text(json.dumps(specificity_ledger, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUTPUT_ROOT / "boundary_survivor_cards.md").write_text(build_survivor_cards(specificity_ledger), encoding="utf-8")
    (OUTPUT_ROOT / "boundary_false_positive_watch.md").write_text(build_false_positive_watch(best_rows, specificity_ledger), encoding="utf-8")
    (OUTPUT_ROOT / "boundary_probe_board.md").write_text(build_probe_board(group_comparison, specificity_ledger), encoding="utf-8")
    (OUTPUT_ROOT / "boundary_probe_decision_note.md").write_text(build_decision_note(specificity_ledger), encoding="utf-8")

    print(
        json.dumps(
            {
                "registered_inputs": len(registry_rows),
                "match_rows": len(best_rows),
                "corridor_count": len(specificity_ledger),
                "generated_dir": str(OUTPUT_ROOT),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
