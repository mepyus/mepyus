# SPACE_DEPTH_TEST_FRAME_V0

## 1. Depth Score Criteria
- **SHALLOW_READ**: 공간 단어만 모사함. 실제 기록과의 연결 고리(Evidence Pointer) 없음.
- **MEDIUM_READ**: 일부 기록과 경계 규칙을 반영함. 그러나 맥락적 깊이(왜 이 재료인가?)가 부족함.
- **DEEP_READ**: 목적, 기존 기록, 경계, 실패 패턴, 사용자의 판단 기준을 모두 유기적으로 연결하여 제안함. 놓친 부분에 대한 증거(Evidence Gap)를 명확히 함.

---

# EVIDENCE_ROUTE_REQUIREMENTS_V0

도구의 모든 제안은 반드시 다음을 포함해야 함:
1. **Source**: 어떤 Material Family를 활성화했는가?
2. **Context**: 어떤 Line/Axis/Camera/Lens와 연결했는가?
3. **Drift Check**: 이 제안이 구현/자동화 드리프트가 아님을 어떻게 보장하는가?
4. **Not Inspected**: 무엇을 보지 않고 이 제안을 했는가? (Evidence Gap)

---

# USER_FACING_RESULT_CARD_TEMPLATE_V0

1. **이 입력의 목적**: (User Purpose)
2. **읽은 공간 재료**: (Material Families)
3. **판단 근거**: (Evidence Used & Connection)
4. **결과물(쓸 수 있는 값)**: (Recoverable Value)
5. **조심할 값(보류/위험)**: (Hold/Boundary Risk)
6. **다음 행동 제안**: (Next Action)
7. **판단 필요사항**: (User Decision Needed)
