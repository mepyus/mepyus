# Pre-1.12 Lower Input Action Map v0

## Verdict

`PASS_WITH_NOTE`

Before Phase 1.12, the useful move is not legacy identity backfill. It is to make the lower input organ readable as a distributed material-intake system and identify the minimum lower-side bridge requirements.

## 1. Immediately Useful Before 1.12

- Define a lower-output-to-upper admission checklist.
- Draft a compare-ready lower packet shape, without implementing it yet.
- Reuse existing observer outputs as examples: source manifest, split units, processing trace, readable board, operator summary.
- Treat preprocess comparison JSON as the strongest current packet-candidate example.
- Preserve the “do not patch inputter/labeler/promotion” boundary.

## 2. Can Be Deferred

- Full provenance graph.
- Global artifact graph.
- UI / Inputs Intake panel work.
- Canonical path migration.
- Final readiness taxonomy lock.
- Direct `inputter.py` or `labeler.py` changes.
- Phase 1.12 legacy identity backfill.

## 3. Minimum Modification Needed To Align With Upper CLI Spine

No code change is required in this pre-step, but the minimum future bridge should map:

| lower field | upper use |
| --- | --- |
| `source_path` / `source_ref` | `search_targets.path`, evidence `source_ref` |
| `detected_profile` / `input_kind` | constraints and ambiguity notes |
| `split_mode_used` | grounding/excerpt mode hint |
| `unit_id`, `start_ref`, `end_ref`, `text_excerpt` | evidence pointer/excerpt candidates |
| `processing_trace.engine_stage` | confidence / fallback note |
| `readiness_read.status` | task mode and hold/proceed note |
| `check_surface.next_checkpoint` | next probe candidates |
| generic/topic-bearing anchor split | merge/diff evidence quality note |

## 4. Lower-Side Cleanup Needed Before 1.12

- Mark which generated outputs are residue-only, evidence-ready, engine-ingest-ready, or packet-candidate.
- Select 3-5 representative lower artifacts as bridge examples.
- Write a small bridge spec before touching legacy identity backfill.
- Keep the lower organ definition limited to material intake, not upper request intake.

## 5. Can Move Into 1.12 Or Later

- Backfilling identity anchors into older runtime artifacts.
- Content-signature family matching.
- Automated lower-to-upper packet builder.
- Full line/axis candidate object emission.
- UI adapter work.

## Why This Is Needed Before 1.12

Phase 1.12 legacy identity backfill would improve artifact identity, but it would not solve the lower organ’s key ambiguity: which lower material outputs are ready to become upper evidence or packet candidates.

If lower readiness is not clarified first, identity backfill can make old artifacts more traceable while leaving line/axis bridge decisions just as manual.

## Risk If Lower Is Not Re-read First

- legacy identity gets added to artifacts that are still only residue;
- packet-candidate and evidence-ready outputs remain mixed;
- upper CLI runs keep relying on manual interpretation;
- line/axis connection remains dependency-heavy;
- middle-layer gap gets mistaken for retrieval or identity gap.

## Recommended Next Move Before Phase 1.12

Create a small `lower_to_upper_bridge_minimum_v0` spec or report that defines:

- lower readiness levels;
- admission checklist;
- representative artifact examples;
- field mapping into upper packet/evidence;
- explicit non-goals: no UI, no path move, no baseline lock, no inputter/labeler patch.

## Validation

- Action map is concrete enough to execute: PASS.
- Next step is narrow: PASS.
- It does not start Phase 1.12 legacy identity backfill: PASS.
- It keeps lower and upper input organs separated: PASS.
