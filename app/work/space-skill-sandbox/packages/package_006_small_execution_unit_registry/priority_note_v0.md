# Priority Note v0 - Small Execution Units

## 0. Status

- status: sandbox candidate
- implementation_created: false
- prototype_decision: false
- automation: false
- baseline: false

## 1. Priority Judgment

The strongest current candidate is:

```text
package_metadata_scan.sh
```

It addresses the most immediate repeated bottleneck:

```text
bounded package discovery before deep read
```

## 2. Why It Is Stronger Than Other Candidates

Compared with other candidates, `package_metadata_scan.sh` has:

- narrower input scope
- clearer output boundary
- lower judgment risk
- direct evidence from Package 004
- clear Found / Guessed / Reviewed boundary
- package-local write target

## 3. Why Not Implement Yet

Implementation should wait because:

- Package 005 already hit user approval stop point
- only one metadata-first trial has been run
- output compactness needs user judgment
- overwrite behavior must be approved
- max header lines and raw/outbox handling must be approved

## 4. Preflight Before Implementation

Before any prototype, decide:

- exact script name
- allowed package root
- output filename
- overwrite refusal behavior
- max header lines
- whether raw/outbox are file-size only or shallow-read
- whether report writes to file or stdout first

## 5. Recommended Next Package

Package 007 should be:

```text
First Tiny Script Prototype Decision
```

It should choose whether `package_metadata_scan.sh` is the first prototype, and define the stop point for user approval.

Do not implement in Package 007 unless the user explicitly changes the boundary.

## 6. Closeout

This is a sandbox priority note only.
No script was implemented.
No source-space promotion was performed.
No baseline was created.
No automation, hook, MCP, watch mode, graph, ontology, router, controller, schema, Gemini result auto-application, or production workflow was created.
