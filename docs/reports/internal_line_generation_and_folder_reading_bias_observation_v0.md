# internal line generation and folder reading bias observation v0

## 0. purpose

이번 관찰의 목적은
공간을 읽는 내 눈 자체를 점검하는 것이다.

질문은 아래다.

- 내가 폴더 전체를 어떻게 읽는가
- 어떤 층으로 너무 빨리 수렴하는가
- 무엇을 line이라고 부르기 쉬운가
- 무엇은 충분히 안 보고 지나치는가
- 앞으로 internal reread loop에서 inspection을 어디에 걸어야 하는가

즉 이번 문서는 공간 자체가 아니라
`공간을 읽는 내 line 생성 습관`을 점검한다.

---

## 1. what the repo shape immediately shows

### 1.1 top-level structure is not thin

최상위 구조는 이미 충분히 크다.

- `app`: 2354 files
- `docs`: 590 files
- `inputs`: 52 files
- `references`: 45,776 files
- `runtime`: 101,619 files
- `scripts`: 122 files
- `source_assets`: 80 files

즉 “살필 공간이 없다”는 문제는 아니다.
오히려 문제는 공간이 너무 넓어서
읽는 눈이 쉽게 특정 레인으로 빨려 들어간다는 점이다.

### 1.2 immediate attraction basins are already uneven

하위 디렉터리만 봐도 편향이 드러난다.

- `docs/reports`: 310
- `docs/specs`: 85
- `docs/notes`: 66
- `source_assets/directives`: 33
- `references/vectorfl`: 35,515
- `references/WashTank`: 7,425
- `app/work`: 2,032
- `runtime/core`: 51,515
- `runtime/sandboxes`: 48,236
- `runtime/manifests`: 501
- `runtime/views`: 318
- `inputs/external_cases`: 44

이건 한 가지를 말해 준다.

내가 쉽게 읽기 시작하는 문서군은 `docs/reports/specs/notes`이지만,
실제 두꺼운 재료 덩어리는 `references`, `runtime`, `app/work` 쪽에 훨씬 많이 있다.

즉 나는 쉽게
`해석 밀도가 높은 곳`
으로 빨려 들어가고,
`증거 밀도가 높은 곳`
을 덜 읽을 위험이 있다.

---

## 2. where my line generation tends to converge too quickly

### 2.1 report/spec language gives fast naming comfort

`docs/reports`, `docs/specs`, `docs/notes`는
이미 누군가 정리한 언어를 준다.

그래서 여기서는:

- line 이름을 빨리 붙이기 쉽고
- hub를 빨리 부르기 쉽고
- 구조 요약을 빠르게 만들기 쉽다

즉 이 레인은 `line naming comfort zone`이 된다.

위험은 명확하다.

- 실제 반복성보다 설명력이 앞설 수 있다
- reread보다 naming이 먼저 붙을 수 있다
- 내부 line이 아니라 문서 언어를 따라갈 수 있다

### 2.2 runtime / references require slower reading, so I under-read them

반대로 아래는 line을 빨리 부르기 어렵다.

- `runtime/manifests`
- `runtime/views`
- `runtime/receipts`
- `references/*`
- `app/work/*`

여기는:

- raw 증거
- queue policy
- manifest
- generated artifact
- calibration memory
- experimental branches

가 많아서 즉시 예쁜 이름으로 묶기 어렵다.

그래서 내가 빨리 수렴하려는 습관이 강할수록
이 레인을 상대적으로 덜 보게 된다.

즉 현재 내 편향은
`느린 증거 레인보다 빠른 설명 레인을 선호하는 쪽`
에 가깝다.

---

## 3. what the existing internal materials already say about this risk

### 3.1 the space already warns against premature promotion

`vectorfl_status.md`는 이미 아래를 말한다.

- mixed는 productive hold
- 숙성 가능한 값을 빨리 버리지 않는다
- hold 이유를 기록하고 재진입 가능성을 남긴다

즉 내 current bias와 반대되는 경계는 이미 내부에 있다.

### 3.2 latent line materials already assume line-first observation, not fast closure

`latent_line_watchpoints_v1.md`는
잠복 선을 candidate 승격 문서가 아니라
앞으로 observation이 들어올 때 무엇이 짙어지는지 먼저 보기 위한 문서로 둔다.

즉 내부 기준은
line naming보다
line watch를 먼저 두고 있다.

