# engine_memory_spine_and_context_externalization_v1_report.md

## 1. why this was needed

지금 엔진은 이미 충분히 커졌다.

- 철학 방향성 문서
- process console core/derived/surface 구조
- run report/receipt/delta log
- Gemini 위임 경계
- cohort/live-run memory

이 상태에서는 “그냥 기억하겠다”로는 부족하다.
기억해야 할 내용이 많아질수록,
무엇을 어디에 기록해야 하는지부터 고정해야 한다.

## 2. adopted method

이번에 채택한 방법은 단순 메모 추가가 아니라
**memory spine + context recovery order**다.

핵심은 다음 다섯 층을 분리하는 것이다.

- philosophical directionality memory
- operator problem-recognition memory
- resource capability boundary memory
- episodic operation memory
- current reality memory

## 3. practical meaning

이 구조가 생기면:

- 철학적 기준은 `docs/specs`에 남고
- 사용자의 문제 인식 방식은 `runtime/memory/problem_recognition`에 남고
- 외부 자원 위임 경계는 `gemini/`에 남고
- 각 run의 결과는 `docs/reports + runtime/receipts + delta log`에 남고
- 현재 읽기 순서는 `runtime/views`가 담당한다

즉 기억을 기능별이 아니라 **운용 층위별로 외부화**하게 된다.

## 4. most important adoption point

이번에 가장 중요한 반영은 이것이다.

- 사용자의 문제 인식 방식 자체를 별도 memory layer로 다룬다

이전에는 철학 방향성 문서만 있었지만,
이제는 사용자가 문제를 어떻게 보고 어떤 간극을 중요하게 여기는지를
runtime memory로 별도 보존한다.

## 5. final read

이 구조는 단순 기록 정리가 아니다.
이건 유한한 메모리 안에서도
엔진이 철학, 문제 인식, 위임 경계, run 결과를 섞지 않고
다시 복구할 수 있게 만드는 복원 구조다.
