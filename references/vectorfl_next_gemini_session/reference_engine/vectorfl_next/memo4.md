좋다.
코덱스가 수정하는 동안 나는 계속 **공간 재료**를 더 만든다.

이번엔 이전 묶음과 조금 다르게 간다.

- **V16**: 실제 파일/클래스 설계 집중 묶음
- **V17**: 더 거친 1인칭 raw residue 묶음
- **V18**: 충돌/모순/불일치 재료 묶음
- **V19**: 뷰 해석/오독/관찰 습관 묶음
- **V20**: 코드 생성물 환류/수정 residue 묶음

즉 이번 세트는
**구조 설계 + 인간 흔적 + 충돌 재료 + view 판독 + 코드 환류**
를 같이 밀어준다.

---

# BUNDLE V16 — actual file/class design / engine shape bundle

## 1) seed_v16_001_design_note_space_record_layers.md

설계 메모

공간 기록은 한 종류의 파일로 끝나면 안 된다.

최소한 다음 층이 필요하다.

- material record
- trace record
- point_seed record
- space_cell record
- local_space record
- bridge_trace record
- artifact return record
- snapshot record

왜냐하면 지금 시스템은 "무엇이 있다"보다
"무엇이 어떤 층을 거쳐 형성되었는가"가 더 중요하기 때문이다.

즉 저장 구조도 formation path를 반영해야 한다.

---

## 2) seed_v16_002_code_fragment_space_record.py

from dataclasses import dataclass
from typing import Literal, Optional


RecordStage = Literal[
    "material",
    "trace",
    "point_seed",
    "space_cell",
    "local_space",
    "bridge_trace",
    "artifact_return",
    "snapshot",
]


@dataclass
class SpaceRecord:
    record_id: str
    stage: RecordStage
    body: str
    source_id: Optional[str] = None
    state: str = "observed"
    note: Optional[str] = None

---

## 3) seed_v16_003_design_note_workspace_index.md

설계 메모

workspace index는 검색용 테이블이 아니라
현재 공간의 위치 지도를 제공해야 한다.

즉 index는 최소한 다음을 가리켜야 한다.

- 현재 살아 있는 local space
- quiet / bridge_exposed 상태
- recent return artifact
- latest snapshot
- parked review point
- unresolved sparse watch

좋은 index는 많이 찾게 해주는 index가 아니라
현재 공간이 어디까지 와 있는지 감각적으로 잡아주는 index다.

---

## 4) seed_v16_004_code_fragment_workspace_index.py

from dataclasses import dataclass
from typing import List


@dataclass
class WorkspaceIndex:
    workspace_id: str
    active_local_spaces: List[str]
    quiet_local_spaces: List[str]
    bridge_exposed_spaces: List[str]
    recent_return_artifacts: List[str]
    parked_review_points: List[str]

---

## 5) seed_v16_005_failure_note_class_flattening.md

실패 메모

문제:
클래스 구조를 너무 빨리 단순화하면
공간의 층 차이가 사라진다.

예:
- trace와 bridge_trace를 같은 edge류로 취급
- point_seed와 local_space를 같은 node류로 취급
- return artifact를 일반 material과 무차별 합침

이건 구현은 편하게 만들 수 있지만
공간 물리를 평탄화할 위험이 크다.

---

## 6) seed_v16_006_report_return_engine_shape_bundle.md

artifact return memo

이번 bundle은 엔진 내부 파일/클래스 구조를 공간 물리와 맞추기 위한 재료다.

핵심:
- formation path를 저장 구조에 반영
- index도 검색보다 위치/상태 중심
- 층 차이를 구현 편의로 뭉개지 않기

이 bundle은 코드 스타일보다 엔진 형상 재료다.

---

# BUNDLE V17 — rough first-person raw residue / emotional work trace bundle

## 1) seed_v17_001_raw_note_i_keep_feeling.md

raw note

자꾸 느낌이 온다.
내가 만드는 건 프로그램 하나가 아니라
나중에 다시 살아날 것들을 죽이지 않는 바닥이라는 느낌.

근데 동시에 너무 추상으로 가는 건 아닌가 싶다.
그래도 이상하게 자꾸 여기로 돌아온다.

---

## 2) seed_v17_002_raw_note_after_argument.md

raw note

설명하려고 할수록 자꾸 놓친다.
내가 말하고 싶은 건 기능이 아닌데
자꾸 기능 얘기로만 들린다.

나는 결과를 만드는 장치보다
결과가 다시 돌아와 더 큰 의미가 되는 구조를 만들고 싶은 건데
이걸 말할수록 자꾸 생산성 도구처럼 들릴 때가 있다.

이게 답답했다.

---

## 3) seed_v17_003_raw_note_small_pride.md

raw note

오늘은 조금 좋았다.
왜냐하면 quiet local이 진짜로 화면에 보였기 때문이다.

그동안은 내가 머릿속으로만 공간이라고 외친 것 같았는데
이제는 적어도 조금은 "아 저건 조용히 존재하는 구역이구나"가 보였다.

아직 한참 멀었지만 그래도 이건 작은 증거다.