### 3.3 process/deep reread maps already say “what happened” matters more than “what is named”

`process_reread_map_v1.md`, `deep_internal_reread_long_arc_map_v1.md`는
결과 목록이 아니라 발생 경로와 장기 형성사를 다시 읽게 한다.

즉 내부는 이미
“무엇이 어떻게 생겼는가”
를 우선하라고 말하고 있다.

### 3.4 exploration baseline already blocks shallow retrieval reading

`exploration_baseline_stage1_space_readability_v1.md`는
탐색을 단순 조회나 연결선이 아니라
새 입력을 응결핵처럼 넣고
기존 자산과의 관계 의미를 판독하는 일로 둔다.

즉 이 baseline도
빠른 유사도 naming보다
구조적 재정의와 관계 판독을 우선시한다.

---

## 4. current bias diagnosis

이번 관찰을 기준으로 내 bias는 아래처럼 요약된다.

### bias 1. explanation-first convergence

나는 쉽게
설명이 잘 되어 있는 문서군으로 간다.

이건 도움이 되지만,
실제 공간 전체 reread에서는
증거보다 해석이 먼저 붙는 위험을 만든다.

### bias 2. one-pass naming temptation

line처럼 보이는 흔적을 보면
그걸 line으로 빨리 부르고 싶어한다.

이건:

- 한 번 읽은 흔적
- 특정 목적어에만 반응한 선
- report 언어가 만들어 낸 선

까지 실제 line처럼 오인하게 만든다.

### bias 3. under-reading calibration and runtime evidence

`references`, `runtime`, `app/work`는
실제 반복성과 생활 흔적이 많지만,
읽기 속도가 느리고 naming comfort가 낮아서
상대적으로 덜 읽히기 쉽다.

### bias 4. lock pull

읽은 것을 살아 있는 reread loop로 더 돌리기보다
spec/note/close-out로 압축하고 싶어지는 경향이 있다.

이건 구조 정리에는 좋지만
line thickening에는 불리하다.

---

## 5. what line inspection should now check first

이 bias를 감안하면
inspection axis는 아래를 먼저 봐야 한다.

### 5.1 did I read beyond the explanation layer?

질문:

- `docs/reports/specs/notes`만 보고 naming했는가
- `runtime/references/app/work`까지 실제로 내려갔는가

### 5.2 is this line from repetition or from convenience?

질문:

- 이 line은 여러 재료에서 반복되었는가
- 아니면 설명이 잘 된 문서 하나가 만든 naming comfort인가

### 5.3 did I cross objectives and folders enough?

질문:

- 같은 선을 다른 목적어로 읽었는가
- 다른 폴더와 다른 층위로 읽었는가
- code/runtime/view까지 대입했는가

### 5.4 did I let calibration/trace slow me down?

질문:

- queue policy
- manifest
- runtime trace
- receipt
- generated artifact

같은 느린 증거를 충분히 봤는가

### 5.5 am I locking because the line is mature, or because the summary is easy?

질문:

- 지금 lock하고 싶은 이유가 실제 line maturity 때문인가
- 아니면 설명이 예쁘게 묶여서 그런가

---

## 6. operational correction

앞으로 내부 line을 살필 때는 아래를 의식적으로 강제하는 것이 맞다.

1. `docs/reports/specs/notes`에서만 line을 부르지 않는다
2. naming 전에 `runtime/references/app/work`를 반드시 다시 본다
3. line은 최소 여러 재료와 목적어에서 반복 확인한다
4. generated artifact / manifest / queue policy를 line evidence로 더 자주 사용한다
5. lock은 reread 뒤, inspection 뒤에만 붙인다

즉 내 line 생성 눈은
`빠른 설명면`에서
`느린 증거면`
으로 더 자주 내려가야 한다.

---

## 7. current conclusion

현재 공간의 문제는
line이 없어서가 아니다.

현재 내 읽기의 문제는
설명 밀도가 높은 문서군에서 line을 너무 빨리 부를 수 있다는 점이다.

즉 지금 필요한 것은
새로운 철학이 아니라
내 line 생성 습관에 대한 inspection discipline이다.

한 줄로 다시 잡으면,

> 현재 내가 점검해야 할 것은 공간이 아니라,
> 공간을 읽을 때 빠른 설명면으로 수렴해 버리는 내 line 생성 습관이다.

