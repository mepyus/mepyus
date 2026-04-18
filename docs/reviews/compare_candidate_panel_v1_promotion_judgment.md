# compare candidate panel v1 promotion judgment

## 1. verdict

아직 guarded extension 유지.

현재 compare candidate panel v1은
구현, 상태 커버리지, validation contract, override isolation까지 닫혔지만,
이 시점에서 곧바로 baseline에 편입하기보다는
**guarded extension first-pass**로 계속 유지하는 쪽이 더 안전하다.

## 2. current status summary

현재까지 닫힌 것:

- right-column secondary placement 확정
- read-only comparison aid 역할 확정
- existing `compareCandidates`만 사용하는 first pass 구현 완료
- integrated state coverage 완료
  - loaded
  - empty
  - no_selected_asset
  - state_unavailable
  - live_unavailable validation path
- validation-only query contract 잠금
- validation override isolation 구조 정리 완료

현재까지 의도적으로 제한한 것:

- recommendation/ranking language 없음
- evidence drilldown 없음
- click workflow 없음
- adapter contract 확장 없음
- route/query contract 확장 없음
- title/meta richness 확장 없음

즉:
- 기능적으로는 충분히 작동하지만
- baseline에 바로 올리기엔 아직 “안전하게 작은 보조층인지”를 더 엄격히 보는 편이 맞다

## 3. promotion criteria

baseline 편입 재검토 기준은 아래로 잠근다.

1. **surface responsibility stability**
   - detail/activity와 책임 충돌이 더 이상 늘어나지 않아야 한다

2. **data contract stability**
   - existing `compareCandidates`만으로도 panel 의미가 유지되어야 한다
   - adapter 확장 없이는 panel 가치가 무너지면 안 된다

3. **integrated state coverage**
   - loaded / empty / no_selected_asset / state_unavailable / live_unavailable가
     모두 controlled path 포함해 검증 가능해야 한다

4. **semantics contamination risk**
   - compare panel이 recommendation/workflow/ranking surface로 오해되지 않아야 한다

5. **validation dependence**
   - panel이 validation-only controlled path 없이는 설명 불가능한 상태가 많으면
     아직 baseline 편입 판단은 보수적으로 본다

## 4. judgment

판정:
- **지금 당장은 baseline 편입 보류**
- **guarded extension first-pass 유지**

## 5. reasoning summary

### why not baseline now

1. compare panel은 본질적으로 `selected asset reading aid`이긴 하지만,
   표면상으로는 쉽게 recommendation panel처럼 보일 여지가 있다.

2. existing `compareCandidates`만으로는 first pass는 가능하지만,
   title richness와 relation richness가 얇아서
   baseline 핵심면으로 보기엔 아직 information density가 불안정하다.

3. runtime에서 empty compareCandidates는 controlled path로는 닫혔지만,
   자연 발생 live path에서 충분히 관찰된 상태는 아니다.

4. 현재 baseline의 핵심은
   `control bar / strip / board / detail / activity`
   책임 안정성에 있고,
   compare panel은 아직 그 위에 얹힌 추가 보조층이다.

### why not reject outright

1. semantics 오염 없이 구현됐다.
2. state coverage와 validation contract까지 닫혀 있다.
3. adapter untouched first pass가 가능했다.
4. baseline을 깨지 않는 범위 안에서 잘 제한돼 있다.

즉:
- 위험해서 제외해야 하는 수준은 아니지만
- baseline의 일부라고 선언하기엔 아직 한 단계 더 보수적으로 봐야 한다.

## 6. consequence

### because it stays guarded extension

당장 baseline freeze에 본격 편입 문구를 넣지 않는다.

대신 재검토 조건:
- compare panel이 recommendation/workflow처럼 읽히지 않는다는 운용 확인이 더 쌓일 것
- natural live usage에서 empty/non-rich compare state가 몇 번 더 관찰될 것
- adapter untouched 상태에서도 panel 의미가 충분히 유지된다고 판단될 것

이 조건이 충족되면:
- 그때 baseline freeze 문서에
  “right-column secondary compare panel included in read-only shell”
  같은 얇은 편입 갱신을 검토할 수 있다.

## 7. next step recommendation

다음 작은 작업 추천:
- **natural live compare panel observation note** 1회 누적

이유:
- 기능 확장보다, 실제 live usage에서 compare panel이 어떻게 읽히는지
  한번 더 observation memory로 남기는 것이 promotion judgment 다음 단계로 더 적절하다.

## 8. summary

한 줄로:
- compare candidate panel v1은 잘 구현됐지만, 현재 시점에서는 **baseline의 일부로 승격하기보다 guarded extension first-pass로 더 유지하는 쪽이 안전하다**.
