from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import json
import re


REPO_ROOT = Path(__file__).resolve().parents[3]
STAGE4_LEDGER = (
    REPO_ROOT
    / "app"
    / "work"
    / "mixed_corridor_format_disentangle_stage4"
    / "generated"
    / "corridor_disentangle_ledger.json"
)
OUTPUT_ROOT = REPO_ROOT / "app" / "work" / "technical_business_corridor_decompose_stage5" / "generated"
FOCUS_CORRIDOR = "technical->business::ai_business"
POSITIVE_CONTROLS = [
    "technical->organization::ai_business",
    "technical->organization::harness_agent",
]

AXIS_KEYWORDS = {
    "business_leverage": [
        "leverage",
        "효율",
        "workflow",
        "생산성",
        "경쟁력",
        "업무",
        "자동화",
        "회사가 굴러",
        "일을 덜어",
    ],
    "monetization_value_capture": [
        "가치",
        "캡처",
        "돈",
        "수익",
        "가격",
        "브랜드",
        "트랙 레코드",
        "핵심 경쟁력",
    ],
    "startup_thesis": [
        "스타트업",
        "기회",
        "market share",
        "플레이북",
        "플랫폼 시프트",
        "distribution",
        "물레방아",
        "클론",
        "복제",
        "타임 갭",
    ],
    "org_business_boundary": [
        "조직",
        "회사",
        "cfo",
        "사업 계획서",
        "재무",
        "마케팅",
        "팀",
        "적응",
        "콘텐츠",
        "gitHub",
    ],
    "software_value_shift": [
        "소프트웨어",
        "코드",
        "제품",
        "saas",
        "인스턴트 앱",
        "app",
        "모델이 가운데",
        "코드는 가치",
        "software",
        "deliver",
    ],
}

TECH_KEYWORDS = [
    "ai",
    "모델",
    "model",
    "agent",
    "에이전트",
    "harness",
    "workflow",
    "코드",
    "소프트웨어",
    "backend.ai",
    "claude code",
    "codex",
    "gemini",
    "gpu",
    "compute",
    "inference",
]

TRANSITION_MARKERS = [
    "그래서",
    "결국",
    "그렇기 때문에",
    "근데",
    "그러면",
    "이게 핵심",
    "이게 중요한",
    "이렇게 되면",
    "왜냐하면",
    "그러다 보니까",
]

FORMAT_MARKERS = [
    "[dust_",
    "why_one_unit",
    "why_this_value",
    "scene:",
    "flow:",
    "confidence:",
    "unit_type:",
]

FAMILY_MARKERS = [
    "seed_v",
    "raw note",
    "quiet local",
    "local space",
    "bridge_trace",
    "point_seed",
    "space record",
    "workspace index",
    "bundle",
    "artifact return",
]

