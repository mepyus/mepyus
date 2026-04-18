#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.core.registry.atomic_io import atomic_write_json, atomic_write_text
from scripts.build_reconstruction_supervisor_surface import (
    RECONSTRUCTION_ROOT,
    VIEWS_ROOT,
    build_latest_markdown,
    build_reconstruction_folder_status,
    build_reconstruction_index_json,
    build_reconstruction_index_markdown,
    load_json,
    now_iso,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sync reconstruction supervisor navigation surfaces.")
    parser.add_argument("--refresh-latest-md-only", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    updated_at = now_iso()

    latest_json_path = VIEWS_ROOT / "reconstruction_supervisor_latest.json"
    if latest_json_path.exists():
        latest_payload = load_json(latest_json_path)
        latest_payload["updated_at"] = updated_at
        atomic_write_json(latest_json_path, latest_payload)
        atomic_write_text(VIEWS_ROOT / "reconstruction_supervisor_latest.md", build_latest_markdown(latest_payload))

    if args.refresh_latest_md_only:
        print("runtime/views/reconstruction_supervisor_latest.json")
        print("runtime/views/reconstruction_supervisor_latest.md")
        return

    index_payload = build_reconstruction_index_json(updated_at)
    atomic_write_json(RECONSTRUCTION_ROOT / "index.json", index_payload)
    atomic_write_text(RECONSTRUCTION_ROOT / "index.md", build_reconstruction_index_markdown(index_payload))
    atomic_write_text(RECONSTRUCTION_ROOT / "folder_status.md", build_reconstruction_folder_status(updated_at))

    print("runtime/views/reconstruction_supervisor_latest.json")
    print("runtime/views/reconstruction_supervisor_latest.md")
    print("runtime/views/reconstruction_supervisor/index.json")
    print("runtime/views/reconstruction_supervisor/index.md")
    print("runtime/views/reconstruction_supervisor/folder_status.md")


if __name__ == "__main__":
    main()
