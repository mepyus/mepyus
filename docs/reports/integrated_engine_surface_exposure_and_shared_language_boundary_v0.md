# Integrated Engine Surface Exposure and Shared Language Boundary v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

이 문서는 3면 언어와 shared operational language의 관계, 그리고 surface별 노출 밀도 규칙을 정리한다.

이 문서는 final glossary, UI copy, wording patch, scaffold 수정, manifest/read-map 변경, external style guide, 새 기능을 만들지 않는다.

## 1. shared language의 위치

Shared operational language는 user-only language가 아니다.

또한 3면 내부 언어를 덮어쓰는 replacement layer도 아니다.

Shared operational language는:

- engine language를 user language로 단순 변환하지 않는다.
- VectorFL language를 숨기지 않는다.
- user language만 예쁘게 만드는 것이 아니다.
- 3면 언어에서 반복되는 line / connection / axis를 다른 주체들이 함께 쓸 수 있게 응축한 층이다.

## 2. surface별 노출 밀도 규칙

### 2.1 engine surface

Engine surface는 internal language direct exposure가 가장 많이 허용되는 면이다.

허용되는 노출:

- shaped input
- work input
- execution state
- processing step
- return material
- reprocess request
- execution history

주의할 점:

- engine surface는 judgment authority가 아니다.
- return material은 final completion으로 보이면 안 된다.
- validation / user decision / reflux route는 engine이 아니라 VectorFL/user route로 올라가야 한다.

노출 규칙:

```text
engine surface = processing / execution / return material language direct exposure allowed
but validation authority and route decision must not be absorbed
```

### 2.2 VectorFL surface

VectorFL surface는 shared grammar 중심 면이다.

허용되는 노출:

- maturation object
- anchor context
- validation mediation
- return validation
- reflux reason
- anchor drift
- reprocess / rewind reason
- support reread recovery
- line / connection / axis mediation

주의할 점:

- VectorFL은 engine executor가 아니다.
- line atlas나 support trace가 maturation body를 대체하면 안 된다.
- anchor / maturation / operating object는 한 카드 언어로 뭉개면 안 된다.

노출 규칙:

```text
VectorFL surface = shared grammar and mediation language primary
internal language partial exposure allowed when it explains anchor, validation, maturation, reflux, or axis growth
```

### 2.3 user surface

User surface는 human-readable shared grammar 중심 면이다.

허용되는 노출:

- current route
- request / return / reflux state at operating level
- what is open
- what remains closed
- decision needed
- hold / watch / carry-forward / reject-conflict as operating state
- package-opening authority

주의할 점:

- user surface는 engine 내부 언어 전체를 보여주는 면이 아니다.
- user surface는 team/role/governance console이 아니다.
- user가 internal engine terms를 모두 외워야 하면 interface 실패다.

노출 규칙:

```text
user surface = human-readable shared grammar primary
internal terms appear only when they are needed for decision, route, boundary, or current status
```

## 3. actor-facing boundary

### User

보여야 하는 것:

- 지금 무엇을 결정해야 하는가
- 무엇이 open/closed인가
- 어떤 route가 살아 있는가
- 어떤 line/axis가 다음 package 후보인가

보이지 않아도 되는 것:

- 모든 engine execution detail
- 모든 manifest/read-map 내부 언어
- 모든 trace density

### VectorFL

보여야 하는 것:

- internal record에서 나온 line
- line 사이의 connection
- emerging axis
- validation / anchor / reflux / reprocess reason

보이지 않아도 되는 것:

- engine execution detail 전체
- user-facing copy 전체

### Engine-side operators

보여야 하는 것:

- shaped input
- processing state
- output/return material
- reprocess request

보이지 않아도 되는 것:

- VectorFL maturation judgment 전체
- user package-opening deliberation 전체

### Codex

보여야 하는 것:

- baseline constraints
- current package scope
- canonical write boundary
- proposal / hold / carry-forward / reject-conflict classification

보이지 않아도 되는 것:

- Gemini proposal material as direct core truth
- user-facing final copy unless explicitly opened

### Gemini

보여야 하는 것:

- proposal-only boundary
- design clay role
- what kind of material is needed
- no direct-to-core path

보이지 않아도 되는 것:

- scaffold write authority
- manifest truth authority
- final promotion authority

## 4. shared language boundary rules

### Rule 1. shared language does not overwrite internal language

Internal terms remain available where needed.

Shared language makes them usable across actors, not replaced.

### Rule 2. shared language is not user-only

If only the user can use it, it is probably a simplified explanation, not operational language.

Shared language must be reusable by User, VectorFL, Engine-side operators, Codex, Gemini, and internal team with different exposure densities.

### Rule 3. surface identity must remain visible

Shared language must not collapse:

- user operation into governance console
- VectorFL mediation into line browser or engine execution
- engine processing into judgment authority

### Rule 4. high-risk terms require boundary-first exposure

The following must be exposed with boundary before convenience:

- `workspace ownership`
- `carry-forward`
- `reject / conflict`
- `collision stop condition`
- `watch keep`
- `hold`

### Rule 5. interface grows from axis

User-facing fixed interface should be derived from repeated axes, not imported as an external template.

If there is no repeated axis, keep the material as line/connection evidence.

## 5. current boundary summary

| layer | should expose | should not expose as |
|---|---|---|
| engine surface | processing/return internal language | final judgment or validation authority |
| VectorFL surface | shared grammar, validation, maturation, axis reading | engine executor or list browser center |
| user surface | human-readable shared grammar for operation/decision | full internal engine language or team governance console |
| shared operational language | cross-actor route/authority/state/boundary grammar | final glossary, UI copy, or replacement lexicon |

## 6. closeout

Shared operational language is the bridge layer where 3면 언어 continues to grow while becoming usable by multiple actors.

It is not a stop point for internal language and not a final human wording layer. It is a controlled exposure layer.