INPUT_REGISTRY = [
    {
        "input_id": "tb_y0318_value_capture",
        "source_path": "youtube_03_18.md",
        "expected_axis": "monetization_value_capture",
        "format_family": "transcript_interview",
        "why_selected": "model/company value capture and software core-value shift are explicitly discussed in the same transcript.",
        "expected_noise_risk": "medium",
        "note": "may also overlap with software_value_shift.",
        "kind": "section",
        "window_size": 2,
        "overlap": 1,
        "preferred_terms": ["가치", "캡처", "핵심 가치", "모델을 만드는 회사", "레이어"],
    },
    {
        "input_id": "tb_y0318_startup",
        "source_path": "youtube_03_18.md",
        "expected_axis": "startup_thesis",
        "format_family": "transcript_interview",
        "why_selected": "startup opportunity, copy risk, time-gap advantage, and new-company logic appear directly.",
        "expected_noise_risk": "medium",
        "note": "can spill into monetization or org-business boundary.",
        "kind": "section",
        "window_size": 2,
        "overlap": 1,
        "preferred_terms": ["스타트업", "기회", "복제", "물레방아", "타임 갭", "사업적인"],
    },
    {
        "input_id": "tb_y0318_org_boundary",
        "source_path": "youtube_03_18.md",
        "expected_axis": "org_business_boundary",
        "format_family": "transcript_interview",
        "why_selected": "workflow, CFO/content operations, and company-wide adoption are directly translated into business planning.",
        "expected_noise_risk": "medium",
        "note": "strong bridge but can blur into business_leverage.",
        "kind": "section",
        "window_size": 2,
        "overlap": 1,
        "preferred_terms": ["cfo", "사업 계획서", "workflow", "회사", "조직", "재무", "마케팅"],
    },
    {
        "input_id": "tb_basic3_startup",
        "source_path": "basic3.md",
        "expected_axis": "startup_thesis",
        "format_family": "transcript_excerpt",
        "why_selected": "platform shift, market-share anxiety, and startup timing logic are tightly concentrated.",
        "expected_noise_risk": "low",
        "note": "clean startup-thesis candidate.",
        "kind": "paragraph",
        "window_size": 4,
        "overlap": 1,
        "preferred_terms": ["플랫폼 시프트", "market share", "기회", "생태계", "플레이북"],
    },
    {
        "input_id": "tb_basic4_value_shift",
        "source_path": "basic4.md",
        "expected_axis": "software_value_shift",
        "format_family": "transcript_excerpt",
        "why_selected": "frontier shift and architecture dominance are described as an industry-value redefinition, not just raw model metrics.",
        "expected_noise_risk": "medium",
        "note": "may echo broad business corridor more than a narrow sub-axis.",
        "kind": "paragraph",
        "window_size": 4,
        "overlap": 1,
        "preferred_terms": ["프런티어", "변화", "주도권", "아키텍처", "좋기 때문에", "흐름의 변화"],
    },
    {
        "input_id": "tb_exam_software_shift_noise",
        "source_path": "references/vectorfl_next_gemini_session/youtube_exam.md",
        "expected_axis": "software_value_shift",
        "format_family": "same_family_history_transcript",
        "why_selected": "same transcript family and AI-history tone can weakly mimic a technology-to-industry transition without real business arrival.",
        "expected_noise_risk": "high",
        "note": "family echo candidate rather than clean business reentry.",
        "kind": "paragraph",
        "window_size": 4,
        "overlap": 1,
        "preferred_terms": ["ai", "tensorflow", "딥러닝", "기대", "충격"],
    },
    {
        "input_id": "tb_codex1_format_noise",
        "source_path": "references/vectorfl_next_gemini_session/codex1.md",
        "expected_axis": "software_value_shift",
        "format_family": "dust_annotation",
        "why_selected": "annotation shell has repeatedly produced weak business echoes even without true business-arrival content.",
        "expected_noise_risk": "high",
        "note": "pure format noise check.",
        "kind": "paragraph",
        "window_size": 6,
        "overlap": 2,
        "preferred_terms": ["AlphaGo", "TensorFlow", "AI"],
    },
    {
        "input_id": "tb_memo4_family_noise",
        "source_path": "references/vectorfl_next_gemini_session/reference_engine/vectorfl_next/memo4.md",
        "expected_axis": "business_leverage",
        "format_family": "same_family_design_bundle",
        "why_selected": "same family and authorial habits, but arrival axis is design/space/record layering rather than business leverage.",
        "expected_noise_risk": "high",
        "note": "family-noise and observer-style shell check.",
        "kind": "section",
        "window_size": 3,
        "overlap": 1,
        "preferred_terms": ["구조", "설계", "공간", "코드", "조직"],
    },
]


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_units(path: Path, kind: str) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    units: list[dict[str, str]] = []
    if kind == "section":
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
        if units:
            return units
    paragraphs = [chunk.strip() for chunk in re.split(r"\n\s*\n", text) if chunk.strip()]
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
                "excerpt": " / ".join(f"[{row['title']}] {row['text'][:150]}" for row in chunk[:3]),
            }
        )
        if start + window_size >= len(units):
            break
    return windows


def count_keywords(text: str, keywords: list[str]) -> int:
    lowered = text.lower()
    return sum(1 for keyword in keywords if keyword.lower() in lowered)


