from __future__ import annotations

import json
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.runtime.vectorfl_page_semi_live_program_detail import (
    write_vectorfl_page_semi_live_program_detail_set,
)


def main() -> None:
    result = write_vectorfl_page_semi_live_program_detail_set(REPO_ROOT)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
