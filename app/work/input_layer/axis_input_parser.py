from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List
import re


LABELLED_BLOCK_RE = re.compile(r"^(?P<label>[A-Za-z_]+|[가-힣A-Za-z_ ]+):\s*$")
TIME_HINTS = ("현재", "이전", "이후", "다시", "돌아", "재", "지속", "오랫동안", "빠르게", "곧")
INTENSITY_HIGH_HINTS = ("강", "과장", "증폭", "응축", "압력", "위험", "충돌", "흔들")
INTENSITY_LOW_HINTS = ("quiet", "조용", "유지", "완만", "약한")
STABILITY_HIGH_HINTS = ("유지", "버틴", "안정", "지속", "숙성")
STABILITY_LOW_HINTS = ("흔들", "불안정", "붕괴", "사라", "변화")


@dataclass(frozen=True)
class AxisObservation:
    direction: str
    intensity: str
    stability: str
    time: str


@dataclass(frozen=True)
class MaterialDraft:
    draft_id: str
    source_text: str
    block_label: str
    axes: AxisObservation
    connectivity_keys: List[str]


def parse_axis_material_drafts(text: str) -> List[MaterialDraft]:
    normalized = _normalize_text(text)
    if not normalized:
        return []

    blocks = _expand_blocks(_split_blocks(normalized))
    drafts: List[MaterialDraft] = []
    for index, block in enumerate(blocks, start=1):
        source_text = block["text"].strip()
        if not source_text:
            continue
        axes = AxisObservation(
            direction=_infer_direction(block["label"], source_text),
            intensity=_infer_intensity(source_text),
            stability=_infer_stability(source_text),
            time=_infer_time(source_text),
        )
        drafts.append(
            MaterialDraft(
                draft_id="draft_%03d" % index,
                source_text=source_text,
                block_label=block["label"],
                axes=axes,
                connectivity_keys=_connectivity_keys(block["label"], source_text, axes),
            )
        )
    return drafts