def classify_window(window: dict[str, object], preferred_terms: list[str]) -> dict[str, object]:
    text = str(window["text"])
    axis_scores = {axis: count_keywords(text, keywords) for axis, keywords in AXIS_KEYWORDS.items()}
    tech_score = count_keywords(text, TECH_KEYWORDS)
    transition_score = count_keywords(text, TRANSITION_MARKERS)
    format_score = count_keywords(text, FORMAT_MARKERS)
    family_score = count_keywords(text, FAMILY_MARKERS)
    preferred_score = count_keywords(text, preferred_terms)
    top_axis, top_score = max(axis_scores.items(), key=lambda item: (item[1], item[0]))
    second_axis, second_score = sorted(axis_scores.items(), key=lambda item: item[1], reverse=True)[1]
    return {
        "window_id": str(window["window_id"]),
        "titles": list(window["titles"]),
        "excerpt": str(window["excerpt"]),
        "axis_scores": axis_scores,
        "top_axis": top_axis,
        "top_score": top_score,
        "second_axis": second_axis,
        "second_score": second_score,
        "tech_score": tech_score,
        "transition_score": transition_score,
        "format_score": format_score,
        "family_score": family_score,
        "preferred_score": preferred_score,
    }


def choose_best_window(rows: list[dict[str, object]], expected_axis: str) -> dict[str, object]:
    def score(row: dict[str, object]) -> tuple[int, int, int, int]:
        axis_scores = row["axis_scores"]
        return (
            int(axis_scores[expected_axis]) * 3 + int(row["preferred_score"]) * 2 + int(row["tech_score"]) + int(row["transition_score"]),
            int(row["top_axis"] == expected_axis),
            int(row["top_score"]),
            -int(row["format_score"] + row["family_score"]),
        )

    return sorted(rows, key=score, reverse=True)[0]


def judge_match(expected_axis: str, row: dict[str, object]) -> tuple[str, str, str]:
    axis_scores = row["axis_scores"]
    expected_score = int(axis_scores[expected_axis])
    top_axis = str(row["top_axis"])
    top_score = int(row["top_score"])
    second_score = int(row["second_score"])
    tech_score = int(row["tech_score"])
    transition_score = int(row["transition_score"])
    format_score = int(row["format_score"])
    family_score = int(row["family_score"])
    multi_axis = top_score > 0 and second_score > 0 and abs(top_score - second_score) <= 1

    if tech_score >= 2 and expected_score >= 2 and transition_score >= 1:
        match_type = "axis_specific_reentry"
        strength = "strong" if expected_score >= 3 else "meaningful"
    elif tech_score >= 1 and top_score >= 2 and transition_score >= 1:
        match_type = "business_corridor_general_echo"
        strength = "meaningful"
    elif tech_score >= 1 and top_score >= 1:
        match_type = "bridge_partial_echo"
        strength = "weak"
    elif format_score >= 2:
        match_type = "format_resonance_only"
        strength = "weak"
    elif family_score >= 2:
        match_type = "family_assisted_echo"
        strength = "weak"
    else:
        match_type = "no_meaningful_match"
        strength = "none"

    if format_score >= 2 and strength in {"weak", "meaningful"} and expected_score <= 1:
        judgment = "format_noisy"
    elif family_score >= 2 and strength in {"weak", "meaningful"} and expected_score <= 1:
        judgment = "family_noisy"
    elif multi_axis and strength in {"meaningful", "strong"}:
        judgment = "multi_axis_mixed"
    elif top_axis == expected_axis and strength in {"meaningful", "strong"} and format_score <= 1 and family_score <= 1:
        judgment = "mostly_axis_specific"
    elif top_axis == expected_axis and strength in {"meaningful", "strong"}:
        judgment = "single_corridor_plausible"
    else:
        judgment = "unclear"
    return match_type, strength, judgment


