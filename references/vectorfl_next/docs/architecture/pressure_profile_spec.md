# Pressure Profile Spec

`PressureProfile`은 hard truth가 아니라 살아 있는 압력 인터페이스다.

구성:

- `profile_id`
- `axes`
- `support_refs`
- `created_at`

각 axis는 아래 구조를 따른다.

- `axis`
- `strength_hint`
- `support_refs`

이 구조는 시간, 감정, 환류를 별도 본체로 고정하지 않는다.
대신 새로운 압력이 들어왔을 때 같은 material이 다른 seed, cell, local space로 재배치될 자리를 남긴다.
