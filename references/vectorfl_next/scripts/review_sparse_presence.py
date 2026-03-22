#!/usr/bin/env python3
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.runtime.sparse_presence_review import build_sparse_presence_review


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    review = build_sparse_presence_review(runtime_root)

    print("runtime_root: %s" % review["runtime_root"])
    print("quiet_local_spaces: %s" % review["quiet_local_space_count"])
    print("forming_local_spaces: %s" % review["forming_local_space_count"])
    print("bridge_exposed_local_spaces: %s" % review["bridge_exposed_local_space_count"])
    print("terrain_components: %s" % review["terrain_component_count"])
    print("sparse_retention_components: %s" % review["sparse_retention_component_count"])
    print("light_forgetting_components: %s" % review["light_forgetting_component_count"])
    print("process_summary: %s" % review["process_summary"])
    if review["quiet_role_counts"]:
        print("quiet_role_counts:")
        for role, count in sorted(review["quiet_role_counts"].items()):
            print("- %s: %s" % (role, count))
    else:
        print("quiet_role_counts: none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
