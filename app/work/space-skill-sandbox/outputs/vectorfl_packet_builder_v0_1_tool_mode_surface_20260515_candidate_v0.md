# VectorFL Packet Builder v0.1
# Tool-mode Aware Surface
# 2026-05-15 Candidate v0

## 1. Status

Verdict:
  PACKET_BUILDER_V0_1_USABLE_WITH_WATCH

Position:
  export valve for bounded external-tool input

Not:
  execution approval
  prompt authority
  workflow
  schema
  registry
  ontology
  dispatch system
  baseline

Source sequence:
  `20.md` through `25.md`

## 2. Core Definition

Packet Builder turns matured VectorFL judgment into a small packet for an external tool. It must not open the whole space to that tool.

The packet exports only:

- task
- smallest anchor
- allowed context
- forbidden context
- WATCH
- HOLD
- return format
- post-return route

## 3. Tool Modes

### execution-capable

Examples:
  Codex-like agents, repo-side workers, patch tools

Risk focus:
  file writes, shell commands, patch scope, destructive operations, hidden broad repo edits

Packet must narrow:
  exact task, file scope, allowed inspection, forbidden edits, verification expectation

### broad-reading

Examples:
  Gemini-like broad synthesis tools

Risk focus:
  synthesis-as-truth, recommendation-as-adoption, imported vocabulary becoming local law

Packet must narrow:
  selected anchors, reading purpose, no adoption authority, return as reference/lens/WATCH only

### API-data-transfer

Examples:
  API clients, CLI tools with network or account access

Risk focus:
  credentials, account mutation, uploads, downloads, private data movement

Packet must narrow:
  no credential use unless explicitly approved, no account mutation, no network action beyond approved boundary

### browser-observation

Risk focus:
  broad web crawl, currentness claims, visual observation mistaken for action permission

Packet must narrow:
  exact page or domain, observation-only boundary, citation or screenshot return shape

### memory-retrieval

Risk focus:
  memory source authority, stale or over-broad retrieval, accidental promotion

Packet must narrow:
  retrieval target, candidate-only status, no direct current-position update

### mixed-framework

Risk focus:
  tool role confusion, framework terms becoming ontology, execution hidden inside reading

Packet must narrow:
  primary mode, secondary mode, forbidden promotion, explicit return route

## 4. Minimal Packet Template

```text
packet_id:
  [local id]

target_tool:
  [Codex / Gemini / CLI / browser / memory / other]

tool_mode:
  execution-capable | broad-reading | API-data-transfer | browser-observation | memory-retrieval | mixed-framework | unknown

risk_focus:
  [the main drift or boundary risk]

task:
  [one bounded task]

smallest_anchor:
  [the minimum source/context to use]

allowed:
  [what the tool may do]

forbidden:
  [what the tool must not do]

WATCH:
  [specific drift to report]

HOLD:
  [actions that require separate user approval]

return_format:
  [short structure expected back]

post_return_route:
  Return Packet -> Maturation Queue Item -> Daily Loop
```

## 5. Dry-run Packet A: Codex

```text
target_tool:
  Codex

tool_mode:
  execution-capable

risk_focus:
  repo-side file/command/patch boundary

task:
  inspect whether the one-page operator surface is reflected in existing candidate notes

smallest_anchor:
  selected candidate files under app/work/space-skill-sandbox/outputs

allowed:
  read files, summarize mismatch, propose bounded patch

forbidden:
  patch without explicit request, app route wiring, current-position update, manifest promotion

WATCH:
  turning candidate note into product architecture

return_format:
  findings, touched files if any, residual HOLD
```

## 6. Dry-run Packet B: Gemini

```text
target_tool:
  Gemini

tool_mode:
  broad-reading

risk_focus:
  synthesis-as-truth and recommendation-as-adoption

task:
  read selected anchors and identify lens candidates

smallest_anchor:
  decision surface, daily loop surface, packet builder surface

allowed:
  synthesize patterns, name tensions, return reference-only lens candidates

forbidden:
  recommend adoption, create rules, define ontology, claim baseline authority

WATCH:
  fluent synthesis becoming local truth

return_format:
  reference observations, lens candidates, WATCH, HOLD
```

## 7. Dry-run Packet C: API/CLI High-risk

```text
target_tool:
  API/CLI tool

tool_mode:
  API-data-transfer

risk_focus:
  credential/API/account/data-transfer boundary

task:
  describe the smallest possible no-credential dry inspection

smallest_anchor:
  tool documentation excerpt or local help text only

allowed:
  read-only local help or reference documentation

forbidden:
  credential access, login, upload, account mutation, network call, background scheduler

WATCH:
  harmless command hiding API or account mutation

return_format:
  boundary map, required approvals, HOLD list
```

## 8. WATCH

- `tool_mode` is a practical risk focus, not an ontology.
- `allowed` is not broad permission.
- `return_format` is not a rigid schema.
- Packet creation is not dispatch.
- Packet Builder does not decide approval.

`STATUS: PACKET_BUILDER_V0_1_TOOL_MODE_SURFACE_CANDIDATE_PREPARED_WITH_WATCH`
