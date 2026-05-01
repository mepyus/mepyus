#!/usr/bin/env python3
"""Build a read-only lookup packet for space-boundary material.

This helper reduces repeated context reads. It suggests source surface,
candidate assets, microspace matches, lens hints, and guardrails, but it does
not decide final state, mutate indexes, fetch web sources, or write runtime
artifacts.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[2]

KNOWN_INDEXES = [
    "docs/indexes/space_boundary_material_flow_map_v0.md",
    "docs/indexes/external_material_microspace_index_v0.md",
    "docs/indexes/space_translation_language_base_v0.md",
    "docs/indexes/space_asset_map_v0.md",
    "docs/guides/space_asset_retrieval_manual_v0.md",
    "docs/notes/executable_runner_index_v0.md",
]

SOURCE_SURFACE_HINTS = [
    ("web_external_material", re.compile(r"https?://|news\.hada\.io|github\.com|arxiv\.org", re.I)),
    ("external_material_file", re.compile(r"\binputs/external_cases/|external_cases/", re.I)),
    ("worker_return", re.compile(r"structured_return\.json|worker_return|expected_return|observed_result|cli_sessions", re.I)),
    ("program_artifact", re.compile(r"line_seed_bundles|camera_support_bundles|content_role_tags|label_packets|origin_maps|folder_inventory|generated/.+\.json", re.I)),
    ("runtime_event", re.compile(r"runtime/events|event_ledger|\.jsonl\b|receipt", re.I)),
    ("runtime_artifact", re.compile(r"\bruntime/|\.jsonl?\b|manifest|receipt|event", re.I)),
    ("generated_report", re.compile(r"\bdocs/reports/|report|closeout|validation|audit", re.I)),
    ("reference_repo", re.compile(r"\breferences/|git_search|repo|repository|github", re.I)),
    ("conversation_material", re.compile(r"내가|우리가|공간|대화|생각|궁금|흐름|재료", re.I)),
]

BROAD_SOURCE_SURFACE = {
    "worker_return": "runtime_artifact",
    "program_artifact": "runtime_artifact",
    "runtime_event": "runtime_artifact",
}

LENS_HINTS = [
    (
        "technical",
        ("기술", "구조", "mechanism", "architecture", "repo", "code", "runtime", "pipeline"),
    ),
    (
        "maker-intent",
        ("의도", "maker", "pain", "bottleneck", "왜 만들", "created", "problem"),
    ),
    (
        "user-intent",
        ("내가", "사용자", "왜 지금", "궁금", "원해", "목적", "direction"),
    ),
    (
        "line/axis",
        ("라인", "축", "line", "axis", "겹", "cluster", "connection"),
    ),
    (
        "feature-direction",
        ("기능", "붙", "적용", "방향", "feature", "purpose", "candidate"),
    ),
    (
        "risk",
        ("위험", "금지", "승격", "baseline", "promotion", "schema", "실행", "risk"),
    ),
    (
        "residue",
        ("residue", "흔적", "남", "archive", "re-emergence", "다시", "reread"),
    ),
    (
        "evidence/event",
        ("event", "ledger", "receipt", "manifest", "trace", "evidence", "actual", "happened", "증거", "발생"),
    ),
    (
        "expected-vs-observed",
        ("expected", "observed", "deviation", "return", "worker_return", "structured_return", "결과", "반환"),
    ),
    (
        "artifact-role",
        ("bundle", "label_packet", "origin_map", "line_seed", "inventory", "artifact", "generated", "역할"),
    ),
    (
        "return-state",
        ("validation_return", "return_state", "closeout", "final", "report", "완료", "회수"),
    ),
    (
        "next-move",
        ("next", "next_move", "next_allowed_move", "recommended", "다음", "이동", "branch"),
    ),
    (
        "narrative-mechanism-operational path",
        ("README", "hype", "서사", "mechanism", "operational", "검증", "validation"),
    ),
]

LENS_ORDER_BY_SOURCE = {
    "web_external_material": [
        "technical",
        "maker-intent",
        "user-intent",
        "line/axis",
        "risk",
        "residue",
        "narrative-mechanism-operational path",
    ],
    "external_material_file": [
        "technical",
        "maker-intent",
        "user-intent",
        "line/axis",
        "risk",
        "residue",
        "narrative-mechanism-operational path",
    ],
    "generated_report": [
        "user-intent",
        "line/axis",
        "risk",
        "residue",
        "return-state",
    ],
    "conversation_material": [
        "user-intent",
        "feature-direction",
        "line/axis",
        "residue",
        "risk",
    ],
    "runtime_event": [
        "evidence/event",
        "technical",
        "risk",
        "residue",
        "line/axis",
    ],
    "worker_return": [
        "expected-vs-observed",
        "risk",
        "residue",
        "next-move",
        "line/axis",
    ],
    "program_artifact": [
        "artifact-role",
        "evidence/event",
        "technical",
        "residue",
        "risk",
    ],
    "runtime_artifact": [
        "evidence/event",
        "technical",
        "risk",
        "residue",
        "line/axis",
    ],
}

GUARDRAIL_PATTERNS = (
    "do not",
    "금지",
    "baseline",
    "schema",
    "implementation",
    "runtime manifest",
    "promotion",
    "승격",
    "validator",
)

SKIP_TOKENS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "be",
    "by",
    "can",
    "com",
    "did",
    "do",
    "does",
    "else",
    "false",
    "for",
    "from",
    "http",
    "https",
    "id",
    "if",
    "in",
    "into",
    "is",
    "it",
    "may",
    "md",
    "no",
    "not",
    "of",
    "on",
    "or",
    "should",
    "that",
    "the",
    "then",
    "this",
    "to",
    "true",
    "v0",
    "v1",
    "was",
    "were",
    "will",
    "with",
    "www",
    "있는",
    "없는",
    "한다",
}


@dataclass(frozen=True)
class LoadedDoc:
    path: str
    text: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Emit a read-only space-boundary lookup packet as JSON."
    )
    parser.add_argument("input", nargs="?", help="Raw input text, URL, or path.")
    parser.add_argument("--input-file", type=Path, help="Read input text from a file.")
    parser.add_argument(
        "--limit",
        type=int,
        default=6,
        help="Maximum candidate assets / guardrails to include.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    raw_input = read_input(args).strip()
    if not raw_input:
        raise SystemExit("Provide input text or --input-file.")

    docs = load_known_docs()
    source_surface = guess_source_surface(raw_input)
    existing_local_path = resolve_local_path(raw_input)
    analysis_text = build_analysis_text(raw_input, existing_local_path)
    tokens = meaningful_tokens(analysis_text)

    candidate_assets = rank_candidate_assets(docs, tokens, limit=args.limit)
    microspace_matches = extract_microspace_matches(docs, analysis_text, tokens, limit=args.limit)
    candidate_lenses = suggest_lenses(analysis_text, docs, tokens, microspace_matches, source_surface)
    guardrails = extract_guardrails(docs, tokens, limit=args.limit)

    packet = {
        "packet_type": "space_boundary_lookup_packet",
        "packet_status": "read_only_suggestion",
        "input_ref": raw_input[:500],
        "input_analysis_scope": {
            "uses_raw_input": True,
            "uses_existing_local_file_text": bool(existing_local_path),
            "local_file_text_limit_chars": 20000 if existing_local_path else 0,
        },
        "source_surface_guess": source_surface,
        "existing_local_path": str(existing_local_path) if existing_local_path else "",
        "matched_indexes": [doc.path for doc in docs],
        "candidate_assets": candidate_assets,
        "matched_microspace_clusters": microspace_matches,
        "candidate_lenses": candidate_lenses,
        "known_guardrails": guardrails,
        "card_template": {
            "current_judgment": "",
            "reason": "",
            "selected_lenses": [row["lens"] for row in candidate_lenses[:4]],
            "next_move": "",
            "do_not": "",
        },
        "script_boundary": {
            "does_not_decide_final_state": True,
            "does_not_fetch_web": True,
            "does_not_write_files": True,
            "does_not_update_runtime": True,
            "codex_must_decide": [
                "user_intent",
                "active_lenses",
                "final_state",
                "guardrail_wording",
                "next_move",
                "whether_to_write_or_update_space_record",
            ],
        },
    }
    print(json.dumps(packet, ensure_ascii=False, indent=2))


def read_input(args: argparse.Namespace) -> str:
    if args.input_file:
        return args.input_file.read_text(encoding="utf-8")
    return str(args.input or "")


def load_known_docs() -> list[LoadedDoc]:
    docs: list[LoadedDoc] = []
    for rel_path in KNOWN_INDEXES:
        path = REPO_ROOT / rel_path
        if not path.exists():
            continue
        docs.append(LoadedDoc(path=rel_path, text=path.read_text(encoding="utf-8")))
    return docs


def meaningful_tokens(text: str) -> list[str]:
    raw = re.findall(r"[A-Za-z0-9_./:-]+|[가-힣]{2,}", text)
    tokens = []
    for token in raw:
        cleaned = token.strip().lower()
        if len(cleaned) < 2 or cleaned in SKIP_TOKENS:
            continue
        tokens.append(cleaned)
    return list(dict.fromkeys(tokens))[:80]


def guess_source_surface(text: str) -> dict[str, object]:
    hits = []
    for surface, pattern in SOURCE_SURFACE_HINTS:
        if pattern.search(text):
            hits.append(surface)
    if not hits:
        hits.append("plain_text_or_unknown")
    subtype = next((hit for hit in hits if hit in BROAD_SOURCE_SURFACE), "")
    primary = BROAD_SOURCE_SURFACE.get(hits[0], hits[0])
    if subtype:
        primary = BROAD_SOURCE_SURFACE[subtype]
    return {
        "primary": primary,
        "subtype": subtype,
        "all_candidates": hits,
        "confidence": "medium" if primary != "plain_text_or_unknown" else "low",
    }


def resolve_local_path(text: str) -> Path | None:
    candidate = text.strip().splitlines()[0].strip() if text.strip() else ""
    if not candidate or re.match(r"https?://", candidate):
        return None
    path = Path(candidate)
    if not path.is_absolute():
        path = REPO_ROOT / path
    return path.resolve() if path.exists() else None


def build_analysis_text(raw_input: str, existing_local_path: Path | None) -> str:
    if not existing_local_path or not existing_local_path.is_file():
        return raw_input
    try:
        file_text = existing_local_path.read_text(encoding="utf-8")[:20000]
    except UnicodeDecodeError:
        return raw_input
    return f"{raw_input}\n\n{file_text}"


def rank_candidate_assets(docs: list[LoadedDoc], tokens: list[str], *, limit: int) -> list[dict[str, object]]:
    rows = []
    for doc in docs:
        matched = match_terms(doc.text, tokens)
        base_score = len(matched)
        if "external_material_microspace_index" in doc.path:
            base_score += 2
        if "space_boundary_material_flow_map" in doc.path:
            base_score += 2
        if "space_translation_language_base" in doc.path:
            base_score += 1
        if base_score <= 0:
            continue
        rows.append(
            {
                "path": doc.path,
                "reason": reason_for_doc(doc.path),
                "matched_terms": matched[:12],
                "score": base_score,
                "authority_hint": authority_for_path(doc.path),
            }
        )
    rows.sort(key=lambda row: (-int(row["score"]), str(row["path"])))
    return rows[:limit]


def extract_microspace_matches(
    docs: list[LoadedDoc], raw_input: str, tokens: list[str], *, limit: int
) -> list[dict[str, object]]:
    micro = next((doc for doc in docs if doc.path.endswith("external_material_microspace_index_v0.md")), None)
    if not micro:
        return []

    sections = split_markdown_sections(micro.text)
    matches = []
    for title, body in sections:
        if not title.lower().startswith("6."):
            continue
        matched = match_terms(f"{title}\n{body}", tokens)
        title_matches = match_terms(title, tokens)
        if raw_input and any(part in body for part in urls_in(raw_input)):
            matched.append("source_url")
        if not matched:
            continue
        if len(matched) < 2 and "source_url" not in matched:
            continue
        score = len(matched) + (len(title_matches) * 4)
        if "source_url" in matched:
            score += 10
        matches.append(
            {
                "title": title,
                "matched_terms": list(dict.fromkeys(matched))[:10],
                "score": score,
                "current_state_hint": extract_yaml_value(body, "current_state"),
                "cluster_hint": extract_yaml_value(body, "cluster") or title,
                "primary_lens_hint": extract_yaml_value(body, "primary_lens"),
                "safe_next_move_hint": extract_yaml_value(body, "safe_next_move"),
                "promotion_barrier_hint": extract_yaml_value(body, "promotion_barrier"),
            }
        )
    matches.sort(key=lambda row: (-int(row["score"]), str(row["title"])))
    return matches[:limit]


def suggest_lenses(
    raw_input: str,
    docs: list[LoadedDoc],
    tokens: list[str],
    microspace_matches: list[dict[str, object]],
    source_surface: dict[str, object],
) -> list[dict[str, object]]:
    haystack = raw_input.lower()
    joined_docs = "\n".join(doc.text.lower() for doc in docs)
    rows = []
    for lens in high_confidence_microspace_lenses(microspace_matches):
        rows.append(
            {
                "lens": lens["lens"],
                "reason": "high_confidence_microspace_primary_lens",
                "matched_terms": lens["matched_terms"],
                "score": lens["score"],
                "surface_weighted": False,
            }
        )
    preferred_lenses = preferred_lens_order(source_surface)
    for index, lens in enumerate(preferred_lenses):
        rows.append(
            {
                "lens": lens,
                "reason": "source_surface_default_lens_order",
                "matched_terms": [
                    str(source_surface.get("subtype") or source_surface.get("primary") or "")
                ],
                "score": 50 - index,
                "surface_weighted": True,
            }
        )
    for lens, keywords in LENS_HINTS:
        direct = [kw for kw in keywords if kw.lower() in haystack]
        indirect = [kw for kw in keywords if kw.lower() in joined_docs and kw.lower() in tokens]
        score = len(direct) * 2 + len(indirect)
        if score:
            rows.append(
                {
                    "lens": lens,
                    "reason": "keyword_or_space_language_match",
                    "matched_terms": list(dict.fromkeys(direct + indirect))[:8],
                    "score": score,
                    "surface_weighted": False,
                }
            )
    for match in microspace_matches:
        hint = str(match.get("primary_lens_hint") or "").strip()
        for lens in split_lens_hint(hint):
            rows.append(
                {
                    "lens": lens,
                    "reason": "microspace_primary_lens_hint",
                    "matched_terms": [str(match.get("title") or "")],
                    "score": 2 + len(list(match.get("matched_terms") or [])),
                    "surface_weighted": False,
                }
            )
    if not rows:
        rows.append(
            {
                "lens": "user-intent",
                "reason": "fallback_lens_for_plain_input",
                "matched_terms": [],
                "score": 0,
                "surface_weighted": False,
            }
        )
    rows.sort(key=lambda row: (-int(row["score"]), str(row["lens"])))
    deduped = []
    seen = set()
    for row in rows:
        lens = str(row["lens"])
        if lens in seen:
            continue
        seen.add(lens)
        deduped.append(row)
    return deduped


def high_confidence_microspace_lenses(
    microspace_matches: list[dict[str, object]],
) -> list[dict[str, object]]:
    if not microspace_matches:
        return []
    top_match = microspace_matches[0]
    if int(top_match.get("score") or 0) < 25:
        return []

    rows = []
    for index, lens in enumerate(split_lens_hint(str(top_match.get("primary_lens_hint") or ""))):
        rows.append(
            {
                "lens": lens,
                "matched_terms": [str(top_match.get("title") or "")],
                "score": 70 - index,
            }
        )
    return rows


def preferred_lens_order(source_surface: dict[str, object]) -> list[str]:
    subtype = str(source_surface.get("subtype") or "")
    primary = str(source_surface.get("primary") or "")
    if subtype and subtype in LENS_ORDER_BY_SOURCE:
        return LENS_ORDER_BY_SOURCE[subtype]
    return LENS_ORDER_BY_SOURCE.get(primary, [])


def extract_guardrails(docs: list[LoadedDoc], tokens: list[str], *, limit: int) -> list[dict[str, object]]:
    rows = []
    for doc in docs:
        for line in doc.text.splitlines():
            normalized = line.strip(" -|`")
            if not normalized or len(normalized) > 220:
                continue
            lower = normalized.lower()
            if not any(pattern in lower for pattern in GUARDRAIL_PATTERNS):
                continue
            matched = match_terms(normalized, tokens)
            if matched or any(pattern in lower for pattern in ("baseline", "schema", "implementation")):
                rows.append(
                    {
                        "source_ref": doc.path,
                        "text": normalized,
                        "matched_terms": matched[:8],
                    }
                )
    unique = []
    seen = set()
    for row in rows:
        key = (row["source_ref"], row["text"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(row)
    return unique[:limit]


def match_terms(text: str, tokens: Iterable[str]) -> list[str]:
    lower = text.lower()
    counter: Counter[str] = Counter()
    for token in tokens:
        if token and token in lower:
            counter[token] += lower.count(token)
    return [term for term, _ in counter.most_common()]


def split_markdown_sections(text: str) -> list[tuple[str, str]]:
    sections: list[tuple[str, str]] = []
    current_title = ""
    current_lines: list[str] = []
    for line in text.splitlines():
        if line.startswith("##") or line.startswith("###"):
            if current_title:
                sections.append((current_title, "\n".join(current_lines)))
            current_title = line.strip("# ").strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_title:
        sections.append((current_title, "\n".join(current_lines)))
    return sections


def extract_yaml_value(text: str, key: str) -> str:
    match = re.search(rf"^\s*{re.escape(key)}:\s*(.+?)\s*$", text, re.M)
    return match.group(1).strip().strip('"') if match else ""


def urls_in(text: str) -> list[str]:
    return re.findall(r"https?://\S+", text)


def split_lens_hint(hint: str) -> list[str]:
    if not hint:
        return []
    pieces = re.split(r"\s*/\s*|,\s*", hint)
    return [piece.strip() for piece in pieces if piece.strip()]


def reason_for_doc(path: str) -> str:
    if "space_boundary_material_flow_map" in path:
        return "Boundary material flow map and default lens/camera route."
    if "external_material_microspace_index" in path:
        return "External material cluster and re-emergence index."
    if "space_translation_language_base" in path:
        return "Space language translation base and do-not-reduce terms."
    if "space_asset_map" in path:
        return "Repository-level asset map."
    if "space_asset_retrieval_manual" in path:
        return "Asset role retrieval guide."
    if "executable_runner_index" in path:
        return "Runner lookup by operating intent."
    return "Known space-support asset."


def authority_for_path(path: str) -> str:
    if path.startswith("docs/indexes/") or path.startswith("docs/guides/"):
        return "guide_or_index"
    if path.startswith("docs/notes/"):
        return "note_or_runner_index"
    return "candidate_context"


if __name__ == "__main__":
    main()
