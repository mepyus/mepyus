# input registry contract v1

## required fields
- `input_id`
- `source_path`
- `label`
- `input_kind`
  - `transcript`
  - `note`
  - `memo`
  - `session_log`
  - `article`
  - `mixed`
- `split_mode`
  - `auto`
  - `timestamp`
  - `heading`
  - `paragraph`
- `note`

## optional fields
- `expected_corridor_family`
- `expected_axis`
- `format_family`
- `tags`

## sample
```json
[
  {
    "input_id": "youtube_03_22",
    "source_path": "./youtube_03_22.md",
    "label": "youtube_03_22",
    "input_kind": "transcript",
    "split_mode": "timestamp",
    "note": "long youtube discussion"
  }
]
```
