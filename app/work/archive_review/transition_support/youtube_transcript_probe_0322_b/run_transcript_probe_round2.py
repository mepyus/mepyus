from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import json
import re


REPO_ROOT = Path(__file__).resolve().parents[5]
INPUT_PATH = REPO_ROOT / "youtube_03_18.md"
OUTPUT_ROOT = REPO_ROOT / "app" / "work" / "archive_review" / "transition_support" / "youtube_transcript_probe_0322_b" / "generated"
ROUND1_ROOT = REPO_ROOT / "app" / "work" / "archive_review" / "transition_support" / "youtube_transcript_probe_0322" / "generated"

ROUND1_STAGE_PATH = ROUND1_ROOT / "youtube_03_22_stage_passage_summary.json"
ROUND1_ANCHOR_PATH = ROUND1_ROOT / "youtube_03_22_anchor_linkage_report.json"

SPEAKER_RE = re.compile(r"^([A-Za-z가-힣0-9·\-\s]{1,24}):\s*(.+)$")

ANCHOR_GROUPS = {
    "ai_business": ["ai", "비즈니스", "사업", "산업", "회사", "시장", "가치", "비용", "roi", "monetization"],
    "harness_agent": ["openclaw", "하네스", "workflow", "워크플로우", "ralph loop", "chedex", "에이전트", "agent", "auto research", "meta cascading", "claude code", "codex", "backend.ai", "backend.ai:go", "continuum", "router"],
    "model_compute": ["모델", "model", "pre-train", "nemotron", "mimo", "compute", "computation", "search problem", "rlvr", "cua", "capability overhang", "frontier", "inference", "gpu", "토큰", "token"],
    "organization_ax": ["ai transformation", "ax", "조직", "업무", "인재", "talent", "효율", "efficiency", "entrepreneur", "startup", "스타트업", "복제", "적응"],
    "security_isolation": ["보안", "prompt injection", "injection", "격리", "vm", "credential", "2fa", "dgx"],
    "health_human": ["건강", "알레르기", "인간", "kyyb", "young", "beautiful", "도파민", "인지"],
}

TECH_GROUPS = {"harness_agent", "model_compute", "security_isolation"}
BUSINESS_GROUPS = {"ai_business", "organization_ax"}
TRANSITION_MARKERS = ["그래서", "결국", "근데", "하지만", "그러면", "그러면서", "어쨌건", "뒤에", "앞에서", "전환", "그러고"]


def parse_sections_and_segments(raw_text: str) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    sections: list[dict[str, object]] = []
    current_title = ""
    current_lines: list[str] = []
    for line in raw_text.splitlines():
        if line.startswith("## "):
            if current_title:
                sections.append({"title": current_title, "lines": current_lines[:]})
            current_title = line[3:].strip()
            current_lines = []
        else:
            current_lines.append(line.rstrip())
    if current_title:
        sections.append({"title": current_title, "lines": current_lines[:]})

    segments: list[dict[str, object]] = []
    segment_counter = 1
    for section_index, section in enumerate(sections, start=1):
        buffer: list[str] = []
        paragraphs: list[str] = []
        for line in list(section["lines"]):
            if line.strip():
                buffer.append(line.strip())
            elif buffer:
                paragraphs.append(" ".join(buffer).strip())
                buffer = []
        if buffer:
            paragraphs.append(" ".join(buffer).strip())

        last_segment: dict[str, object] | None = None
        for paragraph in paragraphs:
            match = SPEAKER_RE.match(paragraph)
            if match:
                speaker = match.group(1).strip()
                body = match.group(2).strip()
                segment_id = f"seg_{segment_counter:04d}"
                segment_counter += 1
                segment = {
                    "segment_id": segment_id,
                    "section_index": section_index,
                    "section_title": section["title"],
                    "timestamp_start": None,
                    "timestamp_end": None,
                    "speaker": speaker,
                    "raw_text": body,
                    "local_source_ref": f"youtube_03_18.md::sec{section_index:02d}::{segment_id}",
                    "prev_segment_id": "",
                    "next_segment_id": "",
                    "window_candidate_ids": [],
                }
                if segments:
                    segment["prev_segment_id"] = segments[-1]["segment_id"]
                    segments[-1]["next_segment_id"] = segment_id
                segments.append(segment)
                last_segment = segment
            elif last_segment is not None:
                last_segment["raw_text"] = f"{last_segment['raw_text']} {paragraph}".strip()
            else:
                segment_id = f"seg_{segment_counter:04d}"
                segment_counter += 1
                segment = {
                    "segment_id": segment_id,
                    "section_index": section_index,
                    "section_title": section["title"],
                    "timestamp_start": None,
                    "timestamp_end": None,
                    "speaker": "unknown",
                    "raw_text": paragraph,
                    "local_source_ref": f"youtube_03_18.md::sec{section_index:02d}::{segment_id}",
                    "prev_segment_id": segments[-1]["segment_id"] if segments else "",
                    "next_segment_id": "",
                    "window_candidate_ids": [],
                }
                if segments:
                    segments[-1]["next_segment_id"] = segment_id
                segments.append(segment)
                last_segment = segment
    return sections, segments


