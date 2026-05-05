# PATCH_BEFORE_LIMITED_TRIAL_V0

## 1. Patch Summary
- **Tool-Readable Surface**: README에 'Controller가 아님'을 명시적으로 강조하고, 도구의 역할을 '상태 읽기 및 제안'으로 재한정함.
- **Context Bundle**: 프로젝트 전체 덤프 방지를 위해 'Material Family'별 우선순위 할당 규칙을 강화.

## 2. TOOL_READABLE_SURFACE_PATCH_V0
- **Problem**: '표면'과 '제어기(Controller)'의 경계가 일부 도구에서 혼동됨.
- **Patch**: README와 BOUNDARY_RULES에 "이 표면은 시스템을 제어하지 않으며, 오직 정보를 제공하고 제안을 접수하는 표면임"을 상단에 굵게 명시.

## 3. CONTEXT_BUNDLE_PATCH_V0
- **Problem**: Context Bundle이 모든 문서를 포함하려는 경향.
- **Patch**: `ACTIVATED_MATERIALS` 필드에 '최소 정보 원칙(Principle of Least Information)' 적용. 필요한 Material Family만 선별하도록 제약 강화.

## 4. LIMITED_TRIAL_ENTRY_CHECK_V0
- Surface/Bundle 명확성: 확보.
- 경계 준수: 확인.
- 사용자 판단권 보존: 확인.
- **결정**: LIMITED_TRIAL_PREP_READY_WITH_NOTES
