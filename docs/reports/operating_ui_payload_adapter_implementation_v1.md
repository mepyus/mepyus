# operating ui payload adapter implementation v1

## 1. verdict

- 구현 완료
- `OperatingUiPayloadAdapter` v1는 raw process-console payload를 UI-friendly model로 정규화하는 pure function으로 구현되었고, fixture case A/B/C/D 기준 핵심 field parity를 통과했다.

## 2. created files

- [operating_ui_payload_adapter.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/operating_ui_payload_adapter.py)
- [run_adapter_fixture_check.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/run_adapter_fixture_check.py)

## 3. adapter coverage

### implemented function

- `adapt_process_console_payload_to_operating_ui_model(payload, initial_asset_id=None)`

### normalized fields

- `pageTitle`
- `selectedAssetId`
- `boardItems`
- `selectedAsset`
- `derivedStrip`
- `detailModal`
- `activityPanel`
- `feedbackComposer`
- `compareCandidates`
- `guards`

### applied rules

- `initialAssetId` 우선 선택
- 없으면 `summary.selected_asset_id`
- 둘 다 없거나 invalid면 `boardItems[0]`
- `boardItems` 비면 `selectedAssetId = null`
- `state_unavailable`
- `no_previous_state`
- `no_active_attention`
- `insufficient_attention_history`
- empty arrays normalize
- `experimental_namespace` 기본 제외

## 4. fixture check

### command

```bash
python3 app/work/operating_ui/run_adapter_fixture_check.py
python3 -m py_compile app/work/operating_ui/operating_ui_payload_adapter.py app/work/operating_ui/run_adapter_fixture_check.py
```

### result

- case A: pass
- case B: pass
- case C: pass
- case D: pass

### validation mode

- fixture check는 full exact match가 아니라 **expected fixture subset parity** 방식으로 검증했다.
- 이유:
  - adapter가 fixture보다 더 많은 보조 필드를 가질 수 있도록 허용하면서
  - 핵심 정규화 필드가 맞는지만 먼저 안정적으로 보기 위함이다.

## 5. limitations

- adapter는 아직 display copy를 완전히 확정하지 않는다.
- `createdAt`은 현재 payload source에 없어서 `null`로 둔다.
- `feedbackComposer`는 local shell만 만들고 persistence contract는 포함하지 않는다.
- `selectedAsset`와 `detailModal`은 현재 동일 구조를 공유한다.
  - 이후 실제 React 구현에서 분리 필요 여부를 다시 볼 수 있다.
- compare candidate shape는 현재 최소 필드만 normalize한다.
- activity item shape는 recent history feed 최소 구조만 담고 있다.

## 6. recommended next step

- 다음 구현 슬라이스는 **`OperatingBoardPage` 없이도 단독으로 검증 가능한 read-only React mock harness`** 또는 `AssetStateCard + DerivedStateStrip` 두 컴포넌트의 최소 렌더 구현이다.
- 이유:
  - adapter 경계가 고정됐으므로 이제 raw payload를 직접 참조하지 않는 첫 UI slice를 안전하게 붙일 수 있다.