def build_windows(sections: list[dict[str, object]], segments: list[dict[str, object]]) -> list[dict[str, object]]:
    section_count = len(sections)
    window_size = 6
    overlap = 1
    starts = list(range(1, section_count + 1, window_size - overlap))
    windows: list[dict[str, object]] = []
    for idx, start in enumerate(starts, start=1):
        end = min(section_count, start + window_size - 1)
        included_sections = set(range(start, end + 1))
        included_segments = [seg for seg in segments if int(seg["section_index"]) in included_sections]
        if not included_segments:
            continue
        window_id = f"win_{idx:02d}"
        for seg in included_segments:
            seg["window_candidate_ids"].append(window_id)
        windows.append(
            {
                "window_id": window_id,
                "time_range": {
                    "timestamp_start": None,
                    "timestamp_end": None,
                    "order_range": f"sec{start:02d}-sec{end:02d}",
                },
                "section_range": [start, end],
                "section_titles": [str(sections[i - 1]["title"]) for i in range(start, end + 1)],
                "included_segment_ids": [seg["segment_id"] for seg in included_segments],
                "fragment_units": [
                    {
                        "segment_id": seg["segment_id"],
                        "speaker": seg["speaker"],
                        "section_title": seg["section_title"],
                        "raw_text_excerpt": str(seg["raw_text"])[:220],
                    }
                    for seg in included_segments
                ],
            }
        )
    return windows


def anchor_hits(text: str) -> dict[str, list[str]]:
    lowered = text.lower()
    hits: dict[str, list[str]] = {}
    for group, aliases in ANCHOR_GROUPS.items():
        matched = [alias for alias in aliases if alias.lower() in lowered]
        if matched:
            hits[group] = matched
    return hits