def group_match_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    by_axis: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        by_axis[str(row["expected_axis"])].append(row)
    results: list[dict[str, object]] = []
    for axis_name in AXIS_KEYWORDS:
        items = by_axis.get(axis_name, [])
        strengths = Counter(str(item["reentry_strength"]) for item in items)
        match_types = Counter(str(item["match_type"]) for item in items)
        judgments = Counter(str(item["decomposition_judgment"]) for item in items)
        results.append(
            {
                "axis_name": axis_name,
                "tested_count": len(items),
                "strong_count": strengths["strong"],
                "meaningful_count": strengths["meaningful"],
                "weak_count": strengths["weak"],
                "none_count": strengths["none"],
                "dominant_match_type": max(match_types, key=match_types.get) if match_types else "no_meaningful_match",
                "dominant_decomposition_judgment": max(judgments, key=judgments.get) if judgments else "unclear",
                "summary": f"{axis_name} mainly reads as {max(match_types, key=match_types.get) if match_types else 'no_meaningful_match'} / {max(judgments, key=judgments.get) if judgments else 'unclear'}",
            }
        )
    return results


def build_ledger(rows: list[dict[str, object]]) -> dict[str, object]:
    meaningful_rows = [row for row in rows if row["reentry_strength"] in {"meaningful", "strong"}]
    strongest_axis = "unclear"
    secondary_axes: list[str] = []
    current_reading = "unclear"
    format_noise_risk = "medium"
    family_noise_risk = "medium"
    keep_as_one = "unclear"

    if meaningful_rows:
        axis_counter = Counter(str(row["expected_axis"]) for row in meaningful_rows)
        strongest_axis = max(axis_counter, key=axis_counter.get)
        secondary_axes = [axis for axis, _count in axis_counter.items() if axis != strongest_axis]

    if any(row["decomposition_judgment"] == "multi_axis_mixed" for row in rows):
        current_reading = "multi_axis_business_mix"
        keep_as_one = "observer_only_split_recommended"
    elif strongest_axis == "business_leverage":
        current_reading = "business_leverage_dominant"
        keep_as_one = "observer_only_split_recommended"
    elif strongest_axis == "startup_thesis":
        current_reading = "startup_thesis_dominant"
        keep_as_one = "observer_only_split_recommended"
    elif strongest_axis == "monetization_value_capture":
        current_reading = "value_capture_dominant_but_noisy"
        keep_as_one = "observer_only_split_recommended"
    elif strongest_axis and strongest_axis != "unclear":
        current_reading = "single_business_corridor_with_noise"
        keep_as_one = "yes_for_now"

    format_noise_hits = sum(1 for row in rows if row["decomposition_judgment"] == "format_noisy")
    family_noise_hits = sum(1 for row in rows if row["decomposition_judgment"] == "family_noisy")
    if format_noise_hits >= 2:
        format_noise_risk = "high"
    elif format_noise_hits == 1:
        format_noise_risk = "medium"
    else:
        format_noise_risk = "low"
    if family_noise_hits >= 2:
        family_noise_risk = "high"
    elif family_noise_hits == 1:
        family_noise_risk = "medium"
    else:
        family_noise_risk = "low"

    return {
        "corridor_id": FOCUS_CORRIDOR,
        "strongest_axis": strongest_axis,
        "secondary_axes": secondary_axes,
        "format_noise_risk": format_noise_risk,
        "family_noise_risk": family_noise_risk,
        "current_reading": current_reading,
        "keep_as_one_corridor": keep_as_one,
        "observer_split_candidate": "yes" if keep_as_one == "observer_only_split_recommended" else "no",
        "promotion_readiness": "far_from_ready",
        "note": "business corridor decomposition improves observer clarity but still shows no stable closure and no promotion basis.",
    }


def build_readable_cards(rows: list[dict[str, object]]) -> str:
    lines = ["# business corridor readable cards", ""]
    for row in rows:
        lines.extend(
            [
                f"## {row['input_id']}",
                f"- expected_axis: `{row['expected_axis']}`",
                f"- actual_response: `{row['match_type']}` / `{row['reentry_strength']}` / `{row['decomposition_judgment']}`",
                f"- business_corridor_echo: `{row['arrival_axis_overlap']}` / top_axis=`{row['top_axis']}`",
                f"- specific_sub_axis: `{row['top_axis']}`",
                f"- format_family_noise: format=`{row['format_score']}` / family=`{row['family_score']}`",
                f"- why_clean_or_noisy: {row['note']}",
                f"- reread_point: {row['excerpt']}",
                "",
            ]
        )
    return "\n".join(lines) + "\n"


