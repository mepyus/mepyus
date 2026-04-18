from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Literal, Optional

from app.core.events.event_append_guard import append_jsonl_locked
from app.core.registry.atomic_io import atomic_write_json, file_lock, locked_load_json, make_idempotency_key


LineStatus = Literal["candidate", "probing", "stable", "operating"]
ThicknessLevel = Literal["thin", "medium", "thick"]
GroundingType = Literal["direct", "fallback", "inferred"]
EvidenceOriginKind = Literal[
    "primary_raw",
    "primary_structured",
    "derived_trace",
    "derived_report",
    "summary_echo",
]
IndependenceClass = Literal["primary", "derived", "self_referential_derived", "mixed"]
PromotionScope = Literal[
    "path_local",
    "source_family_local",
    "surface_family_local",
    "cross_family_candidate",
    "global_candidate",
    "global_operating",
]
ValidationProfile = Literal[
    "weak_summary_local",
    "path_heavy_material_narrow",
    "material_heavy_path_narrow",
    "balanced_broadening_candidate",
    "mixed_derived_supported",
    "insufficient_profile",
]
SupportEcologyBias = Literal[
    "primary_dominant",
    "mixed_derived_supported",
    "derived_heavy",
    "summary_only",
]
DerivedResidueTrend = Literal["decaying", "stable", "reappearing", "insufficient_history"]
DerivedResiduePersistence = Literal[
    "unconfirmed_decay",
    "persistent_decay",
    "stable_mixed",
    "reappearing",
    "insufficient_history",
]
DerivedResidueRobustness = Literal[
    "robust_decay",
    "weak_decay",
    "window_sensitive",
    "non_decay_stable",
    "insufficient_history",
]
DerivedSupportRole = Literal[
    "summary_only",
    "primary_dominant",
    "residue_present",
    "mixed_but_primary_stable",
    "derived_dependency_suspected",
    "derived_heavy",
]
ShareBucket = Literal["high", "medium", "low"]
DependencyHint = Literal["low", "medium", "high"]
BroadeningGapType = Literal[
    "missing_path_diversity",
    "missing_primary_material_breadth",
    "missing_independent_evidence",
    "summary_only",
    "mixed_gap",
]
NextMissingAxis = Literal["path", "primary_material", "independent_evidence", "multiple"]
DerivedReintroductionStatus = Literal[
    "not_observed",
    "observed_recently",
    "observed_but_outside_window",
    "insufficient_history",
]
DerivedReintroductionTrigger = Literal[
    "derived_route_refresh",
    "summary_echo_refresh",
    "mixed_source_refresh",
    "unknown",
]


@dataclass
class RereadObservation:
    run_id: str
    asset_or_surface: str
    view_type: str
    line_name: str
    evidence: str
    grounding_type: GroundingType
    support_points: list[str]
    weakness_points: list[str]
    next_probe_surface: str
    thickness_before: ThicknessLevel
    thickness_after: ThicknessLevel
    observed_at: str
    contradiction_points: list[str] = field(default_factory=list)
    caution_points: list[str] = field(default_factory=list)
    resistance_or_counterexample: list[str] = field(default_factory=list)
    source_kind: str = "other"
    source_path_or_ref: str = ""
    source_run_id_or_event_id: str = ""
    source_pointer: str = ""
    evidence_mode: str = "summary_echo"
    validation_path_id: str = ""
    evidence_origin_kind: EvidenceOriginKind = "summary_echo"
    independence_class: IndependenceClass = "self_referential_derived"
    material_anchor_id: str = ""
    material_anchor_kind: str = "mixed"
    material_source_path: str = ""
    material_anchor_summary: str = ""

    def __post_init__(self) -> None:
        if self.contradiction_points and not self.resistance_or_counterexample:
            self.resistance_or_counterexample = list(self.contradiction_points)
            return
        if not self.contradiction_points and not self.resistance_or_counterexample:
            self.resistance_or_counterexample = []


@dataclass
class LineRegistryEntry:
    line_id: str
    line_name: str
    status: LineStatus
    thickness_level: ThicknessLevel
    first_seen_at: str
    last_seen_at: str
    support_count: int
    contradiction_count: int
    weakness_count: int
    caution_count: int
    resistance_count: int = 0
    promotion_scope: PromotionScope = "path_local"
    scope_basis_summary: str = ""
    validation_profile: ValidationProfile = "insufficient_profile"
    profile_basis_summary: str = ""
    primary_only_validation_profile: ValidationProfile = "insufficient_profile"
    primary_only_basis_summary: str = ""
    support_ecology_bias: SupportEcologyBias = "summary_only"
    derived_support_role: DerivedSupportRole = "summary_only"
    derived_support_summary: str = ""
    primary_vs_derived_balance_summary: str = ""
    primary_support_share_bucket: ShareBucket = "low"
    derived_dependency_hint: DependencyHint = "high"
    broadening_gap_type: BroadeningGapType = "mixed_gap"
    next_missing_axis: NextMissingAxis = "multiple"
    gap_basis_summary: str = ""
    primary_support_row_count: int = 0
    derived_support_row_count: int = 0
    self_referential_derived_row_count: int = 0
    summary_row_count: int = 0
    cumulative_primary_rows: int = 0
    cumulative_derived_rows: int = 0
    recent_primary_rows: int = 0
    recent_derived_rows: int = 0
    recent_window_size_used: int = 0
    recent_primary_vs_derived_summary: str = ""
    derived_residue_trend: DerivedResidueTrend = "insufficient_history"
    derived_residue_trend_summary: str = ""
    recent_decay_streak: int = 0
    last_derived_support_offset: int = 0
    derived_residue_persistence: DerivedResiduePersistence = "insufficient_history"
    persistence_basis_summary: str = ""
    derived_residue_robustness: DerivedResidueRobustness = "insufficient_history"
    trend_window_agreement_summary: str = ""
    tested_window_sizes: list[int] = field(default_factory=list)
    derived_reintroduction_status: DerivedReintroductionStatus = "insufficient_history"
    derived_reintroduction_trigger: DerivedReintroductionTrigger = "unknown"
    last_derived_reintroduction_offset: int = 0
    primary_only_path_count: int = 0
    primary_only_material_count: int = 0
    primary_only_source_document_count: int = 0
    primary_only_independent_evidence_count: int = 0
    distinct_path_count: int = 0
    distinct_source_family_count: int = 0
    distinct_surface_family_count: int = 0
    distinct_run_count: int = 0
    distinct_asset_count: int = 0
    distinct_source_pointer_count: int = 0
    distinct_primary_source_family_count: int = 0
    distinct_derived_source_family_count: int = 0
    distinct_independent_evidence_count: int = 0
    distinct_material_anchor_count: int = 0
    distinct_primary_material_anchor_count: int = 0
    distinct_source_document_count: int = 0
    has_self_referential_derived_support: bool = False
    evidence_independence_summary: str = ""
    material_independence_summary: str = ""
    surface_types_seen: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


@dataclass
class PromotionDecision:
    line_id: str
    line_name: str
    status: LineStatus
    thickness_level: ThicknessLevel
    should_promote: bool
    reason: str
    signals: list[str]
    promotion_scope: PromotionScope
    scope_basis_summary: str
    validation_profile: ValidationProfile
    profile_basis_summary: str
    primary_only_validation_profile: ValidationProfile
    primary_only_basis_summary: str
    support_ecology_bias: SupportEcologyBias
    derived_support_role: DerivedSupportRole
    derived_support_summary: str
    primary_vs_derived_balance_summary: str
    primary_support_share_bucket: ShareBucket
    derived_dependency_hint: DependencyHint
    broadening_gap_type: BroadeningGapType
    next_missing_axis: NextMissingAxis
    gap_basis_summary: str
    primary_support_row_count: int
    derived_support_row_count: int
    self_referential_derived_row_count: int
    summary_row_count: int
    cumulative_primary_rows: int
    cumulative_derived_rows: int
    recent_primary_rows: int
    recent_derived_rows: int
    recent_window_size_used: int
    recent_primary_vs_derived_summary: str
    derived_residue_trend: DerivedResidueTrend
    derived_residue_trend_summary: str
    recent_decay_streak: int
    last_derived_support_offset: int
    derived_residue_persistence: DerivedResiduePersistence
    persistence_basis_summary: str
    derived_residue_robustness: DerivedResidueRobustness
    trend_window_agreement_summary: str
    tested_window_sizes: list[int]
    derived_reintroduction_status: DerivedReintroductionStatus
    derived_reintroduction_trigger: DerivedReintroductionTrigger
    last_derived_reintroduction_offset: int
    primary_only_path_count: int
    primary_only_material_count: int
    primary_only_source_document_count: int
    primary_only_independent_evidence_count: int
    distinct_path_count: int
    distinct_source_family_count: int
    distinct_surface_family_count: int
    distinct_run_count: int
    distinct_asset_count: int
    distinct_source_pointer_count: int
    distinct_primary_source_family_count: int
    distinct_derived_source_family_count: int
    distinct_independent_evidence_count: int
    distinct_material_anchor_count: int
    distinct_primary_material_anchor_count: int
    distinct_source_document_count: int
    has_self_referential_derived_support: bool
    evidence_independence_summary: str
    material_independence_summary: str
    evaluated_at: str


REGISTRY_PATH = Path("manifests/line_registry.json")
OBSERVATION_LOG_PATH = Path("logs/reread_observation_log.jsonl")
PROMOTION_LOG_PATH = Path("logs/line_promotion_log.jsonl")
REGISTRY_SCHEMA_VERSION = "line_registry_v0"


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _slugify(value: str) -> str:
    chars: list[str] = []
    for ch in value.lower():
        if ch.isalnum():
            chars.append(ch)
        else:
            chars.append("_")
    slug = "".join(chars).strip("_")
    while "__" in slug:
        slug = slug.replace("__", "_")
    return slug or "line"


def _line_id(line_name: str) -> str:
    return f"line_{_slugify(line_name)}"


def _registry_path(runtime_root: Path) -> Path:
    return runtime_root / REGISTRY_PATH


def _observation_log_path(runtime_root: Path) -> Path:
    return runtime_root / OBSERVATION_LOG_PATH


def _promotion_log_path(runtime_root: Path) -> Path:
    return runtime_root / PROMOTION_LOG_PATH


def _load_registry(runtime_root: Path) -> Dict[str, Any]:
    path = _registry_path(runtime_root)
    if not path.exists():
        return {
            "schema_version": REGISTRY_SCHEMA_VERSION,
            "updated_at": None,
            "lines": [],
        }
    payload = locked_load_json(path)
    if "lines" not in payload:
        payload["lines"] = []
    payload.setdefault("schema_version", REGISTRY_SCHEMA_VERSION)
    payload.setdefault("updated_at", None)
    return payload


def _save_registry(runtime_root: Path, payload: Dict[str, Any]) -> Path:
    payload = dict(payload)
    payload["updated_at"] = _now_iso()
    payload.setdefault("schema_version", REGISTRY_SCHEMA_VERSION)
    atomic_write_json(_registry_path(runtime_root), payload)
    return _registry_path(runtime_root)


def _load_lines(payload: Dict[str, Any]) -> list[Dict[str, Any]]:
    lines = payload.get("lines") or []
    return [dict(row) for row in lines if isinstance(row, dict)]


def _store_lines(payload: Dict[str, Any], lines: list[Dict[str, Any]]) -> Dict[str, Any]:
    new_payload = dict(payload)
    new_payload["lines"] = lines
    return new_payload


def _observation_signature(observation: RereadObservation) -> str:
    return make_idempotency_key(
        observation.run_id,
        observation.asset_or_surface,
        observation.view_type,
        observation.line_name,
        observation.evidence,
        observation.grounding_type,
        observation.next_probe_surface,
        observation.thickness_before,
        observation.thickness_after,
        observation.source_kind,
        observation.source_path_or_ref,
        observation.source_run_id_or_event_id,
        observation.source_pointer,
        observation.evidence_mode,
        observation.evidence_origin_kind,
        observation.independence_class,
        observation.material_anchor_id,
        observation.material_anchor_kind,
        observation.material_source_path,
        "|".join(observation.support_points),
        "|".join(observation.weakness_points),
        "|".join(observation.contradiction_points),
        "|".join(observation.caution_points),
        observation.validation_path_id,
    )


def _load_observation_rows(runtime_root: Path) -> list[Dict[str, Any]]:
    path = _observation_log_path(runtime_root)
    if not path.exists():
        return []
    rows: list[Dict[str, Any]] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        rows.append(json.loads(line))
    return rows


def _load_observation_rows_for_line(runtime_root: Path, line_name: str) -> list[Dict[str, Any]]:
    line_id = _line_id(line_name)
    return [
        row
        for row in _load_observation_rows(runtime_root)
        if _line_id(str(row.get("line_name") or "")) == line_id
    ]


def _observation_to_row(observation: RereadObservation) -> Dict[str, Any]:
    row = asdict(observation)
    origin_kind, independence_class = _classify_evidence_origin(row)
    row["evidence_origin_kind"] = origin_kind
    row["independence_class"] = independence_class
    material_anchor_id, material_anchor_kind, material_source_path, material_anchor_summary = _classify_material_anchor(row)
    row["material_anchor_id"] = material_anchor_id
    row["material_anchor_kind"] = material_anchor_kind
    row["material_source_path"] = material_source_path
    row["material_anchor_summary"] = material_anchor_summary
    row["observation_id"] = _observation_signature(observation)
    row["recorded_at"] = _now_iso()
    row["dedupe_key"] = row["observation_id"]
    return row


def append_reread_observation(runtime_root: Path, observation: RereadObservation) -> Dict[str, Any]:
    path = _observation_log_path(runtime_root)
    row = _observation_to_row(observation)
    existing = _load_observation_rows(runtime_root)
    if any(str(item.get("dedupe_key") or "") == row["dedupe_key"] for item in existing):
        return {
            "appended": False,
            "duplicate": True,
            "observation": row,
            "observation_log_path": str(path),
        }
    append_jsonl_locked(path, row)
    return {
        "appended": True,
        "duplicate": False,
        "observation": row,
        "observation_log_path": str(path),
    }


def _surface_label(observation: Dict[str, Any]) -> str:
    return f"{observation.get('view_type') or 'view'}:{observation.get('asset_or_surface') or 'surface'}"


def _is_primary_origin_kind(kind: str) -> bool:
    return kind in {"primary_raw", "primary_structured"}


def _is_derived_origin_kind(kind: str) -> bool:
    return kind in {"derived_trace", "derived_report", "summary_echo"}