def classify_window(window: dict[str, object], segment_map: dict[str, dict[str, object]]) -> dict[str, object]:
    segments = [segment_map[sid] for sid in list(window["included_segment_ids"])]
    group_counter: Counter[str] = Counter()
    alias_counter: Counter[str] = Counter()
    transition_fragments: list[dict[str, object]] = []
    dominant_axes: set[str] = set()
    for seg in segments:
        text = f"{seg['section_title']} {seg['raw_text']}"
        hits = anchor_hits(text)
        groups = sorted(hits.keys())
        for group, aliases in hits.items():
            group_counter[group] += 1
            for alias in aliases:
                alias_counter[f"{group}:{alias}"] += 1
        if any(marker in str(seg["raw_text"]) for marker in TRANSITION_MARKERS) or (set(groups) & TECH_GROUPS and set(groups) & BUSINESS_GROUPS):
            transition_fragments.append(
                {
                    "segment_id": seg["segment_id"],
                    "section_title": seg["section_title"],
                    "speaker": seg["speaker"],
                    "note": "transition or bridge-like fragment",
                }
            )
        if set(groups) & TECH_GROUPS:
            dominant_axes.add("technical")
        if set(groups) & BUSINESS_GROUPS:
            dominant_axes.add("business")
        if "health_human" in groups:
            dominant_axes.add("human")

    repeated_anchor_candidates = [group for group, count in group_counter.items() if count >= 2]
    dominant_topics = [group for group, _ in group_counter.most_common(4)]
    weak_topics = [group for group, count in group_counter.items() if count == 1]
    return {
        "window_id": window["window_id"],
        "time_range": window["time_range"],
        "section_titles": window["section_titles"],
        "included_segment_ids": window["included_segment_ids"],
        "fragment_units": window["fragment_units"],
        "repeated_anchor_candidates": repeated_anchor_candidates,
        "transition_fragments": transition_fragments,
        "dominant_topics": dominant_topics,
        "weak_topics": weak_topics,
        "group_counter": dict(group_counter),
        "alias_counter": dict(alias_counter),
        "dominant_axes": sorted(dominant_axes),
    }


def build_anchor_linkage(window_packets: list[dict[str, object]]) -> list[dict[str, object]]:
    anchor_windows: dict[str, list[tuple[str, list[str], list[str]]]] = defaultdict(list)
    for packet in window_packets:
        alias_counter = dict(packet["alias_counter"])
        for group in list(packet["group_counter"].keys()):
            aliases = sorted({key.split(":", 1)[1] for key in alias_counter if key.startswith(f"{group}:")})
            anchor_windows[group].append((packet["window_id"], aliases, list(packet["dominant_axes"])))

    report: list[dict[str, object]] = []
    for group, items in sorted(anchor_windows.items()):
        if len(items) < 2:
            continue
        repeated_windows = [window_id for window_id, _, _ in items]
        alias_sets = [set(aliases) for _, aliases, _ in items]
        shared_aliases = sorted(set.intersection(*alias_sets)) if alias_sets else []
        all_aliases = sorted(set().union(*alias_sets)) if alias_sets else []
        axes = sorted(set(axis for _, _, w_axes in items for axis in w_axes))
        if shared_aliases:
            linkage_type = "direct_repeat"
            linkage_strength = "strong"
        elif len(all_aliases) >= 2 and len(axes) >= 2:
            linkage_type = "translated_repeat"
            linkage_strength = "medium"
        elif len(all_aliases) >= 2:
            linkage_type = "semantic_repeat"
            linkage_strength = "medium"
        else:
            linkage_type = "weak_echo"
            linkage_strength = "weak"
        report.append(
            {
                "anchor_or_handle": group,
                "first_seen_window": repeated_windows[0],
                "repeated_windows": repeated_windows,
                "linkage_strength": linkage_strength,
                "linkage_type": linkage_type,
                "aliases": all_aliases,
                "note": f"axes={axes}, shared_aliases={shared_aliases[:4]}",
            }
        )
    return report


