# operating ui fixture and fallback rule lock

## 1. verdict

- 구현 전 안정화 자산 작성 완료
- `OperatingUiPayloadAdapter`는 이제 representative case A/B/C/D로 입력/출력 예시가 잠겼고, empty/fallback/disabled UI 규칙도 별도 기준으로 고정된다.

## 2. fixture cases

### case A. selected asset + latest/diff/attention/memory present

#### raw payload sample

```json
{
  "summary": {
    "selected_asset_id": "turboquant_youtube",
    "state_unavailable": false
  },
  "header": {
    "state": "loaded",
    "asset_name": "turboquant_youtube",
    "source_type": "dialogue_asset",
    "updated_at": "2026-03-28T21:31:34.399318+00:00",
    "badges": [
      {"key": "packet_texture", "label": "overcompressed / closure-heavy"},
      {"key": "grounding_status", "label": "fallback grounded"},
      {"key": "emergence_status", "label": "low emergence"},
      {"key": "carryover_risk", "label": "high"},
      {"key": "maturation_state", "label": "fallback"},
      {"key": "traceability_status", "label": "traceable"}
    ]
  },
  "asset_rail": [
    {
      "asset_id": "turboquant_youtube",
      "asset_name": "turboquant_youtube",
      "packet_texture_label": "overcompressed / closure-heavy",
      "maturation_state_label": "fallback",
      "traceability_status_label": "traceable",
      "emergence_status_label": "low emergence",
      "updated_at": "2026-03-28T21:31:34.399318+00:00"
    },
    {
      "asset_id": "choi_ai_classroom_cnn",
      "asset_name": "choi_ai_classroom_cnn",
      "packet_texture_label": "structured open / low emergence",
      "maturation_state_label": "weak",
      "traceability_status_label": "traceable",
      "emergence_status_label": "low emergence",
      "updated_at": "2026-03-28T21:48:48.000000+00:00"
    }
  ],
  "state_panel": {
    "state": "loaded",
    "canonical_fields": [
      {"key": "packet_texture", "label": "overcompressed / closure-heavy"},
      {"key": "grounding_status", "label": "fallback grounded"},
      {"key": "emergence_status", "label": "low emergence"},
      {"key": "carryover_risk", "label": "high"},
      {"key": "maturation_state", "label": "fallback"},
      {"key": "traceability_status", "label": "traceable"}
    ],
    "state_notes": "first live run: bridge confirmed, single-window packet, naming-heavy technical transcript kept conservative",
    "evidence_refs": [
      {"ref_kind": "generated_probe", "ref_id": "turboquant_youtube_live_run_v1_w6_s3_20260328T212851Z"}
    ],
    "compare_reasons": ["same_compressed_family", "similar_carryover_pattern"],
    "gate_blockers": ["fallback_grounding_dominance", "scaffold_carryover_risk"],
    "history_summary": {
      "recent_update_count": 2,
      "latest_update_trigger_type": "runtime_evidence",
      "latest_update_reason": "first_live_run_turboquant_youtube_v1",
      "latest_change_kind": "canonical_change"
    },
    "diff_summary": {
      "state": "loaded",
      "diff_class": "canonical_change",
      "changed_field_count": 6,
      "provenance_only": false,
      "interpretation_badges": ["canonical_change", "packet_texture_shift"],
      "compare_to_previous_href": "/process-console?asset_id=turboquant_youtube&compare_index=0"
    }
  },
  "latest_state_preview": {
    "state": "loaded",
    "packet_texture_label": "overcompressed / closure-heavy",
    "maturation_state_label": "fallback",
    "traceability_status_label": "traceable",
    "updated_at": "2026-03-28T21:31:34.399318+00:00"
  },
  "compare_entry": {
    "state": "loaded",
    "related_assets": [
      {"asset_id": "knowledge_editing_youtube", "reason": "same compressed family"}
    ]
  },
  "attention_queue": {
    "selected_asset_attention": {
      "kind": "active_item",
      "queue_status": "new",
      "priority_level": "high",
      "attention_reason": "no_previous_state_anchor",
      "diff_class": "canonical_change",
      "changed_fields": ["packet_texture", "maturation_state"]
    },
    "selected_asset_memory": {
      "attention_pattern_summary": "mostly provenance_only background updates",
      "total_attention_events": 3,
      "reopened_attention_count": 0,
      "suppressed_attention_count": 1,
      "provenance_only_repeat_density": 0.67,
      "dominant_shift_types": ["provenance_only"]
    }
  },
  "history_drilldown": {
    "state": "loaded",
    "items": [
      {
        "updated_at": "2026-03-28T21:31:34.399318+00:00",
        "update_trigger_type": "runtime_evidence",
        "update_reason": "first_live_run_turboquant_youtube_v1",
        "changed_fields": ["packet_texture", "maturation_state"],
        "compare_index": 0
      }
    ],
    "latest_lineage_link": {
      "summary": "current latest formed from recent 2 updates",
      "latest_update_trigger_type": "runtime_evidence",
      "latest_update_reason": "first_live_run_turboquant_youtube_v1",
      "latest_updated_at": "2026-03-28T21:31:34.399318+00:00"
    }
  }
}
```

