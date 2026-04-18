from __future__ import annotations

from collections import Counter
from datetime import datetime
import json
from pathlib import Path
import re

from app.core.events.event_append_guard import append_jsonl_locked
from app.core.registry.atomic_io import atomic_write_json


FOLDER_CHANGES_DIR = Path("runtime/manifests/folder_changes")
FOLDER_CHANGE_LOG_PATH = FOLDER_CHANGES_DIR / "folder_change_log.jsonl"
FOLDER_INVENTORY_DIR = Path("runtime/manifests/folder_inventory")


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
    buffer: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if buffer:
                break
            continue
        if stripped.startswith("#") or stripped.startswith("```"):
            continue
        buffer.append(stripped)
        if len(" ".join(buffer)) > 180:
            break
    summary = re.sub(r"\s+", " ", " ".join(buffer)).strip()
    return title, summary[:240]


def rel_path(path: Path, root: Path) -> str:
    return "." if path == root else str(path.relative_to(root))


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def guess_role(path: Path, root: Path) -> str:
    rel = rel_path(path, root)
    low = rel.lower()
    name = path.name.lower()
    if rel == ".":
        return "Repository root containing engine code, runtime artifacts, references, and operation documents."
    if low == "docs":
        return "Documentation operating memory containing contracts, policies, reports, guides, prompts, and templates."
    if low.endswith("/guides") or name == "guides":
        return "Human-facing operation manuals and quick-start guides."
    if low.endswith("/contracts") or name == "contracts":
        return "Contract layer containing hard boundaries and structural guarantees."
    if low.endswith("/policies") or name == "policies":
        return "Policy layer containing operating rules and governance notes."
    if low.endswith("/reports") or name == "reports":
        return "Report layer containing analysis, reviews, and result summaries."
    if low.endswith("/templates") or name == "templates":
        return "Template lane for reusable document headers, formats, and skeletons."
    if low.endswith("/prompts") or name == "prompts":
        return "Prompt asset folder containing reusable operator and assistant prompt materials."
    if low.endswith("/architecture") or name == "architecture":
        return "Architecture note folder containing structural explanations and design breakdowns."
    if low.endswith("/evaluations") or name == "evaluations":
        return "Evaluation folder containing checks, reviews, and comparative assessments."
    if low.endswith("/observer/gemini"):
        return "Gemini observer log lane for session-batch review outputs."
    if low.endswith("/observer") or "/observer/" in low:
        return "Observer-facing output or review folder."
    if low.endswith("/runtime") or "/runtime/" in low:
        return "Runtime artifact or runtime-facing support folder."
    return "Folder with mixed project assets; inspect child folders and markdown files for exact role."


def group_files(files: list[Path]) -> dict[str, list[Path]]:
    out = {"markdown": [], "python": [], "json": [], "yaml": [], "other": []}
    for file in files:
        suffix = file.suffix.lower()
        if suffix == ".md":
            out["markdown"].append(file)
        elif suffix == ".py":
            out["python"].append(file)
        elif suffix == ".json":
            out["json"].append(file)
        elif suffix in {".yml", ".yaml"}:
            out["yaml"].append(file)
        else:
            out["other"].append(file)
    return out


def folder_key_for(path: Path, root: Path) -> str:
    rel = rel_path(path, root)
    return rel.replace("/", ".") if rel != "." else "root"


def inventory_path_for(path: Path, root: Path) -> Path:
    return root / FOLDER_INVENTORY_DIR / f"{folder_key_for(path, root)}.json"


def collect_file_record(path: Path, root: Path) -> dict[str, object]:
    title = ""
    summary = ""
    if path.suffix.lower() == ".md":
        title, summary = summarize_md(path)
    stat = path.stat()
    return {
        "name": path.name,
        "path": rel_path(path, root),
        "suffix": path.suffix.lower() or "<no_ext>",
        "size": stat.st_size,
        "mtime_ns": stat.st_mtime_ns,
        "title": title,
        "summary": summary,
    }


def build_inventory(path: Path, root: Path) -> dict[str, object]:
    child_dirs = sorted([p for p in path.iterdir() if p.is_dir() and p.name != "__pycache__"], key=lambda p: p.name.lower())
    child_files = sorted([p for p in path.iterdir() if p.is_file()], key=lambda p: p.name.lower())
    grouped = group_files(child_files)
    suffix_counts = Counter((p.suffix.lower() or "<no_ext>") for p in child_files if p.name != "folder_status.md")
    return {
        "folder_key": folder_key_for(path, root),
        "folder_path": rel_path(path, root),
        "parent_folder": None if path == root else rel_path(path.parent, root),
        "child_folders": [
            {
                "name": child.name,
                "path": rel_path(child, root),
                "status_file": rel_path(child / "folder_status.md", root) if (child / "folder_status.md").exists() else "",
            }
            for child in child_dirs
        ],
        "documents": [collect_file_record(file, root) for file in grouped["markdown"] if file.name != "folder_status.md"],
        "assets": [collect_file_record(file, root) for file in child_files if file.name != "folder_status.md" and file.suffix.lower() != ".md"],
        "related_status_files": [rel_path(path / "folder_status.md", root)],
        "last_updated": now_iso(),
        "role_guess": guess_role(path, root),
        "file_type_counts": dict(sorted(suffix_counts.items())),
    }


