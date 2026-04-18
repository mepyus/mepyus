from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import re


HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")


@dataclass
class HeadingBlock:
    level: int
    title: str
    path: list[str]
    start: int
    end: int


def _build_heading_blocks(text: str) -> list[HeadingBlock]:
    lines = text.splitlines(keepends=True)
    blocks: list[HeadingBlock] = []
    stack: list[tuple[int, str]] = []
    offset = 0
    pending_block: HeadingBlock | None = None

    for line in lines:
        stripped = line.rstrip("\n")
        match = HEADING_RE.match(stripped.strip())
        if match:
            if pending_block is not None:
                pending_block.end = max(pending_block.start, offset - 1)
                blocks.append(pending_block)
            level = len(match.group(1))
            title = match.group(2).strip()
            stack = [(lvl, name) for lvl, name in stack if lvl < level]
            stack.append((level, title))
            pending_block = HeadingBlock(
                level=level,
                title=title,
                path=[name for _, name in stack],
                start=offset,
                end=offset,
            )
        offset += len(line)

    if pending_block is not None:
        pending_block.end = max(pending_block.start, len(text))
        blocks.append(pending_block)

    return blocks


def _preview(text: str, start: int, end: int, limit: int = 140) -> str:
    snippet = " ".join(text[start:end].split())
    return snippet[:limit]


def build_origin_map(source_doc_id: str, text: str, derived_from_kind: str) -> dict[str, object]:
    blocks = _build_heading_blocks(text)
    chosen: HeadingBlock | None = None

    for block in blocks:
        if block.level == 2:
            chosen = block
            break
    if chosen is None and blocks:
        chosen = blocks[0]

    if chosen is None:
        start = 0
        end = len(text)
        heading_path: list[str] = []
    else:
        start = chosen.start
        end = chosen.end
        heading_path = chosen.path

    return {
        "origin_map": {
            "source_doc_id": source_doc_id,
            "heading_path": heading_path,
            "source_locator": {
                "type": "char_span",
                "start": start,
                "end": end,
            },
            "source_preview": _preview(text, start, end),
            "derived_at": datetime.now().astimezone().isoformat(timespec="seconds"),
            "derived_from_kind": derived_from_kind,
        }
    }
