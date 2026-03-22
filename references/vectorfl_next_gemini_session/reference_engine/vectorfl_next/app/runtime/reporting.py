from pathlib import Path
from typing import Dict, List

from app.runtime.workspace_manifest import build_workspace_manifest


def should_issue_workspace_report(runtime_root: Path) -> Dict[str, object]:
    manifest = build_workspace_manifest(runtime_root)
    reasons: List[str] = []

    if manifest["coexistence_status"] in {"hybrid", "legacy_only"}:
        reasons.append("legacy coexistence requires readable inspection")
    if sum(manifest["core_counts"].values()) > 0:
        reasons.append("core formation state exists")
    if sum(manifest["manifest_counts"].values()) > 0:
        reasons.append("reactive manifests exist")

    return {
        "issue_report": bool(reasons),
        "reasons": reasons,
        "coexistence_status": manifest["coexistence_status"],
    }