def _classify_evidence_origin(observation: Dict[str, Any]) -> tuple[str, str]:
    validation_path = str(observation.get("validation_path_id") or "").strip()
    evidence_mode = str(observation.get("evidence_mode") or "summary_echo").strip()
    source_kind = str(observation.get("source_kind") or "other").strip()
    source_pointer = str(observation.get("source_pointer") or "").strip()
    source_path = str(observation.get("source_path_or_ref") or "").strip()
    asset_or_surface = str(observation.get("asset_or_surface") or "").strip()

    if evidence_mode == "summary_echo" or source_kind == "preflight_decision":
        return "summary_echo", "self_referential_derived"
    if validation_path == "structured_doc_routing":
        if asset_or_surface.endswith(".md") or "summary" in asset_or_surface or "report" in asset_or_surface:
            return "derived_report", "self_referential_derived"
        return "derived_trace", "self_referential_derived"
    if source_kind == "trace_log":
        return "derived_trace", "derived"
    if source_kind == "raw_surface":
        if "source_range=" in source_pointer:
            return "primary_raw", "primary"
        return "primary_structured", "primary"
    if source_path.endswith(".md") and "generated" in source_path:
        return "derived_report", "self_referential_derived"
    if source_path.endswith(".json") and "generated" in source_path:
        return "derived_trace", "self_referential_derived"
    if evidence_mode == "direct_span":
        return "primary_raw", "primary"
    if evidence_mode == "source_linked":
        return "primary_structured", "primary"
    return "summary_echo", "mixed"


def _scope_source_path(observation: Dict[str, Any]) -> str:
    return str(observation.get("source_path_or_ref") or observation.get("asset_or_surface") or "").strip()


def _scope_source_family(observation: Dict[str, Any]) -> str:
    raw_value = _scope_source_path(observation)
    if not raw_value:
        return ""
    value = Path(raw_value).name
    if "." in value:
        value = value.rsplit(".", 1)[0]
    while value and value[-1].isdigit():
        value = value[:-1]
    value = value.rstrip("_- ")
    return value or Path(raw_value).stem


def _extract_fragment_id(observation: Dict[str, Any]) -> str:
    run_id = str(observation.get("run_id") or "").strip()
    if ":" in run_id:
        prefix, suffix = run_id.split(":", 1)
        if prefix in {"internal_observer", "source_fragment_view"} and suffix:
            return suffix
    source_pointer = str(observation.get("source_pointer") or "").strip()
    if "fragment_id=" in source_pointer:
        return source_pointer.split("fragment_id=", 1)[1].split(";", 1)[0].split("#", 1)[0].strip()
    if "runtime/fragments/" in source_pointer:
        tail = source_pointer.split("runtime/fragments/", 1)[1]
        return tail.split(".json", 1)[0].strip()
    return ""


def _classify_material_anchor(observation: Dict[str, Any]) -> tuple[str, str, str, str]:
    source_path = _scope_source_path(observation)
    fragment_id = _extract_fragment_id(observation)
    source_pointer = str(observation.get("source_pointer") or "").strip()
    evidence_mode = str(observation.get("evidence_mode") or "").strip()

    if fragment_id:
        return (
            f"fragment:{fragment_id}",
            "fragment",
            source_path,
            f"fragment={fragment_id}; source_path={source_path or 'n/a'}",
        )
    if "source_range=" in source_pointer:
        pointer_tail = source_pointer.split("#", 1)[1] if "#" in source_pointer else source_pointer
        return (
            f"source_range:{source_path}#{pointer_tail}",
            "source_range",
            source_path,
            f"source_range={pointer_tail}; source_path={source_path or 'n/a'}",
        )
    if source_pointer:
        pointer_tail = source_pointer.split("#", 1)[1] if "#" in source_pointer else source_pointer
        return (
            f"row:{source_path}#{pointer_tail}",
            "row",
            source_path,
            f"row_pointer={pointer_tail}; source_path={source_path or 'n/a'}",
        )
    if source_path and evidence_mode == "source_linked":
        return (
            f"section:{source_path}",
            "section",
            source_path,
            f"section_like_source={source_path}",
        )
    return ("", "mixed", source_path, "")


def _normalized_evidence_origin_kind(observation: Dict[str, Any]) -> str:
    value = str(observation.get("evidence_origin_kind") or "").strip()
    if value:
        return value
    return _classify_evidence_origin(observation)[0]


def _normalized_independence_class(observation: Dict[str, Any]) -> str:
    value = str(observation.get("independence_class") or "").strip()
    if value:
        return value
    return _classify_evidence_origin(observation)[1]