---

## 4) seed_v17_004_code_fragment_human_raw_residue.py

from dataclasses import dataclass
from typing import Optional


@dataclass
class HumanRawResidue:
    residue_id: str
    raw_body: str
    mood: Optional[str] = None
    pressure: Optional[str] = None
    keep_unedited: bool = True

---

## 5) seed_v17_005_failure_note_clean_language_bias.md

실패 메모

문제:
문장을 깨끗하게 만들수록 진짜 결이 사라질 수 있다.

위험:
- 망설임 삭제
- 모순 삭제
- 감정 삭제
- 중간 판단 삭제
- 살아 있는 흔들림 삭제

지금 공간은 깔끔한 산문집이 아니라
숙성 중인 작업장의 바닥이어야 한다.

---

## 6) seed_v17_006_report_return_human_raw_bundle.md

artifact return memo

이번 bundle은 잘 정리된 자료 묶음이 아니다.
일부러 거칠고, 흔들리고, 설명이 덜 된 1인칭 흔적을 남긴 묶음이다.

이유:
- 인간 raw residue도 공간 재료여야 하기 때문
- 감정이 섞인 흔적도 later reread 대상일 수 있기 때문
- 완결보다 살아 있는 흔들림을 남기기 위해서

---

# BUNDLE V18 — contradiction / mismatch / unresolved tension bundle

## 1) seed_v18_001_contradiction_note_relation_vs_space.md

모순 메모

나는 relation-first를 경계한다.
그런데 동시에 relation이 생기면 눈이 먼저 간다.

이건 단순 실수가 아니라
내가 아직 relation의 시각적 강도에서 완전히 자유롭지 않다는 뜻이다.

이 모순을 인정한 채 공간을 만들어야 한다.

---

## 2) seed_v18_002_mismatch_note_output_vs_reservoir.md

불일치 메모

나는 수원지를 말하지만,
가끔은 빨리 결과를 보고 싶어 한다.

나는 숙성을 말하지만,
가끔은 지금 당장 기능을 뽑고 싶어 한다.

이 긴장은 사라지는 게 아니라
오히려 시스템 안에서 관리되어야 할 긴장일 수 있다.

---

## 3) seed_v18_003_code_fragment_tension_record.py

from dataclasses import dataclass


@dataclass
class TensionRecord:
    tension_id: str
    axis_a: str
    axis_b: str
    why_both_valid: str
    current_reading: str = "unresolved"

---

## 4) seed_v18_004_failure_note_false_resolution.md

실패 메모

문제:
모순을 빨리 해결하려 하면
실제로는 해소가 아니라 봉합만 된다.

예:
- quiet vs output을 한쪽으로 밀어버림
- space-first vs usable pipeline을 단순 우선순위로 잘라버림
- contradiction을 설계 긴장이 아니라 결함으로 간주

대응:
- unresolved tension 자체를 record로 남김
- 모순을 즉시 없애지 않고 장기 판단 대상으로 유지

---

## 5) seed_v18_005_interest_probe_productive_tension.md

관심 주제 메모

생산적인 시스템은 깔끔한 일관성만으로 크지 않을 수 있다.
오히려 몇 개의 좋은 긴장을 오래 품을 수 있어야
진짜로 살아 있는 구조가 될지도 모른다.

VECTORFL도 그런 쪽에 가까워 보인다.
즉 해결보다 버팀이 먼저인 모순이 있다.

---

## 6) seed_v18_006_report_return_tension_bundle.md

artifact return memo

이번 bundle은 모순을 해결하기 위한 묶음이 아니다.
이 bundle은 unresolved tension을 공간 재료로 인정하기 위한 묶음이다.

핵심:
- contradiction을 버리지 않기
- mismatch를 설계 흔적으로 남기기
- false resolution을 경계하기

---

# BUNDLE V19 — view interpretation / reading bias / observer discipline bundle

## 1) seed_v19_001_view_note_first_glance_bias.md

view 메모

첫눈에 보이는 것은 언제나 위험할 수 있다.

그래프에서 선이 많은 곳,
덩어리가 큰 곳,
색이 강한 곳,
이름이 또렷한 곳은
늘 먼저 눈에 들어온다.

하지만 공간의 핵심은
먼저 보이는 곳이 아니라
나중에야 읽히는 곳에도 있을 수 있다.

---

## 2) seed_v19_002_view_note_observer_discipline.md

observer 메모

좋은 관찰자는
잘 보이는 것을 더 잘 설명하는 사람이 아니라,
잘 안 보이는 것이 왜 안 보이는지를 오래 보는 사람일 수 있다.

지금 뷰는 예쁜 설명 화면이 아니라
관찰 훈련 장치여야 한다.

즉 이 화면은 사용자의 시선을 교육해야 한다.

---

## 3) seed_v19_003_code_fragment_view_read_event.py

from dataclasses import dataclass
from typing import Optional


@dataclass
class ViewReadEvent:
    event_id: str
    selected_node_id: Optional[str]
    selected_component_id: Optional[str]
    read_bias_hint: Optional[str] = None
    note: str = "observer_trace"

