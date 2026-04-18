# ai future segment probe result

## 1. probe scope
- engine path:
  - `build_dust_inputs_from_source`
  - `label_dust_inputs`
- helper:
  - [run_ai_future_segment_probe.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_ai_future_segment_probe.py)
- generated output:
  - [ai_future_segment_probe_20260327T231746Z.json](/Users/sungsookim/universe/vectorfl_replica/app/work/archive_review/probe_support/future_segment_probe/generated/ai_future_segment_probe_20260327T231746Z.json)

## 2. what was searched
- scope:
  - `inputs/external_cases` text-like inputs
- filter:
  - `미래`
  - `future`
  - `AGI`
  - `초지능`
  - `자동화`
  - adjacent future-oriented phrases

## 3. high-level result
- matched source count:
  - `21`
- overall scene counts:
  - `review`: `160`
  - `evidence`: `11`
  - `impl`: `10`
  - `spec`: `1`
- overall flow counts:
  - `compare`: `150`
  - `run`: `28`
  - `break`: `3`
  - `fix`: `1`

## 4. what this means
- `AI의 미래` 관련 분절값은 한 층으로만 나오지 않았다.
- 가장 많이는 `review / compare` 층으로 읽히지만,
  `impl / run`, `evidence / run`, `spec / fix` 쪽도 실제로 존재한다.
- 즉 이 축은 이미 엔진 안에서
  - 전망/서술 층
  - 실행/자동화 층
  - 근거/검증 층
  - 일부 명세성 층
  으로 흩어져 있다.

## 5. top sources
- [dario_amodei_youtube.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/dario_amodei_youtube.txt)
  - matched segments: `24`
  - dominant read: `review / compare`
  - recurring anchors: `AGI`, `앞으로`, `소프트웨어`
- [youtube_03_18.md](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/youtube_03_18.md)
  - matched segments: `22`
  - mixed read: `review`, `impl`, `evidence`
  - recurring anchors: `노정석`, `그래서`, `소프트웨어를`
- [claude_code_index.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/claude_code_index.txt)
  - matched segments: `18`
  - dominant read: `review`, with visible `run`
  - recurring anchors: `자동화`, `스킬`, `커스텀`
- [andrej_karpathy_youtube.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/andrej_karpathy_youtube.txt)
  - matched segments: `16`
  - dominant read: `review / compare`, with one `evidence / run`
  - recurring anchors: `앞으로`, `초지능은`
- [youtube_01_29.md](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/youtube_01_29.md)
  - matched segments: `16`
  - dominant read: `review / compare`
  - recurring anchors: `AGI`, `post-AGI`
- [alexkarp_youtube.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/alexkarp_youtube.txt)
  - matched segments: `8`
  - dominant read: `review / compare`
  - recurring anchors: `앞으로`, `기술의`

## 6. layer examples
- future as trajectory / forecast layer:
  - Dario:
    - `우린는 확실히 AGI를 향해 가고 있죠.`
  - Andrej:
    - `20년 뒤에 미래를.`
  - Alex:
    - `앞으로 이런 슈퍼 기술의 가치는 지금과는 비교도 안 될만큼 폭등할 것입니다.`

- future as automation / execution layer:
  - Claude Code index:
    - `커스텀 스킬을 만들어서 이 과정을 자동화할 수도 있는데요.`
  - youtube_03_18:
    - `그런 것도 조금씩 자동화가 되게 되는데 코드 자체는...`

- future as national / strategic layer:
  - youtube_01_29:
    - `누가 더 초지능에 먼저 도달하느냐, 이 부분이 안보에 직결...`

- future as evidence / check layer:
  - some future-related segments do not stay only in speculation;
    a smaller subset lands in `evidence` and `run` lanes.

## 7. important caution
- 이번 probe는 `연결의 단단함`을 본 것이 아니다.
- 이번 probe는 오직
  - 미래 관련 분절값이 실제로 여러 층위로 나타나는지
  - 엔진 내부 분절 구조에서 어떤 scene/flow로 퍼지는지
  를 본 것이다.
- 따라서 지금 단계의 결론은
  - `future-of-ai` 축이 이미 다층적이다
  이지,
  - 그 층들이 잘 연결되었다
  는 뜻은 아니다.

## 8. one-line summary
- 엔진 내부 분절 기준으로 보면 `AI의 미래` 관련 입력값은 단순 전망 서술에만 머물지 않고, review/compare를 중심으로 impl/run, evidence/run, spec/fix까지 얇게 퍼진 다층 분포를 이미 만들고 있다.
