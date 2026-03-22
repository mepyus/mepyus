from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import json


REPO_ROOT = Path(__file__).resolve().parents[3]
STAGE3_ROOT = REPO_ROOT / "app" / "work" / "mixed_corridor_boundary_probe_stage3" / "generated"
OUTPUT_ROOT = REPO_ROOT / "app" / "work" / "mixed_corridor_format_disentangle_stage4" / "generated"

TARGET_CORRIDORS = [
    "technical->business::ai_business",
    "technical->organization::ai_business",
    "technical->organization::harness_agent",
]

INPUT_REGISTRY = [
    {
        "input_id": "sm_df_session_log",
        "source_path": "runtime/logs/work_sessions/session_20260318_180251.md",
        "probe_group": "same_meaning_different_format",
        "expected_corridor_family": ["technical->organization::ai_business", "technical->organization::harness_agent"],
        "expected_format_effect": "meaning should dominate while log format adds only mild support.",
        "why_grouped_here": "technical implementation is repeatedly translated into workflow/process interpretation inside a work-log format.",
        "caution_note": "shared ecosystem vocabulary can add some format help.",
        "kind": "section",
        "window_size": 5,
        "overlap": 2,
    },
    {
        "input_id": "sf_dm_codex1",
        "source_path": "references/vectorfl_next_gemini_session/codex1.md",
        "probe_group": "same_format_different_meaning",
        "expected_corridor_family": [],
        "expected_format_effect": "annotation shell may create weak resonance without true corridor arrival.",
        "why_grouped_here": "dust/annotation format is similar to other structured analysis, but the content is historical AlphaGo explanation rather than org/business corridor.",
        "caution_note": "source-family overlap can inflate weak echoes.",
        "kind": "paragraph",
        "window_size": 6,
        "overlap": 2,
    },
    {
        "input_id": "sf_dm_codex",
        "source_path": "references/vectorfl_next_gemini_session/codex.md",
        "probe_group": "same_format_different_meaning",
        "expected_corridor_family": [],
        "expected_format_effect": "annotation format may keep bridge-like flow words alive even without corridor closure.",
        "why_grouped_here": "same dust-style shell, but mostly event reconstruction rather than technical->org/business transition.",
        "caution_note": "weak resonance here should be treated as format noise.",
        "kind": "paragraph",
        "window_size": 6,
        "overlap": 2,
    },
    {
        "input_id": "sf_sa_youtube_exam",
        "source_path": "references/vectorfl_next_gemini_session/youtube_exam.md",
        "probe_group": "same_family_shifted_axis",
        "expected_corridor_family": ["technical->business::ai_business"],
        "expected_format_effect": "same family can preserve AI/model history echoes while arrival axis drifts away from org/business corridor.",
        "why_grouped_here": "same transcript family and voice, but arrival axis is historical shock/interpretation rather than org redesign.",
        "caution_note": "family similarity can produce weak arrival echoes.",
        "kind": "paragraph",
        "window_size": 4,
        "overlap": 1,
    },
    {
        "input_id": "sf_sa_memo1",
        "source_path": "references/vectorfl_next_gemini_session/reference_engine/vectorfl_next/memo1.md",
        "probe_group": "same_family_shifted_axis",
        "expected_corridor_family": [],
        "expected_format_effect": "same authorial family but shifted toward philosophy/meta reflection, not org/business transition.",
        "why_grouped_here": "same family and style habits, but arrival axis is quiet-space / reservoir / residue rather than the tested corridor.",
        "caution_note": "family bias should be separated from real corridor match.",
        "kind": "section",
        "window_size": 4,
        "overlap": 1,
    },
    {
        "input_id": "cf_sc_basic3",
        "source_path": "basic3.md",
        "probe_group": "cross_family_same_corridor",
        "expected_corridor_family": ["technical->business::ai_business", "technical->organization::ai_business"],
        "expected_format_effect": "different family, but similar platform-shift/business arrival should survive if the corridor is meaning-driven.",
        "why_grouped_here": "different document family, reflective transcript style, but still moves from technical possibility toward platform/business consequences.",
        "caution_note": "arrival axis is present but more reflective than operational.",
        "kind": "paragraph",
        "window_size": 4,
        "overlap": 1,
    },
    {
        "input_id": "cf_sc_basic4",
        "source_path": "basic4.md",
        "probe_group": "cross_family_same_corridor",
        "expected_corridor_family": ["technical->business::ai_business"],
        "expected_format_effect": "different family and format, but business-arrival corridor may survive through frontier shift discussion.",
        "why_grouped_here": "different transcript family with clear technical->industry/business shift around frontier models.",
        "caution_note": "can still be more adjacent than exact for organization corridors.",
        "kind": "paragraph",
        "window_size": 4,
        "overlap": 1,
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
}

TECH_GROUPS = {"harness_agent", "model_compute"}
TRANSITION_MARKERS = ["그래서", "결국", "근데", "하지만", "그러면", "그러면서", "전환", "this makes", "workflow"]


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


def classify_window(window: dict[str, object]) -> dict[str, object]:
    counts = anchor_counts(str(window["text"]))
    tech_present = any(group in TECH_GROUPS for group in counts)
    org_score = counts["organization_ax"]
    business_score = counts["ai_business"]
    if tech_present and org_score >= business_score and org_score > 0:
        arrival_axis = "organization"
    elif tech_present and business_score > 0:
        arrival_axis = "business"
    else:
        arrival_axis = None
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


def judge(group: str, arrival_same: bool, anchor_same: bool, bridge_support: bool, repeated: int) -> tuple[str, str, str]:
    if arrival_same and bridge_support and (anchor_same or repeated >= 2):
        match_type = "corridor_specific_reentry"
        strength = "strong" if group in {"same_meaning_different_format", "cross_family_same_corridor"} else "meaningful"
    elif arrival_same and bridge_support:
        match_type = "arrival_axis_match"
        strength = "meaningful" if group in {"same_meaning_different_format", "cross_family_same_corridor"} else "weak"
    elif bridge_support and (anchor_same or repeated >= 1):
        match_type = "bridge_partial_echo"
        strength = "weak"
    elif anchor_same or repeated >= 1:
        match_type = "anchor_only_echo"
        strength = "weak"
    else:
        match_type = "no_meaningful_match"
        strength = "none"

    if group in {"same_meaning_different_format", "cross_family_same_corridor"} and strength in {"meaningful", "strong"}:
        disentangle = "meaning_driven"
    elif group == "same_format_different_meaning" and strength == "weak":
        disentangle = "format_noisy"
        if match_type == "anchor_only_echo":
            match_type = "format_resonance_only"
    elif group == "same_family_shifted_axis" and strength == "weak":
        disentangle = "family_assisted"
    elif group in {"same_meaning_different_format", "cross_family_same_corridor"} and strength == "weak":
        disentangle = "format_assisted"
    else:
        disentangle = "unclear"
    return match_type, strength, disentangle


def match_corridor(corridor_id: str, group: str, classified: dict[str, object]) -> dict[str, object]:
    _, transition_to, anchor_group = corridor_id.split("::")[0].split("->")[0], corridor_id.split("::")[0].split("->")[1], corridor_id.split("::")[1]
    arrival_same = transition_to == classified["arrival_axis"]
    anchor_same = anchor_group == classified["dominant_anchor"]
    bridge_support = bool(classified["bridge_support"])
    repeated = int(classified["repeated_anchor_support"])
    anchor_overlap = "same_anchor" if anchor_same else ("adjacent_anchor" if classified["anchor_counts"].get(anchor_group, 0) > 0 else "different_anchor")
    arrival_axis_overlap = "same_arrival_axis" if arrival_same else ("missing_arrival_axis" if classified["arrival_axis"] is None else "different_arrival_axis")
    match_type, strength, disentangle = judge(group, arrival_same, anchor_same, bridge_support, repeated)
    return {
        "corridor_id": corridor_id,
        "input_id": classified["input_id"],
        "probe_group": group,
        "anchor_overlap": anchor_overlap,
        "bridge_support": "yes" if bridge_support else "no",
        "arrival_axis_overlap": arrival_axis_overlap,
        "match_type": match_type,
        "reentry_strength": strength,
        "disentangle_judgment": disentangle,
        "note": f"arrival={arrival_axis_overlap}, anchor={anchor_overlap}, repeated={repeated}, bridge={'yes' if bridge_support else 'no'}",
        "excerpt": classified["excerpt"],
    }


def choose_best(rows: list[dict[str, object]]) -> dict[str, object]:
    rank = {"none": 0, "weak": 1, "meaningful": 2, "strong": 3}
    type_rank = {
        "no_meaningful_match": 0,
        "format_resonance_only": 1,
        "anchor_only_echo": 2,
        "bridge_partial_echo": 3,
        "arrival_axis_match": 4,
        "corridor_specific_reentry": 5,
    }
    return sorted(rows, key=lambda row: (rank[str(row["reentry_strength"])], type_rank[str(row["match_type"])]), reverse=True)[0]


def build_group_comparison(best_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    by_group: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in best_rows:
        by_group[str(row["probe_group"])].append(row)
    rows = []
    for group in [
        "same_meaning_different_format",
        "same_format_different_meaning",
        "same_family_shifted_axis",
        "cross_family_same_corridor",
    ]:
        items = by_group.get(group, [])
        strengths = Counter(str(row["reentry_strength"]) for row in items)
        matches = Counter(str(row["match_type"]) for row in items)
        judgments = Counter(str(row["disentangle_judgment"]) for row in items)
        rows.append(
            {
                "group_name": group,
                "tested_count": len(items),
                "strong_count": strengths["strong"],
                "meaningful_count": strengths["meaningful"],
                "weak_count": strengths["weak"],
                "none_count": strengths["none"],
                "dominant_match_type": max(matches, key=matches.get) if matches else "no_meaningful_match",
                "dominant_disentangle_judgment": max(judgments, key=judgments.get) if judgments else "unclear",
                "summary": f"{group} mostly reads as {max(matches, key=matches.get) if matches else 'no_meaningful_match'} / {max(judgments, key=judgments.get) if judgments else 'unclear'}",
            }
        )
    return rows


def build_disentangle_ledger(best_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    by_corridor: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in best_rows:
        by_corridor[str(row["corridor_id"])].append(row)
    rows = []
    for corridor_id in TARGET_CORRIDORS:
        corr_rows = by_corridor[corridor_id]
        by_group = {row["probe_group"]: row for row in corr_rows}
        sm = by_group.get("same_meaning_different_format")
        sf = by_group.get("same_format_different_meaning")
        fam = by_group.get("same_family_shifted_axis")
        cf = by_group.get("cross_family_same_corridor")
        same_meaning = f"{sm['reentry_strength']} / {sm['match_type']} / {sm['disentangle_judgment']}" if sm else "none"
        same_format = f"{sf['reentry_strength']} / {sf['match_type']} / {sf['disentangle_judgment']}" if sf else "none"
        same_family = f"{fam['reentry_strength']} / {fam['match_type']} / {fam['disentangle_judgment']}" if fam else "none"
        cross_family = f"{cf['reentry_strength']} / {cf['match_type']} / {cf['disentangle_judgment']}" if cf else "none"

        if sm and sm["reentry_strength"] in {"meaningful", "strong"} and cf and cf["reentry_strength"] in {"meaningful", "strong"} and sf and sf["reentry_strength"] in {"none", "weak"}:
            current_reading = "mostly_meaning_driven"
            format_noise_risk = "low"
            family_bias_risk = "low" if fam and fam["reentry_strength"] in {"none", "weak"} else "medium"
        elif sm and sm["reentry_strength"] in {"meaningful", "strong"} and cf and cf["reentry_strength"] in {"weak", "meaningful"}:
            current_reading = "meaning_driven_with_format_assist"
            format_noise_risk = "medium"
            family_bias_risk = "medium"
        elif fam and fam["reentry_strength"] in {"meaningful", "strong"}:
            current_reading = "family_sensitive"
            format_noise_risk = "medium"
            family_bias_risk = "high"
        elif sf and sf["reentry_strength"] in {"meaningful", "strong"}:
            current_reading = "format_noisy"
            format_noise_risk = "high"
            family_bias_risk = "medium"
        else:
            current_reading = "unclear"
            format_noise_risk = "medium"
            family_bias_risk = "medium"

        rows.append(
            {
                "corridor_id": corridor_id,
                "same_meaning_different_format_response": same_meaning,
                "same_format_different_meaning_response": same_format,
                "same_family_shifted_axis_response": same_family,
                "cross_family_same_corridor_response": cross_family,
                "current_reading": current_reading,
                "format_noise_risk": format_noise_risk,
                "family_bias_risk": family_bias_risk,
                "promotion_readiness": "still_observe" if current_reading in {"mostly_meaning_driven", "meaning_driven_with_format_assist"} else "far_from_ready",
                "note": "meaning/format disentangle improves observer confidence but still does not create stable closure.",
            }
        )
    return rows


def build_cards(ledger: list[dict[str, object]]) -> str:
    lines = ["# meaning vs format cards", ""]
    for row in ledger:
        lines.extend(
            [
                f"## {row['corridor_id']}",
                "- comparison: same meaning / different format vs same format / different meaning vs same family / shifted axis vs cross family / same corridor",
                f"- same_meaning_different_format: `{row['same_meaning_different_format_response']}`",
                f"- same_format_different_meaning: `{row['same_format_different_meaning_response']}`",
                f"- same_family_shifted_axis: `{row['same_family_shifted_axis_response']}`",
                f"- cross_family_same_corridor: `{row['cross_family_same_corridor_response']}`",
                f"- reading: `{row['current_reading']}`",
                "- why_not_promoted: disentangle improves confidence in meaning, but stable closure is still absent.",
                "",
            ]
        )
    return "\n".join(lines) + "\n"


def build_false_positive_watch(best_rows: list[dict[str, object]]) -> str:
    lines = ["# format false positive watch", ""]
    rows = [
        row
        for row in best_rows
        if row["disentangle_judgment"] in {"format_noisy", "family_assisted"}
        or (row["probe_group"] == "same_format_different_meaning" and row["reentry_strength"] == "weak")
    ]
    for row in rows:
        lines.extend(
            [
                f"## {row['corridor_id']} / {row['input_id']}",
                f"- observed_as: `{row['match_type']}` / `{row['reentry_strength']}` / `{row['disentangle_judgment']}`",
                "- warning: weak resonance here should not be read as true corridor recovery.",
                f"- note: {row['note']}",
                "",
            ]
        )
    if not rows:
        lines.extend(["- no major format/family false positive case dominated this pass.", ""])
    return "\n".join(lines) + "\n"


def build_board(group_comparison: list[dict[str, object]], ledger: list[dict[str, object]]) -> str:
    org_rows = [row for row in ledger if "technical->organization" in row["corridor_id"]]
    biz_rows = [row for row in ledger if "technical->business" in row["corridor_id"]]
    lines = [
        "# format disentangle board",
        "",
        "## 1. strongest meaning-driven corridor",
    ]
    for row in ledger:
        if row["current_reading"] in {"mostly_meaning_driven", "meaning_driven_with_format_assist"}:
            lines.append(f"- `{row['corridor_id']}` / `{row['current_reading']}`")
    lines.extend(["", "## 2. format-assisted로 보이는 corridor"])
    for row in ledger:
        if row["current_reading"] == "meaning_driven_with_format_assist":
            lines.append(f"- `{row['corridor_id']}`")
    lines.extend(["", "## 3. family bias 경고 사례"])
    for row in ledger:
        if row["family_bias_risk"] in {"medium", "high"}:
            lines.append(f"- `{row['corridor_id']}` / family_bias=`{row['family_bias_risk']}`")
    lines.extend(["", "## 4. 4개 입력 그룹 비교표"])
    for row in group_comparison:
        lines.append(
            f"- `{row['group_name']}`: strong=`{row['strong_count']}`, meaningful=`{row['meaningful_count']}`, weak=`{row['weak_count']}`, none=`{row['none_count']}` / dominant=`{row['dominant_match_type']}` / `{row['dominant_disentangle_judgment']}`"
        )
    lines.extend(
        [
            "",
            "## 5. technical->organization vs technical->business 비교",
            f"- technical->organization: `{[row['current_reading'] for row in org_rows]}`",
            f"- technical->business: `{[row['current_reading'] for row in biz_rows]}`",
            "",
            "## 6. stable_closure_reached 여부",
            "- 이번 stage4에서도 `stable_closure_reached` 는 없음",
            "",
            "## 7. 다음 턴 추천",
            "- add more cross-family same-corridor inputs and more same-format different-meaning negatives before any promotion discussion.",
        ]
    )
    return "\n".join(lines) + "\n"


def build_decision_note(ledger: list[dict[str, object]]) -> str:
    meaning_driven = [row["corridor_id"] for row in ledger if row["current_reading"] in {"mostly_meaning_driven", "meaning_driven_with_format_assist"}]
    noisy = [row["corridor_id"] for row in ledger if row["current_reading"] in {"family_sensitive", "format_noisy", "unclear"}]
    lines = [
        "# format disentangle decision note",
        "",
        "## A. current strongest corridors는 mostly meaning-driven 인가",
        f"- 부분적으로 예. `{len(meaning_driven)}` corridor는 meaning-driven 신호가 format/family noise보다 더 크다.",
        "",
        "## B. format/source-family 착시는 어느 정도 남는가",
        "- 약한 annotation/source-family resonance는 남아 있다. 특히 same_format_different_meaning 과 same_family_shifted_axis 에서 weak echo가 계속 나온다.",
        "",
        "## C. 어떤 corridor는 더 깨끗하고 어떤 corridor는 더 noisy한가",
    ]
    for cid in meaning_driven:
        lines.append(f"- cleaner: `{cid}`")
    for cid in noisy:
        lines.append(f"- noisier: `{cid}`")
    lines.extend(
        [
            "",
            "## D. 다음 단계가 더 많은 cross-family 입력인지, 다른 arrival axis 확장인지",
            "- 다음은 cross-family same-corridor 입력을 더 늘리는 쪽이 먼저다.",
            "",
            "## E. 왜 아직 canonical promotion은 아닌가",
            "- meaning-driven is not stable closure.",
            "- format disentangle가 개선돼도 stable_closure_reached 증거는 아직 없다.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    best_rows = []
    registry_rows = []
    for spec in INPUT_REGISTRY:
        registry_rows.append(
            {
                "input_id": spec["input_id"],
                "source_path": spec["source_path"],
                "probe_group": spec["probe_group"],
                "expected_corridor_family": spec["expected_corridor_family"],
                "expected_format_effect": spec["expected_format_effect"],
                "why_grouped_here": spec["why_grouped_here"],
                "caution_note": spec["caution_note"],
            }
        )
        units = parse_units(REPO_ROOT / spec["source_path"], spec["kind"])
        windows = build_windows(spec["input_id"], units, spec["window_size"], spec["overlap"])
        classified = [classify_window(window) for window in windows]
        for corridor_id in TARGET_CORRIDORS:
            rows = [match_corridor(corridor_id, spec["probe_group"], row) for row in classified]
            best_rows.append(choose_best(rows))

    group_comparison = build_group_comparison(best_rows)
    ledger = build_disentangle_ledger(best_rows)

    (OUTPUT_ROOT / "format_probe_input_registry.json").write_text(json.dumps(registry_rows, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUTPUT_ROOT / "format_probe_match_report.json").write_text(json.dumps(best_rows, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUTPUT_ROOT / "format_probe_group_comparison.json").write_text(json.dumps(group_comparison, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUTPUT_ROOT / "corridor_disentangle_ledger.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUTPUT_ROOT / "meaning_vs_format_cards.md").write_text(build_cards(ledger), encoding="utf-8")
    (OUTPUT_ROOT / "format_false_positive_watch.md").write_text(build_false_positive_watch(best_rows), encoding="utf-8")
    (OUTPUT_ROOT / "format_disentangle_board.md").write_text(build_board(group_comparison, ledger), encoding="utf-8")
    (OUTPUT_ROOT / "format_disentangle_decision_note.md").write_text(build_decision_note(ledger), encoding="utf-8")

    print(
        json.dumps(
            {
                "registered_inputs": len(registry_rows),
                "match_rows": len(best_rows),
                "corridor_count": len(ledger),
                "generated_dir": str(OUTPUT_ROOT),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