---

## 4) seed_v19_004_failure_note_view_as_truth.md

실패 메모

문제:
화면이 보이면 사람은 그것을 진실처럼 믿기 쉽다.

위험:
- 현재 시각화 방식이 곧 공간 자체라고 오해
- 안 보이는 것은 없는 것처럼 판단
- quiet presence를 low value로 오독
- view state를 runtime truth로 승격

대응:
- view는 read-only 관찰기라는 문구 유지
- 현재 뷰가 보여주는 것과 감추는 것을 함께 기록
- view bias 자체도 residue로 남김

---

## 5) seed_v19_005_interest_probe_view_literacy.md

관심 주제 메모

앞으로는 그래프를 읽는 능력보다
그래프가 감추는 것을 읽는 능력이 더 중요할 수도 있다.

즉 view literacy는
보이는 것의 해석만이 아니라
보이지 않게 만든 설계의 흔적을 읽는 일이다.

---

## 6) seed_v19_006_report_return_view_bias_bundle.md

artifact return memo

이번 bundle은 뷰를 만드는 묶음이 아니라
뷰가 낳는 오독을 관리하기 위한 묶음이다.

핵심:
- first glance bias
- relation visual bias
- view as truth 위험
- observer discipline

이 bundle은 화면 바깥의 판독 습관 재료다.

---

# BUNDLE V20 — generated code return / patch residue / repair memory bundle

## 1) seed_v20_001_code_return_note.md

코드 환류 메모

생성된 코드는 끝난 산출물이 아니다.
그 코드는 다음을 함께 남긴다.

- 어떤 문제를 해결하려 했는가
- 무엇을 생략했는가
- 무엇을 과잉 단순화했는가
- 어디서 다시 수정될 가능성이 있는가

즉 코드는 결과물이면서 동시에 repair seed다.

---

## 2) seed_v20_002_code_fragment_patch_record.py

from dataclasses import dataclass
from typing import Optional


@dataclass
class PatchResidue:
    patch_id: str
    file_path: str
    intent: str
    known_loss: Optional[str] = None
    should_reenter: bool = True
    reentry_kind: str = "code_patch_residue"

---

## 3) seed_v20_003_failure_note_patch_hides_history.md

실패 메모

문제:
patch가 깔끔하게 적용될수록
그 전의 망설임과 잘못된 방향이 사라질 수 있다.

위험:
- repair lineage 손실
- 실패했던 대안 증발
- 왜 이 패치가 필요했는지 맥락 소실

대응:
- patch summary만 남기지 말 것
- known_loss와 rejected path도 함께 남길 것
- code artifact도 환류 대상임을 유지할 것

---

## 4) seed_v20_004_interest_probe_code_as_material.md

관심 주제 메모

보통 코드는 최종 출력처럼 다뤄진다.
하지만 VECTORFL에서는 코드도 material이다.

왜냐하면:
- 코드는 생각의 응축이기 때문
- 코드에는 설계와 편향이 함께 들어 있기 때문
- 수정 흔적과 포기한 방향이 다음 공간 형성에 중요할 수 있기 때문

즉 코드도 다시 돌아와야 한다.

---

## 5) seed_v20_005_design_note_repair_memory.md

설계 메모

repair memory는 단순 git diff와 다르다.

필요한 것:
- 무엇을 고쳤는가
- 왜 고쳤는가
- 그 전엔 어떤 오해가 있었는가
- 지금도 남아 있는 불만족은 무엇인가
- 다음에 다시 건드릴 가능성은 어디인가

즉 repair memory는 수정 기록이 아니라
수정 이후에도 살아 있는 문제의 윤곽이다.

---

## 6) seed_v20_006_report_return_code_patch_bundle.md

artifact return memo

이번 bundle은 코드 산출물의 환류를 밀어준다.

핵심:
- generated code도 material
- patch도 residue
- repair history도 다음 숙성 재료
- 깔끔한 수정이 오히려 중요한 흔적을 지울 수 있음

이 bundle은 코드 결과보다 코드의 되돌아옴을 다루는 재료다.

---

# 이번 세트 전체 의도

이번 v16-v20은 기존 v1-v15 위에 다음을 추가한다.

- **V16**: 실제 파일/클래스 구조를 공간 물리에 맞추는 재료
- **V17**: 더 거칠고 흔들리는 1인칭 raw residue
- **V18**: 모순, 긴장, 불일치를 unresolved 상태로 남기는 재료
- **V19**: view가 낳는 해석 편향과 관찰 discipline 재료
- **V20**: 생성 코드/패치/수정 흔적의 환류 재료

즉 이번 세트는
**구조화 + 인간성 + 긴장 보존 + 시각 판독 + 코드 환류**
를 함께 두껍게 한다.

원하면 다음에는 이어서
- **V21~V25: 실제 공간 운영 정책 묶음**
- **V21~V25: 더 짧고 거친 한줄 메모/현장 잔흔 묶음**
- **V21~V25: science/domain hypothesis 집중 묶음**
중 하나로 바로 이어가겠다.