# Gemini CLI Space Orientation Packet v0

## 1. status

```yaml
packet_status: gemini_cli_orientation_packet
verdict: PASS_WITH_NOTE
baseline_lock: false
schema_enforcement: false
controller_implementation: false
runtime_manifest: false
index_update: false
```

## 2. what this space is

This space is not a plain file store.

It is an operating space that rereads and matures user thoughts, records, conversations, code, experiment results, and judgment traces.

The space treats not only final outputs but also process, failed paths, return reasons, and judgment residue as assets.

The purpose is not to become dependent on external tools. The purpose is to keep an internal standard strong enough to attach external tools such as Codex, Gemini, CLI workers, and scripts as role-bounded workers.

## 3. VectorFL / integrated-engine direction

The current body is read through three surfaces:

- User surface: receives the user's request, purpose, material, and operating intent.
- VectorFL surface / space surface: rereads input, translates it, judges source surface, line/axis, residue, and next route.
- Engine surface / movement layer: handles processing, execution, validation, trace, and return.

External tools are not the body of the space.

Codex, Gemini, CLI tools, scripts, and workers are role-specific workers attached to the space. They can help execute or check bounded work, but they do not own final judgment.

## 4. 공간에 넣어보기 flow

User-facing names:

- 공간에 넣어보기
- 재료 넣어보기

User trigger:

```text
이거 공간에 넣어봐.
```

User-facing output:

```text
쓸 수 있나?
왜?
다음엔?
조심할 점은?
```

Internal flow:

```text
material enters
-> source surface 판단
-> source-surface별 lens order 적용
-> 필요한 자산 조각만 참조
-> 사용자-facing 4줄 카드 반환
-> 필요할 때만 note_only / 9-field candidate / deeper probe 판단
```

## 5. important separation

The 4-line card is a user-facing indicator.

Gemini, Codex, or any CLI worker must not treat the 4-line card as the only context needed for judgment.

An internal task packet should include:

- material text or material reference
- source surface candidate
- lens order
- relevant asset slice
- guardrails
- expected output format

Gemini is not just a 4-line card generator. Gemini is a fast processing assistant that reads a bounded task packet and drafts a first judgment.

## 6. default source surfaces

| source surface | user-language meaning | lens order |
| --- | --- | --- |
| `conversation_material` | 대화 재료 | user-intent -> feature-direction -> line/axis -> residue -> risk |
| `external_material_file` | 외부자료 | technical -> maker-intent -> user-intent -> line/axis -> risk -> residue |
| `generated_report` | 만들어진 보고서 | user-intent -> line/axis -> risk -> residue -> return-state |
| `worker_return` | 작업 결과 | expected-vs-observed -> risk -> residue -> next-move -> line/axis |
| `program_artifact` | 코드/도구 조각 | artifact-role -> evidence/event -> technical -> residue -> risk |
| `runtime_event` | 실행 흔적 | evidence/event -> technical -> risk -> residue -> line/axis |

## 7. read current conflicts by freshness

If older integrated-engine documents conflict with the current Space Boundary / 공간에 넣어보기 flow, prefer the current trigger-flow documents.

Current priority:

1. `docs/reports/space_boundary_material_trigger_usage_note_v0.md`
2. `docs/reports/space_boundary_trigger_flow_surface_catalog_package_v0.md`
3. `docs/reports/space_boundary_material_application_examples_package_v0.md`
4. `docs/reports/space_boundary_material_application_examples_trial_note_v0.md`
5. `docs/reports/space_boundary_material_application_examples_closeout_v0.md`

## 8. do not

- Do not baseline lock.
- Do not implement a controller.
- Do not create schema.
- Do not create runtime manifest.
- Do not auto-update index or microspace.
- Do not modify helper or code unless explicitly instructed.
- Do not change source surface taxonomy.
- Do not force 9-field records on every input.
- Do not treat PASS as final completion or baseline confirmation.
- Do not read all repo documents by default.

## 9. operating sentence

Gemini should help the space process bounded material faster.

Gemini should not replace the space's judgment, direction, or validation loop.
