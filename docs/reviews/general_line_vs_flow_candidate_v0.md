# General Line vs Flow Candidate v0

## 목적

이 문서는
현재 VectorFL에서
`general line`
과
`flow candidate`
를 왜 분리해야 하는지
실행 spine 기준으로 실무적으로 정리한다.

## 1. general line

현재 VectorFL의 기본 단위는
family / projection / route 중심의
general line이다.

즉 지금 실제로 작동하는 것은:

- current hint
- reentry prebias
- classifier
- final family / projection / route

를 통해
이번 run을 어떤 해석 경로로 읽을지 정하는 구조다.

이 단위는
한 번의 run을 해석하고 경로를 고르는 데 충분하다.

## 2. flow candidate

flow candidate는
한 번의 run 안의 경로가 아니라,
여러 run 사이에서 반복되는
multi-step transition pattern이다.

예:

- input family -> transition family
- transition family -> transition readout projection -> readonly board
- 같은 residue bias가 반복적으로 같은 next family를 여는 경향

중요한 점은,
이건 현재 line을 대체하는 단위가 아니라
line execution traces를 비교해서 나중에 드러나는
관찰 대상이라는 점이다.

## 3. 왜 지금 flow line으로 승격하면 안 되는가

현재는 run 수가 아직 적고,
반복 패턴도 host/context에 따라 쉽게 흔들릴 수 있다.

그래서 지금 단계에서
`flow_line`
을 first-class object로 잠그면
좋아 보이는 예시 두세 개를
너무 빨리 제도화할 위험이 있다.

즉 지금 필요한 것은
formalization이 아니라
bounded observation loop다.

## 4. 현재 적절한 순서

현재 순서는 아래가 맞다.

1. general line으로 run을 해석한다
2. execution trace를 append-only로 남긴다
3. 여러 trace를 비교해 repeated pattern을 관찰한다
4. 그때만 flow candidate라고 부른다
5. 충분한 반복 증거가 쌓인 뒤에만 future flow line promotion을 검토한다

## 5. future promotion에 필요한 최소 증거

나중에 flow line 승격을 검토하려면
적어도 아래가 필요하다.

- 동일하거나 매우 유사한 multi-step sequence의 반복
- family handoff가 우연이 아니라는 근거
- residue hook이 다음 family bias를 안정적으로 여는 근거
- source surface가 조금 달라도 same-root pattern으로 유지되는 근거
- boundary warning이 줄어드는 근거

## 한 줄 요약

지금은 general line을 유지한 채
반복 run에서 보이는 transition pattern만
flow candidate로 관찰해야 하며,
formal flow line promotion은 그 이후의 gated step이어야 한다.
