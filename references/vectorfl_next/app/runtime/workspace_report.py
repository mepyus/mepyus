from pathlib import Path

from app.runtime.workspace_manifest import build_workspace_manifest, write_workspace_manifest


def write_workspace_report(runtime_root: Path) -> Path:
    manifest = build_workspace_manifest(runtime_root)
    write_workspace_manifest(runtime_root)

    report_path = runtime_root / "reports" / "workspace_report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Workspace Report",
        "",
        "## Coexistence",
        "",
        "- status: %s" % manifest["coexistence_status"],
        "- runtime_root: %s" % manifest["runtime_root"],
        "- process_mode: %s" % manifest["process_summary"]["dominant_mode"],
        "- process_summary: %s" % manifest["process_summary"]["summary_line"],
        "",
        "## Core Counts",
        "",
    ]
    for key, value in sorted(manifest["core_counts"].items()):
        lines.append("- %s: %s" % (key, value))

    lines.extend(
        [
            "",
            "## Manifest Counts",
            "",
        ]
    )
    for key, value in sorted(manifest["manifest_counts"].items()):
        lines.append("- %s: %s" % (key, value))

    lines.extend(
        [
            "",
            "## Maturation Signals",
            "",
            "### Local Space",
        ]
    )
    if manifest["local_space_maturation_signals"]:
        for key, value in sorted(manifest["local_space_maturation_signals"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "### Bridge",
        ]
    )
    if manifest["bridge_maturation_signals"]:
        for key, value in sorted(manifest["bridge_maturation_signals"].items()):
            lines.append("- %s: %s" % (key, value))
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Legacy Paths",
            "",
        ]
    )
    legacy_paths = manifest["legacy_paths"]
    if legacy_paths:
        for path in legacy_paths:
            lines.append("- %s" % path)
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Read",
            "",
            "- This report is descriptive only.",
            "- It does not migrate or delete legacy runtime paths.",
            "- The coexistence state itself is a material candidate.",
            "",
        ]
    )
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path
