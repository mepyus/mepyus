#!/usr/bin/env python3
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.runtime.reread_audit import build_reread_audit, write_reread_audit


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    audit = build_reread_audit(runtime_root)
    report_path = write_reread_audit(runtime_root)

    lines = [
        "runtime_root: %s" % runtime_root,
        "posture: %s" % audit["posture"],
        "cell_count: %s" % audit["cell_count"],
        "active_layers: %s" % (", ".join(audit["active_layers"]) or "none"),
        "risks:",
    ]
    if audit["risks"]:
        for item in audit["risks"]:
            lines.append("- %s" % item)
    else:
        lines.append("- none")
    lines.append("report_path: %s" % report_path)
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
