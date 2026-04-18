# second candidate watch rule auto connection v1

## 0. Verdict

**PASS**

## 1. Integration surface

- `app/runtime/runtime_preflight.py`
- `scripts/run_runtime_preflight.py`
- `runtime/manifests/second_candidate_watch_rules.json`
- `runtime/manifests/pipeline_observation_registry.jsonl`

## 2. Sample watch evaluation rows

### 2.1 Reflection on enterprise

- `candidate_name=raw_to_first_pass_to_report`
- `family=enterprise`
- `mode=reflection`
- `watch_rule_evaluated=true`
- `watch_result=boundary_only_variation`
- `collapse_target=raw_to_first_pass_to_report`
- `triggered_seed_name=null`
- `watch_reason=different_mode_leads_to_different_entry_surface; family=enterprise`

This is the important case for the current test because it shows the watch rule can evaluate an observation append and keep the candidate in boundary form rather than spawning a new seed.

## 3. Why no second seed triggered

- The observation still collapses back to the current clear candidate plus a mode boundary note.
- The watch rule therefore does not name a new candidate.
- The registry row now makes that explicit without changing the candidate set.

## 4. Next minimal fix

- Keep the watch rule thin.
- Keep writing the watch result on new observation appends.
- Only revisit `triggered_seed_name` if a genuinely distinct repeated path appears.