def build_noise_watch(rows: list[dict[str, object]], ledger: dict[str, object]) -> str:
    lines = ["# business corridor noise watch", ""]
    noise_rows = [
        row
        for row in rows
        if row["decomposition_judgment"] in {"format_noisy", "family_noisy", "multi_axis_mixed"}
        or row["match_type"] in {"format_resonance_only", "family_assisted_echo"}
    ]
    for row in noise_rows:
        lines.extend(
            [
                f"## {row['input_id']}",
                f"- expected_axis: `{row['expected_axis']}`",
                f"- observed_as: `{row['match_type']}` / `{row['decomposition_judgment']}`",
                f"- why_watch: {row['note']}",
                "",
            ]
        )
    lines.extend(
        [
            "## observer split candidate",
            f"- current_reading: `{ledger['current_reading']}`",
            f"- keep_as_one_corridor: `{ledger['keep_as_one_corridor']}`",
            f"- observer_split_candidate: `{ledger['observer_split_candidate']}`",
            "",
        ]
    )
    return "\n".join(lines) + "\n"


def build_control_board(ledger: dict[str, object], stage4_ledger: list[dict[str, object]], group_rows: list[dict[str, object]]) -> str:
    org_rows = [row for row in stage4_ledger if row["corridor_id"] in POSITIVE_CONTROLS]
    lines = [
        "# business vs org control board",
        "",
        "## 1. organization corridor를 positive control로 둔 이유",
        "- `technical->organization::ai_business`, `technical->organization::harness_agent` 는 stage4에서 `mostly_meaning_driven` 으로 읽혔다.",
        "",
        "## 2. organization corridor와 business corridor의 clean/noisy 차이",
    ]
    for row in org_rows:
        lines.append(
            f"- org control `{row['corridor_id']}`: `{row['current_reading']}` / format_noise=`{row['format_noise_risk']}` / family_bias=`{row['family_bias_risk']}`"
        )
    lines.extend(
        [
            f"- focus business `{ledger['corridor_id']}`: `{ledger['current_reading']}` / format_noise=`{ledger['format_noise_risk']}` / family_noise=`{ledger['family_noise_risk']}`",
            "",
            "## 3. business corridor 내부 axis 혼합 가능성",
            f"- strongest_axis: `{ledger['strongest_axis']}`",
            f"- secondary_axes: `{ledger['secondary_axes']}`",
            "",
            "## 4. current strongest business sub-axis 후보",
        ]
    )
    for row in group_rows:
        if row["strong_count"] or row["meaningful_count"]:
            lines.append(
                f"- `{row['axis_name']}`: strong=`{row['strong_count']}`, meaningful=`{row['meaningful_count']}` / dominant=`{row['dominant_decomposition_judgment']}`"
            )
    lines.extend(
        [
            "",
            "## 5. 아직 promotion이 아닌 이유",
            "- business corridor는 일부 clean sub-axis가 보여도 전체 corridor는 여전히 axis 혼합 + format/family noise를 함께 가진다.",
            "",
            "## 6. 다음 단계 추천",
            "- observer layer에서 `startup_thesis` 와 `org_business_boundary` 를 우선 split candidate로 더 관찰한다.",
        ]
    )
    return "\n".join(lines) + "\n"


