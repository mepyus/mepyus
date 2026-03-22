from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Dict, List, Sequence
import re

from app.runtime.inputter import DustInput


CODE_SYMBOL_RE = re.compile(r"\b(?:def|class)\s+([A-Za-z_][A-Za-z0-9_]*)")
FILE_RE = re.compile(r"([A-Za-z0-9_./-]+\.[A-Za-z0-9_]+)")
ERROR_RE = re.compile(r"\b([A-Za-z_]*Error|Exception|failed|failure|crash|panic|timeout)\b", re.IGNORECASE)
TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9_+-]{2,}|[가-힣]{2,}")
RUN_ID_RE = re.compile(r"\b(?:run|session|task|runtime)[-_]?[A-Za-z0-9]+\b", re.IGNORECASE)

KNOWN_TOOLS = {"claudecode", "codex", "chatgpt", "cursor", "pytest", "python", "bash"}
SCENE_SPEC_HINTS = ("설명", "요구", "의도", "목적", "사용법", "spec", "design")
SCENE_IMPL_HINTS = ("def ", "class ", "return ", "import ", "함수", "메서드", "구현", "로직")
SCENE_EVIDENCE_HINTS = ("로그", "출력", "결과", "traceback", "stderr", "stdout", "error", "failed")
SCENE_REVIEW_HINTS = ("비교", "회고", "판단", "철학", "전략", "생각", "느낌", "review")

FLOW_RUN_HINTS = ("실행", "run", "사용", "호출", "적용")
FLOW_BREAK_HINTS = ("실패", "에러", "깨졌", "충돌", "막힘", "break", "failed", "error")
FLOW_FIX_HINTS = ("수정", "보정", "복구", "완화", "fix", "patch")
FLOW_COMPARE_HINTS = (
    "비교",
    "전환",
    "대비",
    "해석",
    "브릿지",
    "관찰",
    "검토",
    "판단",
    "확인",
    "observe",
    "review",
    "check",
    "whether",
    "contrast",
    "compare",
)

I_HIGH_HINTS = ("중요", "핵심", "반드시", "강", "문제", "위험", "critical", "fail", "error")
I_LOW_HINTS = ("참고", "보조", "약한", "조용", "부수", "note")
S_HIGH_HINTS = ("기준", "반복", "유지", "계속", "재등장", "숙성", "stable")
S_LOW_HINTS = ("임시", "잠깐", "일회성", "휘발", "즉시", "once")

STOP_DOMAIN_TERMS = {
    "그리고",
    "하지만",
    "그러나",
    "현재",
    "이제",
    "정도",
    "구조",
    "공간",
    "입력",
    "연결",
    "먼지",
    "한다",
    "했다",
    "있다",
    "없는",
    "from",
    "return",
    "note",
    "memo",
    "bundle",
    "artifact",
    "enters",
    "아니라",
}


@dataclass(frozen=True)
class TypedAnchor:
    type: str
    value: str


@dataclass(frozen=True)
class LabeledDust:
    dust_id: str
    origin_id: str
    source_type: str
    source_ref: str
    text: str
    source_path: str
    source_span: Dict[str, int]
    siblings: Sequence[str]
    created_at: str
    D: float
    I: float
    S: float
    scene: str
    flow: str
    anchors: Sequence[TypedAnchor]
    time_in: str
    last_seen: str
    recurrence_count: int
    short_label: str
    color: str
    radius: float

    def to_record(self) -> Dict[str, object]:
        record = asdict(self)
        record["anchors"] = [asdict(anchor) for anchor in self.anchors]
        record["siblings"] = list(self.siblings)
        return record


def label_dust_inputs(dust_inputs: Sequence[DustInput]) -> List[LabeledDust]:
    return [label_dust_input(dust_input) for dust_input in dust_inputs]


def label_dust_input(dust_input: DustInput) -> LabeledDust:
    scene = _infer_scene(dust_input.source_type, dust_input.text)
    flow = _infer_flow(dust_input.source_type, scene, dust_input.text)
    direction_value = _infer_direction(dust_input.text)
    intensity_value = _infer_intensity(dust_input.text)
    stability_value = _infer_stability(dust_input.text)
    anchors = tuple(_extract_typed_anchors(dust_input.text, dust_input.source_path))
    short_label = _short_label(dust_input.text)
    return LabeledDust(
        dust_id=dust_input.dust_id,
        origin_id=dust_input.origin_id,
        source_type=dust_input.source_type,
        source_ref=dust_input.source_ref or "",
        text=dust_input.text,
        source_path=dust_input.source_path or "",
        source_span=dust_input.source_span,
        siblings=tuple(dust_input.siblings),
        created_at=dust_input.created_at,
        D=direction_value,
        I=intensity_value,
        S=stability_value,
        scene=scene,
        flow=flow,
        anchors=anchors,
        time_in=dust_input.created_at,
        last_seen=dust_input.created_at,
        recurrence_count=1,
        short_label=short_label,
        color=_node_color(scene),
        radius=_node_radius(intensity_value, stability_value),
    )


