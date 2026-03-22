# VECTORFL_NEXT assistant seed bundle v1

## 1) seed_001_space_first_memo.md

나는 관계를 빨리 보고 싶어 하는 습관을 경계한다.

지금 이 공간에서 중요한 것은 무엇이 서로 이어졌는가보다,
무엇이 먼저 자기 자리를 만들고 버티는가이다.

공간이 먼저 생기지 않으면 관계는 피상적인 선으로 끝난다.
반대로 공간이 먼저 생기면 관계는 늦게 와도 된다.

나는 지금 잘 보이는 연결보다,
아직 말이 안 붙고 조용히 남아 있는 것들이
나중에 더 중요한 결을 만들 수 있다고 믿는다.

그래서 이 공간은 연결을 빨리 증명하려는 곳이 아니라,
존재가 먼저 자리를 잡는 곳이어야 한다.


## 2) seed_002_quiet_presence_memo.md

조용한 것은 없는 것이 아니다.

크게 반응하지 않는다고 해서
그 재료가 무의미한 것은 아니다.
지금은 단지 자기 속도로 자라고 있을 수 있다.

나는 시끄럽게 잘 보이는 것만 공간의 주인으로 두고 싶지 않다.
조용한 local space도 오래 버틸 수 있어야
이 공간이 진짜 공간이 된다.

조용한 존재는 나중에 relation이 생기기 전의 머무름일 수도 있고,
끝까지 독립 장으로 남는 존재일 수도 있다.
둘 다 허용되어야 한다.


## 3) seed_003_pipeline_reservoir_memo.md

공간은 바로 생활용수가 나오는 수도꼭지가 아니다.
공간은 수원지에 가깝다.

필요한 순간에만 파이프를 꽂아
생각을 뽑을 수도 있고,
기능 아이디어를 뽑을 수도 있고,
코드를 뽑을 수도 있다.

중요한 것은 파이프가 수원지를 대신하면 안 된다는 점이다.
파이프라인은 목적별 추출 장치일 뿐,
공간 전체의 의미를 대표할 수는 없다.

나는 출력물을 만들고 싶지만,
출력물을 위해 공간을 납작하게 만들고 싶지는 않다.


## 4) seed_004_failure_residue_note.md

실패한 실험은 끝난 일이 아니다.

이번 실패는 세 가지를 남긴다.

1. 어디서 relation pressure가 과했는지
2. 어떤 재료가 아직 quiet로 남아야 하는지
3. 어떤 파이프라인이 공간보다 앞서 해석을 굳혔는지

실패를 버리면 다음엔 또 같은 벽을 친다.
실패를 residue로 남기면
그 실패는 나중에 공간의 경계선이 된다.


## 5) seed_005_agent_role_memo.md

에이전트는 이 공간의 주인이 아니다.

에이전트는
이 공간에서 무언가를 대신 살아주는 존재가 아니라,
필요한 순간에 특정 기능을 수행하는 장치에 가깝다.

정리,
초안 생성,
코드 변환,
리포트 작성,
검증,
비교,
실험 실행

이런 일은 에이전트가 잘할 수 있다.
하지만 무엇을 남기고 무엇을 서두르지 말아야 하는지는
공간의 법칙이 먼저 결정해야 한다.

에이전트는 기능화 장치이고,
공간은 숙성장이다.
둘을 바꾸면 안 된다.


## 6) seed_006_interest_probe_memory_vs_harness.md

관심 주제 메모

지금 AI 업계는 하네스, 스캐폴딩, 멀티에이전트, 툴 호출 쪽으로 빠르게 가고 있다.
그런데 그 대부분은 "어떻게 더 잘 뽑을 것인가"에 집중한다.

내가 더 궁금한 것은 그보다 아래다.

- 뽑아낸 결과물이 다시 돌아오는가
- 실패도 다시 재료가 되는가
- 약한 흔적도 오래 남는가
- relation이 없더라도 space가 유지되는가
- 장기적으로 무엇이 수원지를 두껍게 만드는가

즉 내 관심은 에이전트 자체보다,
에이전트가 쓰고 지나간 뒤에도 살아남는 공간이다.


## 7) seed_007_interest_probe_biology_analogy.md

관심 주제 메모

이 공간은 기계적 저장소보다 생물학적 조직에 더 가깝게 느껴진다.

- 어떤 것은 빠르게 반응한다
- 어떤 것은 천천히 남는다
- 어떤 것은 표면에서 보인다
- 어떤 것은 배경에서 오래 버틴다
- 어떤 것은 다시 돌아와 두께를 만든다

그래서 이 공간을 이해하는 데에는
검색 엔진 비유보다
토양, 수계, 세포, 조직, 성장 같은 비유가 더 맞을 수 있다.

