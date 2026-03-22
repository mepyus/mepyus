#!/usr/bin/env python3
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.runtime.source_view import write_source_fragment_view


def main() -> int:
    runtime_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("runtime")
    paths = write_source_fragment_view(runtime_root.resolve())
    print(paths["json_path"])
    print(paths["html_path"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
