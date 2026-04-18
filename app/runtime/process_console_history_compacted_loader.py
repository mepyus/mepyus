from __future__ import annotations

from typing import Any, Dict, List

from app.core.state_store.history_compaction_policy import compact_history_items


def build_compacted_history_surface(items_descending: List[Dict[str, Any]]) -> Dict[str, Any]:
    compacted = compact_history_items(items_descending)
    return {
        "recent_items": compacted["recent_items"],
        "older_nodes": compacted["older_nodes"],
        "recent_window": compacted["recent_window"],
        "older_node_count": len(compacted["older_nodes"]),
    }