#### adapted ui model sample

```json
{
  "pageTitle": "turboquant_youtube",
  "selectedAssetId": "turboquant_youtube",
  "boardItems": [
    {
      "id": "turboquant_youtube",
      "title": "turboquant_youtube",
      "packetTextureLabel": "overcompressed / closure-heavy",
      "maturationLabel": "fallback",
      "traceabilityLabel": "traceable",
      "emergenceLabel": "low emergence",
      "updatedAt": "2026-03-28T21:31:34.399318+00:00"
    },
    {
      "id": "choi_ai_classroom_cnn",
      "title": "choi_ai_classroom_cnn",
      "packetTextureLabel": "structured open / low emergence",
      "maturationLabel": "weak",
      "traceabilityLabel": "traceable",
      "emergenceLabel": "low emergence",
      "updatedAt": "2026-03-28T21:48:48.000000+00:00"
    }
  ],
  "derivedStrip": {
    "badgeItems": [
      {"key": "packet_texture", "label": "overcompressed / closure-heavy"},
      {"key": "grounding_status", "label": "fallback grounded"},
      {"key": "emergence_status", "label": "low emergence"},
      {"key": "carryover_risk", "label": "high"},
      {"key": "maturation_state", "label": "fallback"},
      {"key": "traceability_status", "label": "traceable"}
    ],
    "latestPreview": {
      "packetTexture": "overcompressed / closure-heavy",
      "maturation": "fallback",
      "traceability": "traceable",
      "updatedAt": "2026-03-28T21:31:34.399318+00:00"
    },
    "diffSummary": {
      "state": "loaded",
      "diffClass": "canonical_change",
      "changedFieldCount": 6,
      "provenanceOnly": false
    },
    "attentionSummary": {
      "state": "loaded",
      "priority": "high",
      "reason": "no_previous_state_anchor",
      "queueStatus": "new"
    },
    "memorySummary": {
      "summary": "mostly provenance_only background updates",
      "totalEvents": 3,
      "provenanceDensity": 0.67,
      "dominantShiftTypes": ["provenance_only"]
    }
  },
  "detailModal": {
    "title": "turboquant_youtube",
    "subtitle": "dialogue_asset",
    "createdAt": null,
    "updatedAt": "2026-03-28T21:31:34.399318+00:00",
    "canonicalStateRows": [
      {"key": "packet_texture", "label": "overcompressed / closure-heavy"},
      {"key": "grounding_status", "label": "fallback grounded"},
      {"key": "emergence_status", "label": "low emergence"},
      {"key": "carryover_risk", "label": "high"},
      {"key": "maturation_state", "label": "fallback"},
      {"key": "traceability_status", "label": "traceable"}
    ],
    "stateNotes": "first live run: bridge confirmed, single-window packet, naming-heavy technical transcript kept conservative",
    "scopeLabel": "selected asset operating state",
    "dependencyList": ["same_compressed_family", "similar_carryover_pattern"],
    "evidenceRefs": [
      {"kind": "generated_probe", "id": "turboquant_youtube_live_run_v1_w6_s3_20260328T212851Z", "label": "generated_probe: turboquant_youtube_live_run_v1_w6_s3_20260328T212851Z"}
    ],
    "compareReasons": ["same_compressed_family", "similar_carryover_pattern"],
    "gateBlockers": ["fallback_grounding_dominance", "scaffold_carryover_risk"],
    "historySummary": {
      "latestTrigger": "runtime_evidence",
      "latestReason": "first_live_run_turboquant_youtube_v1",
      "recentUpdateCount": 2
    }
  }
}
```

