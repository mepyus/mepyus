# Graphify Note

## Source

Obsidian note:

```text
/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/04-28/graphify 지도3.md
```

## Compact material summary

Graphify is a tool that turns a folder of code, documents, papers, images, video, or audio into a knowledge graph.

Core outputs include:

- `GRAPH_REPORT.md`
- `graph.json`
- `graph.html`
- `cache/`
- query/path/explain style access

The important usage pattern is not to paste the whole graph into a prompt. First read `GRAPH_REPORT.md`, then ask focused graph queries or extract a small subgraph.

Graphify separates relationships as:

- `EXTRACTED`
- `INFERRED`
- `AMBIGUOUS`

This matches the user's provenance-first principle because found relationships, inferred relationships, and uncertain relationships must not be treated as the same kind of truth.

## Candidate reading

In the user's space, Graphify is not an immediate adoption target.

It is a `Graph Layer Candidate`:

```text
Deep Space
-> Graph Layer Candidate
-> small context injection for Worker/CLI
```

## Risks

- graph result mistaken as truth
- inferred edge mistaken as baseline
- whole Deep Space graphified too early
- sensitive material sent to model/API extraction
- always-on hook installed too early
- graph output becoming another noisy generated layer

## Current recommended posture

Use only as a read-only candidate in a small test folder.

Do not apply to the whole Deep Space.
Do not install hooks/MCP/watch mode.
Do not commit graphify output as baseline.