def _normalize_text(text: str) -> str:
    lines = [line.rstrip() for line in text.replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    return "\n".join(lines).strip()


def _split_blocks(text: str) -> List[Dict[str, str]]:
    lines = text.split("\n")
    blocks: List[Dict[str, str]] = []
    current_label = "plain"
    current_lines: List[str] = []

    def flush() -> None:
        nonlocal current_lines, current_label
        body = "\n".join(line for line in current_lines if line.strip()).strip()
        if body:
            blocks.append({"label": current_label, "text": body})
        current_lines = []

    for raw_line in lines:
        line = raw_line.strip()
        label_match = LABELLED_BLOCK_RE.match(line)
        if not line:
            flush()
            continue
        if label_match:
            flush()
            current_label = _normalize_label(label_match.group("label"))
            continue
        current_lines.append(raw_line)

    flush()
    return blocks or [{"label": "plain", "text": text}]


def _expand_blocks(blocks: List[Dict[str, str]]) -> List[Dict[str, str]]:
    expanded: List[Dict[str, str]] = []
    for block in blocks:
        expanded.extend(_split_inline_units(block))
    return expanded


def _split_inline_units(block: Dict[str, str]) -> List[Dict[str, str]]:
    text = block["text"].strip()
    if not text:
        return []

    if block["label"] != "plain":
        units = _segment_conditional_flow(text)
        if len(units) <= 1:
            return [block]
        return [{"label": unit["label"], "text": unit["text"]} for unit in units]

    expanded_units: List[Dict[str, str]] = []
    for sentence in _split_sentence_candidates(text):
        expanded_units.extend(_segment_conditional_flow(sentence))

    return _merge_axis_continuous_units(expanded_units)


def _segment_conditional_flow(text: str) -> List[Dict[str, str]]:
    normalized = " ".join(text.split())
    condition_markers = ("않으면", "없으면", "못하면", "경우", "라면")
    marker = next((candidate for candidate in condition_markers if candidate in normalized), None)
    if marker is None:
        return [{"label": "plain", "text": text}]

    split_at = normalized.find(marker) + len(marker)
    left = normalized[:split_at].strip(" ,")
    right = normalized[split_at:].strip(" ,")
    if not left or not right:
        return [{"label": "plain", "text": text}]

    units: List[Dict[str, str]] = [{"label": "condition", "text": left}]

    if "바탕" in left or "기반" in left:
        basis_text = _extract_basis_text(left)
        if basis_text:
            units.append({"label": "basis", "text": basis_text})

    tail_label = "risk" if any(hint in right for hint in ("가능성", "위험", "흔들", "붕괴")) else "result"
    units.append({"label": tail_label, "text": right})
    return units


def _split_sentence_candidates(text: str) -> List[str]:
    normalized = re.sub(r"\s+", " ", text.strip())
    if not normalized:
        return []

    parts = re.split(r"(?<=[.!?])\s+|(?<=다\.)\s+|(?<=요\.)\s+|(?<=까\?)\s+|(?<=죠\?)\s+", normalized)
    candidates = [part.strip(" ,") for part in parts if part.strip(" ,")]
    return candidates or [normalized]


def _merge_axis_continuous_units(units: List[Dict[str, str]]) -> List[Dict[str, str]]:
    if not units:
        return []

    merged: List[Dict[str, str]] = []
    for unit in units:
        label = unit.get("label", "plain")
        text = unit.get("text", "").strip()
        if not text:
            continue
        if not merged:
            merged.append({"label": label, "text": text})
            continue

        current_axes = _axis_signature(label, text)
        previous = merged[-1]
        previous_axes = _axis_signature(previous["label"], previous["text"])
        if current_axes == previous_axes and label == previous["label"]:
            previous["text"] = previous["text"] + " " + text
            continue
        merged.append({"label": label, "text": text})
    return merged


def _axis_signature(label: str, text: str) -> tuple:
    return (
        _infer_direction(label, text),
        _infer_intensity(text),
        _infer_stability(text),
        _infer_time(text),
    )


def _extract_basis_text(text: str) -> str:
    source = text.strip(" ,")
    topic_match = re.match(r"^(?P<head>.+?[은는])\s+(?P<body>.+)$", source)
    if topic_match:
        source = topic_match.group("body").strip()

    for marker in ("바탕이", "기반이", "바탕", "기반"):
        if marker in source:
            end = source.find(marker) + len(marker)
            candidate = source[:end].strip(" ,")
            if candidate and candidate != text.strip(" ,"):
                return candidate
    return ""


def _normalize_label(label: str) -> str:
    compact = " ".join(label.split()).strip().lower()
    return compact or "plain"


def _infer_direction(label: str, text: str) -> str:
    lowered = text.lower()
    if label in {"문제", "problem", "risk", "위험"}:
        return "divergent_tension"
    if label in {"대응", "response", "action"}:
        return "corrective_flow"
    if label in {"condition", "basis"}:
        return "structural_grounding"
    if label in {"result", "conclusion"}:
        return "forward_resolution"
    if "비교" in lowered or "분리" in lowered:
        return "comparative_split"
    if "유지" in lowered or "버틴" in lowered:
        return "quiet_holding"
    return "descriptive_forward"


def _infer_intensity(text: str) -> str:
    high = sum(1 for hint in INTENSITY_HIGH_HINTS if hint in text)
    low = sum(1 for hint in INTENSITY_LOW_HINTS if hint in text.lower() or hint in text)
    if high >= 2:
        return "high"
    if low >= 1 and high == 0:
        return "low"
    return "medium"


def _infer_stability(text: str) -> str:
    high = sum(1 for hint in STABILITY_HIGH_HINTS if hint in text)
    low = sum(1 for hint in STABILITY_LOW_HINTS if hint in text)
    if high > low:
        return "stable"
    if low > high:
        return "unstable"
    return "transitional"


def _infer_time(text: str) -> str:
    hits = [hint for hint in TIME_HINTS if hint in text]
    if not hits:
        return "unspecified"
    if any(hint in text for hint in ("다시", "돌아", "재등장", "재진입")):
        return "reentry"
    if any(hint in text for hint in ("오랫동안", "지속", "유지")):
        return "durational"
    if any(hint in text for hint in ("빠르게", "곧")):
        return "rapid"
    return "marked"


def _connectivity_keys(label: str, text: str, axes: AxisObservation) -> List[str]:
    keys = {
        label,
        axes.direction,
        axes.intensity,
        axes.stability,
        axes.time,
    }
    if "ai" in text.lower():
        keys.add("topic_ai")
    if "구조" in text:
        keys.add("structure")
    if "변화" in text:
        keys.add("change")
    if "위험" in text or "가능성" in text:
        keys.add("risk_signal")
    return sorted(key for key in keys if key and key != "plain")