def load_existing_inventory(path: Path, root: Path) -> dict[str, object] | None:
    inventory_path = inventory_path_for(path, root)
    if not inventory_path.exists():
        return None
    return json.loads(inventory_path.read_text(encoding="utf-8"))


def append_change_event(root: Path, event: dict[str, object]) -> None:
    full_dir = root / FOLDER_CHANGES_DIR
    full_dir.mkdir(parents=True, exist_ok=True)
    append_jsonl_locked(root / FOLDER_CHANGE_LOG_PATH, event)


def diff_inventory_events(
    *,
    previous: dict[str, object] | None,
    current: dict[str, object],
    actor: str,
    source: str,
) -> list[dict[str, object]]:
    folder_rel = str(current["folder_path"])
    event_class = "bootstrap_seed" if previous is None else "delta_update"
    events: list[dict[str, object]] = []
    previous_docs = {row["path"]: row for row in (previous or {}).get("documents", [])}
    current_docs = {row["path"]: row for row in current["documents"]}
    previous_assets = {row["path"]: row for row in (previous or {}).get("assets", [])}
    current_assets = {row["path"]: row for row in current["assets"]}
    previous_children = {row["path"] for row in (previous or {}).get("child_folders", [])}
    current_children = {row["path"] for row in current["child_folders"]}

    if previous is None:
        events.append(
            {
                "timestamp": now_iso(),
                "event_type": "folder_created",
                "folder_key": current["folder_key"],
                "folder_path": folder_rel,
                "target_ref": folder_rel,
                "actor": actor,
                "source": source,
                "event_class": event_class,
            }
        )

    for doc_path, doc in current_docs.items():
        prev = previous_docs.get(doc_path)
        if prev is None:
            event_type = "doc_created"
        elif prev.get("mtime_ns") != doc.get("mtime_ns") or prev.get("size") != doc.get("size"):
            event_type = "doc_updated"
        else:
            continue
        events.append(
            {
                "timestamp": now_iso(),
                "event_type": event_type,
                "folder_key": current["folder_key"],
                "folder_path": folder_rel,
                "target_ref": doc_path,
                "actor": actor,
                "source": source,
                "event_class": event_class,
            }
        )

    for asset_path, asset in current_assets.items():
        prev = previous_assets.get(asset_path)
        if prev is None:
            event_type = "asset_registered"
        elif prev.get("mtime_ns") != asset.get("mtime_ns") or prev.get("size") != asset.get("size"):
            event_type = "rule_updated" if asset_path.endswith(".json") else "asset_registered"
        else:
            continue
        events.append(
            {
                "timestamp": now_iso(),
                "event_type": event_type,
                "folder_key": current["folder_key"],
                "folder_path": folder_rel,
                "target_ref": asset_path,
                "actor": actor,
                "source": source,
                "event_class": event_class,
            }
        )

    for child in sorted(current_children - previous_children):
        events.append(
            {
                "timestamp": now_iso(),
                "event_type": "folder_created",
                "folder_key": current["folder_key"],
                "folder_path": folder_rel,
                "target_ref": child,
                "actor": actor,
                "source": source,
                "event_class": event_class,
            }
        )

    return events


def write_inventory(path: Path, root: Path, inventory: dict[str, object]) -> Path:
    target = inventory_path_for(path, root)
    target.parent.mkdir(parents=True, exist_ok=True)
    atomic_write_json(target, inventory)
    return target