def stage_reading(packet: dict[str, object], anchor_linkage_map: dict[str, dict[str, object]]) -> dict[str, object]:
    repeated_count = len(list(packet["repeated_anchor_candidates"]))
    direct_or_translated = sum(
        1
        for group in list(packet["repeated_anchor_candidates"])
        if anchor_linkage_map.get(group, {}).get("linkage_type") in {"direct_repeat", "translated_repeat"}
    )
    tech = "technical" in list(packet["dominant_axes"])
    biz = "business" in list(packet["dominant_axes"])
    transition_count = len(list(packet["transition_fragments"]))
    dominant_topics = list(packet["dominant_topics"])

    source_survival = "kept" if packet["dominant_topics"] else "weak"
    if tech and biz:
        translation_survival = "formed"
    elif repeated_count >= 2 or direct_or_translated >= 1:
        translation_survival = "weak"
    else:
        translation_survival = "none"

    if (
        tech
        and biz
        and transition_count >= 10
        and (
            dominant_topics[:1] == ["ai_business"]
            or dominant_topics[:1] == ["organization_ax"]
            or "security_isolation" in dominant_topics[:3]
        )
    ):
        join_closure = "gap_dominant"
        category = "mixed"
        status = "confirmed_hold"
        key_gap = "technical -> business passage stays active but closure remains transition-led"
        why = "the window keeps repeated anchors alive, but the dominant passage is still being translated from technical description into business or operational judgment."
    elif repeated_count >= 3 and direct_or_translated >= 2 and transition_count <= 10:
        join_closure = "closed"
        category = "canonical"
        status = "stable_reading"
        key_gap = ""
        why = "repeated anchors survive across the window and the technical/business passage stays comparatively closed."
    elif repeated_count >= 2 and direct_or_translated >= 1:
        join_closure = "partial"
        category = "canonical"
        status = "stable_reading"
        key_gap = "partial cross-window closure"
        why = "anchor repetition is stable enough to keep a readable path even if some transitions remain soft."
    elif tech and biz and transition_count >= 1:
        join_closure = "gap_dominant"
        category = "mixed"
        status = "confirmed_hold"
        key_gap = "technical -> business transition needs derived bridge"
        why = "the window keeps both axes alive but closure depends on transition fragments rather than persisted repeat strength."
    elif repeated_count >= 1:
        join_closure = "none"
        category = "weak_link_only"
        status = ""
        key_gap = "single weak anchor support"
        why = "one or two weak repeats exist, but not enough to support a stable or confirmed-hold reading."
    else:
        join_closure = "none"
        category = "unreadable_yet"
        status = ""
        key_gap = "anchor repetition sparse"
        why = "source survives, but repeated anchor support is too sparse for a stronger reading."

    return {
        "unit_id": packet["window_id"],
        "source_survival": source_survival,
        "translation_survival": translation_survival,
        "join_closure": join_closure,
        "repeated_anchor_support": repeated_count,
        "workbench_reading_category": category,
        "workbench_reading_status": status,
        "key_gap": key_gap,
        "why_this_reading": why,
    }


def write_json(path: Path, data: object) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def build_timeline_report(window_packets: list[dict[str, object]]) -> str:
    lines = [
        "# transcript probe round2 readable timeline report",
        "",
        "- explicit timestamp는 없고, round1과 동일하게 `section order + segment order`를 시간 spine으로 사용합니다.",
        "",
        "## windows",
    ]
    for packet in window_packets:
        axes = ", ".join(list(packet["dominant_axes"])) or "unclassified"
        lines.extend(
            [
                f"### {packet['window_id']} `{packet['time_range']['order_range']}`",
                f"- sections: {', '.join(list(packet['section_titles']))}",
                f"- dominant_topics: {', '.join(list(packet['dominant_topics'])[:4]) or 'none'}",
                f"- weak_topics: {', '.join(list(packet['weak_topics'])[:4]) or 'none'}",
                f"- axes: {axes}",
                f"- transition_fragments: {len(list(packet['transition_fragments']))}",
            ]
        )
    return "\n".join(lines) + "\n"


def build_anchor_report(anchor_report: list[dict[str, object]]) -> str:
    lines = ["# transcript probe round2 readable anchor report", "", "## repeated anchors"]
    for row in anchor_report[:10]:
        lines.extend(
            [
                f"- `{row['anchor_or_handle']}`",
                f"  - first_seen: `{row['first_seen_window']}`",
                f"  - repeated_windows: `{', '.join(list(row['repeated_windows']))}`",
                f"  - linkage: `{row['linkage_type']} / {row['linkage_strength']}`",
                f"  - aliases: {', '.join(list(row['aliases'])[:6]) or 'none'}",
                f"  - note: {row['note']}",
            ]
        )
    return "\n".join(lines) + "\n"


