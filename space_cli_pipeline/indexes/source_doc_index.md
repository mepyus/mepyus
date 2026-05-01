# Source Document Index

| Source ID | Path | Role | Use When | Do Not Copy |
| :--- | :--- | :--- | :--- | :--- |
| manual_pipeline | docs/reports/space_cli_manual_pipeline_v0.md | Core Logic | 파이프라인 11단계 이해 | 원문 전체 |
| io_contract | docs/reports/space_cli_pipeline_stage_io_contract_v0.md | I/O Specs | 입출력 데이터 정합성 확인 | 원문 전체 |
| task_packet | docs/reports/space_cli_lightweight_task_packet_minimum_fields_v0.md | Packet Spec | 작업 패킷 구성 시 참조 | 원문 전체 |
| reflux_model | docs/reports/space_cli_reflux_memory_state_model_v0.md | Memory Model | 환류 기억 분류 시 참조 | 원문 전체 |
| dispatch_policy | gemini/protocols/gemini_task_dispatch_policy_v1.md | Role Policy | 제미나이 업무 배정 시 참조 | 원문 전체 |
| package_readme | space_cli_pipeline/README.md | package entry | 처음 패키지 목적과 읽기 순서를 확인할 때 | full file |
| package_manual | space_cli_pipeline/MANUAL.md | operation manual | 실제 수동 운용 절차를 확인할 때 | full file |
| package_pipeline | space_cli_pipeline/PIPELINE.md | 11-stage manual pipeline | 단계 순서와 stop condition을 확인할 때 | full file |
| package_guardrails | space_cli_pipeline/GUARDRAILS.md | guardrails and anti-rationalization | 과승격, 자동 실행, 외부자료 과수용 위험을 점검할 때 | full file |
| package_roles | space_cli_pipeline/ROLES.md | role boundary | Space/User/Codex/Gemini 역할을 확인할 때 | full file |
| package_case_001 | space_cli_pipeline/cases/run_001_gemini_role_overpromotion.md | incident case | Gemini role over-promotion risk를 확인할 때 | full file |
| manual_pipeline_closeout | docs/reports/space_cli_manual_pipeline_closeout_v0.md | pipeline closeout | 수동 파이프라인 v0의 결론, 다음 단계, 자동화 금지 원칙을 확인할 때 | full file |
| trigger_usage_note | docs/reports/space_boundary_material_trigger_usage_note_v0.md | user-facing trigger usage note | “공간에 넣어보기” 사용자 트리거와 4줄 카드 흐름을 확인할 때 | full file |
| surface_catalog | docs/reports/space_boundary_trigger_flow_surface_catalog_package_v0.md | source surface and lens catalog | 재료 표면(source surface)과 lens order 판단 기준을 확인할 때 | full file |
| gemini_incident_record | gemini/reports/gemini_upgrade_report_20260426.md | quarantined Gemini role over-promotion incident record | Gemini 과승격 위험, bounded worker 원칙, quarantine 사례를 확인할 때 | full file |
| assets_md_layer_lens_mismatch_case | space_cli_pipeline/cases/assets_md_layer_lens_mismatch_case_v0.md | case | Use when a proposed structure seems coherent but may stand on a different layer than the user's space philosophy. Do not use as ASSETS.md creation mandate. | full file |
