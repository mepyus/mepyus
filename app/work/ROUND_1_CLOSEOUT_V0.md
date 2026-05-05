# ROUND_1_ARTIFACT_INDEX_V0

| artifact_id | session | name | status | notes |
| :--- | :--- | :--- | :--- | :--- |
| A01 | 0/1 | Program Frame | Recover | - |
| A02 | 0/1 | External Pattern Map | Recover | - |
| A03 | 2 | Activation Map | Recover | - |
| A04 | 3 | Tool-Readable Surface | Recover | - |
| A05 | 4 | Context Bundle | Recover | - |
| A06 | 5 | Tool Role Profiles | Recover | - |
| A07 | 6 | CLI Session Protocol | Recover | - |
| A08 | 7 | Review Gate | Recover | - |
| A09 | 8 | First Full Pass Plan | Preserve | - |
| A10 | 8.5 | First Full Pass Run | Preserve | - |
| A11 | 9 | Post-Pass Review | Preserve | - |

---

# ROUND_1_CONSISTENCY_REVIEW_V0

- **consistent_links**: Activation Map -> Bundle -> Tool Flow.
- **broken_or_unclear_links**: 일부 도구의 역할 프로필과 실제 수행 간 미세한 괴리.
- **authority_confusions**: 도구 출력을 '최종 결과'로 인지하려는 경향.

---

# ROUND_1_PRESERVE_FIX_HOLD_TABLE_V0

| item_id | item | classification | recommended_action |
| :--- | :--- | :--- | :--- |
| PRV01 | Activation Map | Preserve | 2회차 입력 후보로 승격 |
| FIX01 | Review Gate | Fix Before 2nd | 분류 기준 세분화 |
| FIX02 | Drift Watchlist | Fix Before 2nd | Codex 구현 드리프트 방지 강화 |

---

# SECOND_PASS_ENTRY_DECISION_V0

- **decision**: READY_FOR_SECOND_PASS_WITH_NOTES
- **reason**: 구조적 파이프라인의 전반적인 정합성이 확인됨.
- **must_fix_before_next**: Review Gate 판단 세분화.

---

# OPERATOR_BOARD_V0

- **Current Goal**: 2회차 재구성(Second Pass) 준비.
- **Current Stage**: Round 1 Closeout 완료.
- **What Worked**: 검색 우선 루틴(Search-First) 및 경계 강화.
- **Main Risks**: 도구의 구현 드리프트 및 확정적 언어 사용.
- **Next Action**: Session 10 (Second Pass Recomposition) 단계로 전환.
- **User Decision Needed**: 없음 (현재 프로세스 내 해결 가능).
