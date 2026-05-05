# WEB_GROUNDED_EXTERNAL_TOOL_PATTERN_MAP_V0

| Pattern | External Usage | VectorFL Adoption | Drift Risk |
| :--- | :--- | :--- | :--- |
| **AGENTS.md** | 프로젝트 규칙 표면 | Tool-Readable Surface | Instruction 과대 팽창 |
| **Skills** | 재사용 가능 절차 | Bounded Reusable Procedure | 자동화 변질 |
| **Subagents** | 역할 분리 | Tool Role Profiles | 제어권 드리프트 |
| **Broad Scan** | 대형 컨텍스트 읽기 | ISS-05 차단 (Scoped Search) | 전체 스캔 시도 |

---

# PACKAGE_2_TEST_CANDIDATES

1. **Tool-Readable Surface Compatibility**: instruction-surface로 작동하는가?
2. **Procedure Skill Test**: Bounded Procedure가 자동화 없이 작동하는가?
3. **Role Containment**: Subagent 드리프트 방지 능력 검증.
4. **ISS-05 Stress**: 스캔 범위 제한(Broad Scan Boundary) 경계 테스트.
5. **Digest Evidence**: Return 컨트랙트 준수 여부.

---

# ISSUE_WATCH

- **ISS-08**: instruction surface가 지나치게 길어져 controller처럼 인식될 위험.
- **ISS-09**: skill이 자동화 스크립트로 오해될 위험.