def build_decision_note(ledger: dict[str, object], group_rows: list[dict[str, object]]) -> str:
    strongest = [row["axis_name"] for row in group_rows if row["strong_count"] > 0 or row["meaningful_count"] > 0]
    lines = [
        "# business corridor decision note",
        "",
        "## A. technical->business::ai_business 는 하나의 corridor로 유지 가능한가",
        f"- 현재 판독: `{ledger['keep_as_one_corridor']}`",
        "",
        "## B. observer layer에서 하위축 후보 분리가 필요한가",
        f"- `{ledger['observer_split_candidate']}`",
        "",
        "## C. noise의 주원인은 format/family인가 axis 혼합인가",
        f"- 현재는 `axis 혼합 + format/family noise의 혼합` 으로 읽는 것이 가장 정확하다. strongest_axis=`{ledger['strongest_axis']}` / secondary_axes=`{ledger['secondary_axes']}`",
        "",
        "## D. organization corridor 대비 business corridor가 왜 더 흐린가",
        "- organization corridor는 stage4에서 mostly_meaning_driven으로 유지됐지만, business corridor는 startup/value/org-boundary/software-value가 같은 family 아래 섞여 움직인다.",
        "",
        "## E. 왜 아직 promotion은 아닌가",
        "- sub-axis 분해가 observer clarity를 올려도 stable_closure_reached 는 여전히 없다.",
        "",
        "## strongest business sub-axis 후보",
        f"- `{strongest}`",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    stage4_ledger = load_json(STAGE4_LEDGER)

    registry_rows: list[dict[str, object]] = []
    match_rows: list[dict[str, object]] = []

    for entry in INPUT_REGISTRY:
        path = REPO_ROOT / str(entry["source_path"])
        units = parse_units(path, str(entry["kind"]))
        windows = build_windows(str(entry["input_id"]), units, int(entry["window_size"]), int(entry["overlap"]))
        classified = [classify_window(window, list(entry["preferred_terms"])) for window in windows]
        best = choose_best_window(classified, str(entry["expected_axis"]))
        match_type, strength, judgment = judge_match(str(entry["expected_axis"]), best)

        registry_rows.append(
            {
                "input_id": entry["input_id"],
                "source_path": entry["source_path"],
                "expected_axis": entry["expected_axis"],
                "format_family": entry["format_family"],
                "why_selected": entry["why_selected"],
                "expected_noise_risk": entry["expected_noise_risk"],
                "note": entry["note"],
            }
        )

        match_rows.append(
            {
                "corridor_id": FOCUS_CORRIDOR,
                "input_id": entry["input_id"],
                "expected_axis": entry["expected_axis"],
                "anchor_overlap": "ai_business_anchor" if best["axis_scores"]["monetization_value_capture"] or best["axis_scores"]["startup_thesis"] or best["axis_scores"]["business_leverage"] else "weak_business_anchor",
                "bridge_support": "yes" if best["transition_score"] > 0 else "partial",
                "arrival_axis_overlap": "same_arrival_axis" if best["top_axis"] == entry["expected_axis"] else ("adjacent_business_axis" if best["top_score"] > 0 else "missing_arrival_axis"),
                "match_type": match_type,
                "reentry_strength": strength,
                "decomposition_judgment": judgment,
                "top_axis": best["top_axis"],
                "top_score": best["top_score"],
                "second_axis": best["second_axis"],
                "second_score": best["second_score"],
                "tech_score": best["tech_score"],
                "transition_score": best["transition_score"],
                "format_score": best["format_score"],
                "family_score": best["family_score"],
                "note": f"best_window={best['window_id']}, top_axis={best['top_axis']}:{best['top_score']}, second_axis={best['second_axis']}:{best['second_score']}, tech={best['tech_score']}, transition={best['transition_score']}, format={best['format_score']}, family={best['family_score']}",
                "excerpt": best["excerpt"],
            }
        )

    group_rows = group_match_rows(match_rows)
    ledger = build_ledger(match_rows)

    (OUTPUT_ROOT / "business_axis_candidate_registry.json").write_text(
        json.dumps(registry_rows, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (OUTPUT_ROOT / "business_corridor_match_report.json").write_text(
        json.dumps(match_rows, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (OUTPUT_ROOT / "business_axis_group_comparison.json").write_text(
        json.dumps(group_rows, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (OUTPUT_ROOT / "business_corridor_decomposition_ledger.json").write_text(
        json.dumps(ledger, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (OUTPUT_ROOT / "business_corridor_readable_cards.md").write_text(build_readable_cards(match_rows), encoding="utf-8")
    (OUTPUT_ROOT / "business_corridor_noise_watch.md").write_text(build_noise_watch(match_rows, ledger), encoding="utf-8")
    (OUTPUT_ROOT / "business_vs_org_control_board.md").write_text(
        build_control_board(ledger, stage4_ledger, group_rows),
        encoding="utf-8",
    )
    (OUTPUT_ROOT / "business_corridor_decision_note.md").write_text(
        build_decision_note(ledger, group_rows),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
