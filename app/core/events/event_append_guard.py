from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from app.core.registry.atomic_io import file_lock


def append_jsonl_locked(path: Path, row: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lock_path = path.with_suffix(path.suffix + ".lock")
    payload = json.dumps(row, ensure_ascii=True) + "\n"
    with file_lock(lock_path):
        with path.open("a", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())


def load_jsonl_with_tail_recovery(path: Path) -> tuple[list[dict[str, Any]], bool]:
    if not path.exists():
        return [], False
    recovered = False
    rows: list[dict[str, Any]] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            recovered = True
            break
    return rows, recovered


def recover_jsonl_tail(path: Path) -> bool:
    lock_path = path.with_suffix(path.suffix + ".lock")
    with file_lock(lock_path):
        rows, recovered = load_jsonl_with_tail_recovery(path)
        if not recovered:
            return False
        broken_path = path.with_suffix(path.suffix + ".broken")
        if path.exists():
            path.replace(broken_path)
        payload = "".join(json.dumps(row, ensure_ascii=True) + "\n" for row in rows)
        with path.open("w", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        return True
