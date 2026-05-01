#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


SEED_CONFIDENCE_SCORE = {"low": 1, "medium": 2, "high": 3}
SUPPORT_STRENGTH_SCORE = {"insufficient": 0, "unclear": 1, "thin": 1, "has_signal": 2}


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _role_map(role_rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {row["split_unit_ref"]: row for row in role_rows}


def _seed_score(seed: dict[str, Any], role_by_ref: dict[str, dict[str, Any]]) -> int:
    refs = seed.get("split_unit_refs", [])
    roles = [role_by_ref.get(ref, {}).get("content_role", "unknown") for ref in refs]
    non_unknown = [role for role in roles if role != "unknown"]
    score = SEED_CONFIDENCE_SCORE.get(seed.get("seed_confidence", "low"), 1)
    score += min(len(set(non_unknown)), 2)
    if seed.get("misunderstanding_correction"):
        score += 1
    if seed.get("tension_marker"):
        score += 1
    if seed.get("repeated_pressure_note"):
        score += 1
    return score


def _camera_score(camera: dict[str, Any], seed_score: int) -> int:
    return seed_score + sum(
        SUPPORT_STRENGTH_SCORE.get(camera.get(slot, {}).get("strength", "insufficient"), 0)
        for slot in ("change_support", "boundary_support", "flow_support")
    )


def _flow_camera_score(camera: dict[str, Any], seed_score: int) -> int:
    flow_strength = camera.get("flow_support", {}).get("strength", "insufficient")
    flow_score = SUPPORT_STRENGTH_SCORE.get(flow_strength, 0) * 3
    return seed_score + flow_score


def _select_seed(seed_rows: list[dict[str, Any]], role_by_ref: dict[str, dict[str, Any]]) -> dict[str, Any] | None:
    if not seed_rows:
        return None
    return max(seed_rows, key=lambda row: (_seed_score(row, role_by_ref), row.get("bundle_id", "")))


def _select_seed_by_ref(seed_rows: list[dict[str, Any]], seed_ref: str) -> dict[str, Any] | None:
    for row in seed_rows:
        if row.get("bundle_id") == seed_ref:
            return row
    return None


def _camera_by_seed(camera_rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    for row in camera_rows:
        refs = row.get("upstream_artifact_refs", [])
        if refs:
            rows[refs[0]] = row
    return rows


def _select_camera_by_ref(camera_rows: list[dict[str, Any]], camera_ref: str) -> dict[str, Any] | None:
    for row in camera_rows:
        if row.get("camera_support_id") == camera_ref:
            return row
    return None


def _role_mix(seed: dict[str, Any]) -> list[str]:
    return [role for role in seed.get("provisional_role_mix", []) if role and role != "unknown"][:4]


def _seed_focus(seed: dict[str, Any]) -> str:
    roles = _role_mix(seed)
    if "correction" in roles or seed.get("misunderstanding_correction"):
        return "Re-read the local correction pressure around the selected units."
    if "objection" in roles or seed.get("tension_marker"):
        return "Re-read the local risk or resistance pressure around the selected units."
    if any(role in roles for role in ("transition", "connective")):
        return "Re-read the adjacent units where local handoff pressure stays visible."
    return "Re-read the local pressure that keeps the selected units worth grouping together."


def _fallback_seed(role_rows: list[dict[str, Any]], source_ref: str) -> dict[str, Any]:
    refs = [row.get("split_unit_ref", "") for row in role_rows[:2] if row.get("split_unit_ref")]
    roles = [row.get("content_role", "unknown") for row in role_rows[:2] if row.get("content_role")]
    return {
        "bundle_id": "line_seed_fallback_reader_001",
        "source_ref": source_ref,
        "split_unit_refs": refs,
        "repeated_pressure_note": "No bounded line seed bundle was emitted; keep only a minimal reread trace.",
        "linkage_hint": "The local material is too compact for a stronger seed grouping.",
        "question_inducement": "Which nearby unit should be reread first if more context becomes available?",
        "misunderstanding_correction": "",
        "tension_marker": "",
        "provisional_role_mix": roles or ["unknown"],
        "why_line_seed": "This fallback keeps reread traceability without inventing a stronger middle layer.",
        "seed_confidence": "low",
    }


def _camera_focus(camera: dict[str, Any], seed: dict[str, Any]) -> str:
    strengths = {
        "change": camera.get("change_support", {}).get("strength", "insufficient"),
        "boundary": camera.get("boundary_support", {}).get("strength", "insufficient"),
        "flow": camera.get("flow_support", {}).get("strength", "insufficient"),
    }
    live = [name for name, strength in strengths.items() if strength in {"has_signal", "thin", "unclear"}]
    if live == ["change"]:
        return "Re-read what locally shifts across the selected units."
    if live == ["boundary"]:
        return "Re-read the local limit or not-yet wording around the selected units."
    if live == ["flow"]:
        return "Re-read the local sequence or handoff wording around the selected units."
    if "change" in live and "boundary" in live:
        return "Re-read the local shift and local limit wording together."
    if "change" in live and "flow" in live:
        return "Re-read the local shift together with the nearby sequence wording."
    if "boundary" in live and "flow" in live:
        return "Re-read the local limit wording together with nearby sequence cues."
    if len(live) == 3:
        return "Re-read the selected units with local shift, limit, and sequence cues kept together."
    return _seed_focus(seed)


def _signal_recap(camera: dict[str, Any]) -> dict[str, str]:
    return {
        "change": camera.get("change_support", {}).get("strength", "insufficient"),
        "boundary": camera.get("boundary_support", {}).get("strength", "insufficient"),
        "flow": camera.get("flow_support", {}).get("strength", "insufficient"),
    }


def _role_seed_note(seed: dict[str, Any], role_by_ref: dict[str, dict[str, Any]]) -> dict[str, Any]:
    refs = seed.get("split_unit_refs", [])
    role_rows = [role_by_ref.get(ref, {}) for ref in refs]
    return {
        "selected_seed_ref": seed.get("bundle_id", ""),
        "reread_focus": _seed_focus(seed),
        "role_mix": _role_mix(seed) or ["unknown"],
        "repeated_pressure_note": seed.get("repeated_pressure_note", ""),
        "linkage_hint": seed.get("linkage_hint", ""),
        "question_inducement": seed.get("question_inducement", ""),
        "insufficiency": "Role and seed preserve local pressure, but camera-facing support is still unchecked.",
        "reread_refs": refs,
        "role_refs": [row.get("tag_id", "") for row in role_rows if row],
    }


def _role_seed_camera_note(
    seed: dict[str, Any],
    camera: dict[str, Any] | None,
    role_by_ref: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    base = _role_seed_note(seed, role_by_ref)
    if not camera:
        base.update(
            {
                "selected_camera_ref": "",
                "camera_signal_summary": "No camera support row matched the selected seed.",
                "signal_recap": {"change": "insufficient", "boundary": "insufficient", "flow": "insufficient"},
                "insufficiency": "Camera support is missing for this seed, so reread remains role+seed only.",
                "carry_forward_refs": base["reread_refs"],
            }
        )
        return base
    base.update(
        {
            "selected_camera_ref": camera.get("camera_support_id", ""),
            "reread_focus": _camera_focus(camera, seed),
            "camera_signal_summary": camera.get("camera_signal_summary", ""),
            "signal_recap": _signal_recap(camera),
            "insufficiency": camera.get("insufficiency_or_gap", ""),
            "carry_forward_refs": camera.get("carry_forward_handle", {}).get("source_unit_refs", []) or base["reread_refs"],
        }
    )
    return base


def _role_seed_flow_note(
    seed: dict[str, Any],
    camera: dict[str, Any] | None,
    role_by_ref: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    base = _role_seed_note(seed, role_by_ref)
    if not camera:
        base.update(
            {
                "selected_camera_ref": "",
                "camera_signal_summary": "No camera support row matched the selected seed.",
                "signal_recap": {"change": "insufficient", "boundary": "insufficient", "flow": "insufficient"},
                "insufficiency": "Flow-focused reread stays at role+seed because no camera row matched.",
                "carry_forward_refs": base["reread_refs"],
            }
        )
        return base
    flow_strength = camera.get("flow_support", {}).get("strength", "insufficient")
    if flow_strength in {"has_signal", "thin", "unclear"}:
        focus = "Re-read the local sequence or handoff wording around the selected units."
    else:
        focus = base["reread_focus"]
    base.update(
        {
            "selected_camera_ref": camera.get("camera_support_id", ""),
            "reread_focus": focus,
            "camera_signal_summary": camera.get("camera_signal_summary", ""),
            "signal_recap": {
                "change": "insufficient",
                "boundary": "insufficient",
                "flow": flow_strength,
            },
            "insufficiency": (
                camera.get("insufficiency_or_gap", "")
                if flow_strength in {"has_signal", "thin", "unclear"}
                else "Flow support did not narrow reread beyond role+seed."
            ),
            "carry_forward_refs": camera.get("carry_forward_handle", {}).get("source_unit_refs", []) or base["reread_refs"],
        }
    )
    return base


def _comparison_note(variant_a: dict[str, Any], variant_b: dict[str, Any]) -> dict[str, str]:
    signal_recap = variant_b.get("signal_recap", {})
    live = [name for name, strength in signal_recap.items() if strength in {"has_signal", "thin", "unclear"}]
    if variant_b.get("selected_camera_ref") and any(signal_recap.values()):
        if any(strength == "has_signal" for strength in signal_recap.values()):
            helpfulness = "도움 됨"
        elif live:
            helpfulness = "약하게 도움 됨"
        else:
            helpfulness = "별 차이 없음"
    else:
        helpfulness = "별 차이 없음"
    if not live and variant_b.get("selected_camera_ref"):
        helpfulness = "noise 가능성 있음"
    return {
        "result": helpfulness,
        "why": (
            "Camera support narrowed the reread focus with explicit signal recap."
            if helpfulness in {"도움 됨", "약하게 도움 됨"}
            else "Camera support did not add enough bounded signal beyond role+seed."
        ),
        "camera_added_value": ", ".join(live) if live else "none",
        "still_thin": variant_b.get("insufficiency", ""),
    }


def _flow_comparison_note(variant_a: dict[str, Any], variant_b: dict[str, Any], variant_c: dict[str, Any]) -> dict[str, str]:
    b_live = [name for name, strength in variant_b.get("signal_recap", {}).items() if strength in {"has_signal", "thin", "unclear"}]
    c_flow = variant_c.get("signal_recap", {}).get("flow", "insufficient")
    if c_flow in {"has_signal", "thin", "unclear"} and variant_c.get("reread_focus") != variant_a.get("reread_focus"):
        result = "independent value"
    elif "flow" in b_live:
        result = "supportive only"
    else:
        result = "no clear added value"
    return {
        "result": result,
        "flow_strength": c_flow,
        "why": (
            "Flow-focused reread narrowed focus beyond role+seed."
            if result == "independent value"
            else (
                "Flow remained secondary and only helped inside the full camera read."
                if result == "supportive only"
                else "Flow did not add bounded reread value beyond role+seed in this trial."
            )
        ),
    }


def run_trial(
    *,
    label: str,
    role_path: Path,
    seed_path: Path,
    camera_path: Path,
    output_path: Path,
    seed_ref: str = "",
    camera_ref: str = "",
    prefer_flow: bool = False,
) -> dict[str, Any]:
    role_rows = _load_json(role_path)
    seed_rows = _load_json(seed_path)
    camera_rows = _load_json(camera_path)
    role_by_ref = _role_map(role_rows)
    source_ref = ""
    if role_rows:
        source_ref = role_rows[0].get("source_ref", "")
    elif camera_rows:
        source_ref = camera_rows[0].get("source_ref", "")
    selected_seed = (
        _select_seed_by_ref(seed_rows, seed_ref)
        if seed_ref
        else _select_seed(seed_rows, role_by_ref)
    ) or _fallback_seed(role_rows, source_ref)
    camera_rows_by_seed = _camera_by_seed(camera_rows)
    matching_camera = _select_camera_by_ref(camera_rows, camera_ref) if camera_ref else camera_rows_by_seed.get(selected_seed.get("bundle_id", ""))
    if prefer_flow and camera_rows:
        matching_camera = max(
            camera_rows,
            key=lambda row: _flow_camera_score(
                row,
                _seed_score(selected_seed, role_by_ref),
            ),
        )
        upstream_refs = matching_camera.get("upstream_artifact_refs", [])
        if upstream_refs:
            selected_seed = _select_seed_by_ref(seed_rows, upstream_refs[0]) or selected_seed
    elif matching_camera is None and camera_rows:
        matching_camera = max(
            camera_rows,
            key=lambda row: _camera_score(
                row,
                _seed_score(selected_seed, role_by_ref),
            ),
        )

    variant_a = _role_seed_note(selected_seed, role_by_ref)
    variant_b = _role_seed_camera_note(selected_seed, matching_camera, role_by_ref)
    variant_c = _role_seed_flow_note(selected_seed, matching_camera, role_by_ref)
    payload = {
        "trial_label": label,
        "source_ref": selected_seed.get("source_ref", ""),
        "inputs": {
            "content_role_path": str(role_path.relative_to(REPO_ROOT)).replace("\\", "/"),
            "line_seed_path": str(seed_path.relative_to(REPO_ROOT)).replace("\\", "/"),
            "camera_support_path": str(camera_path.relative_to(REPO_ROOT)).replace("\\", "/"),
        },
        "variant_a_role_seed": variant_a,
        "variant_b_role_seed_camera": variant_b,
        "variant_c_role_seed_flow": variant_c,
        "comparison_note_ab": _comparison_note(variant_a, variant_b),
        "comparison_note_ac": _comparison_note(variant_a, variant_c),
        "flow_judgment": _flow_comparison_note(variant_a, variant_b, variant_c),
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--label", required=True)
    parser.add_argument("--role", required=True)
    parser.add_argument("--seed", required=True)
    parser.add_argument("--camera", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--seed-ref", default="")
    parser.add_argument("--camera-ref", default="")
    parser.add_argument("--prefer-flow", action="store_true")
    args = parser.parse_args()

    role_path = Path(args.role)
    seed_path = Path(args.seed)
    camera_path = Path(args.camera)
    output_path = Path(args.output)
    if not role_path.is_absolute():
        role_path = (REPO_ROOT / role_path).resolve()
    if not seed_path.is_absolute():
        seed_path = (REPO_ROOT / seed_path).resolve()
    if not camera_path.is_absolute():
        camera_path = (REPO_ROOT / camera_path).resolve()
    if not output_path.is_absolute():
        output_path = (REPO_ROOT / output_path).resolve()

    payload = run_trial(
        label=args.label,
        role_path=role_path,
        seed_path=seed_path,
        camera_path=camera_path,
        output_path=output_path,
        seed_ref=args.seed_ref,
        camera_ref=args.camera_ref,
        prefer_flow=args.prefer_flow,
    )
    print(json.dumps({"output_path": str(output_path.relative_to(REPO_ROOT)).replace("\\", "/"), "comparison_ab": payload["comparison_note_ab"], "flow_judgment": payload["flow_judgment"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
