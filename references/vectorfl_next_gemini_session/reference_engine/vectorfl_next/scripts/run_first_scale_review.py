#!/usr/bin/env python3
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.runtime.scale_review import build_first_scale_review, write_first_scale_review


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    review = build_first_scale_review(runtime_root)
    report_path = write_first_scale_review(runtime_root)

    lines = [
        "runtime_root: %s" % runtime_root,
        "local_space_count: %s" % review["local_space_count"],
        "bridge_count: %s" % review["bridge_count"],
        "terrain_component_count: %s" % review["terrain_component_count"],
        "report_path: %s" % report_path,
    ]
    for axis_name, axis in review["axes"].items():
        lines.append("%s: %s" % (axis_name, axis["summary"]))
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
