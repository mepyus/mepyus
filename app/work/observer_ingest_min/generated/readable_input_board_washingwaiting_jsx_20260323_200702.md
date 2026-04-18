# readable input board / washingwaiting_jsx_20260323_200702

## 1. 입력 정보
- input_id: `washingwaiting_jsx`
- label: `washingwaiting_jsx`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/references/WashTank/src/WashingWaiting.jsx`
- input_kind: `mixed`
- detected_profile: `article`

## 2. split 결과
- split_mode_used: `paragraph`
- raw_line_count: `1889`
- unit_count: `123`

## 3. unit 목록 요약
- unit_001 — paragraph / para_001 ~ para_002 — "import React, { useEffect, useMemo, useState, useCallback } from 'react';
import {
  ChevronLeft,
  LayoutGrid,
  Activi..."
- unit_002 — paragraph / para_003 ~ para_004 — "const UI = {
  blue: '#3b82f6',
  green: '#10b981',
  red: '#ef4444',
  amber: '#f59e0b',
  violet: '#8b5cf6',
  slate90..."
- unit_003 — paragraph / para_005 ~ para_006 — "const BAY_LAYOUT = [
  { key: 'LEFT_BAY', label: 'LEFT BAY', slots: [1, 2, 3, 4, 5] },
  { key: 'RIGHT_BAY', label: 'RIG..."
- unit_004 — paragraph / para_007 ~ para_008 — "function upper(value) {
  return String(value ?? '').trim().toUpperCase();
} function hasValue(value) {
  if (Array.isAr..."
- unit_005 — paragraph / para_009 ~ para_010 — "function pickFirst(...values) {
  for (const value of values) {
    if (hasValue(value)) return value;
  }
  return null..."
- unit_006 — paragraph / para_011 ~ para_012 — "function normalizeBayName(bayName) {
  const b = upper(bayName);
  const match = b.match(/^(LEFT_BAY|RIGHT_BAY)_\d+$/);
..."
- unit_007 — paragraph / para_013 ~ para_014 — "function makeSlotKey(bayName, slotNo) {
  return `${normalizeBayName(bayName)}-${normalizeSlotNo(slotNo)}`;
} function m..."
- unit_008 — paragraph / para_015 ~ para_016 — "function makeAnonymousSpaceKey(slotKey) {
  return `SPACE_ANON:${slotKey}`;
} function toArrayStrings(value) {
  if (Arr..."
- unit_009 — paragraph / para_017 ~ para_018 — "/* =============================================================================
 * [각주-03] 시간 유틸
 * ===================..."
- unit_010 — paragraph / para_019 ~ para_020 — "let diffSec = Math.floor((nowTs - startMs) / 1000);
  if (!Number.isFinite(diffSec)) return '--:--:--';
  if (diffSec < ..."
- unit_011 — paragraph / para_021 ~ para_022 — "/* =============================================================================
 * [각주-04] 데이터 해석
 * ==================..."
- unit_012 — paragraph / para_023 ~ para_024 — "function resolveTankInfo(row) {
  const tankType = pickFirst(row?.tank_type, row?.spec_type, row?.tank?.tank_type, row?...."
- unit_013 — paragraph / para_025 ~ para_026 — "return parts.length ? parts.join(' / ') : '기본 정보 없음';
} function resolveCargo(row) {
  return pickFirst(
    row?.cargo_..."
- unit_014 — paragraph / para_027 ~ para_028 — "function resolvePrevCargo(row) {
  return pickFirst(
    row?.previous_cargo_name,
    row?.prev_cargo_name,
    row?.la..."
- unit_015 — paragraph / para_029 ~ para_030 — "if (typeof raw === 'boolean') return raw ? 'REQUIRED' : 'NORMAL';
  if (!hasValue(raw)) return 'N/A';
  return String(ra..."
- unit_016 — paragraph / para_031 ~ para_032 — "function resolveInstruction(row) {
  return pickFirst(
    row?.wash_instruction,
    row?.special_instruction,
    row?..."
- unit_017 — paragraph / para_033 ~ para_034 — "function deriveSyncState({ job, space }) {
  if (job && space) return SYNC_STATE.MATCHED;
  if (job && !space) return SY..."
- unit_018 — paragraph / para_035 ~ para_036 — "function getDisplayTankNo(record) {
  if (!record) return '-';
  if (record.tank_number) return record.tank_number;
  if..."
- unit_019 — paragraph / para_037 ~ para_038 — "if (record.sync_state === SYNC_STATE.JOB_ONLY) {
    issues.push('세척 Job은 있으나 실제 베이 적재가 확인되지 않습니다.');
  } if (record.syn..."
- unit_020 — paragraph / para_039 ~ para_040 — "if (record.job_status && !['READY', 'IN_PROGRESS', 'DONE'].includes(upper(record.job_status))) {
    issues.push(`예상 외 j..."
