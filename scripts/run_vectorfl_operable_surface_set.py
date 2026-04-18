from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.runtime.vectorfl_operable_surface_set import write_vectorfl_operable_surface_set


def main() -> int:
    parser = argparse.ArgumentParser(description="Render the VectorFL operable surface set.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Optional output directory. Defaults to runtime/views/vectorfl_operable_surface",
    )
    args = parser.parse_args()

    result = write_vectorfl_operable_surface_set(REPO_ROOT, output_dir=args.output_dir)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
