# origin_map_minimum_fields_v1

## 1. Purpose
This contract fixes the minimum origin map fields used to return from a derived artifact back to its source document location.

The origin map is not a full source copy.
It is a minimal provenance handle for source return.

## 2. Minimum Fields
Required fields:
- `source_doc_id`
- `heading_path`
- `source_locator`
- `source_preview`
- `derived_at`
- `derived_from_kind`

## 3. Field Rules

### `source_doc_id`
- stable source document identifier
- should avoid depending only on raw filename

### `heading_path`
- internal source section path
- list form is allowed

Example:
```json
["0. 문서 목적", "3. STEP 1 — origin map 최소 스펙 문서 고정"]
```

### `source_locator`
At least one locator is required:
- `block_id`
- `char_span(start,end)`

The v1 minimum accepts either one.

### `source_preview`
- short human verification preview
- one to two sentences maximum

### `derived_at`
- timestamp when the derivative was created

### `derived_from_kind`
Examples:
- `fragment`
- `summary`
- `receipt_seed`
- `ticket_seed`

## 4. Recommended JSON Shape
```json
{
  "origin_map": {
    "source_doc_id": "doc_xxx",
    "heading_path": ["section_a", "section_b"],
    "source_locator": {
      "type": "char_span",
      "start": 120,
      "end": 248
    },
    "source_preview": "원본 복귀용 최소 손잡이 예시",
    "derived_at": "2026-03-24T00:00:00+09:00",
    "derived_from_kind": "fragment"
  }
}
```

## 5. Operating Rule
- origin map is attached automatically at derive time
- it is not a required manual intake field
- it prepares later receipt/board/source-return reading

## 6. Current Lock
- v1 is intentionally minimal
- no merge provenance graph
- no version graph
- no heavy user-side metadata burden
