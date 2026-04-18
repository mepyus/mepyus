# natural live compare panel observation v1

## 1. verdict

이번 observation 기준에서도
`compare candidate panel v1`은 **guarded extension 유지**가 맞다.

이 패널은 자연 live path에서
selected asset 읽기 보조층으로는 무리 없이 붙지만,
아직 baseline 편입을 선언할 만큼 information density가 충분히 두껍지는 않다.

## 2. observation scope

이번 관찰은 **natural live path only** 기준으로 본다.

대상:

- `/operating-ui-live`
- `/operating-ui-live?asset_id=turboquant_youtube`
- `/operating-ui-live?asset_id=missing_asset`

제외:

- `live_mode=...`
- `compare_mode=...`

즉 validation-only controlled path 결과는
이번 observation judgment에 섞지 않는다.

## 3. reading quality summary

### 3-1. selected asset reading aid로 자연스럽게 붙는가

관찰 결과:
- yes

이유:
- panel placement가 right-column secondary라서
  `Selected Detail Summary` 바로 아래의 보조층으로 읽힌다
- board 전역면이나 recommendation surface처럼 보이지 않는다
- `Activity Panel`과도 역할 충돌이 크지 않다

### 3-2. recommendation 면처럼 보이지 않는가

관찰 결과:
- 현재 natural live path에서는 과하게 recommendation surface처럼 보이지 않는다

이유:
- count + asset id/title + reason만 보여준다
- score/rank/priority 문구가 없다
- action/click workflow가 없다
- helper 문구도 조용한 수준이다

다만:
- `compare candidates`라는 제목 자체는
  future 확장에서 쉽게 recommendation 쪽으로 읽힐 수 있는 여지는 남아 있다
- 그래서 여전히 guarded extension 유지가 보수적으로 맞다

### 3-3. detail/activity와 책임 충돌 없이 붙는가

관찰 결과:
- 현재 수준에서는 큰 충돌은 없다

정리:
- detail summary는 selected asset 자체 상태를 읽는다
- compare panel은 selected asset 주변의 compare candidate만 보조적으로 읽는다
- activity panel은 lineage/history hint를 읽는다

즉 natural live path 기준에서는
각 panel의 reading role이 아직 분리되어 있다.

## 4. information thinness summary

### 4-1. existing compareCandidates만으로 first pass 의미가 유지되는가

관찰 결과:
- 최소 의미는 유지된다

이유:
- `assetId`와 `reason`만으로도
  “selected asset 주변에 어떤 compare candidate가 붙는지” 정도는 읽을 수 있다

### 4-2. 어디서 얇게 느껴지는가

얇게 느껴지는 지점:

- title richness가 낮다
  - 실제로는 `assetId` fallback에 많이 기대게 된다
- candidate count가 있어도 정보 밀도를 크게 올리지는 않는다
- reason이 짧을 때는 “왜 이 candidate가 붙는지”가 보조 힌트 수준에 머문다

중요:
- 이 observation은 즉시 확장 제안으로 이어지지 않는다
- 여기서는 단지 **first pass 의미는 유지되지만 정보는 아직 얇다**는 정도로만 남긴다

## 5. fallback and live behavior observation

### invalid query natural path

경로:
- `/operating-ui-live?asset_id=missing_asset`

관찰:
- compare panel은 `fallback-selected asset` 기준으로 자연스럽게 따라온다
- query 오류 설명은 control bar가 맡고
- compare panel은 그 오류를 다시 설명하려 들지 않는다

의미:
- compare panel이 query semantics surface로 번지지 않았다는 점은 긍정적이다

### normal live path

관찰:
- compare panel은 loaded 상태에서만 조용히 붙고,
  normal live 상황에서 과한 explanation surface로 커지지 않는다

한계:
- 이번 natural observation 범위에서는
  empty compareCandidates가 직접 자연 발생하는 runtime asset를 보지 못했다

## 6. judgment note

이번 natural observation만 놓고 봐도
판정은 그대로다:

- **guarded extension 유지가 여전히 맞다**

이유:
- panel은 자연스럽게 붙는다
- semantics contamination은 아직 크지 않다
- 하지만 information thinness가 남아 있고,
  natural live usage 기준으로 더 다양한 상태가 쌓인 것은 아니다

즉:
- “위험해서 빼야 한다”는 쪽은 아니고
- “이제 baseline으로 올려도 된다”까지는 아직 아니다

baseline promotion 재검토까지 남은 거리:
- 크지는 않지만 아직 한 단계 남아 있다
- 특히 natural live usage observation이 한 번 더 누적되는 편이 더 적절하다

## 7. next small recommendation

다음 작은 작업 추천:
- **natural live compare panel observation v2를 다른 selected asset cohort에서 1회 더 누적**

이유:
- 기능 확장보다
  자연 live usage에서 compare panel이 계속 recommendation 면으로 비대해지지 않는지
  observation memory를 한 번 더 쌓는 편이 promotion judgment 후속으로 더 맞다

## 8. concise summary

한 줄로:
- 자연 live path 기준에서도 compare panel v1은 **selected asset reading aid로는 잘 붙지만, 아직 baseline 승격보다 guarded extension 유지가 더 안전한 얇은 보조층**이다.
