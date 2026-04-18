#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent
EXCLUDE_DIRS = {"__pycache__"}
MAX_DEPTH = 2


def should_include_dir(path: Path) -> bool:
    if path == ROOT:
        return True
    rel = path.relative_to(ROOT)
    if any(part in EXCLUDE_DIRS for part in rel.parts):
        return False
    return len(rel.parts) <= MAX_DEPTH


def collect_dirs() -> list[Path]:
    dirs = [ROOT]
    for path in sorted(ROOT.rglob("*")):
        if path.is_dir() and should_include_dir(path):
            dirs.append(path)
    return dirs


def guess_role(path: Path) -> str:
    rel = "." if path == ROOT else str(path.relative_to(ROOT))
    low = rel.lower()
    if rel == ".":
        return "Application root containing engine core, runtime, input layers, fragments, models, measurement, and work records."
    if low == "core":
        return "Engine core root for formation, ingest, state, schemas, registry, and runtime contracts."
    if low.startswith("core/"):
        return "Core subsystem folder inside the engine foundation."
    if low == "runtime":
        return "Runtime execution and view layer for input, reporting, space view, measurement view, and operator-facing state."
    if low.startswith("runtime/"):
        return "Runtime subsystem folder containing a focused execution or view slice."
    if low == "input_layer":
        return "Input-layer root for segmentation, labeling, anchoring, and source location logic."
    if low.startswith("input_layer/"):
        return "Focused input-layer module folder."
    if low == "fragment":
        return "Fragment storage and projection layer."
    if low == "measurement":
        return "Ambient measurement and observer-related support layer."
    if low == "events":
        return "Event schema and event-side public surface."
    if low == "models":
        return "Shared entity/model definitions."
    if low == "work":
        return "Working notes, specs, probes, evaluations, and experiment folders."
    if low.startswith("work/"):
        return "Focused work folder containing a specific probe, contract, experiment, or utility."
    return "App subfolder with implementation or work assets; inspect notable files for exact role."


def summarize_md(path: Path) -> tuple[str, str]:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return "(unreadable)", ""
    lines = text.splitlines()
    title = ""
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            title = stripped.lstrip("#").strip()
            break
    if not title:
        title = path.stem
    summary = ""
    buffer: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if buffer:
                break
            continue
        if stripped.startswith("#"):
            continue
        if stripped.startswith("```"):
            continue
        buffer.append(stripped)
        if len(" ".join(buffer)) > 160:
            break
    summary = " ".join(buffer)
    summary = re.sub(r"\s+", " ", summary).strip()
    return title, summary[:220]


def group_files(files: list[Path]) -> dict[str, list[Path]]:
    out = {
        "markdown": [],
        "python": [],
        "json": [],
        "other": [],
    }
    for file in files:
        suffix = file.suffix.lower()
        if suffix == ".md":
            out["markdown"].append(file)
        elif suffix == ".py":
            out["python"].append(file)
        elif suffix == ".json":
            out["json"].append(file)
        else:
            out["other"].append(file)
    return out


def render_status(path: Path) -> str:
    rel = "." if path == ROOT else str(path.relative_to(ROOT))
    child_dirs = sorted(
        [p for p in path.iterdir() if p.is_dir() and p.name not in EXCLUDE_DIRS],
        key=lambda p: p.name.lower(),
    )
    child_files = sorted([p for p in path.iterdir() if p.is_file()], key=lambda p: p.name.lower())
    grouped = group_files(child_files)
    suffix_counts = Counter((p.suffix.lower() or "<no_ext>") for p in child_files)

    lines: list[str] = []
    lines.append(f"# folder_status / {rel}")
    lines.append("")
    lines.append("## 1. Folder Identity")
    lines.append(f"- path: `{rel}`")
    lines.append(f"- role_guess: {guess_role(path)}")
    lines.append("")
    lines.append("## 2. Snapshot")
    lines.append(f"- immediate_child_dirs: `{len(child_dirs)}`")
    lines.append(f"- immediate_child_files: `{len(child_files)}`")
    if suffix_counts:
        top = ", ".join(f"`{k}` x {v}" for k, v in suffix_counts.most_common(10))
        lines.append(f"- file_types: {top}")
    else:
        lines.append("- file_types: none")
    lines.append("")
    lines.append("## 3. Child Folders")
    if child_dirs:
        for d in child_dirs[:40]:
            lines.append(f"- `{d.name}`")
        if len(child_dirs) > 40:
            lines.append(f"- ... `{len(child_dirs) - 40}` more")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## 4. Markdown Files")
    if grouped["markdown"]:
        for md in grouped["markdown"][:20]:
            title, summary = summarize_md(md)
            lines.append(f"- `{md.name}`")
            lines.append(f"  title: {title}")
            if summary:
                lines.append(f"  summary: {summary}")
        if len(grouped["markdown"]) > 20:
            lines.append(f"- ... `{len(grouped['markdown']) - 20}` more markdown files")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## 5. Code / Data Files")
    if grouped["python"]:
        shown = ", ".join(f"`{p.name}`" for p in grouped["python"][:20])
        lines.append(f"- python: {shown}")
    if grouped["json"]:
        shown = ", ".join(f"`{p.name}`" for p in grouped["json"][:20])
        lines.append(f"- json: {shown}")
    others = [p.name for p in grouped["other"] if p.name != "folder_status.md"]
    if others:
        shown = ", ".join(f"`{name}`" for name in others[:20])
        lines.append(f"- other: {shown}")
    if not grouped["python"] and not grouped["json"] and not others:
        lines.append("- no immediate code/data files")
    lines.append("")
    lines.append("## 6. Quick Reading")
    if child_dirs:
        lines.append("- 이 폴더는 immediate child folder 중심으로 읽는 것이 맞다.")
    else:
        lines.append("- 이 폴더는 immediate file 중심으로 읽는 것이 맞다.")
    if grouped["markdown"]:
        lines.append("- md 문서가 immediate context 설명에 중요한 역할을 한다.")
    if grouped["python"]:
        lines.append("- 실행 가능한 스크립트/코드가 있어 행동 가능한 작업 폴더로 볼 수 있다.")
    lines.append("")
    lines.append("## 7. Current Use Hint")
    lines.append("- 이 문서는 first-pass app folder index 이다.")
    lines.append("- 다음 탐색에서는 이 문서의 md summary 를 먼저 읽고, 필요한 코드/데이터 파일만 열면 된다.")
    return "\n".join(lines) + "\n"


def main() -> None:
    targets = collect_dirs()
    for path in targets:
        (path / "folder_status.md").write_text(render_status(path), encoding="utf-8")
    print(f"generated {len(targets)} folder_status.md files")


if __name__ == "__main__":
    main()