#### 적용 규칙

- normal state
- no fallback suppression
- diff CTA 활성
- detail modal 열 수 있음
- feedback는 기본 enabled 가능

#### UI 영향

- `DerivedStateStrip` 전부 표시
- `AssetStateBoard` 정상 렌더
- `SelectedAssetDetailModal` 정상 렌더
- `ActivityPanel` recent item 1개 이상 표시
- `FeedbackComposer` enabled

### case B. no_previous_state

#### raw payload sample

```json
{
  "summary": {
    "selected_asset_id": "choi_ai_classroom_cnn",
    "state_unavailable": false
  },
  "header": {
    "state": "loaded",
    "asset_name": "choi_ai_classroom_cnn",
    "source_type": "dialogue_asset",
    "updated_at": "2026-03-28T21:48:48.000000+00:00",
    "badges": [
      {"key": "packet_texture", "label": "structured open / low emergence"},
      {"key": "grounding_status", "label": "partially grounded"}
    ]
  },
  "asset_rail": [
    {
      "asset_id": "choi_ai_classroom_cnn",
      "asset_name": "choi_ai_classroom_cnn",
      "packet_texture_label": "structured open / low emergence",
      "maturation_state_label": "weak",
      "traceability_status_label": "traceable",
      "emergence_status_label": "low emergence",
      "updated_at": "2026-03-28T21:48:48.000000+00:00"
    }
  ],
  "state_panel": {
    "state": "loaded",
    "canonical_fields": [
      {"key": "packet_texture", "label": "structured open / low emergence"}
    ],
    "state_notes": "first cohort anchor",
    "evidence_refs": [],
    "compare_reasons": ["breathing_contrast"],
    "gate_blockers": [],
    "history_summary": {
      "recent_update_count": 1,
      "latest_update_trigger_type": "runtime_evidence",
      "latest_update_reason": "lecture_transcript_cohort_batch_test_v1",
      "latest_change_kind": "no_previous_state_anchor"
    },
    "diff_summary": {
      "state": "no_previous_state",
      "compare_to_previous_href": null
    }
  },
  "latest_state_preview": {
    "state": "loaded",
    "packet_texture_label": "structured open / low emergence",
    "maturation_state_label": "weak",
    "traceability_status_label": "traceable",
    "updated_at": "2026-03-28T21:48:48.000000+00:00"
  },
  "attention_queue": {
    "selected_asset_attention": {
      "kind": "active_item",
      "queue_status": "new",
      "priority_level": "high",
      "attention_reason": "no_previous_state_anchor",
      "diff_class": "no_previous_state",
      "changed_fields": []
    },
    "selected_asset_memory": null
  },
  "history_drilldown": {
    "state": "loaded",
    "items": [],
    "latest_lineage_link": {
      "summary": "latest has no previous state anchor",
      "latest_update_trigger_type": "runtime_evidence",
      "latest_update_reason": "lecture_transcript_cohort_batch_test_v1",
      "latest_updated_at": "2026-03-28T21:48:48.000000+00:00"
    }
  }
}
```

#### adapted ui model sample

