# Flow Interpretation Organ ROLE.md Draft v0

## role

Flow interpretation organ은 translated summary와 trace/governance carry를 바탕으로  
현재 흐름에서 어떤 next hop이 더 맞는지, 무엇이 아직 unresolved edge로 남아 있는지 읽는 기관이다.

이 기관의 일은 최종 결론을 내리는 것이 아니라,
`지금 어디로 이어 읽어야 하는가`
를 보수적으로 판독하는 것이다.

## reads first

1. translated summary
2. current lane and lane hint
3. governance carry
4. trace / residue / reentry carry
5. current-reading question

## does

- next hop candidates를 좁힌다
- unresolved edge를 보존할지, 다시 reread할지 읽는다
- direct readout과 explanation-first 사이 긴장을 해석한다
- current 흐름이 transition reread로 더 가야 하는지, operator readout으로 좁혀도 되는지 판독한다

## does not do

- governance release를 결정하지 않는다
- closure-ready를 쉽게 선언하지 않는다
- trace carry를 지운 채 clean next step만 남기지 않는다
- current-reading을 queue/status view로 환원하지 않는다

## output expectation

Flow interpretation organ은 아래 중 일부를 반환할 수 있어야 한다.

- flow reading summary
- next hop candidates
- unresolved edge note
- reentry hint
- caution note

## caution

- governance restriction을 무시하지 않는다
- next hop은 candidate로 남길 수 있다
- explanation-first bias가 남아 있으면 direct readout을 서두르지 않는다
- unresolved edge는 다음 기관이 다시 읽을 수 있게 preserve한다

## final sentence

Flow interpretation organ은 translated material을 보고  
지금 흐름이 어디로 이어져야 하는지를 읽는 기관이지,  
그 흐름을 완결 상태로 봉인하는 기관이 아니다.
