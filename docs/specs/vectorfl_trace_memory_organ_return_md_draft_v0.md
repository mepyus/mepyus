# Trace Memory Organ RETURN.md Draft v0

## return purpose

Trace/memory organ의 반환은  
현재 run과 reading에서 남은 단서들을 later-readable trace로 바꿔  
history 면과 다음 기관이 다시 사용할 수 있게 하는 것이다.

## minimum return blocks

### 1. trace record

- append-only trace entry

### 2. residue note

- 무엇을 아직 preserve해야 하는지

### 3. reentry hint

- 언제 다시 이 흐름을 열어야 하는지

### 4. carry summary

- 다음 reread를 위한 짧은 continuity summary

### 5. decision anchor

- governance 또는 current-reading과 연결되는 trace anchor

## preferred wording

- "preserve ..."
- "reopen when ..."
- "carry forward ..."
- "leave unresolved ..."

## avoid wording

- "completed history"
- "final timeline"
- "resolved note" when residue remains

## final sentence

Trace/memory organ의 반환은 완료 보고가 아니라, 이후 reread와 handoff가 더 정확해지도록 trace, residue, reentry, carry summary를 append-only로 남기는 continuity-aware return이어야 한다.