```json
{
  "pageTitle": "choi_ai_classroom_cnn",
  "selectedAssetId": "choi_ai_classroom_cnn",
  "derivedStrip": {
    "badgeItems": [
      {"key": "packet_texture", "label": "structured open / low emergence"},
      {"key": "grounding_status", "label": "partially grounded"}
    ],
    "latestPreview": {
      "packetTexture": "structured open / low emergence",
      "maturation": "weak",
      "traceability": "traceable",
      "updatedAt": "2026-03-28T21:48:48.000000+00:00"
    },
    "diffSummary": {
      "state": "no_previous_state",
      "diffClass": null,
      "changedFieldCount": 0,
      "provenanceOnly": false
    },
    "attentionSummary": {
      "state": "loaded",
      "priority": "high",
      "reason": "no_previous_state_anchor",
      "queueStatus": "new"
    },
    "memorySummary": {
      "summary": "insufficient_attention_history",
      "totalEvents": 0,
      "provenanceDensity": null,
      "dominantShiftTypes": []
    }
  }
}
```

#### 적용 규칙

- `no_previous_state`
- compare CTA 비활성
- memory는 `insufficient_attention_history`

#### UI 영향

- `DerivedStateStrip`는 diff를 neutral badge로 표시
- `SelectedAssetDetailModal`는 열 수 있지만 diff action 비활성
- `ActivityPanel`는 lineage summary만 표시

### case C. insufficient_attention_history

#### raw payload sample

```json
{
  "summary": {
    "selected_asset_id": "gary_tan_brain",
    "state_unavailable": false
  },
  "header": {
    "state": "loaded",
    "asset_name": "gary_tan_brain",
    "source_type": "dialogue_asset",
    "updated_at": "2026-03-28T12:05:47.000000+00:00",
    "badges": [
      {"key": "packet_texture", "label": "overcompressed / breathing"}
    ]
  },
  "asset_rail": [
    {
      "asset_id": "gary_tan_brain",
      "asset_name": "gary_tan_brain",
      "packet_texture_label": "overcompressed / breathing",
      "maturation_state_label": "fallback",
      "traceability_status_label": "traceable",
      "emergence_status_label": "minimal emergence",
      "updated_at": "2026-03-28T12:05:47.000000+00:00"
    }
  ],
  "state_panel": {
    "state": "loaded",
    "canonical_fields": [
      {"key": "packet_texture", "label": "overcompressed / breathing"}
    ],
    "state_notes": "bridge confirmed, packet still compressed but breathing remains",
    "evidence_refs": [],
    "compare_reasons": ["breathing_contrast"],
    "gate_blockers": ["scaffold_carryover_risk"],
    "history_summary": {
      "recent_update_count": 1,
      "latest_update_trigger_type": "runtime_evidence",
      "latest_update_reason": "gary_tan_brain_process_trace_validation_v1",
      "latest_change_kind": "canonical_change"
    },
    "diff_summary": {
      "state": "loaded",
      "diff_class": "canonical_change",
      "changed_field_count": 1,
      "provenance_only": false
    }
  },
  "latest_state_preview": {
    "state": "loaded",
    "packet_texture_label": "overcompressed / breathing",
    "maturation_state_label": "fallback",
    "traceability_status_label": "traceable",
    "updated_at": "2026-03-28T12:05:47.000000+00:00"
  },
  "attention_queue": {
    "selected_asset_attention": null,
    "selected_asset_memory": null
  },
  "history_drilldown": {
    "state": "loaded",
    "items": [],
    "latest_lineage_link": {
      "summary": "current latest formed from recent 1 updates",
      "latest_update_trigger_type": "runtime_evidence",
      "latest_update_reason": "gary_tan_brain_process_trace_validation_v1",
      "latest_updated_at": "2026-03-28T12:05:47.000000+00:00"
    }
  }
}
```

#### adapted ui model sample

```json
{
  "pageTitle": "gary_tan_brain",
  "selectedAssetId": "gary_tan_brain",
  "derivedStrip": {
    "badgeItems": [
      {"key": "packet_texture", "label": "overcompressed / breathing"}
    ],
    "latestPreview": {
      "packetTexture": "overcompressed / breathing",
      "maturation": "fallback",
      "traceability": "traceable",
      "updatedAt": "2026-03-28T12:05:47.000000+00:00"
    },
    "diffSummary": {
      "state": "loaded",
      "diffClass": "canonical_change",
      "changedFieldCount": 1,
      "provenanceOnly": false
    },
    "attentionSummary": null,
    "memorySummary": {
      "summary": "insufficient_attention_history",
      "totalEvents": 0,
      "provenanceDensity": null,
      "dominantShiftTypes": []
    }
  }
}
```