- unit_021 — paragraph / para_041 ~ para_042 — "return issues;
} function sortHybridRecords(a, b) {
  const syncPriority = {
    [SYNC_STATE.JOB_ONLY]: 0,
    [SYNC_STA..."
- unit_022 — paragraph / para_043 ~ para_044 — "const ap = syncPriority[a.sync_state] ?? 9;
  const bp = syncPriority[b.sync_state] ?? 9;
  if (ap !== bp) return ap - b..."
- unit_023 — paragraph / para_045 ~ para_046 — "const aTime = toMs(a.started_at) ?? toMs(a.created_at) ?? 0;
  const bTime = toMs(b.started_at) ?? toMs(b.created_at) ??..."
- unit_024 — paragraph / para_047 ~ para_048 — "/* =============================================================================
 * [각주-01] WASH PAGE CONTAINER
 * -----..."
- unit_025 — paragraph / para_049 ~ para_050 — "/* ---------------------------------------------------------------------------
   * [각주-02] 페이지 데이터 재조회
   * - washJobs:..."
- unit_026 — paragraph / para_051 ~ para_052 — "setWashJobs(normalizedJobs);
    setWashBayStatus(Array.isArray(bays) ? bays : []);
  }, []); useEffect(() => {
    refr..."
- unit_027 — paragraph / para_053 ~ para_054 — "/* ---------------------------------------------------------------------------
   * [각주-03] 공통 상태 전이 실행기
   * - page에서 이..."
- unit_028 — paragraph / para_055 ~ para_056 — "for (const target of targets) {
        try {
          // ✅ 기준선: 상태 전이는 triggerEvent 계열로만 처리
          await jms.trigge..."
- unit_029 — paragraph / para_057 ~ para_058 — "// 일부 실패가 있으면 페이지 쪽에서 message로 보여줄 수 있도록 throw
      if (failures.length > 0) {
        const summary = failures
       ..."
- unit_030 — paragraph / para_059 ~ para_060 — "/* ---------------------------------------------------------------------------
   * [각주-04] 세척 시작: READY -> IN_PROGRESS
..."
- unit_031 — paragraph / para_061 ~ para_062 — "return (
    // WashingWaitingPage 렌더 구간
<WashingWaitingPage
  onBack={onBack}
  washJobs={washJobs}
  washBayStatus={wa..."
- unit_032 — paragraph / para_063 ~ para_064 — "function getJobTone(status) {
  const s = upper(status);
  if (s === 'READY') return { bg: `${UI.violet}15`, color: UI.v..."
- unit_033 — paragraph / para_065 ~ para_066 — "const jobByTank = new Map();
  const spaceByTank = new Map();
  const spaceBySlot = new Map(); const diagnostics = {
   ..."
- unit_034 — paragraph / para_067 ~ para_068 — "for (const row of jobs) {
    const tankNoKey = upper(resolveTankNumber(row));
    if (!tankNoKey) continue; if (jobByTa..."
- unit_035 — paragraph / para_069 ~ para_070 — "jobByTank.set(tankNoKey, row);
  } for (const row of spaces) {
    const slotKey = makeSlotKey(row?.bay_name, row?.slot_..."
- unit_036 — paragraph / para_071 ~ para_072 — "const tankNoKey = upper(row?.tank_number);
    if (!tankNoKey) continue; if (spaceByTank.has(tankNoKey)) {
      diagnos..."
- unit_037 — paragraph / para_073 ~ para_074 — "spaceByTank.set(tankNoKey, row);
  } const allTankKeys = new Set([...jobByTank.keys(), ...spaceByTank.keys()]);
  const ..."
- unit_038 — paragraph / para_075 ~ para_076 — "for (const tankNoKey of allTankKeys) {
    const job = jobByTank.get(tankNoKey) || null;
    const space = spaceByTank.g..."
- unit_039 — paragraph / para_077 ~ para_078 — "const record = {
      record_key: makeTankKey(tankNoKey),
      tank_number: resolveTankNumber(job) || space?.tank_numb..."
- unit_040 — paragraph / para_079 ~ para_080 — "job_id: job?.job_id || job?.id || null,
      tank_id: resolveTankId(job),
      job_type: job?.job_type || 'WASH',
    ..."
- unit_041 — paragraph / para_081 ~ para_082 — "tank_info_text: resolveTankInfo(job),
      cargo_name: resolveCargo(job),
      previous_cargo_name: resolvePrevCargo(j..."
- unit_042 — paragraph / para_083 ~ para_084 — "record.issues = buildIssues(record);
    records.push(record);
  } for (const [slotKey, space] of spaceBySlot.entries())..."
- unit_043 — paragraph / para_085 ~ para_086 — "if (!occupied) continue;
    if (tankNoKey && allTankKeys.has(tankNoKey)) continue; const record = {
      record_key: m..."
- unit_044 — paragraph / para_087 ~ para_088 — "sync_state: SYNC_STATE.SPACE_ONLY,
      issues: [], job_id: null,
      tank_id: null,
      job_type: 'WASH',
      jo..."
- unit_045 — paragraph / para_089 ~ para_090 — "bay_name: space?.bay_name ?? null,
      bay_group: normalizeBayName(space?.bay_name),
      slot_no: space?.slot_no ?? ..."
- unit_046 — paragraph / para_091 ~ para_092 — "elapsed: '--:--:--'
    }; record.issues = buildIssues(record);
    records.push(record);
  }..."
- unit_047 — paragraph / para_093 ~ para_094 — "records.sort(sortHybridRecords); return {
    records,
    indexes: {
      spaceBySlot
    },
    diagnostics
  };
}..."
- unit_048 — paragraph / para_095 ~ para_096 — "/* =============================================================================
 * [각주-08] 일괄 처리 대상 필터
 * - 시작: MATCHED..."
- unit_049 — paragraph / para_097 ~ para_098 — "/* =============================================================================
 * [각주-09] 메인 컴포넌트
 * =================..."
- unit_050 — paragraph / para_099 ~ para_100 — "const hybridBundle = useMemo(
    () => buildHybridRecords(washJobs, washBayStatus, nowTs),
    [washJobs, washBayStatus..."
- unit_051 — paragraph / para_101 ~ para_102 — "const recordByKey = useMemo(() => {
    const map = new Map();
    for (const record of hybridData) map.set(record.recor..."
- unit_052 — paragraph / para_103 ~ para_104 — "const activeRecords = useMemo(() => {
    return hybridData.filter((record) => {
      const status = upper(record.job_s..."
- unit_053 — paragraph / para_105 ~ para_106 — "useEffect(() => {
    if (selectedRecordKey && !recordByKey.has(selectedRecordKey)) {
      setSelectedRecordKey(null);
..."
- unit_054 — paragraph / para_107 ~ para_108 — "for (const record of hybridData) {
      if (record.sync_state === SYNC_STATE.MATCHED) acc.matched += 1;
      if (recor..."
- unit_055 — paragraph / para_109 ~ para_110 — "for (const row of safeArray(washBayStatus)) {
      if (isSpaceOccupied(row)) acc.occupiedSlots += 1;
      else acc.vac..."
- unit_056 — paragraph / para_111 ~ para_112 — "const syncRate = useMemo(() => {
    if (summary.total === 0) return 100;
    return Math.round((summary.matched / summa..."
- unit_057 — paragraph / para_113 ~ para_114 — "const openDetail = useCallback((recordKey) => {
    if (!recordKey) return;
    setSelectedRecordKey(recordKey);
  }, []..."
- unit_058 — paragraph / para_115 ~ para_116 — "const handleSelectSlot = useCallback(
    (slotKey) => {
      const record = recordBySlotKey.get(slotKey);
      if (re..."
- unit_059 — paragraph / para_117 ~ para_118 — "setMessage('');
      setErrorMessage(''); if (typeof runner !== 'function') {
        setErrorMessage(
          action..."
- unit_060 — paragraph / para_119 ~ para_120 — "if (!targets.length) {
        setErrorMessage(
          actionType === 'START'
            ? '처리 가능한 시작 대상이 없습니다.'
   ..."
- unit_061 — paragraph / para_121 ~ para_122 — "const confirmed =
        typeof window === 'undefined'
          ? true
          : window.confirm(`${groupLabel} ${tar..."
- unit_062 — paragraph / para_123 ~ para_124 — "const nextBusyKey = `${actionType}:${bayGroup}:${targets.length}`;
      setBusyKey(nextBusyKey); try {
        await ru..."
- unit_063 — paragraph / para_125 ~ para_126 — "setMessage(`${groupLabel} ${targets.length}대 ${actionLabel} 처리 완료`);
      } catch (error) {
        setErrorMessage(err..."
- unit_064 — paragraph / para_127 ~ para_128 — "return (
      <span
        style={{
          display: 'inline-flex',
          alignItems: 'center',
          minHei..."
- unit_065 — paragraph / para_129 ~ para_130 — "return (
      <button
        key={record.record_key}
        type="button"
        onClick={() => openDetail(record.re..."
- unit_066 — paragraph / para_131 ~ para_132 — "<div style={styles.badgeRow}>
          <span style={styles.badge(syncTone.bg, syncTone.color, syncTone.border)}>
      ..."
- unit_067 — paragraph / para_133 ~ para_134 — "{record.msds_status !== 'N/A' ? renderChip(`MSDS ${record.msds_status}`, 'amber') : null}
        </div> <div style={sty..."
- unit_068 — paragraph / para_135 ~ para_136 — "<div style={styles.infoLine}>
            <span style={styles.infoLabel}>PREV</span>
            <span style={styles.inf..."
- unit_069 — paragraph / para_137 ~ para_138 — "const renderBaySlot = (bayName, slotNo) => {
    const slotKey = makeSlotKey(bayName, slotNo);
    const space = spaceBy..."
- unit_070 — paragraph / para_139 ~ para_140 — "{occupied ? (
          <>
            <div style={styles.slotTankNo}>
              {getDisplayTankNo(record || { tank_..."
- unit_071 — paragraph / para_141 ~ para_142 — "return (
    <div style={styles.container}>
      {/* HEADER */}
      <header style={styles.header}>
        <div style..."
- unit_072 — paragraph / para_143 ~ para_144 — "<div style={styles.headerRight}>
          {renderChip(`SYNC ${syncRate}%`, 'green')}
          {renderChip(`JOB_ONLY ${..."
- unit_073 — paragraph / para_145 ~ para_145 — "<div style={styles.actionGroup}>
          <div style={styles.actionGroupTitle}>우측 베이</div>
          <button
          ..."
- unit_074 — paragraph / para_146 ~ para_147 — "<div style={styles.messageArea}>
          {message ? <div style={styles.successMessage}>{message}</div> : null}
       ..."
- unit_075 — paragraph / para_148 ~ para_149 — "<div style={styles.summaryRow}>
            {renderChip(`TOTAL ${activeRecords.length}`, 'blue')}
            {renderChi..."
- unit_076 — paragraph / para_150 ~ para_151 — "{/* BAY MONITOR */}
        <section style={styles.monitorSection}>
          <div style={styles.sectionHeader}>
       ..."
- unit_077 — paragraph / para_152 ~ para_153 — "<div style={styles.slotColumn}>
                  {bay.slots.map((slotNo) => renderBaySlot(bay.key, slotNo))}
          ..."
- unit_078 — paragraph / para_154 ~ para_155 — "{/* DETAIL MODAL */}
      {selectedRecord ? (
        <div style={styles.modalOverlay} onClick={closeDetail}>
         ..."
- unit_079 — paragraph / para_156 ~ para_157 — "<div style={styles.modalBadgeRow}>
              {(() => {
                const syncTone = getSyncTone(selectedRecord.s..."
- unit_080 — paragraph / para_158 ~ para_159 — "{(() => {
                const jobTone = getJobTone(selectedRecord.job_status);
                return (
              ..."
- unit_081 — paragraph / para_160 ~ para_161 — "<div style={styles.modalInfoRow}>
                <MapPin size={15} color={UI.blue} />
                <span style={styl..."
- unit_082 — paragraph / para_162 ~ para_163 — "<div style={styles.modalInfoRow}>
                <Database size={15} color={UI.violet} />
                <span style={..."
- unit_083 — paragraph / para_164 ~ para_165 — "<div style={styles.modalBlock}>
                <div style={styles.modalBlockTitle}>CARGO</div>
                <div sty..."
- unit_084 — paragraph / para_166 ~ para_167 — "<div style={styles.modalBlock}>
                <div style={styles.modalBlockTitle}>MSDS / HAZARD</div>
                ..."
- unit_085 — paragraph / para_168 ~ para_169 — "<div style={styles.modalBlock}>
                <div style={styles.modalBlockTitle}>WASH INSTRUCTION</div>
             ..."
- unit_086 — paragraph / para_170 ~ para_171 — "<ul style={styles.issueList}>
                    {selectedRecord.issues.map((msg, idx) => (
                      <li k..."
- unit_087 — paragraph / para_172 ~ para_173 — "header: {
    minHeight: 72,
    padding: '12px 20px',
    background: UI.white,
    borderBottom: `1px solid ${UI.borde..."
- unit_088 — paragraph / para_174 ~ para_175 — "headerRight: {
    display: 'flex',
    alignItems: 'center',
    gap: 8,
    flexWrap: 'wrap'
  }, backBtn: {
    width..."
- unit_089 — paragraph / para_176 ~ para_177 — "title: {
    margin: 0,
    fontSize: 20,
    fontWeight: 950,
    color: UI.slate900
  }, headerMeta: {
    marginTop: ..."
- unit_090 — paragraph / para_178 ~ para_179 — "actionBar: {
    padding: '12px 20px',
    borderBottom: `1px solid ${UI.border}`,
    background: UI.white,
    display..."
- unit_091 — paragraph / para_180 ~ para_181 — "actionGroupTitle: {
    fontSize: 13,
    fontWeight: 900,
    color: UI.slate900
  }, startButton: (disabled) => ({
   ..."
- unit_092 — paragraph / para_182 ~ para_183 — "completeButton: (disabled) => ({
    minHeight: 40,
    border: 'none',
    borderRadius: 12,
    background: disabled ?..."
- unit_093 — paragraph / para_184 ~ para_185 — "successMessage: {
    padding: '10px 12px',
    borderRadius: 12,
    background: UI.softGreen,
    border: `1px solid $..."
- unit_094 — paragraph / para_186 ~ para_187 — "main: {
    flex: 1,
    display: 'grid',
    gridTemplateColumns: '1.6fr 1fr',
    gap: 16,
    padding: 16,
    overfl..."
- unit_095 — paragraph / para_188 ~ para_189 — "monitorSection: {
    minWidth: 0,
    background: UI.white,
    border: `1px solid ${UI.border}`,
    borderRadius: 20,..."
- unit_096 — paragraph / para_190 ~ para_191 — "sectionTitle: {
    fontSize: 14,
    fontWeight: 950,
    color: UI.slate900
  }, sectionSub: {
    marginTop: 4,
    f..."
- unit_097 — paragraph / para_192 ~ para_193 — "summaryRow: {
    display: 'flex',
    gap: 8,
    flexWrap: 'wrap',
    marginBottom: 12
  }, listScroll: {
    flex: 1..."
- unit_098 — paragraph / para_194 ~ para_195 — "emptyBox: {
    minHeight: 120,
    borderRadius: 16,
    border: `1px dashed ${UI.border}`,
    display: 'flex',
    al..."
- unit_099 — paragraph / para_196 ~ para_197 — "return {
      width: '100%',
      textAlign: 'left',
      border: `2px solid ${borderColor}`,
      background: selec..."
- unit_100 — paragraph / para_198 ~ para_199 — "listMain: {
    minWidth: 0,
    display: 'flex',
    flexDirection: 'column',
    gap: 4
  }, listRight: {
    minWidth..."
- unit_101 — paragraph / para_200 ~ para_201 — "tankNo: {
    fontSize: 22,
    fontWeight: 950,
    color: UI.slate900,
    lineHeight: 1.1
  }, tankSub: {
    fontSiz..."
- unit_102 — paragraph / para_202 ~ para_203 — "smallMeta: {
    fontSize: 11,
    color: UI.slate700,
    fontWeight: 800
  }, badgeRow: {
    display: 'flex',
    gap..."
- unit_103 — paragraph / para_204 ~ para_205 — "badge: (bg, color, borderColor) => ({
    display: 'inline-flex',
    alignItems: 'center',
    gap: 5,
    minHeight: 2..."
- unit_104 — paragraph / para_206 ~ para_207 — "infoLine: {
    display: 'flex',
    alignItems: 'center',
    gap: 8,
    minWidth: 0
  }, infoLabel: {
    minWidth: 4..."
- unit_105 — paragraph / para_208 ~ para_209 — "infoValue: {
    fontSize: 12,
    fontWeight: 800,
    color: UI.slate800,
    overflow: 'hidden',
    textOverflow: 'e..."
- unit_106 — paragraph / para_210 ~ para_211 — "hazardChip: {
    display: 'inline-flex',
    alignItems: 'center',
    minHeight: 24,
    padding: '0 10px',
    border..."
- unit_107 — paragraph / para_212 ~ para_213 — "monitorColumn: {
    minWidth: 0,
    display: 'flex',
    flexDirection: 'column',
    gap: 10
  }, monitorColumnHeader..."
- unit_108 — paragraph / para_214 ~ para_215 — "monitorColumnTitle: {
    fontSize: 13,
    fontWeight: 950,
    color: UI.slate900
  }, monitorColumnSub: {
    marginT..."
- unit_109 — paragraph / para_216 ~ para_217 — "slotColumn: {
    flex: 1,
    minHeight: 0,
    display: 'grid',
    gridTemplateRows: 'repeat(5, 1fr)',
    gap: 10
  ..."
- unit_110 — paragraph / para_218 ~ para_219 — "if (!occupied) {
      border = '#e5e7eb';
      bg = '#f8fafc';
    } if (syncState === SYNC_STATE.SPACE_ONLY) border =..."
- unit_111 — paragraph / para_220 ~ para_221 — "return {
      position: 'relative',
      width: '100%',
      minHeight: 0,
      borderRadius: 16,
      border: `2px..."
- unit_112 — paragraph / para_222 ~ para_223 — "slotTankNo: {
    fontSize: 19,
    fontWeight: 950,
    color: UI.slate900,
    textAlign: 'center'
  }, slotPill: (bg,..."
- unit_113 — paragraph / para_224 ~ para_225 — "vacantText: {
    fontSize: 14,
    fontWeight: 900,
    color: UI.slate300
  }, footer: {
    minHeight: 48,
    paddin..."
- unit_114 — paragraph / para_226 ~ para_227 — "footerText: {
    fontSize: 11,
    color: UI.slate400,
    fontWeight: 700,
    fontFamily: 'monospace',
    whiteSpace..."
- unit_115 — paragraph / para_228 ~ para_229 — "modalCard: {
    width: 'min(760px, 100%)',
    maxHeight: '85vh',
    overflowY: 'auto',
    background: UI.white,
    ..."
- unit_116 — paragraph / para_230 ~ para_231 — "modalLabel: {
    fontSize: 10,
    fontWeight: 950,
    color: UI.slate400,
    letterSpacing: '0.08em'
  }, modalTankN..."
- unit_117 — paragraph / para_232 ~ para_233 — "closeBtn: {
    width: 36,
    height: 36,
    borderRadius: 10,
    border: `1px solid ${UI.border}`,
    background: '..."
- unit_118 — paragraph / para_234 ~ para_235 — "modalBody: {
    marginTop: 16,
    display: 'flex',
    flexDirection: 'column',
    gap: 14
  }, modalInfoRow: {
    d..."
- unit_119 — paragraph / para_236 ~ para_237 — "modalInfoLabel: {
    minWidth: 86,
    fontSize: 11,
    fontWeight: 950,
    color: UI.slate400
  }, modalInfoValue: {..."
- unit_120 — paragraph / para_238 ~ para_239 — "modalMono: {
    flex: 1,
    fontSize: 11,
    fontWeight: 700,
    color: UI.slate800,
    fontFamily: 'monospace',
  ..."
- unit_121 — paragraph / para_240 ~ para_241 — "modalBlockTitle: {
    fontSize: 11,
    fontWeight: 950,
    color: UI.slate500,
    marginBottom: 8
  }, modalBlockTex..."
- unit_122 — paragraph / para_242 ~ para_243 — "modalHazardWrap: {
    marginTop: 10,
    display: 'flex',
    gap: 6,
    flexWrap: 'wrap'
  }, emptyText: {
    fontSi..."
- unit_123 — paragraph / para_244 ~ para_246 — "issueBox: {
    borderRadius: 14,
    border: `1px solid ${UI.amber}40`,
    background: UI.softAmber,
    padding: 12
 ..."

## 4. 당장 읽히는 흐름
- 입력은 중간 단위 block으로 나뉘었고, 앞/중간/뒤 흐름을 빠르게 재확인하기 좋은 분해다.