def _observed_source_paths(observations: Iterable[Dict[str, Any]]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for observation in observations:
        if not str(observation.get("line_name") or "").strip():
            continue
        source_path = _scope_source_path(observation)
        if not source_path or source_path in seen:
            continue
        seen.add(source_path)
        ordered.append(source_path)
    return ordered


def _observed_source_families(observations: Iterable[Dict[str, Any]]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for observation in observations:
        if not str(observation.get("line_name") or "").strip():
            continue
        family = _scope_source_family(observation)
        if not family or family in seen:
            continue
        seen.add(family)
        ordered.append(family)
    return ordered


def _increment_support(observation: Dict[str, Any]) -> int:
    support_points = observation.get("support_points") or []
    if support_points:
        return 1
    if str(observation.get("grounding_type") or "") == "direct":
        return 1
    return 0


def _increment_contradiction(observation: Dict[str, Any]) -> int:
    contradiction = observation.get("contradiction_points") or []
    if contradiction:
        return 1
    legacy = observation.get("resistance_or_counterexample") or []
    return 1 if _looks_like_contradiction(legacy) else 0


def _increment_weakness(observation: Dict[str, Any]) -> int:
    weakness = observation.get("weakness_points") or []
    return 1 if weakness else 0


def _increment_caution(observation: Dict[str, Any]) -> int:
    caution = observation.get("caution_points") or []
    if caution:
        return 1
    legacy = observation.get("resistance_or_counterexample") or []
    if legacy and not _looks_like_contradiction(legacy):
        return 1
    return 0


def _looks_like_contradiction(points: Iterable[str]) -> bool:
    text = " ".join(str(point).strip().lower() for point in points if str(point).strip())
    if not text:
        return False
    contradiction_keywords = (
        "counterexample",
        "contradict",
        "contradiction",
        "refut",
        "invalidate",
        "invalid",
        "breaks",
        "broken",
        "false",
        "wrong",
        "oppos",
    )
    return any(keyword in text for keyword in contradiction_keywords)


def _aggregate_line_metrics(observations: Iterable[Dict[str, Any]]) -> Dict[str, Any]:
    rows = [row for row in observations if str(row.get("line_name") or "").strip()]
    support_count = sum(_increment_support(row) for row in rows)
    contradiction_count = sum(_increment_contradiction(row) for row in rows)
    weakness_count = sum(_increment_weakness(row) for row in rows)
    caution_count = sum(_increment_caution(row) for row in rows)
    surface_types_seen = _dedupe_preserve_order([_surface_label(row) for row in rows])
    source_paths_seen = _dedupe_preserve_order([_scope_source_path(row) for row in rows if _scope_source_path(row)])
    return {
        "support_count": support_count,
        "contradiction_count": contradiction_count,
        "weakness_count": weakness_count,
        "caution_count": caution_count,
        "surface_types_seen": surface_types_seen,
        "source_paths_seen": source_paths_seen,
    }


def _observed_evidence_modes(observations: Iterable[Dict[str, Any]]) -> set[str]:
    return {
        str(observation.get("evidence_mode") or "summary_echo")
        for observation in observations
        if str(observation.get("line_name") or "").strip()
    }


def _observed_evidence_origin_kinds(observations: Iterable[Dict[str, Any]]) -> set[str]:
    kinds: set[str] = set()
    for observation in observations:
        if not str(observation.get("line_name") or "").strip():
            continue
        kind = _normalized_evidence_origin_kind(observation)
        if kind:
            kinds.add(kind)
    return kinds


def _observed_independence_classes(observations: Iterable[Dict[str, Any]]) -> set[str]:
    classes: set[str] = set()
    for observation in observations:
        if not str(observation.get("line_name") or "").strip():
            continue
        value = _normalized_independence_class(observation)
        if value:
            classes.add(value)
    return classes


def _observed_source_kinds(observations: Iterable[Dict[str, Any]]) -> set[str]:
    return {
        str(observation.get("source_kind") or "other")
        for observation in observations
        if str(observation.get("line_name") or "").strip()
    }


def _observed_source_pointers(observations: Iterable[Dict[str, Any]]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for observation in observations:
        if not str(observation.get("line_name") or "").strip():
            continue
        pointer = str(observation.get("source_pointer") or "").strip()
        if not pointer or pointer in seen:
            continue
        seen.add(pointer)
        ordered.append(pointer)
    return ordered


def _observed_primary_validation_paths(observations: Iterable[Dict[str, Any]]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for observation in observations:
        if not str(observation.get("line_name") or "").strip():
            continue
        if not _is_primary_origin_kind(_normalized_evidence_origin_kind(observation)):
            continue
        value = str(observation.get("validation_path_id") or "").strip()
        if not value or value in seen:
            continue
        seen.add(value)
        ordered.append(value)
    return ordered


def _observed_primary_source_families(observations: Iterable[Dict[str, Any]]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for observation in observations:
        if not str(observation.get("line_name") or "").strip():
            continue
        if not _is_primary_origin_kind(_normalized_evidence_origin_kind(observation)):
            continue
        family = _scope_source_family(observation)
        if not family or family in seen:
            continue
        seen.add(family)
        ordered.append(family)
    return ordered


def _observed_material_anchor_ids(observations: Iterable[Dict[str, Any]]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for observation in observations:
        if not str(observation.get("line_name") or "").strip():
            continue
        value = str(observation.get("material_anchor_id") or "").strip()
        if not value:
            value = _classify_material_anchor(observation)[0]
        if not value or value in seen:
            continue
        seen.add(value)
        ordered.append(value)
    return ordered


def _observed_primary_material_anchor_ids(observations: Iterable[Dict[str, Any]]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for observation in observations:
        if not str(observation.get("line_name") or "").strip():
            continue
        if not _is_primary_origin_kind(_normalized_evidence_origin_kind(observation)):
            continue
        value = str(observation.get("material_anchor_id") or "").strip()
        if not value:
            value = _classify_material_anchor(observation)[0]
        if not value or value in seen:
            continue
        seen.add(value)
        ordered.append(value)
    return ordered


def _observed_source_documents(observations: Iterable[Dict[str, Any]]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for observation in observations:
        if not str(observation.get("line_name") or "").strip():
            continue
        value = str(observation.get("material_source_path") or "").strip()
        if not value:
            value = str(_classify_material_anchor(observation)[2] or _scope_source_path(observation) or "").strip()
        if not value or value in seen:
            continue
        seen.add(value)
        ordered.append(value)
    return ordered


def _observed_derived_source_families(observations: Iterable[Dict[str, Any]]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for observation in observations:
        if not str(observation.get("line_name") or "").strip():
            continue
        if not _is_derived_origin_kind(_normalized_evidence_origin_kind(observation)):
            continue
        family = _scope_source_family(observation)
        if not family or family in seen:
            continue
        seen.add(family)
        ordered.append(family)
    return ordered


def _observed_validation_paths(observations: Iterable[Dict[str, Any]]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for observation in observations:
        if not str(observation.get("line_name") or "").strip():
            continue
        if str(observation.get("evidence_mode") or "summary_echo") == "summary_echo":
            continue
        value = str(observation.get("validation_path_id") or "").strip()
        if not value or value in seen:
            continue
        seen.add(value)
        ordered.append(value)
    return ordered


def _surface_family_key(surface_type: str) -> str:
    if not surface_type:
        return ""
    return str(surface_type).split(":", 1)[0].strip()


def _observed_contradiction_count(observations: Iterable[Dict[str, Any]]) -> int:
    return sum(1 for observation in observations if _increment_contradiction(observation))


def _observed_weakness_count(observations: Iterable[Dict[str, Any]]) -> int:
    return sum(1 for observation in observations if bool(observation.get("weakness_points") or []))


def _observed_caution_count(observations: Iterable[Dict[str, Any]]) -> int:
    return sum(1 for observation in observations if _increment_caution(observation))


def _observed_independent_evidence_count(observations: Iterable[Dict[str, Any]]) -> int:
    return len(_observed_primary_validation_paths(observations))


def _evidence_independence_summary(observations: Iterable[Dict[str, Any]]) -> str:
    primary_paths = _observed_primary_validation_paths(observations)
    primary_families = _observed_primary_source_families(observations)
    derived_families = _observed_derived_source_families(observations)
    origin_kinds = _observed_evidence_origin_kinds(observations)
    self_ref = "yes" if "self_referential_derived" in _observed_independence_classes(observations) else "no"
    return (
        f"primary_paths={len(primary_paths)}; primary_families={len(primary_families)}; "
        f"derived_families={len(derived_families)}; origin_kinds={';'.join(sorted(origin_kinds)) or 'n/a'}; "
        f"self_referential_derived={self_ref}"
    )


def _material_independence_summary(observations: Iterable[Dict[str, Any]]) -> str:
    material_anchors = _observed_material_anchor_ids(observations)
    primary_material_anchors = _observed_primary_material_anchor_ids(observations)
    source_documents = _observed_source_documents(observations)
    anchor_kinds = sorted(
        {
            str(observation.get("material_anchor_kind") or "mixed")
            for observation in observations
            if str(observation.get("line_name") or "").strip()
        }
    )
    return (
        f"material_anchors={len(material_anchors)}; primary_material_anchors={len(primary_material_anchors)}; "
        f"source_documents={len(source_documents)}; anchor_kinds={';'.join(anchor_kinds) or 'n/a'}"
    )


def _primary_only_observations(observations: Iterable[Dict[str, Any]]) -> list[Dict[str, Any]]:
    return [
        observation
        for observation in observations
        if str(observation.get("line_name") or "").strip()
        and _is_primary_origin_kind(_normalized_evidence_origin_kind(observation))
    ]


def _primary_only_source_documents(observations: Iterable[Dict[str, Any]]) -> list[str]:
    return _observed_source_documents(_primary_only_observations(observations))


def _derive_support_ecology_bias(
    *,
    primary_count: int,
    derived_count: int,
    summary_echo_only: bool,
) -> SupportEcologyBias:
    if summary_echo_only:
        return "summary_only"
    if primary_count > 0 and derived_count > 0:
        return "mixed_derived_supported"
    if primary_count > 0:
        return "primary_dominant"
    return "derived_heavy"


def _support_role_counts(observations: Iterable[Dict[str, Any]]) -> tuple[int, int, int, int]:
    primary_count = 0
    derived_count = 0
    self_ref_count = 0
    summary_count = 0
    for observation in observations:
        if not str(observation.get("line_name") or "").strip():
            continue
        origin_kind = _normalized_evidence_origin_kind(observation)
        independence_class = _normalized_independence_class(observation)
        if origin_kind == "summary_echo":
            summary_count += 1
        elif _is_primary_origin_kind(origin_kind):
            primary_count += 1
        elif _is_derived_origin_kind(origin_kind):
            derived_count += 1
            if independence_class == "self_referential_derived":
                self_ref_count += 1
    return primary_count, derived_count, self_ref_count, summary_count


def _derive_derived_residue_trend(
    observations: Iterable[Dict[str, Any]],
    *,
    window_size: int = 5,
) -> tuple[
    DerivedResidueTrend,
    int,
    int,
    int,
    int,
    int,
    int,
    str,
    str,
]:
    rows = [row for row in observations if str(row.get("line_name") or "").strip()]
    cumulative_primary_rows, cumulative_derived_rows, _, summary_row_count = _support_role_counts(rows)
    recent_rows = rows[-window_size:] if window_size > 0 else rows
    previous_rows = rows[:-window_size] if window_size > 0 and len(rows) > window_size else []
    recent_primary_rows, recent_derived_rows, _, _ = _support_role_counts(recent_rows)
    previous_primary_rows, previous_derived_rows, _, _ = _support_role_counts(previous_rows)
    recent_window_size_used = len(recent_rows)
    cumulative_non_summary = cumulative_primary_rows + cumulative_derived_rows
    recent_non_summary = recent_primary_rows + recent_derived_rows
    previous_non_summary = previous_primary_rows + previous_derived_rows

    recent_primary_share = recent_primary_rows / recent_non_summary if recent_non_summary else 0.0
    recent_derived_share = recent_derived_rows / recent_non_summary if recent_non_summary else 0.0
    previous_derived_share = previous_derived_rows / previous_non_summary if previous_non_summary else 0.0

    if cumulative_non_summary < 3:
        trend: DerivedResidueTrend = "insufficient_history"
    elif cumulative_derived_rows == 0:
        trend = "stable" if cumulative_primary_rows >= 3 else "insufficient_history"
    elif recent_derived_rows == 0:
        trend = "decaying"
    elif previous_non_summary == 0:
        trend = "reappearing"
    elif recent_derived_share <= max(0.15, previous_derived_share - 0.15):
        trend = "decaying"
    elif recent_derived_share >= previous_derived_share + 0.15 and recent_derived_rows >= 2:
        trend = "reappearing"
    else:
        trend = "stable"

    recent_summary = (
        f"recent_window={recent_primary_rows}/{recent_derived_rows}; "
        f"cumulative={cumulative_primary_rows}/{cumulative_derived_rows}; "
        f"previous_window={previous_primary_rows}/{previous_derived_rows}; "
        f"summary_rows={summary_row_count}"
    )
    trend_summary = (
        f"trend={trend}; recent_primary_share={recent_primary_share:.2f}; "
        f"recent_derived_share={recent_derived_share:.2f}; previous_derived_share={previous_derived_share:.2f}; "
        f"window_size={recent_window_size_used}"
    )
    return (
        trend,
        cumulative_primary_rows,
        cumulative_derived_rows,
        recent_primary_rows,
        recent_derived_rows,
        recent_window_size_used,
        summary_row_count,
        recent_summary,
        trend_summary,
    )


def _derive_derived_residue_persistence(
    observations: Iterable[Dict[str, Any]],
    *,
    window_size: int = 5,
) -> tuple[DerivedResiduePersistence, int, int, str]:
    rows = [row for row in observations if str(row.get("line_name") or "").strip()]
    if len(rows) < 3:
        return (
            "insufficient_history",
            0,
            0,
            f"history_too_short={len(rows)}; window_size={window_size}",
        )

    recent_rows = rows[-window_size:] if window_size > 0 else rows
    cumulative_primary_rows, cumulative_derived_rows, _, _ = _support_role_counts(rows)
    recent_primary_rows, recent_derived_rows, _, _ = _support_role_counts(recent_rows)
    last_derived_support_offset = 0
    found_derived = False
    for idx in range(len(rows) - 1, -1, -1):
        origin_kind = _normalized_evidence_origin_kind(rows[idx])
        if _is_derived_origin_kind(origin_kind):
            last_derived_support_offset = len(rows) - idx - 1
            found_derived = True
            break
    if not found_derived:
        last_derived_support_offset = len(rows)

    recent_decay_streak = 0
    cursor = len(rows)
    while cursor > 0:
        start = max(0, cursor - window_size)
        window = rows[start:cursor]
        if not window:
            break
        _, window_derived_rows, _, _ = _support_role_counts(window)
        if window_derived_rows == 0:
            recent_decay_streak += 1
            if start == 0:
                break
            cursor = start
            continue
        break

    recent_window_has_derived = recent_derived_rows > 0
    trend_hint = "decaying" if not recent_window_has_derived else "reappearing" if recent_derived_rows > cumulative_derived_rows / 2 else "stable"

    if cumulative_primary_rows + cumulative_derived_rows < window_size:
        persistence: DerivedResiduePersistence = "insufficient_history"
    elif cumulative_derived_rows == 0 and cumulative_primary_rows >= window_size:
        persistence = "stable_mixed"
    elif recent_window_has_derived:
        persistence = "reappearing" if recent_derived_rows >= 2 else "stable_mixed"
    elif recent_decay_streak >= 2 and last_derived_support_offset >= window_size:
        persistence = "persistent_decay"
    elif recent_decay_streak >= 1 and trend_hint == "decaying":
        persistence = "unconfirmed_decay"
    else:
        persistence = "insufficient_history"

    basis_summary = (
        f"trend_hint={trend_hint}; recent_decay_streak={recent_decay_streak}; "
        f"last_derived_support_offset={last_derived_support_offset}; "
        f"recent_primary_rows={recent_primary_rows}; recent_derived_rows={recent_derived_rows}; "
        f"cumulative_primary_rows={cumulative_primary_rows}; cumulative_derived_rows={cumulative_derived_rows}"
    )
    return persistence, recent_decay_streak, last_derived_support_offset, basis_summary


def _derive_derived_residue_robustness(
    observations: Iterable[Dict[str, Any]],
    *,
    window_sizes: Iterable[int] = (3, 5, 7, 9),
) -> tuple[DerivedResidueRobustness, str, list[int]]:
    rows = [row for row in observations if str(row.get("line_name") or "").strip()]
    tested_window_sizes = [size for size in window_sizes if size > 0]
    if len(rows) < 3 or not tested_window_sizes:
        return "insufficient_history", f"history_too_short={len(rows)}", tested_window_sizes

    informative: list[tuple[int, DerivedResidueTrend, DerivedResiduePersistence, int, int]] = []
    for window_size in tested_window_sizes:
        trend, _, _, recent_primary_rows, recent_derived_rows, _, _, _, _ = _derive_derived_residue_trend(
            rows,
            window_size=window_size,
        )
        persistence, _, _, _ = _derive_derived_residue_persistence(
            rows,
            window_size=window_size,
        )
        if trend == "insufficient_history" and persistence == "insufficient_history":
            continue
        informative.append(
            (window_size, trend, persistence, recent_primary_rows, recent_derived_rows)
        )

    if not informative:
        return (
            "insufficient_history",
            f"informative_windows=0; tested={','.join(str(size) for size in tested_window_sizes)}",
            tested_window_sizes,
        )

    trend_set = {trend for _, trend, _, _, _ in informative}
    persistence_set = {persistence for _, _, persistence, _, _ in informative}
    decay_windows = [
        size
        for size, trend, persistence, _, _ in informative
        if trend == "decaying" and persistence in {"persistent_decay", "unconfirmed_decay"}
    ]
    stable_windows = [
        size
        for size, trend, persistence, _, _ in informative
        if trend == "stable" and persistence == "stable_mixed"
    ]
    conflict_windows = [
        size
        for size, trend, persistence, _, _ in informative
        if trend == "reappearing" or persistence == "reappearing"
    ]

    if conflict_windows or (len(trend_set) > 1 and not trend_set <= {"decaying", "stable"}):
        robustness: DerivedResidueRobustness = "window_sensitive"
    elif len(decay_windows) >= 2 and not conflict_windows and not stable_windows:
        robustness = "robust_decay"
    elif len(decay_windows) >= 1:
        robustness = "weak_decay"
    elif stable_windows and not decay_windows:
        robustness = "non_decay_stable"
    else:
        robustness = "window_sensitive"

    agreement_summary = "; ".join(
        f"w={size}:trend={trend},persistence={persistence},recent={recent_primary_rows}/{recent_derived_rows}"
        for size, trend, persistence, recent_primary_rows, recent_derived_rows in informative
    )
    return robustness, agreement_summary, tested_window_sizes


def _classify_reintroduction_trigger(row: Dict[str, Any]) -> DerivedReintroductionTrigger:
    origin_kind = _normalized_evidence_origin_kind(row)
    validation_path_id = str(row.get("validation_path_id") or "").strip()
    if origin_kind in {"derived_report", "derived_trace"} or validation_path_id == "structured_doc_routing":
        return "derived_route_refresh"
    if origin_kind == "summary_echo":
        return "summary_echo_refresh"
    if origin_kind in {"primary_raw", "primary_structured"} and str(row.get("independence_class") or "").strip() == "mixed":
        return "mixed_source_refresh"
    return "unknown"


def _derive_derived_reintroduction_sentinel(
    observations: Iterable[Dict[str, Any]],
    *,
    window_size: int = 5,
) -> tuple[DerivedReintroductionStatus, DerivedReintroductionTrigger, int]:
    rows = [row for row in observations if str(row.get("line_name") or "").strip()]
    if len(rows) < 3:
        return "insufficient_history", "unknown", 0

    non_summary_kinds = {
        _normalized_evidence_origin_kind(row)
        for row in rows
        if _normalized_evidence_origin_kind(row) in {"primary_raw", "primary_structured", "derived_trace", "derived_report"}
    }
    if not non_summary_kinds:
        return "insufficient_history", "unknown", 0

    last_derived_row: Optional[Dict[str, Any]] = None
    last_derived_offset = 0
    for idx in range(len(rows) - 1, -1, -1):
        origin_kind = _normalized_evidence_origin_kind(rows[idx])
        if _is_derived_origin_kind(origin_kind):
            last_derived_row = rows[idx]
            last_derived_offset = len(rows) - idx - 1
            break

    if last_derived_row is None:
        return "not_observed", "unknown", len(rows)

    trigger = _classify_reintroduction_trigger(last_derived_row)
    if last_derived_offset < window_size:
        return "observed_recently", trigger, last_derived_offset
    return "observed_but_outside_window", trigger, last_derived_offset


def _share_bucket(numerator: int, denominator: int) -> ShareBucket:
    if denominator <= 0:
        return "low"
    ratio = numerator / denominator
    if ratio >= 0.7:
        return "high"
    if ratio >= 0.4:
        return "medium"
    return "low"


def _derive_derived_support_role(
    *,
    summary_echo_only: bool,
    support_ecology_bias: SupportEcologyBias,
    primary_support_row_count: int,
    derived_support_row_count: int,
    self_referential_derived_row_count: int,
    validation_profile: ValidationProfile,
    primary_only_validation_profile: ValidationProfile,
) -> tuple[DerivedSupportRole, ShareBucket, DependencyHint, str, str]:
    non_summary_total = primary_support_row_count + derived_support_row_count
    primary_bucket = _share_bucket(primary_support_row_count, non_summary_total)
    if summary_echo_only:
        return (
            "summary_only",
            "low",
            "high",
            f"summary_only=yes; primary_rows={primary_support_row_count}; derived_rows={derived_support_row_count}; self_ref_rows={self_referential_derived_row_count}",
            f"primary_rows={primary_support_row_count}; derived_rows={derived_support_row_count}; self_ref_rows={self_referential_derived_row_count}",
        )
    if derived_support_row_count == 0:
        return (
            "primary_dominant",
            primary_bucket,
            "low",
            f"no_derived_support; primary_rows={primary_support_row_count}; derived_rows=0",
            f"primary_rows={primary_support_row_count}; derived_rows=0; self_ref_rows=0",
        )
    if (
        primary_only_validation_profile == "balanced_broadening_candidate"
        and validation_profile == "mixed_derived_supported"
        and primary_support_row_count >= derived_support_row_count
    ):
        return (
            "mixed_but_primary_stable",
            primary_bucket,
            "medium",
            f"primary_only_strong_but_mixed_overall; primary_rows={primary_support_row_count}; derived_rows={derived_support_row_count}; self_ref_rows={self_referential_derived_row_count}",
            f"primary_rows={primary_support_row_count}; derived_rows={derived_support_row_count}; self_ref_rows={self_referential_derived_row_count}",
        )
    if support_ecology_bias == "derived_heavy" or derived_support_row_count > primary_support_row_count:
        return (
            "derived_heavy",
            primary_bucket,
            "high",
            f"derived_rows_dominate; primary_rows={primary_support_row_count}; derived_rows={derived_support_row_count}; self_ref_rows={self_referential_derived_row_count}",
            f"primary_rows={primary_support_row_count}; derived_rows={derived_support_row_count}; self_ref_rows={self_referential_derived_row_count}",
        )
    if self_referential_derived_row_count >= max(1, derived_support_row_count // 2) and primary_support_row_count <= 1:
        return (
            "derived_dependency_suspected",
            primary_bucket,
            "high",
            f"limited_primary_base_with_self_referential_support; primary_rows={primary_support_row_count}; derived_rows={derived_support_row_count}; self_ref_rows={self_referential_derived_row_count}",
            f"primary_rows={primary_support_row_count}; derived_rows={derived_support_row_count}; self_ref_rows={self_referential_derived_row_count}",
        )
    return (
        "residue_present",
        primary_bucket,
        "low",
        f"derived_residue_present_without_clear_dependency; primary_rows={primary_support_row_count}; derived_rows={derived_support_row_count}; self_ref_rows={self_referential_derived_row_count}",
        f"primary_rows={primary_support_row_count}; derived_rows={derived_support_row_count}; self_ref_rows={self_referential_derived_row_count}",
    )


def _derive_primary_only_validation_profile(
    observations: Iterable[Dict[str, Any]],
) -> tuple[ValidationProfile, str, int, int, int, int]:
    primary_observations = _primary_only_observations(observations)
    if not primary_observations:
        return (
            "weak_summary_local",
            "no_primary_evidence; primary_paths=0; primary_materials=0; primary_documents=0",
            0,
            0,
            0,
            0,
        )
    primary_path_count = len(_observed_primary_validation_paths(primary_observations))
    primary_material_count = len(_observed_primary_material_anchor_ids(primary_observations))
    primary_source_document_count = len(_primary_only_source_documents(primary_observations))
    primary_independent_evidence_count = len(_observed_primary_validation_paths(primary_observations))
    profile, summary = _derive_validation_profile(
        status="stable",
        thickness="thick" if primary_material_count >= 2 else "medium" if primary_material_count >= 1 else "thin",
        distinct_path_count=primary_path_count,
        distinct_independent_evidence_count=primary_independent_evidence_count,
        distinct_primary_material_anchor_count=primary_material_count,
        has_self_referential_derived_support=False,
        summary_echo_only=False,
    )
    return (
        profile,
        f"primary_only; {summary}; primary_documents={primary_source_document_count}",
        primary_path_count,
        primary_material_count,
        primary_source_document_count,
        primary_independent_evidence_count,
    )


def _derive_validation_profile(
    *,
    status: LineStatus,
    thickness: ThicknessLevel,
    distinct_path_count: int,
    distinct_independent_evidence_count: int,
    distinct_primary_material_anchor_count: int,
    has_self_referential_derived_support: bool,
    summary_echo_only: bool,
) -> tuple[ValidationProfile, str]:
    if summary_echo_only:
        return (
            "weak_summary_local",
            f"summary_echo_only; paths={distinct_path_count}; independent_evidence={distinct_independent_evidence_count}; primary_materials={distinct_primary_material_anchor_count}",
        )
    if (
        distinct_path_count >= 2
        and distinct_independent_evidence_count >= 2
        and distinct_primary_material_anchor_count <= 2
    ):
        return (
            "path_heavy_material_narrow",
            f"path_rich={distinct_path_count}; independent_evidence={distinct_independent_evidence_count}; primary_materials={distinct_primary_material_anchor_count}",
        )
    if distinct_path_count <= 1 and distinct_primary_material_anchor_count >= 3:
        return (
            "material_heavy_path_narrow",
            f"path_rich={distinct_path_count}; independent_evidence={distinct_independent_evidence_count}; primary_materials={distinct_primary_material_anchor_count}",
        )
    if (
        distinct_path_count >= 2
        and distinct_primary_material_anchor_count >= 3
        and distinct_independent_evidence_count >= 2
        and not has_self_referential_derived_support
    ):
        return (
            "balanced_broadening_candidate",
            f"path_rich={distinct_path_count}; independent_evidence={distinct_independent_evidence_count}; primary_materials={distinct_primary_material_anchor_count}",
        )
    if has_self_referential_derived_support and (status in {"stable", "operating"} or thickness == "thick"):
        return (
            "mixed_derived_supported",
            f"self_referential_derived_support=yes; paths={distinct_path_count}; primary_materials={distinct_primary_material_anchor_count}",
        )
    return (
        "insufficient_profile",
        f"status={status}; thickness={thickness}; paths={distinct_path_count}; independent_evidence={distinct_independent_evidence_count}; primary_materials={distinct_primary_material_anchor_count}",
    )


def _derive_broadening_gap(
    *,
    validation_profile: ValidationProfile,
    distinct_path_count: int,
    distinct_independent_evidence_count: int,
    distinct_primary_material_anchor_count: int,
    has_self_referential_derived_support: bool,
    summary_echo_only: bool,
) -> tuple[BroadeningGapType, NextMissingAxis, str]:
    if summary_echo_only:
        return (
            "summary_only",
            "multiple",
            f"summary_echo_only=yes; path_count={distinct_path_count}; independent_evidence={distinct_independent_evidence_count}; primary_materials={distinct_primary_material_anchor_count}",
        )
    if validation_profile == "path_heavy_material_narrow":
        return (
            "missing_primary_material_breadth",
            "primary_material",
            f"path_count={distinct_path_count}; independent_evidence={distinct_independent_evidence_count}; primary_materials={distinct_primary_material_anchor_count}",
        )
    if validation_profile == "material_heavy_path_narrow":
        return (
            "missing_path_diversity",
            "path",
            f"path_count={distinct_path_count}; independent_evidence={distinct_independent_evidence_count}; primary_materials={distinct_primary_material_anchor_count}",
        )
    if distinct_independent_evidence_count < 2 and distinct_path_count >= 2 and distinct_primary_material_anchor_count >= 2:
        return (
            "missing_independent_evidence",
            "independent_evidence",
            f"path_count={distinct_path_count}; independent_evidence={distinct_independent_evidence_count}; primary_materials={distinct_primary_material_anchor_count}",
        )
    if has_self_referential_derived_support:
        return (
            "mixed_gap",
            "multiple",
            f"self_referential_derived_support=yes; path_count={distinct_path_count}; independent_evidence={distinct_independent_evidence_count}; primary_materials={distinct_primary_material_anchor_count}",
        )
    return (
        "mixed_gap",
        "multiple",
        f"profile={validation_profile}; path_count={distinct_path_count}; independent_evidence={distinct_independent_evidence_count}; primary_materials={distinct_primary_material_anchor_count}",
    )


def _derive_promotion_scope(
    *,
    line_name: str,
    support: int,
    contradiction_count: int,
    weakness_count: int,
    caution_count: int,
    evidence_modes: set[str],
    has_direct_span: bool,
    distinct_runs: int,
    distinct_assets: int,
    distinct_surfaces: int,
    distinct_source_pointers: int,
    distinct_path_count: int,
    distinct_source_paths: int,
    distinct_source_families: int,
    distinct_surface_families: int,
    distinct_primary_source_families: int,
    distinct_derived_source_families: int,
    distinct_independent_evidence_count: int,
    distinct_primary_material_anchor_count: int,
    has_self_referential_derived_support: bool,
    source_paths_seen: list[str],
    source_families_seen: list[str],
) -> tuple[PromotionScope, str]:
    primary_path = source_paths_seen[0] if source_paths_seen else "n/a"
    primary_family = source_families_seen[0] if source_families_seen else "n/a"
    if not evidence_modes or evidence_modes <= {"summary_echo"}:
        return "path_local", (
            f"summary_echo; path_count={distinct_path_count}; source_path={primary_path}; source_family={primary_family}"
        )
    independence_note = (
        f"primary_families={distinct_primary_source_families}; derived_families={distinct_derived_source_families}; "
        f"independent_evidence={distinct_independent_evidence_count}; self_referential_derived={str(has_self_referential_derived_support).lower()}"
    )
    if distinct_source_families <= 1:
        if distinct_source_pointers >= 2 or distinct_surfaces >= 2:
            return "source_family_local", (
                f"path_count={distinct_path_count}; single source family={primary_family}; "
                f"source_paths={distinct_source_paths}; source_pointers={distinct_source_pointers}; "
                f"surfaces={distinct_surfaces}; surface_families={distinct_surface_families}; {independence_note}"
            )
        return "path_local", (
            f"path_count={distinct_path_count}; single source family={primary_family}; local reread only; {independence_note}"
        )
    if distinct_source_families >= 2 and distinct_path_count <= 1 and distinct_source_pointers >= 2:
        basis = (
            f"path_count={distinct_path_count}; distinct source families={distinct_source_families}; "
            f"source_families={';'.join(source_families_seen)}; distinct source paths={distinct_source_paths}; "
            f"source_paths={';'.join(source_paths_seen)}; pointers={distinct_source_pointers}; "
            f"surfaces={distinct_surfaces}; surface_families={distinct_surface_families}; runs={distinct_runs}; assets={distinct_assets}; {independence_note}"
        )
        if has_direct_span and support >= 2 and contradiction_count == 0 and distinct_surfaces >= 2:
            return "cross_family_candidate", basis
        return "surface_family_local", basis
    if distinct_source_families >= 2 and distinct_path_count >= 2:
        basis = (
            f"path_count={distinct_path_count}; distinct source families={distinct_source_families}; "
            f"source_families={';'.join(source_families_seen)}; distinct source paths={distinct_source_paths}; "
            f"source_paths={';'.join(source_paths_seen)}; pointers={distinct_source_pointers}; "
            f"surfaces={distinct_surfaces}; surface_families={distinct_surface_families}; runs={distinct_runs}; assets={distinct_assets}; {independence_note}"
        )
        if (
            has_direct_span
            and support >= 5
            and contradiction_count == 0
            and distinct_runs >= 2
            and distinct_assets >= 2
            and distinct_surfaces >= 2
            and distinct_independent_evidence_count >= 2
            and distinct_primary_material_anchor_count >= 2
            and not has_self_referential_derived_support
        ):
            return "global_candidate", basis
        if has_direct_span and support >= 2 and contradiction_count == 0 and distinct_surfaces >= 2:
            return "cross_family_candidate", basis
        return "surface_family_local", basis
    return "path_local", (
        f"line={line_name}; support={support}; contradiction={contradiction_count}; "
        f"weakness={weakness_count}; caution={caution_count}; path_count={distinct_path_count}; "
        f"source_paths={distinct_source_paths}; pointers={distinct_source_pointers}; surface_families={distinct_surface_families}; {independence_note}"
    )


def evaluate_promotion_rule(
    entry: LineRegistryEntry,
    *,
    recent_observations: Optional[list[Dict[str, Any]]] = None,
) -> PromotionDecision:
    observations = recent_observations or []
    direct_grounding = any(str(obs.get("grounding_type") or "") == "direct" for obs in observations)
    evidence_modes = _observed_evidence_modes(observations)
    evidence_origin_kinds = _observed_evidence_origin_kinds(observations)
    independence_classes = _observed_independence_classes(observations)
    source_kinds = _observed_source_kinds(observations)
    source_pointers = _observed_source_pointers(observations)
    validation_paths = _observed_validation_paths(observations)
    primary_validation_paths = _observed_primary_validation_paths(observations)
    source_paths_seen = _observed_source_paths(observations)
    source_families_seen = _observed_source_families(observations)
    primary_source_families_seen = _observed_primary_source_families(observations)
    derived_source_families_seen = _observed_derived_source_families(observations)
    contradiction_count = _observed_contradiction_count(observations)
    weakness_count = _observed_weakness_count(observations)
    caution_count = _observed_caution_count(observations)
    independent_evidence_count = _observed_independent_evidence_count(observations)
    material_anchor_ids = _observed_material_anchor_ids(observations)
    primary_material_anchor_ids = _observed_primary_material_anchor_ids(observations)
    source_documents = _observed_source_documents(observations)
    has_self_referential_derived_support = "self_referential_derived" in independence_classes or "derived_report" in evidence_origin_kinds or "derived_trace" in evidence_origin_kinds
    summary_echo_only = evidence_modes <= {"summary_echo"}
    primary_observations = _primary_only_observations(observations)
    (
        primary_support_row_count,
        derived_support_row_count,
        self_referential_derived_row_count,
        summary_row_count,
    ) = _support_role_counts(observations)
    (
        derived_residue_trend,
        cumulative_primary_rows,
        cumulative_derived_rows,
        recent_primary_rows,
        recent_derived_rows,
        recent_window_size_used,
        _recent_summary_row_count,
        recent_primary_vs_derived_summary,
        derived_residue_trend_summary,
    ) = _derive_derived_residue_trend(observations)
    (
        derived_residue_persistence,
        recent_decay_streak,
        last_derived_support_offset,
        persistence_basis_summary,
    ) = _derive_derived_residue_persistence(observations)
    (
        derived_residue_robustness,
        trend_window_agreement_summary,
        tested_window_sizes,
    ) = _derive_derived_residue_robustness(observations)
    (
        derived_reintroduction_status,
        derived_reintroduction_trigger,
        last_derived_reintroduction_offset,
    ) = _derive_derived_reintroduction_sentinel(
        observations,
        window_size=recent_window_size_used or 5,
    )
    support_ecology_bias = _derive_support_ecology_bias(
        primary_count=len(primary_observations),
        derived_count=max(0, len(observations) - len(primary_observations)),
        summary_echo_only=summary_echo_only,
    )
    has_source_linked = any(mode in {"source_linked", "direct_span"} for mode in evidence_modes)
    has_direct_span = "direct_span" in evidence_modes
    distinct_runs = len({str(obs.get("run_id") or "") for obs in observations if str(obs.get("run_id") or "").strip()})
    distinct_assets = len({str(obs.get("asset_or_surface") or "") for obs in observations if str(obs.get("asset_or_surface") or "").strip()})
    distinct_surfaces = len(set(entry.surface_types_seen))
    distinct_source_pointers = len(source_pointers)
    distinct_path_count = len(validation_paths)
    distinct_source_paths = len(source_paths_seen)
    distinct_source_families = len(source_families_seen)
    distinct_surface_families = len({_surface_family_key(surface) for surface in entry.surface_types_seen if surface})
    has_direct_span = "direct_span" in evidence_modes
    support = entry.support_count
    weakness = getattr(entry, "weakness_count", 0)
    caution = getattr(entry, "caution_count", 0)
    existing_scope = getattr(entry, "promotion_scope", "path_local")
    existing_scope_basis = getattr(entry, "scope_basis_summary", "")
    scope, scope_basis_summary = _derive_promotion_scope(
        line_name=entry.line_name,
        support=support,
        contradiction_count=contradiction_count,
        weakness_count=weakness_count,
        caution_count=caution_count,
        evidence_modes=evidence_modes,
        has_direct_span=has_direct_span,
        distinct_runs=distinct_runs,
        distinct_assets=distinct_assets,
        distinct_surfaces=distinct_surfaces,
        distinct_source_pointers=distinct_source_pointers,
        distinct_path_count=distinct_path_count,
        distinct_source_paths=distinct_source_paths,
        distinct_source_families=distinct_source_families,
        distinct_surface_families=distinct_surface_families,
        distinct_primary_source_families=len(primary_source_families_seen),
        distinct_derived_source_families=len(derived_source_families_seen),
        distinct_independent_evidence_count=independent_evidence_count,
        distinct_primary_material_anchor_count=len(primary_material_anchor_ids),
        has_self_referential_derived_support=has_self_referential_derived_support,
        source_paths_seen=source_paths_seen,
        source_families_seen=source_families_seen,
    )
    signals: list[str] = []

    if direct_grounding:
        signals.append("direct_grounding_present")
    if source_kinds:
        signals.append("source_kind_observed")
    if summary_echo_only:
        signals.append("summary_echo_only")
    if has_source_linked:
        signals.append("source_linked_present")
    if has_direct_span:
        signals.append("direct_span_present")
    if distinct_source_pointers == 1 and len(observations) >= 2:
        signals.append("same_source_pointer_replay")
    if distinct_source_pointers >= 2:
        signals.append("distinct_source_pointer_repeat")
    if distinct_path_count >= 2:
        signals.append("distinct_validation_path_repeat")
    if primary_validation_paths:
        signals.append(f"primary_validation_paths={len(primary_validation_paths)}")
    if independent_evidence_count >= 1:
        signals.append(f"distinct_independent_evidence_count={independent_evidence_count}")
    if material_anchor_ids:
        signals.append(f"distinct_material_anchor_count={len(material_anchor_ids)}")
    if primary_material_anchor_ids:
        signals.append(f"distinct_primary_material_anchor_count={len(primary_material_anchor_ids)}")
    if source_documents:
        signals.append(f"distinct_source_document_count={len(source_documents)}")
    if primary_source_families_seen:
        signals.append(f"distinct_primary_source_family_count={len(primary_source_families_seen)}")
    if derived_source_families_seen:
        signals.append(f"distinct_derived_source_family_count={len(derived_source_families_seen)}")
    if has_self_referential_derived_support:
        signals.append("self_referential_derived_support_present")
    if distinct_surfaces >= 2:
        signals.append("multi_surface_repeat")
    if distinct_runs >= 2:
        signals.append("multi_run_repeat")
    if distinct_assets >= 2:
        signals.append("multi_asset_repeat")
    if support >= 2:
        signals.append("minimum_support_reached")
    if contradiction_count > 0:
        signals.append("contradiction_observed")
    if weakness_count > 0:
        signals.append("weakness_observed")
    if caution_count > 0:
        signals.append("caution_observed")
    if existing_scope and existing_scope != scope:
        signals.append(f"prior_scope={existing_scope}")
    if existing_scope_basis:
        signals.append("scope_basis_observed")
    signals.append(f"derived_residue_trend={derived_residue_trend}")
    signals.append(f"recent_window_size_used={recent_window_size_used}")
    signals.append(f"cumulative_primary_rows={cumulative_primary_rows}")
    signals.append(f"cumulative_derived_rows={cumulative_derived_rows}")
    signals.append(f"recent_primary_rows={recent_primary_rows}")
    signals.append(f"recent_derived_rows={recent_derived_rows}")
    signals.append(f"recent_primary_vs_derived_summary={recent_primary_vs_derived_summary}")
    signals.append(f"derived_residue_persistence={derived_residue_persistence}")
    signals.append(f"recent_decay_streak={recent_decay_streak}")
    signals.append(f"last_derived_support_offset={last_derived_support_offset}")
    signals.append(f"derived_residue_robustness={derived_residue_robustness}")
    signals.append(f"tested_window_sizes={','.join(str(size) for size in tested_window_sizes)}")
    signals.append(f"derived_reintroduction_status={derived_reintroduction_status}")
    signals.append(f"derived_reintroduction_trigger={derived_reintroduction_trigger}")
    signals.append(f"last_derived_reintroduction_offset={last_derived_reintroduction_offset}")
    signals.append(f"promotion_scope={scope}")
    signals.append(f"distinct_path_count={distinct_path_count}")
    signals.append(f"distinct_source_family_count={distinct_source_families}")
    signals.append(f"distinct_surface_family_count={distinct_surface_families}")
    signals.append(f"distinct_run_count={distinct_runs}")
    signals.append(f"distinct_asset_count={distinct_assets}")
    signals.append(f"distinct_source_pointer_count={distinct_source_pointers}")
    signals.append(f"evidence_independence={_evidence_independence_summary(observations)}")

    if summary_echo_only:
        status: LineStatus = "candidate"
        thickness: ThicknessLevel = "thin"
        should_promote = False
        reason = "summary_echo only observations stay in candidate/thin until source-linked grounding appears"
    elif contradiction_count > 0 and contradiction_count >= support:
        status = "candidate"
        thickness = "thin"
        should_promote = False
        reason = "contradiction pressure outweighs support"
    elif (
        support >= 5
        and contradiction_count == 0
        and has_direct_span
        and (distinct_runs >= 2 or distinct_assets >= 2)
        and distinct_surfaces >= 2
        and independent_evidence_count >= 2
        and len(primary_material_anchor_ids) >= 2
        and not has_self_referential_derived_support
    ):
        status: LineStatus = "operating"
        thickness: ThicknessLevel = "thick"
        should_promote = True
        reason = "line is repeated across multiple runs or assets with a direct span and no recorded resistance"
    elif (
        support >= 3
        and contradiction_count == 0
        and has_direct_span
        and distinct_surfaces >= 2
        and distinct_source_pointers >= 2
        and independent_evidence_count >= 1
    ):
        status = "stable"
        thickness = "thick"
        should_promote = True
        reason = "line is repeated across surfaces with direct span recurrence and no contradiction pressure"
    elif support >= 2 and contradiction_count == 0 and distinct_surfaces >= 2 and has_source_linked:
        status = "probing"
        thickness = "medium"
        should_promote = False
        reason = "line has repeated support across more than one surface and has source-linked grounding, but is not yet thick enough"
    elif support >= 1:
        status = "candidate"
        thickness = "thin"
        should_promote = False
        if caution > 0 or weakness > 0:
            reason = "line has first support but still needs source-linked reread"
        else:
            reason = "line has first support but still needs source-linked reread"
    else:
        status = "candidate"
        thickness = "thin"
        should_promote = False
        reason = "line is still weakly grounded and should stay in candidate state"

    validation_profile, profile_basis_summary = _derive_validation_profile(
        status=status,
        thickness=thickness,
        distinct_path_count=distinct_path_count,
        distinct_independent_evidence_count=independent_evidence_count,
        distinct_primary_material_anchor_count=len(primary_material_anchor_ids),
        has_self_referential_derived_support=has_self_referential_derived_support,
        summary_echo_only=summary_echo_only,
    )
    (
        primary_only_validation_profile,
        primary_only_basis_summary,
        primary_only_path_count,
        primary_only_material_count,
        primary_only_source_document_count,
        primary_only_independent_evidence_count,
    ) = _derive_primary_only_validation_profile(observations)
    (
        derived_support_role,
        primary_support_share_bucket,
        derived_dependency_hint,
        derived_support_summary,
        primary_vs_derived_balance_summary,
    ) = _derive_derived_support_role(
        summary_echo_only=summary_echo_only,
        support_ecology_bias=support_ecology_bias,
        primary_support_row_count=primary_support_row_count,
        derived_support_row_count=derived_support_row_count,
        self_referential_derived_row_count=self_referential_derived_row_count,
        validation_profile=validation_profile,
        primary_only_validation_profile=primary_only_validation_profile,
    )
    broadening_gap_type, next_missing_axis, gap_basis_summary = _derive_broadening_gap(
        validation_profile=validation_profile,
        distinct_path_count=distinct_path_count,
        distinct_independent_evidence_count=independent_evidence_count,
        distinct_primary_material_anchor_count=len(primary_material_anchor_ids),
        has_self_referential_derived_support=has_self_referential_derived_support,
        summary_echo_only=summary_echo_only,
    )
    signals.append(f"validation_profile={validation_profile}")
    signals.append(f"primary_only_validation_profile={primary_only_validation_profile}")
    signals.append(f"support_ecology_bias={support_ecology_bias}")
    signals.append(f"derived_support_role={derived_support_role}")
    signals.append(f"derived_dependency_hint={derived_dependency_hint}")
    signals.append(f"broadening_gap_type={broadening_gap_type}")
    signals.append(f"next_missing_axis={next_missing_axis}")

    return PromotionDecision(
        line_id=entry.line_id,
        line_name=entry.line_name,
        status=status,
        thickness_level=thickness,
        should_promote=should_promote,
        reason=reason,
        signals=signals,
        promotion_scope=scope,
        scope_basis_summary=scope_basis_summary,
        validation_profile=validation_profile,
        profile_basis_summary=profile_basis_summary,
        primary_only_validation_profile=primary_only_validation_profile,
        primary_only_basis_summary=primary_only_basis_summary,
        support_ecology_bias=support_ecology_bias,
        derived_support_role=derived_support_role,
        derived_support_summary=derived_support_summary,
        primary_vs_derived_balance_summary=primary_vs_derived_balance_summary,
        primary_support_share_bucket=primary_support_share_bucket,
        derived_dependency_hint=derived_dependency_hint,
        broadening_gap_type=broadening_gap_type,
        next_missing_axis=next_missing_axis,
        gap_basis_summary=gap_basis_summary,
        cumulative_primary_rows=cumulative_primary_rows,
        cumulative_derived_rows=cumulative_derived_rows,
        recent_primary_rows=recent_primary_rows,
        recent_derived_rows=recent_derived_rows,
        recent_window_size_used=recent_window_size_used,
        recent_primary_vs_derived_summary=recent_primary_vs_derived_summary,
        derived_residue_trend=derived_residue_trend,
        derived_residue_trend_summary=derived_residue_trend_summary,
        recent_decay_streak=recent_decay_streak,
        last_derived_support_offset=last_derived_support_offset,
        derived_residue_persistence=derived_residue_persistence,
        persistence_basis_summary=persistence_basis_summary,
        derived_residue_robustness=derived_residue_robustness,
        trend_window_agreement_summary=trend_window_agreement_summary,
        tested_window_sizes=tested_window_sizes,
        derived_reintroduction_status=derived_reintroduction_status,
        derived_reintroduction_trigger=derived_reintroduction_trigger,
        last_derived_reintroduction_offset=last_derived_reintroduction_offset,
        primary_support_row_count=primary_support_row_count,
        derived_support_row_count=derived_support_row_count,
        self_referential_derived_row_count=self_referential_derived_row_count,
        summary_row_count=summary_row_count,
        primary_only_path_count=primary_only_path_count,
        primary_only_material_count=primary_only_material_count,
        primary_only_source_document_count=primary_only_source_document_count,
        primary_only_independent_evidence_count=primary_only_independent_evidence_count,
        distinct_path_count=distinct_path_count,
        distinct_source_family_count=distinct_source_families,
        distinct_surface_family_count=distinct_surface_families,
        distinct_run_count=distinct_runs,
        distinct_asset_count=distinct_assets,
        distinct_source_pointer_count=distinct_source_pointers,
        distinct_primary_source_family_count=len(primary_source_families_seen),
        distinct_derived_source_family_count=len(derived_source_families_seen),
        distinct_independent_evidence_count=independent_evidence_count,
        distinct_material_anchor_count=len(material_anchor_ids),
        distinct_primary_material_anchor_count=len(primary_material_anchor_ids),
        distinct_source_document_count=len(source_documents),
        has_self_referential_derived_support=has_self_referential_derived_support,
        evidence_independence_summary=_evidence_independence_summary(observations),
        material_independence_summary=_material_independence_summary(observations),
        evaluated_at=_now_iso(),
    )


def _upsert_line_entry(
    runtime_root: Path,
    observation: Dict[str, Any],
) -> tuple[LineRegistryEntry, bool]:
    registry = _load_registry(runtime_root)
    lines = _load_lines(registry)
    line_name = str(observation.get("line_name") or "").strip()
    if not line_name:
        raise ValueError("line_name is required")
    line_id = _line_id(line_name)
    now = str(observation.get("recorded_at") or observation.get("observed_at") or _now_iso())
    surface_label = _surface_label(observation)
    line_history = _load_observation_rows_for_line(runtime_root, line_name)
    metrics = _aggregate_line_metrics(line_history)
    support_count = int(metrics["support_count"])
    contradiction_count = int(metrics["contradiction_count"])
    weakness_count = int(metrics["weakness_count"])
    caution_count = int(metrics["caution_count"])
    surface_types_seen = list(metrics["surface_types_seen"])
    source_paths_seen = list(metrics.get("source_paths_seen") or [])
    primary_source_families_seen = _observed_primary_source_families(line_history)
    derived_source_families_seen = _observed_derived_source_families(line_history)
    independent_evidence_count = _observed_independent_evidence_count(line_history)
    has_self_referential_derived_support = "self_referential_derived" in _observed_independence_classes(line_history) or any(
        str(row.get("evidence_origin_kind") or "") in {"derived_report", "derived_trace"}
        for row in line_history
    )
    evidence_independence_summary = _evidence_independence_summary(line_history)
    material_independence_summary = _material_independence_summary(line_history)
    note_bits = [
        f"run_id={observation.get('run_id') or ''}",
        f"view_type={observation.get('view_type') or ''}",
        f"grounding={observation.get('grounding_type') or ''}",
        f"evidence_mode={observation.get('evidence_mode') or 'summary_echo'}",
        f"source_kind={observation.get('source_kind') or 'other'}",
        f"evidence_origin_kind={observation.get('evidence_origin_kind') or 'summary_echo'}",
        f"independence_class={observation.get('independence_class') or 'mixed'}",
        f"next_probe={observation.get('next_probe_surface') or ''}",
    ]
    if observation.get("source_pointer"):
        note_bits.append(f"source_pointer={observation.get('source_pointer')}")
    obs_reasons = (
        list(observation.get("support_points") or [])
        + list(observation.get("weakness_points") or [])
        + list(observation.get("caution_points") or [])
        + list(observation.get("contradiction_points") or [])
        + list(observation.get("resistance_or_counterexample") or [])
    )
    if obs_reasons:
        note_bits.append(f"evidence={'; '.join(str(item) for item in obs_reasons)}")

    for idx, row in enumerate(lines):
        if str(row.get("line_id") or "") != line_id:
            continue
        updated = dict(row)
        updated["last_seen_at"] = now
        updated["support_count"] = support_count
        updated["contradiction_count"] = contradiction_count
        updated["weakness_count"] = weakness_count
        updated["caution_count"] = caution_count
        updated["resistance_count"] = contradiction_count
        updated["surface_types_seen"] = surface_types_seen
        notes = list(updated.get("notes") or [])
        notes.extend(note_bits)
        updated["notes"] = _dedupe_preserve_order(notes)
        decision = evaluate_promotion_rule(
            LineRegistryEntry(
                line_id=line_id,
                line_name=line_name,
                status=str(updated.get("status") or "candidate"),
                thickness_level=str(updated.get("thickness_level") or "thin"),
                first_seen_at=str(updated.get("first_seen_at") or now),
                last_seen_at=now,
                support_count=support_count,
                contradiction_count=contradiction_count,
                weakness_count=weakness_count,
                caution_count=caution_count,
                resistance_count=contradiction_count,
                promotion_scope=str(updated.get("promotion_scope") or "path_local"),
                scope_basis_summary=str(updated.get("scope_basis_summary") or ""),
                validation_profile=str(updated.get("validation_profile") or "insufficient_profile"),
                profile_basis_summary=str(updated.get("profile_basis_summary") or ""),
                primary_only_validation_profile=str(updated.get("primary_only_validation_profile") or "insufficient_profile"),
                primary_only_basis_summary=str(updated.get("primary_only_basis_summary") or ""),
                support_ecology_bias=str(updated.get("support_ecology_bias") or "summary_only"),
                derived_support_role=str(updated.get("derived_support_role") or "summary_only"),
                derived_support_summary=str(updated.get("derived_support_summary") or ""),
                primary_vs_derived_balance_summary=str(updated.get("primary_vs_derived_balance_summary") or ""),
                primary_support_share_bucket=str(updated.get("primary_support_share_bucket") or "low"),
                derived_dependency_hint=str(updated.get("derived_dependency_hint") or "high"),
                broadening_gap_type=str(updated.get("broadening_gap_type") or "mixed_gap"),
                next_missing_axis=str(updated.get("next_missing_axis") or "multiple"),
                gap_basis_summary=str(updated.get("gap_basis_summary") or ""),
                cumulative_primary_rows=int(updated.get("cumulative_primary_rows") or 0),
                cumulative_derived_rows=int(updated.get("cumulative_derived_rows") or 0),
                recent_primary_rows=int(updated.get("recent_primary_rows") or 0),
                recent_derived_rows=int(updated.get("recent_derived_rows") or 0),
                recent_window_size_used=int(updated.get("recent_window_size_used") or 0),
                recent_primary_vs_derived_summary=str(updated.get("recent_primary_vs_derived_summary") or ""),
                derived_residue_trend=str(updated.get("derived_residue_trend") or "insufficient_history"),
                derived_residue_trend_summary=str(updated.get("derived_residue_trend_summary") or ""),
                recent_decay_streak=int(updated.get("recent_decay_streak") or 0),
                last_derived_support_offset=int(updated.get("last_derived_support_offset") or 0),
                derived_residue_persistence=str(updated.get("derived_residue_persistence") or "insufficient_history"),
                persistence_basis_summary=str(updated.get("persistence_basis_summary") or ""),
                derived_residue_robustness=str(updated.get("derived_residue_robustness") or "insufficient_history"),
                trend_window_agreement_summary=str(updated.get("trend_window_agreement_summary") or ""),
                tested_window_sizes=list(updated.get("tested_window_sizes") or []),
                derived_reintroduction_status=str(updated.get("derived_reintroduction_status") or "insufficient_history"),
                derived_reintroduction_trigger=str(updated.get("derived_reintroduction_trigger") or "unknown"),
                last_derived_reintroduction_offset=int(updated.get("last_derived_reintroduction_offset") or 0),
                primary_support_row_count=int(updated.get("primary_support_row_count") or 0),
                derived_support_row_count=int(updated.get("derived_support_row_count") or 0),
                self_referential_derived_row_count=int(updated.get("self_referential_derived_row_count") or 0),
                summary_row_count=int(updated.get("summary_row_count") or 0),
                primary_only_path_count=int(updated.get("primary_only_path_count") or 0),
                primary_only_material_count=int(updated.get("primary_only_material_count") or 0),
                primary_only_source_document_count=int(updated.get("primary_only_source_document_count") or 0),
                primary_only_independent_evidence_count=int(updated.get("primary_only_independent_evidence_count") or 0),
                surface_types_seen=list(updated.get("surface_types_seen") or []),
                notes=list(updated.get("notes") or []),
            ),
            recent_observations=line_history,
        )
        updated["status"] = decision.status
        updated["thickness_level"] = decision.thickness_level
        updated["promotion_scope"] = decision.promotion_scope
        updated["scope_basis_summary"] = decision.scope_basis_summary
        updated["validation_profile"] = decision.validation_profile
        updated["profile_basis_summary"] = decision.profile_basis_summary
        updated["primary_only_validation_profile"] = decision.primary_only_validation_profile
        updated["primary_only_basis_summary"] = decision.primary_only_basis_summary
        updated["support_ecology_bias"] = decision.support_ecology_bias
        updated["derived_support_role"] = decision.derived_support_role
        updated["derived_support_summary"] = decision.derived_support_summary
        updated["primary_vs_derived_balance_summary"] = decision.primary_vs_derived_balance_summary
        updated["primary_support_share_bucket"] = decision.primary_support_share_bucket
        updated["derived_dependency_hint"] = decision.derived_dependency_hint
        updated["broadening_gap_type"] = decision.broadening_gap_type
        updated["next_missing_axis"] = decision.next_missing_axis
        updated["gap_basis_summary"] = decision.gap_basis_summary
        updated["cumulative_primary_rows"] = decision.cumulative_primary_rows
        updated["cumulative_derived_rows"] = decision.cumulative_derived_rows
        updated["recent_primary_rows"] = decision.recent_primary_rows
        updated["recent_derived_rows"] = decision.recent_derived_rows
        updated["recent_window_size_used"] = decision.recent_window_size_used
        updated["recent_primary_vs_derived_summary"] = decision.recent_primary_vs_derived_summary
        updated["derived_residue_trend"] = decision.derived_residue_trend
        updated["derived_residue_trend_summary"] = decision.derived_residue_trend_summary
        updated["recent_decay_streak"] = decision.recent_decay_streak
        updated["last_derived_support_offset"] = decision.last_derived_support_offset
        updated["derived_residue_persistence"] = decision.derived_residue_persistence
        updated["persistence_basis_summary"] = decision.persistence_basis_summary
        updated["derived_residue_robustness"] = decision.derived_residue_robustness
        updated["trend_window_agreement_summary"] = decision.trend_window_agreement_summary
        updated["tested_window_sizes"] = decision.tested_window_sizes
        updated["derived_reintroduction_status"] = decision.derived_reintroduction_status
        updated["derived_reintroduction_trigger"] = decision.derived_reintroduction_trigger
        updated["last_derived_reintroduction_offset"] = decision.last_derived_reintroduction_offset
        updated["primary_support_row_count"] = decision.primary_support_row_count
        updated["derived_support_row_count"] = decision.derived_support_row_count
        updated["self_referential_derived_row_count"] = decision.self_referential_derived_row_count
        updated["summary_row_count"] = decision.summary_row_count
        updated["primary_only_path_count"] = decision.primary_only_path_count
        updated["primary_only_material_count"] = decision.primary_only_material_count
        updated["primary_only_source_document_count"] = decision.primary_only_source_document_count
        updated["primary_only_independent_evidence_count"] = decision.primary_only_independent_evidence_count
        updated["distinct_path_count"] = decision.distinct_path_count
        updated["distinct_source_family_count"] = decision.distinct_source_family_count
        updated["distinct_surface_family_count"] = decision.distinct_surface_family_count
        updated["distinct_run_count"] = decision.distinct_run_count
        updated["distinct_asset_count"] = decision.distinct_asset_count
        updated["distinct_source_pointer_count"] = decision.distinct_source_pointer_count
        updated["distinct_primary_source_family_count"] = decision.distinct_primary_source_family_count
        updated["distinct_derived_source_family_count"] = decision.distinct_derived_source_family_count
        updated["distinct_independent_evidence_count"] = decision.distinct_independent_evidence_count
        updated["distinct_material_anchor_count"] = decision.distinct_material_anchor_count
        updated["distinct_primary_material_anchor_count"] = decision.distinct_primary_material_anchor_count
        updated["distinct_source_document_count"] = decision.distinct_source_document_count
        updated["has_self_referential_derived_support"] = decision.has_self_referential_derived_support
        updated["evidence_independence_summary"] = decision.evidence_independence_summary
        updated["material_independence_summary"] = decision.material_independence_summary
        lines[idx] = updated
        return _row_to_entry(updated), False

    decision = evaluate_promotion_rule(
        LineRegistryEntry(
            line_id=line_id,
            line_name=line_name,
            status="candidate",
            thickness_level="thin",
            first_seen_at=now,
            last_seen_at=now,
            support_count=support_count,
            contradiction_count=contradiction_count,
            weakness_count=weakness_count,
            caution_count=caution_count,
            resistance_count=contradiction_count,
            promotion_scope="path_local",
            scope_basis_summary="",
            validation_profile="insufficient_profile",
            profile_basis_summary="",
            primary_only_validation_profile="insufficient_profile",
            primary_only_basis_summary="",
            support_ecology_bias="summary_only",
            derived_support_role="summary_only",
            derived_support_summary="",
            primary_vs_derived_balance_summary="",
            primary_support_share_bucket="low",
            derived_dependency_hint="high",
            broadening_gap_type="mixed_gap",
            next_missing_axis="multiple",
                gap_basis_summary="",
                cumulative_primary_rows=0,
                cumulative_derived_rows=0,
                recent_primary_rows=0,
                recent_derived_rows=0,
                recent_window_size_used=0,
                recent_primary_vs_derived_summary="",
                derived_residue_trend="insufficient_history",
                derived_residue_trend_summary="",
                recent_decay_streak=0,
                last_derived_support_offset=0,
                derived_residue_persistence="insufficient_history",
                persistence_basis_summary="",
                derived_residue_robustness="insufficient_history",
                trend_window_agreement_summary="",
                tested_window_sizes=[],
                derived_reintroduction_status="insufficient_history",
                derived_reintroduction_trigger="unknown",
                last_derived_reintroduction_offset=0,
                primary_support_row_count=0,
                derived_support_row_count=0,
                self_referential_derived_row_count=0,
            summary_row_count=0,
            primary_only_path_count=0,
            primary_only_material_count=0,
            primary_only_source_document_count=0,
            primary_only_independent_evidence_count=0,
            surface_types_seen=[surface_label],
            notes=_dedupe_preserve_order(note_bits),
        ),
        recent_observations=line_history,
    )
    entry = LineRegistryEntry(
        line_id=line_id,
        line_name=line_name,
        status=decision.status,
        thickness_level=decision.thickness_level,
        first_seen_at=now,
        last_seen_at=now,
        support_count=support_count,
        contradiction_count=contradiction_count,
        weakness_count=weakness_count,
        caution_count=caution_count,
        resistance_count=contradiction_count,
        promotion_scope=decision.promotion_scope,
        scope_basis_summary=decision.scope_basis_summary,
        validation_profile=decision.validation_profile,
        profile_basis_summary=decision.profile_basis_summary,
        primary_only_validation_profile=decision.primary_only_validation_profile,
        primary_only_basis_summary=decision.primary_only_basis_summary,
        support_ecology_bias=decision.support_ecology_bias,
        derived_support_role=decision.derived_support_role,
        derived_support_summary=decision.derived_support_summary,
        primary_vs_derived_balance_summary=decision.primary_vs_derived_balance_summary,
        primary_support_share_bucket=decision.primary_support_share_bucket,
        derived_dependency_hint=decision.derived_dependency_hint,
        broadening_gap_type=decision.broadening_gap_type,
        next_missing_axis=decision.next_missing_axis,
        gap_basis_summary=decision.gap_basis_summary,
        cumulative_primary_rows=decision.cumulative_primary_rows,
        cumulative_derived_rows=decision.cumulative_derived_rows,
        recent_primary_rows=decision.recent_primary_rows,
        recent_derived_rows=decision.recent_derived_rows,
        recent_window_size_used=decision.recent_window_size_used,
        recent_primary_vs_derived_summary=decision.recent_primary_vs_derived_summary,
        derived_residue_trend=decision.derived_residue_trend,
        derived_residue_trend_summary=decision.derived_residue_trend_summary,
        recent_decay_streak=decision.recent_decay_streak,
        last_derived_support_offset=decision.last_derived_support_offset,
        derived_residue_persistence=decision.derived_residue_persistence,
        persistence_basis_summary=decision.persistence_basis_summary,
        derived_residue_robustness=decision.derived_residue_robustness,
        trend_window_agreement_summary=decision.trend_window_agreement_summary,
        tested_window_sizes=decision.tested_window_sizes,
        derived_reintroduction_status=decision.derived_reintroduction_status,
        derived_reintroduction_trigger=decision.derived_reintroduction_trigger,
        last_derived_reintroduction_offset=decision.last_derived_reintroduction_offset,
        primary_support_row_count=decision.primary_support_row_count,
        derived_support_row_count=decision.derived_support_row_count,
        self_referential_derived_row_count=decision.self_referential_derived_row_count,
        summary_row_count=decision.summary_row_count,
        primary_only_path_count=decision.primary_only_path_count,
        primary_only_material_count=decision.primary_only_material_count,
        primary_only_source_document_count=decision.primary_only_source_document_count,
        primary_only_independent_evidence_count=decision.primary_only_independent_evidence_count,
        distinct_path_count=decision.distinct_path_count,
        distinct_source_family_count=decision.distinct_source_family_count,
        distinct_surface_family_count=decision.distinct_surface_family_count,
        distinct_run_count=decision.distinct_run_count,
        distinct_asset_count=decision.distinct_asset_count,
        distinct_source_pointer_count=decision.distinct_source_pointer_count,
        distinct_primary_source_family_count=decision.distinct_primary_source_family_count,
        distinct_derived_source_family_count=decision.distinct_derived_source_family_count,
        distinct_independent_evidence_count=decision.distinct_independent_evidence_count,
        distinct_material_anchor_count=decision.distinct_material_anchor_count,
        distinct_primary_material_anchor_count=decision.distinct_primary_material_anchor_count,
        distinct_source_document_count=decision.distinct_source_document_count,
        has_self_referential_derived_support=decision.has_self_referential_derived_support,
        evidence_independence_summary=decision.evidence_independence_summary,
        material_independence_summary=decision.material_independence_summary,
        surface_types_seen=[surface_label],
        notes=_dedupe_preserve_order(note_bits),
    )
    lines.append(asdict(entry))
    new_registry = _store_lines(registry, lines)
    _save_registry(runtime_root, new_registry)
    return entry, True


def _row_to_entry(row: Dict[str, Any]) -> LineRegistryEntry:
    return LineRegistryEntry(
        line_id=str(row.get("line_id") or ""),
        line_name=str(row.get("line_name") or ""),
        status=str(row.get("status") or "candidate"),
        thickness_level=str(row.get("thickness_level") or "thin"),
        first_seen_at=str(row.get("first_seen_at") or ""),
        last_seen_at=str(row.get("last_seen_at") or ""),
        support_count=int(row.get("support_count") or 0),
        contradiction_count=int(row.get("contradiction_count") or 0),
        weakness_count=int(row.get("weakness_count") or 0),
        caution_count=int(row.get("caution_count") or 0),
        resistance_count=int(row.get("resistance_count") or row.get("contradiction_count") or 0),
        promotion_scope=str(row.get("promotion_scope") or "path_local"),
        scope_basis_summary=str(row.get("scope_basis_summary") or ""),
        validation_profile=str(row.get("validation_profile") or "insufficient_profile"),
        profile_basis_summary=str(row.get("profile_basis_summary") or ""),
        primary_only_validation_profile=str(row.get("primary_only_validation_profile") or "insufficient_profile"),
        primary_only_basis_summary=str(row.get("primary_only_basis_summary") or ""),
        support_ecology_bias=str(row.get("support_ecology_bias") or "summary_only"),
        derived_support_role=str(row.get("derived_support_role") or "summary_only"),
        derived_support_summary=str(row.get("derived_support_summary") or ""),
        primary_vs_derived_balance_summary=str(row.get("primary_vs_derived_balance_summary") or ""),
        primary_support_share_bucket=str(row.get("primary_support_share_bucket") or "low"),
        derived_dependency_hint=str(row.get("derived_dependency_hint") or "high"),
        broadening_gap_type=str(row.get("broadening_gap_type") or "mixed_gap"),
        next_missing_axis=str(row.get("next_missing_axis") or "multiple"),
        gap_basis_summary=str(row.get("gap_basis_summary") or ""),
        cumulative_primary_rows=int(row.get("cumulative_primary_rows") or 0),
        cumulative_derived_rows=int(row.get("cumulative_derived_rows") or 0),
        recent_primary_rows=int(row.get("recent_primary_rows") or 0),
        recent_derived_rows=int(row.get("recent_derived_rows") or 0),
        recent_window_size_used=int(row.get("recent_window_size_used") or 0),
        recent_primary_vs_derived_summary=str(row.get("recent_primary_vs_derived_summary") or ""),
        derived_residue_trend=str(row.get("derived_residue_trend") or "insufficient_history"),
        derived_residue_trend_summary=str(row.get("derived_residue_trend_summary") or ""),
        recent_decay_streak=int(row.get("recent_decay_streak") or 0),
        last_derived_support_offset=int(row.get("last_derived_support_offset") or 0),
        derived_residue_persistence=str(row.get("derived_residue_persistence") or "insufficient_history"),
        persistence_basis_summary=str(row.get("persistence_basis_summary") or ""),
        derived_residue_robustness=str(row.get("derived_residue_robustness") or "insufficient_history"),
        trend_window_agreement_summary=str(row.get("trend_window_agreement_summary") or ""),
        tested_window_sizes=list(row.get("tested_window_sizes") or []),
        derived_reintroduction_status=str(row.get("derived_reintroduction_status") or "insufficient_history"),
        derived_reintroduction_trigger=str(row.get("derived_reintroduction_trigger") or "unknown"),
        last_derived_reintroduction_offset=int(row.get("last_derived_reintroduction_offset") or 0),
        primary_support_row_count=int(row.get("primary_support_row_count") or 0),
        derived_support_row_count=int(row.get("derived_support_row_count") or 0),
        self_referential_derived_row_count=int(row.get("self_referential_derived_row_count") or 0),
        summary_row_count=int(row.get("summary_row_count") or 0),
        primary_only_path_count=int(row.get("primary_only_path_count") or 0),
        primary_only_material_count=int(row.get("primary_only_material_count") or 0),
        primary_only_source_document_count=int(row.get("primary_only_source_document_count") or 0),
        primary_only_independent_evidence_count=int(row.get("primary_only_independent_evidence_count") or 0),
        distinct_path_count=int(row.get("distinct_path_count") or 0),
        distinct_source_family_count=int(row.get("distinct_source_family_count") or 0),
        distinct_surface_family_count=int(row.get("distinct_surface_family_count") or 0),
        distinct_run_count=int(row.get("distinct_run_count") or 0),
        distinct_asset_count=int(row.get("distinct_asset_count") or 0),
        distinct_source_pointer_count=int(row.get("distinct_source_pointer_count") or 0),
        distinct_primary_source_family_count=int(row.get("distinct_primary_source_family_count") or 0),
        distinct_derived_source_family_count=int(row.get("distinct_derived_source_family_count") or 0),
        distinct_independent_evidence_count=int(row.get("distinct_independent_evidence_count") or 0),
        distinct_material_anchor_count=int(row.get("distinct_material_anchor_count") or 0),
        distinct_primary_material_anchor_count=int(row.get("distinct_primary_material_anchor_count") or 0),
        distinct_source_document_count=int(row.get("distinct_source_document_count") or 0),
        has_self_referential_derived_support=bool(row.get("has_self_referential_derived_support") or False),
        evidence_independence_summary=str(row.get("evidence_independence_summary") or ""),
        material_independence_summary=str(row.get("material_independence_summary") or ""),
        surface_types_seen=list(row.get("surface_types_seen") or []),
        notes=list(row.get("notes") or []),
    )


def _find_registry_row(runtime_root: Path, line_name: str) -> Optional[Dict[str, Any]]:
    line_id = _line_id(line_name)
    registry = _load_registry(runtime_root)
    for row in _load_lines(registry):
        if str(row.get("line_id") or "") == line_id:
            return row
    return None


def refresh_line_registry_entry(runtime_root: Path, line_name: str) -> Optional[Dict[str, Any]]:
    registry = _load_registry(runtime_root)
    lines = _load_lines(registry)
    current_row = _find_registry_row(runtime_root, line_name)
    line_history = _load_observation_rows_for_line(runtime_root, line_name)
    if not line_history:
        return None

    metrics = _aggregate_line_metrics(line_history)
    first_seen_at = str((current_row or {}).get("first_seen_at") or line_history[0].get("recorded_at") or _now_iso())
    last_seen_at = str(line_history[-1].get("recorded_at") or _now_iso())
    entry = LineRegistryEntry(
        line_id=_line_id(line_name),
        line_name=line_name,
        status=str((current_row or {}).get("status") or "candidate"),
        thickness_level=str((current_row or {}).get("thickness_level") or "thin"),
        first_seen_at=first_seen_at,
        last_seen_at=last_seen_at,
        support_count=int(metrics["support_count"]),
        contradiction_count=int(metrics["contradiction_count"]),
        weakness_count=int(metrics["weakness_count"]),
        caution_count=int(metrics["caution_count"]),
        resistance_count=int(metrics["contradiction_count"]),
        promotion_scope=str((current_row or {}).get("promotion_scope") or "path_local"),
        scope_basis_summary=str((current_row or {}).get("scope_basis_summary") or ""),
        validation_profile=str((current_row or {}).get("validation_profile") or "insufficient_profile"),
        profile_basis_summary=str((current_row or {}).get("profile_basis_summary") or ""),
        primary_only_validation_profile=str((current_row or {}).get("primary_only_validation_profile") or "insufficient_profile"),
        primary_only_basis_summary=str((current_row or {}).get("primary_only_basis_summary") or ""),
        support_ecology_bias=str((current_row or {}).get("support_ecology_bias") or "summary_only"),
        derived_support_role=str((current_row or {}).get("derived_support_role") or "summary_only"),
        derived_support_summary=str((current_row or {}).get("derived_support_summary") or ""),
        primary_vs_derived_balance_summary=str((current_row or {}).get("primary_vs_derived_balance_summary") or ""),
        primary_support_share_bucket=str((current_row or {}).get("primary_support_share_bucket") or "low"),
        derived_dependency_hint=str((current_row or {}).get("derived_dependency_hint") or "high"),
        broadening_gap_type=str((current_row or {}).get("broadening_gap_type") or "mixed_gap"),
        next_missing_axis=str((current_row or {}).get("next_missing_axis") or "multiple"),
        gap_basis_summary=str((current_row or {}).get("gap_basis_summary") or ""),
        cumulative_primary_rows=int((current_row or {}).get("cumulative_primary_rows") or 0),
        cumulative_derived_rows=int((current_row or {}).get("cumulative_derived_rows") or 0),
        recent_primary_rows=int((current_row or {}).get("recent_primary_rows") or 0),
        recent_derived_rows=int((current_row or {}).get("recent_derived_rows") or 0),
        recent_window_size_used=int((current_row or {}).get("recent_window_size_used") or 0),
        recent_primary_vs_derived_summary=str((current_row or {}).get("recent_primary_vs_derived_summary") or ""),
        derived_residue_trend=str((current_row or {}).get("derived_residue_trend") or "insufficient_history"),
        derived_residue_trend_summary=str((current_row or {}).get("derived_residue_trend_summary") or ""),
        recent_decay_streak=int((current_row or {}).get("recent_decay_streak") or 0),
        last_derived_support_offset=int((current_row or {}).get("last_derived_support_offset") or 0),
        derived_residue_persistence=str((current_row or {}).get("derived_residue_persistence") or "insufficient_history"),
        persistence_basis_summary=str((current_row or {}).get("persistence_basis_summary") or ""),
        derived_residue_robustness=str((current_row or {}).get("derived_residue_robustness") or "insufficient_history"),
        trend_window_agreement_summary=str((current_row or {}).get("trend_window_agreement_summary") or ""),
        tested_window_sizes=list((current_row or {}).get("tested_window_sizes") or []),
        derived_reintroduction_status=str((current_row or {}).get("derived_reintroduction_status") or "insufficient_history"),
        derived_reintroduction_trigger=str((current_row or {}).get("derived_reintroduction_trigger") or "unknown"),
        last_derived_reintroduction_offset=int((current_row or {}).get("last_derived_reintroduction_offset") or 0),
        primary_support_row_count=int((current_row or {}).get("primary_support_row_count") or 0),
        derived_support_row_count=int((current_row or {}).get("derived_support_row_count") or 0),
        self_referential_derived_row_count=int((current_row or {}).get("self_referential_derived_row_count") or 0),
        summary_row_count=int((current_row or {}).get("summary_row_count") or 0),
        primary_only_path_count=int((current_row or {}).get("primary_only_path_count") or 0),
        primary_only_material_count=int((current_row or {}).get("primary_only_material_count") or 0),
        primary_only_source_document_count=int((current_row or {}).get("primary_only_source_document_count") or 0),
        primary_only_independent_evidence_count=int((current_row or {}).get("primary_only_independent_evidence_count") or 0),
        distinct_path_count=int((current_row or {}).get("distinct_path_count") or 0),
        distinct_source_family_count=int((current_row or {}).get("distinct_source_family_count") or 0),
        distinct_surface_family_count=int((current_row or {}).get("distinct_surface_family_count") or 0),
        distinct_run_count=int((current_row or {}).get("distinct_run_count") or 0),
        distinct_asset_count=int((current_row or {}).get("distinct_asset_count") or 0),
        distinct_source_pointer_count=int((current_row or {}).get("distinct_source_pointer_count") or 0),
        distinct_primary_source_family_count=int((current_row or {}).get("distinct_primary_source_family_count") or 0),
        distinct_derived_source_family_count=int((current_row or {}).get("distinct_derived_source_family_count") or 0),
        distinct_independent_evidence_count=int((current_row or {}).get("distinct_independent_evidence_count") or 0),
        distinct_material_anchor_count=int((current_row or {}).get("distinct_material_anchor_count") or 0),
        distinct_primary_material_anchor_count=int((current_row or {}).get("distinct_primary_material_anchor_count") or 0),
        distinct_source_document_count=int((current_row or {}).get("distinct_source_document_count") or 0),
        has_self_referential_derived_support=bool((current_row or {}).get("has_self_referential_derived_support") or False),
        evidence_independence_summary=str((current_row or {}).get("evidence_independence_summary") or ""),
        material_independence_summary=str((current_row or {}).get("material_independence_summary") or ""),
        surface_types_seen=list(metrics["surface_types_seen"]),
        notes=list((current_row or {}).get("notes") or []),
    )
    decision = evaluate_promotion_rule(entry, recent_observations=line_history)
    refreshed = asdict(entry)
    refreshed["status"] = decision.status
    refreshed["thickness_level"] = decision.thickness_level
    refreshed["promotion_scope"] = decision.promotion_scope
    refreshed["scope_basis_summary"] = decision.scope_basis_summary
    refreshed["validation_profile"] = decision.validation_profile
    refreshed["profile_basis_summary"] = decision.profile_basis_summary
    refreshed["primary_only_validation_profile"] = decision.primary_only_validation_profile
    refreshed["primary_only_basis_summary"] = decision.primary_only_basis_summary
    refreshed["support_ecology_bias"] = decision.support_ecology_bias
    refreshed["derived_support_role"] = decision.derived_support_role
    refreshed["derived_support_summary"] = decision.derived_support_summary
    refreshed["primary_vs_derived_balance_summary"] = decision.primary_vs_derived_balance_summary
    refreshed["primary_support_share_bucket"] = decision.primary_support_share_bucket
    refreshed["derived_dependency_hint"] = decision.derived_dependency_hint
    refreshed["broadening_gap_type"] = decision.broadening_gap_type
    refreshed["next_missing_axis"] = decision.next_missing_axis
    refreshed["gap_basis_summary"] = decision.gap_basis_summary
    refreshed["cumulative_primary_rows"] = decision.cumulative_primary_rows
    refreshed["cumulative_derived_rows"] = decision.cumulative_derived_rows
    refreshed["recent_primary_rows"] = decision.recent_primary_rows
    refreshed["recent_derived_rows"] = decision.recent_derived_rows
    refreshed["recent_window_size_used"] = decision.recent_window_size_used
    refreshed["recent_primary_vs_derived_summary"] = decision.recent_primary_vs_derived_summary
    refreshed["derived_residue_trend"] = decision.derived_residue_trend
    refreshed["derived_residue_trend_summary"] = decision.derived_residue_trend_summary
    refreshed["recent_decay_streak"] = decision.recent_decay_streak
    refreshed["last_derived_support_offset"] = decision.last_derived_support_offset
    refreshed["derived_residue_persistence"] = decision.derived_residue_persistence
    refreshed["persistence_basis_summary"] = decision.persistence_basis_summary
    refreshed["derived_residue_robustness"] = decision.derived_residue_robustness
    refreshed["trend_window_agreement_summary"] = decision.trend_window_agreement_summary
    refreshed["tested_window_sizes"] = decision.tested_window_sizes
    refreshed["derived_reintroduction_status"] = decision.derived_reintroduction_status
    refreshed["derived_reintroduction_trigger"] = decision.derived_reintroduction_trigger
    refreshed["last_derived_reintroduction_offset"] = decision.last_derived_reintroduction_offset
    refreshed["primary_support_row_count"] = decision.primary_support_row_count
    refreshed["derived_support_row_count"] = decision.derived_support_row_count
    refreshed["self_referential_derived_row_count"] = decision.self_referential_derived_row_count
    refreshed["summary_row_count"] = decision.summary_row_count
    refreshed["primary_only_path_count"] = decision.primary_only_path_count
    refreshed["primary_only_material_count"] = decision.primary_only_material_count
    refreshed["primary_only_source_document_count"] = decision.primary_only_source_document_count
    refreshed["primary_only_independent_evidence_count"] = decision.primary_only_independent_evidence_count
    refreshed["distinct_path_count"] = decision.distinct_path_count
    refreshed["distinct_source_family_count"] = decision.distinct_source_family_count
    refreshed["distinct_surface_family_count"] = decision.distinct_surface_family_count
    refreshed["distinct_run_count"] = decision.distinct_run_count
    refreshed["distinct_asset_count"] = decision.distinct_asset_count
    refreshed["distinct_source_pointer_count"] = decision.distinct_source_pointer_count
    refreshed["distinct_primary_source_family_count"] = decision.distinct_primary_source_family_count
    refreshed["distinct_derived_source_family_count"] = decision.distinct_derived_source_family_count
    refreshed["distinct_independent_evidence_count"] = decision.distinct_independent_evidence_count
    refreshed["distinct_material_anchor_count"] = decision.distinct_material_anchor_count
    refreshed["distinct_primary_material_anchor_count"] = decision.distinct_primary_material_anchor_count
    refreshed["distinct_source_document_count"] = decision.distinct_source_document_count
    refreshed["has_self_referential_derived_support"] = decision.has_self_referential_derived_support
    refreshed["evidence_independence_summary"] = decision.evidence_independence_summary
    refreshed["material_independence_summary"] = decision.material_independence_summary
    append_promotion_decision(runtime_root, decision)

    updated_lines: list[Dict[str, Any]] = []
    replaced = False
    for row in lines:
        if str(row.get("line_id") or "") == refreshed["line_id"]:
            updated_lines.append(refreshed)
            replaced = True
        else:
            updated_lines.append(row)
    if not replaced:
        updated_lines.append(refreshed)
    _save_registry(runtime_root, _store_lines(registry, updated_lines))
    return refreshed


def _project_thickness_after_observation(
    runtime_root: Path,
    observation: RereadObservation,
) -> tuple[ThicknessLevel, ThicknessLevel]:
    current_row = _find_registry_row(runtime_root, observation.line_name)
    before = str((current_row or {}).get("thickness_level") or observation.thickness_before or "thin")
    if current_row:
        entry = _row_to_entry(current_row)
    else:
        entry = LineRegistryEntry(
            line_id=_line_id(observation.line_name),
            line_name=observation.line_name,
            status="candidate",
            thickness_level=before,  # type: ignore[assignment]
            first_seen_at=observation.observed_at,
            last_seen_at=observation.observed_at,
            support_count=0,
            contradiction_count=0,
            weakness_count=0,
            caution_count=0,
            resistance_count=0,
            validation_profile="insufficient_profile",
            profile_basis_summary="",
            primary_only_validation_profile="insufficient_profile",
            primary_only_basis_summary="",
            support_ecology_bias="summary_only",
            derived_support_role="summary_only",
            derived_support_summary="",
            primary_vs_derived_balance_summary="",
            primary_support_share_bucket="low",
            derived_dependency_hint="high",
            broadening_gap_type="mixed_gap",
            next_missing_axis="multiple",
            gap_basis_summary="",
            primary_support_row_count=0,
            derived_support_row_count=0,
            self_referential_derived_row_count=0,
            summary_row_count=0,
            primary_only_path_count=0,
            primary_only_material_count=0,
            primary_only_source_document_count=0,
            primary_only_independent_evidence_count=0,
            distinct_primary_source_family_count=0,
            distinct_derived_source_family_count=0,
            distinct_independent_evidence_count=0,
            distinct_material_anchor_count=0,
            distinct_primary_material_anchor_count=0,
            distinct_source_document_count=0,
            has_self_referential_derived_support=False,
            evidence_independence_summary="",
            material_independence_summary="",
            surface_types_seen=[],
            notes=[],
        )

    observation_row = _observation_to_row(observation)
    projected_history = _load_observation_rows_for_line(runtime_root, observation.line_name)
    projected_history.append(observation_row)
    metrics = _aggregate_line_metrics(projected_history)
    projected = LineRegistryEntry(
        line_id=entry.line_id,
        line_name=entry.line_name,
        status=entry.status,
        thickness_level=entry.thickness_level,
        first_seen_at=entry.first_seen_at,
        last_seen_at=observation_row["recorded_at"],
        support_count=int(metrics["support_count"]),
        contradiction_count=int(metrics["contradiction_count"]),
        weakness_count=int(metrics["weakness_count"]),
        caution_count=int(metrics["caution_count"]),
        resistance_count=int(metrics["contradiction_count"]),
        distinct_primary_source_family_count=int(
            len(_observed_primary_source_families(projected_history))
        ),
        distinct_derived_source_family_count=int(
            len(_observed_derived_source_families(projected_history))
        ),
        distinct_independent_evidence_count=_observed_independent_evidence_count(projected_history),
        distinct_material_anchor_count=len(_observed_material_anchor_ids(projected_history)),
        distinct_primary_material_anchor_count=len(_observed_primary_material_anchor_ids(projected_history)),
        distinct_source_document_count=len(_observed_source_documents(projected_history)),
        has_self_referential_derived_support=(
            "self_referential_derived" in _observed_independence_classes(projected_history)
            or any(str(row.get("evidence_origin_kind") or "") in {"derived_report", "derived_trace"} for row in projected_history)
        ),
        evidence_independence_summary=_evidence_independence_summary(projected_history),
        material_independence_summary=_material_independence_summary(projected_history),
        surface_types_seen=list(metrics["surface_types_seen"]),
        notes=_dedupe_preserve_order(list(entry.notes)),
        primary_only_validation_profile=entry.primary_only_validation_profile,
        primary_only_basis_summary=entry.primary_only_basis_summary,
        support_ecology_bias=entry.support_ecology_bias,
        derived_support_role=entry.derived_support_role,
        derived_support_summary=entry.derived_support_summary,
        primary_vs_derived_balance_summary=entry.primary_vs_derived_balance_summary,
        primary_support_share_bucket=entry.primary_support_share_bucket,
        derived_dependency_hint=entry.derived_dependency_hint,
        broadening_gap_type=entry.broadening_gap_type,
        next_missing_axis=entry.next_missing_axis,
        gap_basis_summary=entry.gap_basis_summary,
        primary_support_row_count=entry.primary_support_row_count,
        derived_support_row_count=entry.derived_support_row_count,
        self_referential_derived_row_count=entry.self_referential_derived_row_count,
        summary_row_count=entry.summary_row_count,
    )
    decision = evaluate_promotion_rule(projected, recent_observations=projected_history)
    return before, decision.thickness_level


def _line_next_probe_surface(line_name: str, decision: Dict[str, Any]) -> str:
    first_read_ref = str(decision.get("first_read_ref") or decision.get("requested_artifact_ref") or "")
    selected_group = decision.get("selected_artifact_group") or {}
    group_key = str(selected_group.get("group_key") or "")
    line_specific = {
        "pre_read_eye": "runtime/breadcrumbs.jsonl",
        "raw_return_preservation": first_read_ref or "runtime/breadcrumbs.jsonl",
        "transition_over_surface": group_key or first_read_ref or "runtime/breadcrumbs.jsonl",
        "input_to_reading_organ": "runtime/manifests/pipeline_observation_registry.jsonl",
        "alignment_before_autonomy": "runtime/receipts/doc_youtube_03_29_operation_receipt.md",
        "harness_over_model": "runtime/receipts/doc_claude_code_operation_receipt.md",
        "work_absorption_harness": "runtime/manifests/line_registry.json",
    }
    return line_specific.get(line_name, first_read_ref or "runtime/breadcrumbs.jsonl")


def build_preflight_reread_observation(
    runtime_root: Path,
    *,
    decision: Dict[str, Any],
    phase_record: Dict[str, Any],
    line_name: str,
) -> RereadObservation:
    selected_mode = str(decision.get("selected_mode") or "space_reading")
    first_read_ref = str(decision.get("first_read_ref") or decision.get("requested_artifact_ref") or "")
    selected_group = decision.get("selected_artifact_group") or {}
    group_key = str(selected_group.get("group_key") or selected_mode)
    phase_breadcrumb_refs = list((phase_record.get("related_breadcrumb_refs") or []) or [])
    phase_source_turn = str(phase_record.get("phase_source_turn") or "")
    source_kind = "preflight_decision"
    source_path_or_ref = "runtime/preflight_last_decision.json"
    source_run_id_or_event_id = str(decision.get("preflight_id") or "")
    source_pointer = "runtime/preflight_last_decision.json#phase_transition.active_latent_lines[0]"
    evidence_mode = "summary_echo"
    if phase_breadcrumb_refs:
        source_pointer = f"runtime/breadcrumbs.jsonl#{phase_breadcrumb_refs[0]}"
    elif phase_source_turn:
        source_pointer = f"runtime/current_phase.json#phase_source_turn={phase_source_turn}"
    base_evidence = (
        f"preflight selected {line_name} during {selected_mode}; "
        f"group={group_key}; first_read_ref={first_read_ref or 'n/a'}"
    )
    support_points = [
        f"active latent line selected by pre-read gate: {line_name}",
        f"mode={selected_mode}",
        f"first_read_ref={first_read_ref or 'n/a'}",
    ]
    weakness_points = [
        "cross-surface repeatability is still thin",
        "needs a later reread to confirm the line is not only gate-local",
    ]
    if line_name == "pre_read_eye":
        weakness_points = [
            "needs a later reread beyond the preflight gate",
            "still only grounded before content begins",
        ]
    elif line_name == "raw_return_preservation":
        weakness_points = [
            "needs another family or surface to stabilize the return path",
            "report separation can still collapse if reread is summary-only",
        ]
    caution = [
        str((decision.get("drift_risks") or ["summary-only reread would collapse the line"])[0]),
        f"summary-only reread would flatten {line_name}",
    ]
    evidence_origin_kind = "summary_echo"
    independence_class = "self_referential_derived"
    thickness_before, thickness_after = _project_thickness_after_observation(
        runtime_root,
        RereadObservation(
            run_id=str(decision.get("preflight_id") or "preflight_reread"),
            asset_or_surface=first_read_ref or group_key,
            view_type=selected_mode,
            line_name=line_name,
            evidence=base_evidence,
            grounding_type="direct",
            support_points=support_points,
            weakness_points=weakness_points,
            contradiction_points=[],
            caution_points=caution,
            next_probe_surface=_line_next_probe_surface(line_name, decision),
            thickness_before="thin",
            thickness_after="thin",
            observed_at=str(decision.get("selected_at") or _now_iso()),
            source_kind=source_kind,
            source_path_or_ref=source_path_or_ref,
            source_run_id_or_event_id=source_run_id_or_event_id,
            source_pointer=source_pointer,
            evidence_mode=evidence_mode,
            validation_path_id="preflight",
            evidence_origin_kind=evidence_origin_kind,
            independence_class=independence_class,
        ),
    )
    return RereadObservation(
        run_id=str(decision.get("preflight_id") or "preflight_reread"),
        asset_or_surface=first_read_ref or group_key,
        view_type=selected_mode,
        line_name=line_name,
        evidence=base_evidence,
        grounding_type="direct",
        support_points=support_points,
        weakness_points=weakness_points,
        contradiction_points=[],
        caution_points=caution,
        next_probe_surface=_line_next_probe_surface(line_name, decision),
        thickness_before=thickness_before,
        thickness_after=thickness_after,
        observed_at=str(decision.get("selected_at") or _now_iso()),
        source_kind=source_kind,
        source_path_or_ref=source_path_or_ref,
        source_run_id_or_event_id=source_run_id_or_event_id,
        source_pointer=source_pointer,
        evidence_mode=evidence_mode,
        validation_path_id="preflight",
        evidence_origin_kind=evidence_origin_kind,
        independence_class=independence_class,
    )


def record_preflight_line_thickening(
    runtime_root: Path,
    *,
    decision: Dict[str, Any],
    phase_record: Dict[str, Any],
    enabled: bool = True,
) -> List[Dict[str, Any]]:
    if not enabled:
        return []
    active_lines = [str(item or "") for item in phase_record.get("active_latent_lines") or [] if str(item or "").strip()]
    results: list[Dict[str, Any]] = []
    for line_name in active_lines[:2]:
        observation = build_preflight_reread_observation(
            runtime_root,
            decision=decision,
            phase_record=phase_record,
            line_name=line_name,
        )
        results.append(record_reread_observation(runtime_root, observation))
    return results


def _dedupe_preserve_order(items: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        value = str(item)
        if value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result


def append_promotion_decision(runtime_root: Path, decision: PromotionDecision) -> Dict[str, Any]:
    path = _promotion_log_path(runtime_root)
    row = asdict(decision)
    append_jsonl_locked(path, {"type": "line_promotion", "decision": row})
    return row


def record_reread_observation(
    runtime_root: Path,
    observation: RereadObservation,
) -> Dict[str, Any]:
    appended = append_reread_observation(runtime_root, observation)
    if appended.get("duplicate"):
        return appended

    line_entry, created = _upsert_line_entry(runtime_root, appended["observation"])
    line_history = _load_observation_rows_for_line(runtime_root, line_entry.line_name)
    promotion = evaluate_promotion_rule(line_entry, recent_observations=line_history)
    append_promotion_decision(runtime_root, promotion)

    registry = _load_registry(runtime_root)
    lines = _load_lines(registry)
    updated_lines: list[Dict[str, Any]] = []
    for row in lines:
        if str(row.get("line_id") or "") == line_entry.line_id:
            updated_lines.append(asdict(line_entry))
        else:
            updated_lines.append(row)
    if created and not updated_lines:
        updated_lines.append(asdict(line_entry))
    _save_registry(runtime_root, _store_lines(registry, updated_lines))

    return {
        "appended": True,
        "duplicate": False,
        "observation": appended["observation"],
        "registry_entry": asdict(line_entry),
        "promotion": asdict(promotion),
        "observation_log_path": appended["observation_log_path"],
        "registry_path": str(_registry_path(runtime_root)),
        "promotion_log_path": str(_promotion_log_path(runtime_root)),
    }