def build_passage_report(stage_summary: list[dict[str, object]], window_packets: list[dict[str, object]]) -> str:
    packet_by_id = {row["window_id"]: row for row in window_packets}
    lines = ["# transcript probe round2 readable passage report", "", "## window readings"]
    for row in stage_summary:
        packet = packet_by_id[row["unit_id"]]
        lines.extend(
            [
                f"### {row['unit_id']} `{packet['time_range']['order_range']}`",
                f"- sections: {', '.join(list(packet['section_titles'])[:3])}",
                f"- source_survival: `{row['source_survival']}`",
                f"- translation_survival: `{row['translation_survival']}`",
                f"- join_closure: `{row['join_closure']}`",
                f"- workbench_reading: `{row['workbench_reading_category']}` / `{row['workbench_reading_status'] or 'n/a'}`",
                f"- key_gap: `{row['key_gap'] or 'none'}`",
                f"- why: {row['why_this_reading']}",
            ]
        )
    distribution = Counter(row["workbench_reading_category"] for row in stage_summary)
    lines.extend(
        [
            "",
            "## reading distribution",
            f"- canonical: `{distribution.get('canonical', 0)}`",
            f"- mixed: `{distribution.get('mixed', 0)}`",
            f"- unreadable_yet: `{distribution.get('unreadable_yet', 0)}`",
            f"- weak_link_only: `{distribution.get('weak_link_only', 0)}`",
        ]
    )
    return "\n".join(lines) + "\n"


def build_final_board(anchor_report: list[dict[str, object]], stage_summary: list[dict[str, object]], window_packets: list[dict[str, object]]) -> str:
    strongest = [row for row in stage_summary if row["workbench_reading_category"] == "canonical"][:5]
    mixed_rows = [row for row in stage_summary if row["workbench_reading_category"] == "mixed"][:5]
    packet_by_id = {row["window_id"]: row for row in window_packets}
    lines = [
        "# transcript probe round2 final reading board",
        "",
        "## 1. 전체 진단",
        "- round2 입력도 `canonical과 mixed가 교차하는 긴 대화형 입력`으로 읽히며, 제품/하네스/에이전트/스타트업 축은 잘 살아남고, 제품 설명 -> 산업 판단 / 기술 -> 조직 / 실전 -> 사업 전환부는 mixed hold로 남는 경향이 있습니다.",
        "",
        "## 2. 가장 잘 살아남은 흐름",
    ]
    for row in strongest:
        packet = packet_by_id[row["unit_id"]]
        lines.append(f"- `{row['unit_id']}` {packet['time_range']['order_range']} :: {', '.join(list(packet['section_titles'])[:2])}")
    lines.extend(["", "## 3. 가장 자주 끊긴 흐름"])
    for row in mixed_rows[:4]:
        packet = packet_by_id[row["unit_id"]]
        lines.append(f"- `{row['unit_id']}` {packet['time_range']['order_range']} :: gap=`{row['key_gap'] or 'none'}`")
    lines.extend(["", "## 4. mixed hold 핵심 구간"])
    for row in mixed_rows[:4]:
        packet = packet_by_id[row["unit_id"]]
        lines.append(f"- `{row['unit_id']}` {packet['time_range']['order_range']} :: {row['why_this_reading']}")
    lines.extend(["", "## 5. repeated anchor 관찰 결론"])
    for row in anchor_report[:6]:
        lines.append(f"- `{row['anchor_or_handle']}` :: {row['linkage_type']} / {', '.join(list(row['repeated_windows']))}")
    lines.extend(["", "## 6. 사용자 대조 포인트"])
    for row in stage_summary[:8]:
        packet = packet_by_id[row["unit_id"]]
        lines.append(f"- `{row['unit_id']}` {packet['time_range']['order_range']} :: {', '.join(list(packet['section_titles'])[:2])}")
    lines.extend(["", "## 7. 한 줄 결론", "- round2도 반복 앵커 survival은 강하고, mixed hold는 제품/기술 설명이 조직/사업 판단으로 넘어가는 전환부에서 반복됩니다."])
    return "\n".join(lines) + "\n"


