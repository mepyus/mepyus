#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXCLUDE_DIRS = {".git", "node_modules", "__pycache__", ".vite", ".obsidian"}
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
        return "Top-level reference warehouse for internal repos, notes, derived materials, and comparison assets."
    if "/observer" in low or low.endswith("observer"):
        return "Reference interpretation layer with manual readings, compare boards, and preprocessor pilot notes."
    if "/preprocessed" in low or low.endswith("preprocessed"):
        return "Derived fragment lane for source -> preprocessed -> ingest preparation."
    if low.endswith("/src") or "/src/" in low:
        return "Primary source code tree for the referenced project."
    if low.endswith("/app") or "/app/" in low:
        return "Application code tree containing implementation modules and work layers."
    if low.endswith("/docs") or "/docs/" in low:
        return "Documentation tree with architecture, contracts, decisions, and reports."
    if low.endswith("/runtime") or "/runtime/" in low:
        return "Runtime artifact space containing generated state, manifests, reports, and traces."
    if low.endswith("/logs") or "/logs/" in low:
        return "Log and run-history storage for audits, incidents, or execution traces."
    if low.endswith("/scripts") or "/scripts/" in low:
        return "Executable utility and automation scripts."
    if low.endswith("/tests") or "/tests/" in low:
        return "Test suites and fixtures."
    if low.endswith("/skills") or "/skills/" in low:
        return "Skill or instruction assets used to extend workflows."
    if "synapsis" in low or "notes" in low or "memo" in low or "jcstudy" in low:
        return "Note and memo space preserving thought flow, experiments, or study traces."
    if "washtank" in low:
        return "WashTank reference family root with source code, notes, observers, and preprocessed derivatives."
    if "vectorfl_next_gemini_session" in low:
        return "Session-specific reference workspace mixing notes, experiments, and a mirrored reference engine."
    if "vectorfl_next" in low:
        return "Next-generation reference engine repository with app, docs, runtime, and tests."
    if "vectorfl" in low:
        return "Reference repository for vectorfl contracts, runtime, commands, and staged work."
    return "Reference subfolder with mixed materials; inspect child folders and notable files for exact role."


def group_files(files: list[Path]) -> dict[str, list[str]]:
    out = {
        "declarations": [],
        "scripts": [],
        "source": [],
        "data": [],
        "other": [],
    }
    for file in files:
        name = file.name
        suffix = file.suffix.lower()
        if name.lower() in {
            "readme.md",
            "current.md",
            "constitution.md",
            "agents.md",
            "master_index.md",
            "raw_source_map.md",
            "stop_rule.md",
            "report_issuance_rule.md",
            "workflow.md",
            "axis_guide.md",
        }:
            out["declarations"].append(name)
        elif suffix in {".py", ".sh", ".js", ".ts", ".sql"}:
            out["scripts"].append(name)
        elif suffix in {".jsx", ".tsx", ".ts", ".js"}:
            out["source"].append(name)
        elif suffix in {".md", ".json", ".toml", ".yml", ".yaml"}:
            out["data"].append(name)
        else:
            out["other"].append(name)
    return out


def count_suffixes(files: list[Path]) -> Counter[str]:
    counter: Counter[str] = Counter()
    for file in files:
        suffix = file.suffix.lower() or "<no_ext>"
        counter[suffix] += 1
    return counter


def render_status(path: Path) -> str:
    rel = "." if path == ROOT else str(path.relative_to(ROOT))
    child_dirs = sorted(
        [p for p in path.iterdir() if p.is_dir() and p.name not in EXCLUDE_DIRS],
        key=lambda p: p.name.lower(),
    )
    child_files = sorted([p for p in path.iterdir() if p.is_file()], key=lambda p: p.name.lower())
    grouped = group_files(child_files)
    suffix_counts = count_suffixes(child_files)

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
        top = ", ".join(f"`{k}` x {v}" for k, v in suffix_counts.most_common(8))
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
    lines.append("## 4. Notable Files")
    for label, key in [
        ("declarations_or_governance", "declarations"),
        ("scripts_or_commands", "scripts"),
        ("docs_or_data", "data"),
        ("other_files", "other"),
    ]:
        items = grouped[key]
        if items:
            shown = ", ".join(f"`{name}`" for name in items[:15])
            extra = "" if len(items) <= 15 else f", ... `{len(items) - 15}` more"
            lines.append(f"- {label}: {shown}{extra}")
    if not child_files:
        lines.append("- no immediate files")
    lines.append("")
    lines.append("## 5. Quick Reading")
    if child_dirs:
        lines.append("- 이 폴더는 하위 폴더 중심으로 읽는 것이 맞다.")
    else:
        lines.append("- 이 폴더는 immediate file 중심으로 읽는 것이 맞다.")
    if grouped["declarations"]:
        lines.append("- 선언문/현재 상태 문서가 있어 폴더 역할을 빠르게 파악할 수 있다.")
    if grouped["scripts"]:
        lines.append("- 실행 스크립트 또는 코드 파일이 있어 행동 가능한 reference 로 쓸 수 있다.")
    if any(name == "folder_status.md" for name in grouped["data"] + grouped["other"]):
        lines.append("- existing folder_status.md present")
    lines.append("")
    lines.append("## 6. Current Use Hint")
    lines.append("- 이 문서는 first-pass folder index 이다.")
    lines.append("- 세부 구조가 필요하면 이 폴더의 선언문/README/current 문서부터 읽고, 그 다음 코드/데이터를 연다.")
    return "\n".join(lines) + "\n"


def main() -> None:
    targets = collect_dirs()
    for path in targets:
        status_path = path / "folder_status.md"
        status_path.write_text(render_status(path), encoding="utf-8")
    print(f"generated {len(targets)} folder_status.md files")


if __name__ == "__main__":
    main()
