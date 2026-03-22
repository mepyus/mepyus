# Mismatch Branch Policy

pressure mismatch로 생긴 branch는 오류 정리 대상이 아니라 공간 과정의 관찰 기록으로 남긴다.

잠금 기준:

- `space_cell_branched` 이벤트는 append-only로 유지한다.
- `pressure_signature_mismatch_or_absent`는 실패 코드가 아니라 branch reason으로 읽는다.
- mismatch branch는 observer에서 직접 보이게 해야 한다.

의도:

- 공간은 정답을 찾기보다 과정을 탐구한다.
- mismatch는 잘못된 흔적이 아니라 다른 형성 조건이 드러난 흔적일 수 있다.
- 이미 생긴 분기를 지워서 깨끗한 경로만 남기지 않는다.

운영 기준:

- observer는 branch reason count와 branch sequence를 보여준다.
- clean-path demo가 필요하더라도 기존 runtime branch history는 보존한다.

금지 기준:

- mismatch branch를 silent cleanup 하지 않는다.
- branch reason을 hidden metadata로만 두지 않는다.
