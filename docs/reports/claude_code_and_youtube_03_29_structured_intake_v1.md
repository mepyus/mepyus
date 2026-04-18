# claude_code and youtube_03_29 structured intake v1

## 1. 목적

이 문서는 `claude_code.txt`와 `youtube_03_29.md`가 실제 structured intake를 통과했다는 사실을 기록하는 최소 기록이다.

핵심은 내용 요약이 아니라, 두 입력이 `process_structured_doc_with_routing.py`를 통해 receipt / label packet / origin map을 생성했다는 점이다.

## 2. 통과한 입력

- `inputs/external_cases/claude_code.txt`
  - doc_id: `doc_claude_code`
  - receipt: `runtime/receipts/doc_claude_code_operation_receipt.md`
  - origin map: `runtime/manifests/origin_maps/doc_claude_code_receipt_seed_origin_map.json`

- `inputs/external_cases/youtube_03_29.md`
  - doc_id: `doc_youtube_03_29`
  - receipt: `runtime/receipts/doc_youtube_03_29_operation_receipt.md`
  - origin map: `runtime/manifests/origin_maps/doc_youtube_03_29_receipt_seed_origin_map.json`

## 3. 왜 이것이 중요한가

- `claude_code.txt`는 이제 bridge 문서가 아니라 실제 intake된 입력으로 공간에 들어왔다.
- `youtube_03_29.md`도 같은 structured routing을 통과해 외부 입력층의 일부로 다시 연결됐다.
- 즉 둘 다 단순 파일 존재가 아니라, structured doc routing -> observer ingest -> receipt/origin map 생성 경로를 탔다.

## 4. 현재 상태

- `claude_code.txt`:
  - structured intake 완료
  - receipt 생성 완료
  - origin map 생성 완료
  - latent lines bridge 문서와 연결 가능

- `youtube_03_29.md`:
  - structured intake 완료
  - receipt 생성 완료
  - origin map 생성 완료
  - 외부 입력층의 대표 사례로 다시 사용할 수 있음

## 5. 이 문서로 다시 볼 수 있는 것

- `claude_code` 계열 자료가 단순 bridge note가 아니라 실제 입력기 통과 자료라는 점
- `youtube_03_29.md`가 외부 자료 입력층에 실제로 들어와 있다는 점
- 다음 단계에서 raw / first-pass / report / provenance 경로를 다시 읽을 때, 이 둘을 같은 입력 계열로 다룰 수 있다는 점

