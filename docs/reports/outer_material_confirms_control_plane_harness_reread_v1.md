# outer material confirms control plane harness reread v1

## 1. 목적

이 문서는 새 candidate를 만들기 위한 문서가 아니다.

목적은 외부 자료가 내 공간의 내부 구조를 단순 참고가 아니라 재확인해 주는 상태를 짧게 기록하는 것이다.

즉 바깥 자료가 `manifest / objective / verifier / evaluator / harness / loop`가 왜 중요한지 다시 보여주고,
내부의 제어면 / 하네스 / 재독해층이 같은 방향을 가리킨다는 점을 남긴다.

## 2. 현재 읽기

이제 공간은 세 층으로 읽힌다.

### 2.1 원칙층

- 먼저 의지와 기준을 적는다.
- verifier를 세운다.
- drift를 본다.
- plan / manifest / evaluation / semi-formal / controllability가 여기에 해당한다.

### 2.2 구현층

- 그 원칙을 실제 장치로 내린다.
- control plane
- preflight
- breadcrumbs
- candidate summary
- watch rule

### 2.3 재독해층

- 새 자료가 들어오면 candidate를 먼저 만들지 않는다.
- 어떤 latent line이 더 짙어졌는지 먼저 본다.
- `latent_line_watchpoints_v1`가 바로 이 층이다.

## 3. 외부 자료가 다시 확인해주는 것

- 검증 가능한 영역은 자동화가 강하다.
- 검증이 어려운 영역은 drift가 난다.
- 그래서 먼저 정렬과 제어 가능성을 세워야 한다.
- 모델보다 하네스가 본체다.
- 작업은 command / skill / trigger / manifest / evaluator로 흡수될 수 있다.

즉 외부 자료는 내 공간의 제어면과 하네스가 과장이 아니라 구조적으로 타당하다는 점을 다시 보여준다.

## 4. 지금 상태

- raw를 덮어쓰지 않고 다시 돌아갈 수 있게 하는 감각이 살아 있다.
- breadcrumbs와 observation registry가 실제로 작동한다.
- latent line registry가 candidate보다 먼저 관찰 단위를 세운다.
- 새 observation을 받을 때는 후보 이전에 latent line을 먼저 태깅하는 것이 맞다.

## 5. 다음 최소 단계

앞으로 새 observation이 들어오면 먼저 묻는다.

- 이 관찰은 `pre_read_eye`를 더 짙게 하는가
- 이 관찰은 `raw_return_preservation`을 더 짙게 하는가
- 이 관찰은 `transition_over_surface`를 더 짙게 하는가
- 이 관찰은 `input_to_reading_organ`을 더 짙게 하는가

그 다음에야 candidate 여부를 본다.

## 6. 한 줄 결론

> 바깥 자료와 안쪽 장치가 같은 방향을 가리키기 시작했으므로, 앞으로는 새 흔적을 받을 때마다 후보보다 먼저 latent line이 무엇인지부터 본다.

