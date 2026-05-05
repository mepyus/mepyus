# REVIEW_RECOVERY_GATE_V0

## 1. Judgment Fields
- `gate_id`: 고유 식별자
- `input_source`: 결과물 제공 도구
- `input_type`: 결과물 유형
- `authority_check`: 권위 침범 여부
- `boundary_check`: 경계 위반 여부
- `evidence_check`: 근거 충분성
- `classification`: 분류(Recover, Candidate, Watch, Hold, Reject, 등)
- `recoverable_material`: 공간 회수 대상
- `next_session_handoff`: 차기 세션 지정

---

# CLASSIFICATION_RULES_V0

| Class | Definition | Action |
| :--- | :--- | :--- |
| **Recover** | 즉시 활용 가능 | Material로 회수 및 기록 |
| **Candidate** | 검토 후 활용 가능 | Candidate 보관 및 관리 |
| **Watch** | 신호는 있으나 위험/불확실 | Issue Log 기록 후 관찰 |
| **Hold** | 추후 활용 예정 | 보관(Hold) 폴더로 이동 |
| **Reject** | 목적/경계 위반 | 폐기 후 사유 기록 |
| **Needs User** | 사용자 판단 필수 | 사용자 보고 |

---

# REVIEW_CHECKLIST_V0

1. 도구 역할 준수 여부
2. Context Bundle 사용 적절성
3. 기존 기록 우선 활용 여부
4. Tool-Readable Surface 참조 여부
5. 경계 규칙(Boundary Rules) 준수 여부
6. 결과 반환 형식 준수 여부
... (총 15개 항목)

---

# DIGEST_EVIDENCE_RULES_V0

- **Digest-first**: 사용자를 위해 핵심 요약은 먼저 제시하되, 증거는 반드시 포함.
- **Evidence Requirement**: [재료군, 포인터, 활용 방식, 권위/경계 체크]

---

# USER_JUDGMENT_GATE_V0

- **Mandatory User Input**: 정책/권한/경계 위반 대응/Baseline 승격.
- **Avoid**: 일상적인 분류, 단순한 서식 수정, 루틴 검토.