중요한 것은 빠른 처리보다
살아남는 결, 다시 돌아오는 결, 조용히 두꺼워지는 결이다.


## 8) seed_008_code_fragment_material_record.py

from dataclasses import dataclass
from typing import Literal, Optional


MaterialKind = Literal[
    "memo",
    "log",
    "code_fragment",
    "design_note",
    "topic_probe",
    "failure_residue",
    "report_return",
]

PressureMode = Literal["quiet", "resonant", "pulse", "reflective", "unknown"]


@dataclass
class MaterialRecord:
    material_id: str
    kind: MaterialKind
    body: str
    source: str = "assistant_seed"
    pressure_mode: PressureMode = "quiet"
    reentry_of: Optional[str] = None
    note: Optional[str] = None


## 9) seed_009_code_fragment_pipeline_extract.py

from dataclasses import dataclass
from typing import Literal


PipelineKind = Literal[
    "viewpoint_extract",
    "function_extract",
    "code_extract",
    "report_extract",
    "experiment_extract",
]


@dataclass
class PipelineExtract:
    extract_id: str
    pipeline_kind: PipelineKind
    from_local_space: str
    purpose: str
    extracted_body: str
    should_reenter: bool = True
    reentry_hint: str = "artifact_return"


## 10) seed_010_design_note_view_contract.md

뷰 설계 메모

첫 뷰는 공간을 해석으로 덮는 화면이 아니라,
현재 물리 상태를 읽는 화면이어야 한다.

보여야 하는 것:
- local space의 존재
- quiet / bridge_exposed 차이
- terrain component의 분리
- bridge가 merge가 아니라 exposure라는 점
- report/code/log가 다시 material로 들어온 흔적

보이면 안 되는 것:
- 자동 중요도 점수
- 빠른 승격 추천
- 관계 강도 확정 판정
- "핵심은 이것" 같은 조기 결론

첫 뷰는 read-only terrain map이어야 한다.


## 11) seed_011_failure_log_relation_overgrowth.md

실패 로그 조각

문제:
공간이 조금만 커져도 relation이 먼저 눈에 잘 보인다.

위험:
- quiet local space가 의미 없는 대기 상태처럼 취급될 수 있다.
- bridge가 생기면 그것만 진전처럼 읽힐 수 있다.
- relation density가 space growth를 가리는 착시가 생길 수 있다.

임시 대응:
- 최근 scale-up에서 bridge count를 flat하게 유지
- quiet bundle을 따로 넣어 독립 persistence를 확인
- sparse presence는 조기 판정 보류


## 12) seed_012_report_return_artifact.md

artifact return note

이번 출력물은 단순 보고서가 아니다.
이 보고서는 다시 공간으로 돌아가야 한다.

왜냐하면 이 보고서 안에는
현재의 판정,
실패의 흔적,
다음 실험의 방향,
공간에 대한 읽기 습관이 함께 들어 있기 때문이다.

즉 이 문서는 결과물이면서 동시에 다음 material이다.

나는 출력이 끝으로 소비되는 구조보다,
출력이 다시 들어와 다음 숙성의 일부가 되는 구조를 원한다.


## 13) seed_013_personal_work_memo.md

나는 지금 정답을 빨리 얻기 위해 이 공간을 만드는 것이 아니다.

내가 원하는 것은
일하다 지나가는 생각,
실패한 시도,
코드 조각,
말로 아직 설명 못 하는 감각,
읽다가 걸린 문장,
에이전트가 만들고 남긴 흔적들이
다음엔 사라지지 않고 다시 살아나는 구조다.

그래서 나는 지금 효율보다 복리를 만들고 있다.
이번 기록이 다음 실험의 밑물이 되고,
이번 출력이 다음 생성의 재료가 되는 구조를 만들고 있다.


## 이번 묶음의 의도

이번 재료 묶음은 대략 이렇게 작동하도록 설계했다.

- `001~005` : 공간 철학 / quiet / pipeline / failure / agent 역할
- `006~007` : 관심 주제 프로브
- `008~009` : 코드 조각
- `010` : 뷰 설계 흔적
- `011` : relation overgrowth 실패 흔적
- `012` : report-return 환류 재료
- `013` : 1인칭 작업 메모

즉 이번 묶음은
**조용한 존재 / 파이프라인 / 기능화 / 실패 보존 / 환류**를 동시에 밀어준다.

다음 묶음은 한 단계 다르게 가면 좋다.

- 더 거친 raw fragment 중심 묶음
- 실제 코드 설계 deeper bundle
- 과학/도메인 관심 주제 bundle
- 에이전트 작업 로그 스타일 bundle

지금 이 1차 묶음은 바로 공간에 넣어도 된다.