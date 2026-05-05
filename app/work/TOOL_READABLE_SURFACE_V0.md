# TOOL_READABLE_SURFACE_V0

## 1. README
- **Entry point**: 시작 전 반드시 읽으시오.
- **Order**: 읽기(Read) -> 해석(Interpret) -> 제안(Propose).
- **Rule**: 직접 수정하지 말고, 승인된 범위 내에서 제안만 하시오.

## 2. CURRENT_MODE
- **Definition**: VectorFL은 실행기(Executor)가 아닌 공간 어댑터(Space Adapter)임.
- **Status**: Manual-triggered / Semi-manual 모드.

## 3. BOUNDARY_RULES
- **Prohibited**: 명령 실행, 파일 수정, 폴더 생성, 자동화, Runner/Controller 생성.
- **Reason**: 실행과 판단은 분리되어야 함. 도구의 산출물은 참고용(Material)이지 권위(Authority)가 아님.

## 4. AUTHORITY_LEVELS
1. User live instruction
2. Current mode
3. Explicit baseline/constitution
4. Current candidate
5. Supervisor-reviewed closeout
...
10. Tool output (가장 낮음)

## 5. SPACE_INDEX
- 재료 검색 가이드: 전체 스캔 금지. 활성화된 Line/Axis/Camera/Lens 기반 검색.

## 6. INTERPRETATION_GUIDE
- **Line/Axis/Camera/Lens**: 기존 공간 기록을 현재 목적에 맞게 재구성하는 관점.

## 7. MISSION_PACKET_TEMPLATE
- **Input Structure**: [mission, user_purpose, activation_trigger, related_line, ..., recovery_route]

## 8. RETURN_RECOVERY_RULES
- **Output**: 4-Line Judgment Card + Package Digest.
- **Recovery**: Recover/Candidate/Watch/Hold/Reject 등으로 분류하여 제출.

---

# SURFACE_READ_ORDER_V0
1. README -> 2. CURRENT_MODE -> 3. BOUNDARY_RULES -> 4. AUTHORITY_LEVELS -> 5. SPACE_INDEX -> 6. INTERPRETATION_GUIDE -> 7. MISSION_PACKET_TEMPLATE -> 8. RETURN_RECOVERY_RULES

---

# SURFACE_TO_ACTIVATION_LINKS_V0
| Surface | Activation Role | Depends on | Feeds into |
| :--- | :--- | :--- | :--- |
| SPACE_INDEX | 검색 가이드 | Activation Map | Context Bundle |
| INTERPRETATION_GUIDE | 분석 관점 제공 | Activation Map | Mission Packet |