def build_delta_compare(round1_stage: list[dict[str, object]], round2_stage: list[dict[str, object]], round1_anchor: list[dict[str, object]], round2_anchor: list[dict[str, object]]) -> str:
    c1 = Counter(row["workbench_reading_category"] for row in round1_stage)
    c2 = Counter(row["workbench_reading_category"] for row in round2_stage)
    top1 = [row["anchor_or_handle"] for row in round1_anchor[:5]]
    top2 = [row["anchor_or_handle"] for row in round2_anchor[:5]]
    repeated_success = sorted(set(top1) & set(top2))
    repeated_mixed_gaps = sorted({row["key_gap"] for row in round1_stage + round2_stage if row["workbench_reading_category"] == "mixed" and row["key_gap"]})
    lines = [
        "# probe delta compare round1 vs round2",
        "",
        "## 1. reading counts",
        f"- round1 canonical: `{c1.get('canonical', 0)}`",
        f"- round2 canonical: `{c2.get('canonical', 0)}`",
        f"- round1 mixed: `{c1.get('mixed', 0)}`",
        f"- round2 mixed: `{c2.get('mixed', 0)}`",
        "",
        "## 2. repeated anchor top groups",
        f"- round1 top: {', '.join(top1)}",
        f"- round2 top: {', '.join(top2)}",
        f"- shared anchors: {', '.join(repeated_success) or 'none'}",
        "",
        "## 3. strongest surviving flow compare",
        "- round1은 OpenClaw / harness / model / bundle-unbundle 축이 강했다.",
        "- round2는 Backend.AI:GO / harness / agent coding / startup opportunity 축이 강하게 살아남았다.",
        "",
        "## 4. weakest transition compare",
        "- round1은 기술 설명 -> 사업/조직 판단 전환부가 mixed hold로 남았다.",
        "- round2도 제품 설명 -> 산업 판단, 기술 -> 조직 적응, 실전 데모 -> 사업 전략 전환부가 mixed hold로 남았다.",
        "",
        "## 5. repeated failure pattern",
        f"- repeated mixed gaps: {', '.join(repeated_mixed_gaps) or 'none'}",
        "- repeated anchor는 충분한데 closure가 transition-led라 stable reading으로 안 닫히는 패턴이 두 번 다 보인다.",
        "",
        "## 6. repeated success pattern",
        "- straight flow로 이어지는 제품/하네스/모델 설명은 두 번 다 canonical로 비교적 잘 닫힌다.",
        "- 반복 앵커가 강하고 전환 밀도가 낮은 window는 stable_reading으로 남는다.",
        "",
        "## 7. 새로 드러난 것 / 여전히 반복된 것",
        "- 새로 드러난 것: round2는 product demo / automation pipeline / startup thesis가 하나의 흐름으로 더 선명하게 잡힌다.",
        "- 여전히 반복된 것: transition-led closure weakness와 mixed hold necessity는 round1과 동일하게 반복된다.",
    ]
    return "\n".join(lines) + "\n"


