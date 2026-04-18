from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.runtime.vectorfl_page_semi_live_shell import write_vectorfl_page_semi_live_shell


def main() -> int:
    parser = argparse.ArgumentParser(description="Render VectorFL Page semi-live shell.")
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Optional output directory. Defaults to runtime/views/vectorfl_page_shell/semi_live",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir).resolve() if args.output_dir else None
    written = write_vectorfl_page_semi_live_shell(REPO_ROOT, output_dir=output_dir)
    print(json.dumps(written, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
