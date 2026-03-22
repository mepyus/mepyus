from __future__ import annotations

from typing import Iterable, List, Sequence, TypeVar, Dict, Any


T = TypeVar("T")


def take_with_overflow(items: Iterable[T], limit: int = 3) -> Dict[str, Any]:
    values: List[T] = list(items)
    visible = values[:limit]
    overflow_count = max(0, len(values) - len(visible))
    return {
        "items": visible,
        "overflow_count": overflow_count,
    }


def compact_state(*, available: bool, items: Sequence[object], none_label: str = "none") -> str:
    if not available:
        return "not_available_yet"
    return "present" if list(items) else none_label


def compact_payload(
    *,
    available: bool,
    items: Iterable[T],
    limit: int = 3,
    none_label: str = "none",
) -> Dict[str, Any]:
    summary = take_with_overflow(items, limit=limit)
    return {
        "state": compact_state(available=available, items=summary["items"], none_label=none_label),
        "items": summary["items"],
        "overflow_count": summary["overflow_count"],
    }