def render_folder_status_from_inventory(inventory: dict[str, object], root: Path) -> str:
    suffix_counts = Counter(inventory.get("file_type_counts", {}))
    lines: list[str] = []
    lines.append(f"# folder_status / {inventory['folder_path']}")
    lines.append("")
    lines.append("## 1. Folder Identity")
    lines.append(f"- path: `{inventory['folder_path']}`")
    lines.append(f"- role_guess: {inventory['role_guess']}")
    lines.append("- status_mode: `rendered_from_inventory`")
    lines.append("")
    lines.append("## 2. Snapshot")
    lines.append(f"- immediate_child_dirs: `{len(inventory['child_folders'])}`")
    lines.append(f"- immediate_child_files: `{len(inventory['documents']) + len(inventory['assets'])}`")
    if suffix_counts:
        lines.append("- file_types: " + ", ".join(f"`{suffix}` x {count}" for suffix, count in suffix_counts.most_common(10)))
    else:
        lines.append("- file_types: none")
    lines.append("")
    lines.append("## 3. Child Folders")
    if inventory["child_folders"]:
        for child in inventory["child_folders"][:40]:
            if child.get("status_file"):
                lines.append(f"- `{child['name']}` -> `{child['status_file']}`")
            else:
                lines.append(f"- `{child['name']}`")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## 4. Markdown Files")
    if inventory["documents"]:
        for doc in inventory["documents"][:24]:
            lines.append(f"- `{doc['name']}`")
            if doc.get("title"):
                lines.append(f"  title: {doc['title']}")
            if doc.get("summary"):
                lines.append(f"  summary: {doc['summary']}")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## 5. Code / Data Files")
    python_files = [asset for asset in inventory["assets"] if asset["suffix"] == ".py"]
    json_files = [asset for asset in inventory["assets"] if asset["suffix"] == ".json"]
    yaml_files = [asset for asset in inventory["assets"] if asset["suffix"] in {".yml", ".yaml"}]
    other_files = [asset for asset in inventory["assets"] if asset["suffix"] not in {".py", ".json", ".yml", ".yaml"}]
    if python_files:
        lines.append("- python: " + ", ".join(f"`{asset['name']}`" for asset in python_files[:20]))
    if json_files:
        lines.append("- json: " + ", ".join(f"`{asset['name']}`" for asset in json_files[:20]))
    if yaml_files:
        lines.append("- yaml: " + ", ".join(f"`{asset['name']}`" for asset in yaml_files[:20]))
    if other_files:
        lines.append("- other: " + ", ".join(f"`{asset['name']}`" for asset in other_files[:20]))
    if not python_files and not json_files and not yaml_files and not other_files:
        lines.append("- no immediate code/data files")
    lines.append("")
    lines.append("## 6. Current Use Hint")
    lines.append("- 변화가 생기면 먼저 change log 와 inventory 를 갱신하고, 이 문서는 그 결과를 얇게 렌더한다.")
    lines.append("- 이 문서는 원장이 아니라 읽기면이다.")
    lines.append("")
    lines.append("## 7. Inventory Link")
    lines.append(f"- folder_key: `{inventory['folder_key']}`")
    lines.append(f"- inventory_manifest: `{rel_path(root / FOLDER_INVENTORY_DIR / (inventory['folder_key'] + '.json'), root)}`")
    lines.append(f"- parent_folder: `{inventory.get('parent_folder') or 'none'}`")
    lines.append(f"- related_status_files: `{', '.join(inventory['related_status_files'])}`")
    lines.append(f"- last_updated: `{inventory['last_updated']}`")
    lines.append("")
    lines.append("## 8. Render Rule")
    lines.append("- 변화 이력은 `runtime/manifests/folder_changes/folder_change_log.jsonl` 에 append-only 로 남긴다.")
    lines.append("- change log 의 `event_class` 는 초기 inventory seed 와 이후 delta update 를 구분한다.")
    lines.append("- 현재 상태는 inventory manifest 로 유지하고, folder_status.md 는 그 위에 얹힌 렌더 문서다.")
    return "\n".join(lines) + "\n"


def collect_target_dirs(root: Path, raw_paths: list[str], include_ancestors: bool = True, child_depth: int = 0) -> list[Path]:
    targets: set[Path] = set()
    for raw in raw_paths:
        path = Path(raw)
        if not path.is_absolute():
            path = (root / path).resolve()
        base = path if path.exists() and path.is_dir() else path.parent
        if not base.exists():
            continue
        if root not in [base, *base.parents]:
            continue
        targets.add(base)
        if include_ancestors:
            current = base.parent
            while current != root and root in [current, *current.parents]:
                targets.add(current)
                current = current.parent
            if base != root:
                targets.add(root)
        if child_depth > 0 and base.is_dir():
            for child in sorted(base.rglob("*")):
                if child.is_dir() and len(child.relative_to(base).parts) <= child_depth:
                    targets.add(child)
    return sorted(targets, key=lambda p: (len(p.relative_to(root).parts), str(p)))


def sync_folder_status(
    root: Path,
    raw_paths: list[str],
    include_ancestors: bool = True,
    child_depth: int = 0,
    actor: str = "codex",
    source: str = "manual_delta_sync",
) -> dict[str, list[str]]:
    written_status: list[str] = []
    written_inventory: list[str] = []
    change_events: list[str] = []
    for directory in collect_target_dirs(root, raw_paths, include_ancestors=include_ancestors, child_depth=child_depth):
        if directory == root:
            continue
        previous = load_existing_inventory(directory, root)
        current = build_inventory(directory, root)
        for event in diff_inventory_events(previous=previous, current=current, actor=actor, source=source):
            append_change_event(root, event)
            change_events.append(f"{event['event_type']}::{event['target_ref']}")
        inventory_path = write_inventory(directory, root, current)
        written_inventory.append(rel_path(inventory_path, root))
        status_path = directory / "folder_status.md"
        status_path.write_text(render_folder_status_from_inventory(current, root), encoding="utf-8")
        written_status.append(rel_path(status_path, root))
    return {
        "inventory_files": written_inventory,
        "status_files": written_status,
        "change_events": change_events,
    }