def _infer_scene(source_type: str, text: str) -> str:
    lowered = text.lower()
    if source_type == "code" or any(hint in lowered for hint in SCENE_IMPL_HINTS):
        return "impl"
    if source_type == "log" or any(hint in lowered for hint in SCENE_EVIDENCE_HINTS):
        return "evidence"
    if source_type == "text" and any(hint in lowered for hint in SCENE_SPEC_HINTS):
        return "spec"
    if source_type == "text" and any(hint in lowered for hint in SCENE_REVIEW_HINTS):
        return "review"
    if source_type == "bullet":
        return "review"
    return {"code": "impl", "log": "evidence", "text": "review", "bullet": "review"}.get(source_type, "unknown")


def _infer_flow(source_type: str, scene: str, text: str) -> str:
    lowered = text.lower()
    if any(hint in lowered for hint in FLOW_BREAK_HINTS):
        return "break"
    if any(hint in lowered for hint in FLOW_FIX_HINTS):
        return "fix"
    if any(hint in lowered for hint in FLOW_COMPARE_HINTS):
        return "compare"
    if any(hint in lowered for hint in FLOW_RUN_HINTS):
        return "run"
    if scene == "evidence" or source_type == "log":
        return "run"
    if scene in {"review", "spec"} and source_type in {"text", "bullet"}:
        return "compare"
    if scene == "impl" or source_type == "code":
        return "run"
    return "unknown"


def _infer_direction(text: str) -> float:
    lowered = text.lower()
    if any(hint in lowered for hint in ("반대", "충돌", "긴장", "문제", "위험", "break", "error")):
        return 0.20
    if any(hint in lowered for hint in ("수정", "복구", "비교", "전환", "fix", "compare")):
        return 0.65
    if any(hint in lowered for hint in ("구현", "실행", "설명", "run", "spec")):
        return 0.80
    return 0.50


def _infer_intensity(text: str) -> float:
    lowered = text.lower()
    if any(hint in lowered for hint in I_HIGH_HINTS):
        return 0.80
    if any(hint in lowered for hint in I_LOW_HINTS):
        return 0.30
    return 0.50


def _infer_stability(text: str) -> float:
    lowered = text.lower()
    if any(hint in lowered for hint in S_HIGH_HINTS):
        return 0.80
    if any(hint in lowered for hint in S_LOW_HINTS):
        return 0.25
    return 0.50


def _extract_typed_anchors(text: str, source_path: str) -> List[TypedAnchor]:
    anchors: List[TypedAnchor] = []
    seen = set()

    def add(anchor_type: str, value: str) -> None:
        normalized = value.strip()
        if not normalized:
            return
        key = (anchor_type, normalized)
        if key in seen:
            return
        seen.add(key)
        anchors.append(TypedAnchor(type=anchor_type, value=normalized))

    lowered_tokens = [token.lower() for token in TOKEN_RE.findall(text)]
    for token in lowered_tokens:
        if token in KNOWN_TOOLS:
            add("tool", token if token != "claudecode" else "ClaudeCode")
    for symbol in CODE_SYMBOL_RE.findall(text):
        add("code_symbol", symbol)
    for file_name in FILE_RE.findall(text):
        add("file", file_name)
    for error in ERROR_RE.findall(text):
        add("error", error)
    for run_id in RUN_ID_RE.findall(text):
        add("project", run_id)
    for token in TOKEN_RE.findall(text):
        lowered = token.lower()
        if lowered in KNOWN_TOOLS or lowered in STOP_DOMAIN_TERMS:
            continue
        if len(token) < 3:
            continue
        add("domain_term", token)
        if len(anchors) >= 8:
            break
    return anchors[:8]


def _short_label(text: str) -> str:
    compact = " ".join(text.split())
    return compact[:18] + ("…" if len(compact) > 18 else "")


def _node_color(scene: str) -> str:
    return {
        "spec": "#c08457",
        "impl": "#2563eb",
        "evidence": "#047857",
        "review": "#7c3aed",
        "unknown": "#64748b",
    }.get(scene, "#8b5e34")


def _node_radius(intensity: float, stability: float) -> float:
    return round(8 + (intensity * 8) + (stability * 4), 1)
