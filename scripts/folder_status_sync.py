#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.registry.folder_status_sync import sync_folder_status


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Apply delta-based folder change logging, inventory sync, and status rendering.")
    parser.add_argument("paths", nargs="+", help="Changed file/folder paths")
    parser.add_argument("--actor", default="codex")
    parser.add_argument("--source", default="folder_status_sync")
    parser.add_argument("--no-ancestors", action="store_true")
    parser.add_argument("--child-depth", type=int, default=0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = sync_folder_status(
        REPO_ROOT,
        args.paths,
        include_ancestors=not args.no_ancestors,
        child_depth=max(args.child_depth, 0),
        actor=args.actor,
        source=args.source,
    )
    for event in result["change_events"]:
        print(event)
    for path in result["inventory_files"]:
        print(path)
    for path in result["status_files"]:
        print(path)


if __name__ == "__main__":
    main()
