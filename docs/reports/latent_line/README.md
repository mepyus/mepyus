# Latent Line Family

이 폴더는 아직 문서를 이동하지 않고, `latent_line_*` belt의 의미를 먼저 묶어 읽기 위한 index 면이다.

의미:

- `observation and line-thickening line` 에서 latent line을 어떻게 등록하고, 감시하고, reread 규칙으로 연결하는지 보여준다.
- 연결 밀도가 높아서 즉시 재배치하면 링크 파손 범위가 커질 수 있으므로, 이번 단계에서는 `move`보다 `surface`를 먼저 세운다.

핵심 문서:

- [latent_line_watchpoints_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/latent_line_watchpoints_v1.md)
- [latent_line_registry_and_material_scan_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/latent_line_registry_and_material_scan_v1.md)
- [latent_line_first_reread_rule_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/latent_line_first_reread_rule_v1.md)

핵심 runtime surface:

- [latent_line_registry_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/latent_line_registry_v1.json)

정리 규칙:

- 이 belt는 참조를 먼저 줄이지 않은 채 물리 이동하지 않는다.
- 이후 재배치는 `family index`, `today_handoff_index`, `line_first_cleanup_map`, 주요 note/policy 링크를 먼저 줄인 뒤에만 한다.
