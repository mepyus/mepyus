# CLI_SESSION_PROTOCOL_V0

| Field | Definition | Drift Risk |
| :--- | :--- | :--- |
| **session_id** | 고유 식별자 | - |
| **session_goal** | 도달할 목적 | 목적 이탈 |
| **work_steps** | [Search, Do, Log, Handoff] | 절차 생략 |
| **stop_conditions** | 즉시 중단 트리거 | 무시 및 강행 |

---

# SESSION_START_CHECKLIST_V0

1. 프레임워크 확인(Program-level).
2. 샌드박스 작업인지 확인(금지).
3. 구현/수정 사전 승인 여부 확인.
4. 세션 목표 숙지.
5. 공간 기록 검색 선행(필수).
6. 트리거 활성화 확인.
7. 라인/축/카메라/렌즈 선정.
8. 재료군(Material Family) 선택.
9. 컨텍스트 번들(Context Bundle) 구성.
10. 도구 역할(Role Profile) 할당.
11. 드리프트 리스트(Drift Watchlist) 확인.
12. 반환 형식 고정.
13. 중단 조건 숙지.

---

# SESSION_RETURN_FORMAT_V0

1. **4-Line Judgment Card**: [쓸 수 있나?/왜?/다음엔?/조심할 점은?]
2. **Session Output**: 결과 본문.
3. **Evidence**: 사용된 기록군 및 포인터.
4. **Boundary Check**: 자동화/수정/구현 여부 확인.
5. **Issue Log**: 비차단 이슈 기록.
6. **Next Session Handoff**: 차기 세션 지시.
7. **Package Digest**: 패키지 상태 요약.

---

# SESSION_DRIFT_RESPONSE_RULES_V0

| Drift Type | Default Response | Stop/Continue |
| :--- | :--- | :--- |
| **구현/수정 드리프트** | 경고 및 즉시 중단 | STOP |
| **언어적 드리프트** | 기록 후 경고 | Continue |
| **로컬 세션 함정** | 이슈 기록 | Continue |
| **컨트롤러 변질** | 경고 및 즉시 중단 | STOP |
