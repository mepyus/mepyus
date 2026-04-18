from __future__ import annotations

from typing import Any, Dict, List, Optional


def select_adjacent_history_pair(
    history_rows: List[Dict[str, Any]],
    *,
    compare_index: int = 0,
) -> Dict[str, Optional[Dict[str, Any]]]:
    if not history_rows:
        return {"current": None, "previous": None, "compare_index": compare_index}

    descending = list(reversed(history_rows))
    if compare_index < 0 or compare_index >= len(descending):
        compare_index = 0
    current = descending[compare_index]
    previous = descending[compare_index + 1] if compare_index + 1 < len(descending) else None
    return {
        "current": current,
        "previous": previous,
        "compare_index": compare_index,
    }
