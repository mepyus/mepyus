# readable input board / eirpage_20260323_192612

## 1. 입력 정보
- input_id: `eirpage`
- label: `eirpage`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/references/WashTank/src/pages/EIRPage.jsx`
- input_kind: `mixed`
- detected_profile: `article`

## 2. split 결과
- split_mode_used: `paragraph`
- raw_line_count: `114`
- unit_count: `7`

## 3. unit 목록 요약
- unit_001 — paragraph / para_001 ~ para_002 — "// src/pages/EIRPage.jsx
import React from 'react';
import { useInbound } from '../hooks/useInbound'; /**
 * EIR (Entry ..."
- unit_002 — paragraph / para_003 ~ para_004 — "// Placeholder for a tank ID for demonstration purposes
  // In a real application, this would come from a selected tank..."
- unit_003 — paragraph / para_005 ~ para_006 — "const handleStart = () => {
    console.log(`Attempting to start inbound job for tank: ${demoTankId}`);
    startInbound..."
- unit_004 — paragraph / para_007 ~ para_008 — "const handleCancel = () => {
    console.log(`Attempting to cancel inbound job for tank: ${demoTankId}`);
    cancelInbo..."
- unit_005 — paragraph / para_009 ~ para_010 — "{loading && <p style={{ color: 'blue' }}>Loading...</p>}
      {error && <p style={{ color: 'red', fontWeight: 'bold' }}..."
- unit_006 — paragraph / para_011 ~ para_011 — "<div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
        <button
          onClick={handleInitiate}
    ..."
- unit_007 — paragraph / para_012 ~ para_013 — "{/* Here is where you would integrate specific components for the EIR workflow,
          e.g., an InspectionForm for da..."

## 4. 당장 읽히는 흐름
- 입력은 중간 단위 block으로 나뉘었고, 앞/중간/뒤 흐름을 빠르게 재확인하기 좋은 분해다.