#### 적용 규칙

- `no_active_attention`
- `insufficient_attention_history`

#### UI 영향

- `DerivedStateStrip` attention slot은 neutral helper로 표시
- `ActivityPanel`는 history empty state
- `FeedbackComposer`는 normal, 단 auto-submit CTA는 없음

### case D. selected asset 없음 / state_unavailable

#### raw payload sample

```json
{
  "summary": {
    "selected_asset_id": null,
    "state_unavailable": true
  },
  "header": {
    "state": "state_unavailable",
    "badges": []
  },
  "asset_rail": [],
  "state_panel": {
    "state": "state_unavailable",
    "canonical_fields": [],
    "evidence_refs": [],
    "compare_reasons": [],
    "gate_blockers": [],
    "history_summary": {
      "recent_update_count": 0
    },
    "diff_summary": {
      "state": "state_unavailable"
    }
  },
  "latest_state_preview": {
    "state": "state_unavailable"
  },
  "compare_entry": {
    "state": "state_unavailable",
    "related_assets": []
  },
  "attention_queue": {
    "selected_asset_attention": null,
    "selected_asset_memory": null
  },
  "history_drilldown": {
    "state": "history_unavailable",
    "items": [],
    "latest_lineage_link": {
      "summary": "no_history_yet"
    }
  }
}
```

#### adapted ui model sample

```json
{
  "pageTitle": "no_canonical_state_yet",
  "selectedAssetId": null,
  "boardItems": [],
  "selectedAsset": null,
  "derivedStrip": {
    "badgeItems": [],
    "latestPreview": null,
    "diffSummary": {
      "state": "state_unavailable",
      "diffClass": null,
      "changedFieldCount": 0,
      "provenanceOnly": false
    },
    "attentionSummary": null,
    "memorySummary": {
      "summary": "insufficient_attention_history",
      "totalEvents": 0,
      "provenanceDensity": null,
      "dominantShiftTypes": []
    }
  },
  "detailModal": null,
  "compareCandidates": []
}
```

#### 적용 규칙

- `state_unavailable`
- `no_selected_asset`
- `empty_activity`
- `feedback_disabled`

#### UI 영향

- `AssetStateBoard` empty state
- `SelectedAssetDetailModal` 열지 않음
- `DerivedStateStrip` neutral fallback only
- `ActivityPanel` empty helper
- `FeedbackComposer` disabled

## 3. empty and fallback rules

- component별 상세 규칙은 [operating_ui_empty_and_fallback_rules_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/operating_ui_empty_and_fallback_rules_v1.md)에 잠갔다.

## 4. selection defaults

- `initialAssetId`가 있으면 우선 선택
- 없으면 adapter가 준 `boardItems[0]`를 선택
- `boardItems`가 비면 `selectedAssetId = null`
- modal 초기값은 `false`
- asset 전환 시 `feedbackDraft`는 reset
- 동일 asset 재오픈 시에만 retain 허용 가능하지만 v1 기본은 reset

## 5. adapter boundary

- adapter 책임:
  - raw payload presence check
  - nullable normalize
  - array normalize
  - UI-friendly field regrouping
  - fallback state code 부여

- component 책임:
  - 표시 문구 렌더
  - CTA 활성/비활성
  - draft 입력 제어
  - visual empty/fallback treatment

- adapter가 하지 않는 것:
  - business interpretation 추가
  - UI copy 최종 문구 확정
  - persistence
  - experimental namespace 노출

## 6. recommended next step

- 실제 구현에 들어간다면 가장 먼저 칠 파일은 여전히 `OperatingUiPayloadAdapter`다.
- 이유:
  - fixture A/B/C/D와 fallback rule이 모두 adapter를 기준으로 정규화되기 때문이다.