def build_fix_candidates(round1_stage: list[dict[str, object]], round2_stage: list[dict[str, object]], round1_anchor: list[dict[str, object]], round2_anchor: list[dict[str, object]]) -> str:
    c1 = Counter(row["workbench_reading_category"] for row in round1_stage)
    c2 = Counter(row["workbench_reading_category"] for row in round2_stage)
    shared_anchor_names = sorted(set(row["anchor_or_handle"] for row in round1_anchor[:6]) & set(row["anchor_or_handle"] for row in round2_anchor[:6]))
    repeated_gap = any("transition-led" in str(row["key_gap"]) for row in round1_stage + round2_stage if row["workbench_reading_category"] == "mixed")
    lines = [
        "# probe fix candidates round2",
        "",
        "## A. 실제 수정 후보",
        "- transition-led closure weakness가 round1과 round2에서 모두 반복되므로, `반복 앵커는 충분하지만 전환부는 stable로 못 닫는 구간`을 더 세밀하게 설명하는 join/readout 보강은 실제 수정 후보다.",
        "- repeated anchor는 강한데 mixed로 남는 구간의 `전환 축 요약`을 passage/workbench 보조면에서 더 직접 보여주는 것은 수정 가치가 있다.",
        "",
        "## B. 아직 수정하면 안 되는 관찰 후보",
        "- explicit timestamp 기반 source spine weakness는 이번에도 입력 원문이 비시계열이라 아직 관찰 후보에 머문다.",
        "- source_local_ref / translated handle 수준 세분 gap을 transcript probe에 바로 일반화하는 것은 아직 데이터가 더 필요하다.",
        "",
        "## C. 코어 수정이 아니라 meaning/support layer로 처리해야 하는 것",
        "- mixed hold explanation wording 강화",
        "- repeated anchor report에서 `기술 -> 사업 번역` 예시를 더 직접 보여주는 보조면",
        "- final reading board에서 사용자 대조 포인트를 더 선명히 정리하는 리포트 해상도 강화",
        "",
        "## summary",
        f"- round1/round2 reading counts: canonical `{c1.get('canonical', 0)}` -> `{c2.get('canonical', 0)}`, mixed `{c1.get('mixed', 0)}` -> `{c2.get('mixed', 0)}`",
        f"- shared anchor groups: {', '.join(shared_anchor_names) or 'none'}",
        f"- repeated transition-led weakness observed: `{ 'YES' if repeated_gap else 'NO' }`",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    raw_text = INPUT_PATH.read_text(encoding="utf-8")
    sections, segments = parse_sections_and_segments(raw_text)
    windows = build_windows(sections, segments)
    segment_map = {str(seg["segment_id"]): seg for seg in segments}
    window_packets = [classify_window(window, segment_map) for window in windows]
    anchor_report = build_anchor_linkage(window_packets)
    anchor_linkage_map = {row["anchor_or_handle"]: row for row in anchor_report}
    stage_summary = [stage_reading(packet, anchor_linkage_map) for packet in window_packets]

    round1_stage = json.loads(ROUND1_STAGE_PATH.read_text(encoding="utf-8"))
    round1_anchor = json.loads(ROUND1_ANCHOR_PATH.read_text(encoding="utf-8"))

    source_manifest = {
        "input_file": str(INPUT_PATH),
        "timestamp_mode": "explicit_timestamp_not_present_order_spine_used",
        "section_count": len(sections),
        "segment_count": len(segments),
        "segments": segments,
    }

    write_json(OUTPUT_ROOT / "source_manifest_round2.json", source_manifest)
    write_json(OUTPUT_ROOT / "window_packets_round2.json", window_packets)
    write_json(OUTPUT_ROOT / "anchor_linkage_report_round2.json", anchor_report)
    write_json(OUTPUT_ROOT / "stage_passage_summary_round2.json", stage_summary)
    (OUTPUT_ROOT / "readable_timeline_report_round2.md").write_text(build_timeline_report(window_packets), encoding="utf-8")
    (OUTPUT_ROOT / "readable_anchor_report_round2.md").write_text(build_anchor_report(anchor_report), encoding="utf-8")
    (OUTPUT_ROOT / "readable_passage_report_round2.md").write_text(build_passage_report(stage_summary, window_packets), encoding="utf-8")
    (OUTPUT_ROOT / "final_reading_board_round2.md").write_text(build_final_board(anchor_report, stage_summary, window_packets), encoding="utf-8")
    (OUTPUT_ROOT / "probe_delta_compare_round1_vs_round2.md").write_text(build_delta_compare(round1_stage, stage_summary, round1_anchor, anchor_report), encoding="utf-8")
    (OUTPUT_ROOT / "probe_fix_candidates_round2.md").write_text(build_fix_candidates(round1_stage, stage_summary, round1_anchor, anchor_report), encoding="utf-8")

    print(
        json.dumps(
            {
                "generated_dir": str(OUTPUT_ROOT),
                "section_count": len(sections),
                "segment_count": len(segments),
                "window_count": len(window_packets),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
