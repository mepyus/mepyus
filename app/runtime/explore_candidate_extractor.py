from __future__ import annotations

from typing import Any, Dict, List


def extract_explore_candidates(
    *,
    raw_asset: Dict[str, Any],
    fallback_object: str,
    readable_original_refs: List[str],
) -> List[Dict[str, str]]:
    base = str(raw_asset.get("title") or fallback_object or "선택 객체")
    evidence_refs = [ref for ref in (raw_asset.get("evidenceRefs") or []) if isinstance(ref, dict)]
    state_rows = [row for row in (raw_asset.get("canonicalStateRows") or []) if isinstance(row, dict)]
    compare_reasons = [str(item).strip() for item in (raw_asset.get("compareReasons") or []) if str(item).strip()]
    dependency_list = [str(item).strip() for item in (raw_asset.get("dependencyList") or []) if str(item).strip()]
    state_note = str(raw_asset.get("stateNotes") or "").strip()
    default_original = readable_original_refs[0] if readable_original_refs else f"{base} 원본 자리"

    candidates: List[Dict[str, str]] = []

    for index, ref in enumerate(evidence_refs[:2], start=1):
        ref_label = readable_original_refs[index - 1] if len(readable_original_refs) >= index else str(ref.get("label") or ref.get("id") or default_original)
        row_label = str((state_rows[index - 1] if len(state_rows) >= index else {}).get("label") or "").strip()
        candidates.append(
            {
                "id": f"evidence-{index}",
                "candidate_kind": "evidence",
                "object": base,
                "source_asset": str(raw_asset.get("id") or base),
                "title": f"{base} / 원본 단서 {index}",
                "original_preview": ref_label,
                "layer": row_label or "원본층",
                "meaning": f"{base}를 원본 단서에서 다시 읽으며 {row_label or '현재 층위'}를 먼저 붙잡아 보는 연결이다.",
                "sticker_slot": "읽고 난 뒤 남겨 둘 연결이면 스티커로 이어질 수 있다.",
                "source_pointer": str(ref.get("id") or ref_label),
                "row_key": str((state_rows[index - 1] if len(state_rows) >= index else {}).get("key") or "").strip(),
                "source_kind": str(ref.get("kind") or ""),
            }
        )

    for row in state_rows[:6]:
        row_label = str(row.get("label") or row.get("key") or "현재 층위").strip()
        row_key = str(row.get("key") or row_label).strip()
        reason_text = _pick_reason(compare_reasons, dependency_list)
        candidates.append(
            {
                "id": f"state-{row_key}",
                "candidate_kind": "state",
                "object": base,
                "source_asset": str(raw_asset.get("id") or base),
                "title": f"{base} / {row_label}",
                "original_preview": default_original,
                "layer": row_label,
                "meaning": f"{base}를 {row_label}에서 다시 읽고{reason_text} 연결로 이어 볼 수 있다.",
                "sticker_slot": "이 층위에서 반복해서 살아남는 연결이면 스티커로 남길 수 있다.",
                "source_pointer": row_key,
                "row_key": row_key,
                "source_kind": "state_row",
            }
        )

    if compare_reasons:
        reason = compare_reasons[0]
        support_row = state_rows[0] if state_rows else {}
        candidates.append(
            {
                "id": f"reason-{reason}",
                "candidate_kind": "reason",
                "object": base,
                "source_asset": str(raw_asset.get("id") or base),
                "title": f"{base} / 비교 단서",
                "original_preview": default_original,
                "layer": state_rows[0].get("label") if state_rows else "비교층",
                "meaning": f"{base}에서 드러난 {reason.replace('_', ' ')}를 따라 다른 연결로 건너갈 수 있다.",
                "sticker_slot": "비교 단서가 반복되면 스티커로 고정할 자리가 된다.",
                "source_pointer": reason,
                "row_key": "",
                "support_row_key": str(support_row.get("key") or ""),
                "source_kind": "compare_reason",
            }
        )

    deduped: List[Dict[str, str]] = []
    seen = set()
    for candidate in candidates:
        key = (
            candidate["title"],
            candidate["layer"],
            candidate["source_pointer"],
        )
        if key in seen:
            continue
        seen.add(key)
        deduped.append(candidate)
        if len(deduped) >= 12:
            break

    if deduped:
        return deduped

    fallback_meaning = state_note or f"{base}를 다시 읽을 연결 단서가 아직 얇다."
    return [
        {
            "id": "fallback-empty",
            "candidate_kind": "fallback",
            "object": base,
            "source_asset": str(raw_asset.get("id") or base),
            "title": f"{base} / 아직 얇은 연결",
            "original_preview": default_original,
            "layer": "초기층",
            "meaning": fallback_meaning,
            "sticker_slot": "아직 연결 후보가 얇아 스티커 자리는 비워 둔다.",
            "source_pointer": "fallback-empty",
            "row_key": "",
            "support_row_key": "",
            "source_kind": "fallback",
        }
    ]


def _pick_reason(compare_reasons: List[str], dependency_list: List[str]) -> str:
    token = ""
    if compare_reasons:
        token = compare_reasons[0]
    elif dependency_list:
        token = dependency_list[0]
    if not token:
        return ""
    return f" {token.replace('_', ' ')}를 단서로 삼아"
