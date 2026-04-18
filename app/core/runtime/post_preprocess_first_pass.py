from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List
from uuid import uuid4

from app.core.runtime.external_transcript_preprocess import preprocess_transcript_file
from app.core.runtime.inputter import build_dust_inputs_from_source
from app.core.runtime.labeler import label_dust_inputs


@dataclass(frozen=True)
class FirstPassProbeResult:
    input_path: str
    preprocessed_path: str
    generated_at: str
    first_pass_read: Dict[str, object]


def build_post_preprocess_first_pass(input_path: Path, *, preprocessed_path: Path) -> FirstPassProbeResult:
    created_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    raw_text = preprocessed_path.read_text(encoding="utf-8").strip()
    source_id = f"src_{uuid4().hex[:12]}"
    source_ref = str(preprocessed_path).replace("\\", "/")
    dust_inputs = build_dust_inputs_from_source(
        source_id=source_id,
        source_type="text",
        source_ref=source_ref,
        raw_payload=raw_text,
        created_at=created_at,
    )
    labeled = label_dust_inputs(dust_inputs)

    scene_counter: Counter[str] = Counter(row.scene for row in labeled)
    flow_counter: Counter[str] = Counter(row.flow for row in labeled)
    sample_rows = [
        {
            "short_label": row.short_label,
            "scene": row.scene,
            "flow": row.flow,
            "preview": row.text[:220] + ("..." if len(row.text) > 220 else ""),
        }
        for row in labeled[:8]
    ]

    dominant_scene, dominant_scene_count = scene_counter.most_common(1)[0] if scene_counter else ("unknown", 0)
    dominant_flow, dominant_flow_count = flow_counter.most_common(1)[0] if flow_counter else ("unknown", 0)
    count = max(1, len(labeled))

    first_pass_read = {
        "dust_count": len(labeled),
        "top_scene_counts": dict(scene_counter.most_common(5)),
        "top_flow_counts": dict(flow_counter.most_common(5)),
        "scene_flatness_ratio": round(dominant_scene_count / count, 3),
        "flow_flatness_ratio": round(dominant_flow_count / count, 3),
        "sample_rows": sample_rows,
        "human_read_summary": _human_read_summary(
            dust_count=len(labeled),
            scene_flatness_ratio=round(dominant_scene_count / count, 3),
            flow_flatness_ratio=round(dominant_flow_count / count, 3),
            sample_rows=sample_rows,
        ),
        "caution_notes": _caution_notes(
            scene_flatness_ratio=round(dominant_scene_count / count, 3),
            flow_flatness_ratio=round(dominant_flow_count / count, 3),
        ),
        "next_read": _next_read(
            scene_flatness_ratio=round(dominant_scene_count / count, 3),
            flow_flatness_ratio=round(dominant_flow_count / count, 3),
        ),
    }
    return FirstPassProbeResult(
        input_path=str(input_path).replace("\\", "/"),
        preprocessed_path=str(preprocessed_path).replace("\\", "/"),
        generated_at=created_at,
        first_pass_read=first_pass_read,
    )


def preprocess_and_probe_first_pass(input_path: Path, *, output_path: Path) -> FirstPassProbeResult:
    preprocess = preprocess_transcript_file(input_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(preprocess.normalized_text, encoding="utf-8")
    return build_post_preprocess_first_pass(input_path, preprocessed_path=output_path)


def _human_read_summary(
    *,
    dust_count: int,
    scene_flatness_ratio: float,
    flow_flatness_ratio: float,
    sample_rows: List[Dict[str, object]],
) -> str:
    if dust_count == 0:
        return "전처리 후에도 읽을 chunk가 거의 남지 않아 first pass를 말하기 어렵다."
    if scene_flatness_ratio >= 0.9 and flow_flatness_ratio >= 0.9:
        return "전처리 후에도 first pass가 거의 한 가지 review/compare 질감으로 눌려 있어 읽기 면이 아직 평평하다."
    if flow_flatness_ratio >= 0.8:
        return "전처리로 shard 압력은 줄었지만, first pass는 아직 compare 쪽으로 많이 눌린다."
    first_preview = str(sample_rows[0]["preview"]) if sample_rows else "sample 없음"
    return f"전처리 후에는 일부 chunk가 문맥을 더 길게 담기 시작했고, first pass sample도 '{first_preview[:40]}...'처럼 읽힌다."


def _caution_notes(*, scene_flatness_ratio: float, flow_flatness_ratio: float) -> List[str]:
    notes: List[str] = []
    if flow_flatness_ratio >= 0.8:
        notes.append("flow flatness가 아직 높아 compare/read review 쪽으로 다시 눌릴 수 있다.")
    if scene_flatness_ratio >= 0.9:
        notes.append("scene flatness가 높아 case-specific reading으로 바로 올리면 과장될 수 있다.")
    if not notes:
        notes.append("first pass가 조금 나아졌더라도 promotion-ready나 line-ready로 곧바로 읽으면 안 된다.")
    return notes


def _next_read(*, scene_flatness_ratio: float, flow_flatness_ratio: float) -> str:
    if flow_flatness_ratio >= 0.8 or scene_flatness_ratio >= 0.9:
        return "전처리된 sidecar를 기준으로 bounded first-pass report를 만들되, 아직 line corroboration보다 case block readability를 먼저 본다."
    return "전처리된 sidecar를 기준으로 transcript-aware first pass를 얇게 진행할 수 있다."
