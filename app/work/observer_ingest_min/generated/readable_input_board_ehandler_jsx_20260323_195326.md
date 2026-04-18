# readable input board / ehandler_jsx_20260323_195326

## 1. 입력 정보
- input_id: `ehandler_jsx`
- label: `ehandler_jsx`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/references/WashTank/src/Ehandler.jsx`
- input_kind: `mixed`
- detected_profile: `article`

## 2. split 결과
- split_mode_used: `paragraph`
- raw_line_count: `1059`
- unit_count: `52`

## 3. unit 목록 요약
- unit_001 — paragraph / para_001 ~ para_002 — "/* -------------------------------------------------------------------------- */
/* [SYSTEM_ARCHITECT] EMPTY_EQUIPMENT_O..."
- unit_002 — paragraph / para_003 ~ para_004 — "// ✅ 프로젝트 경로에 맞게 수정
import { supabase } from "./supabaseClient"; const UI = {
  main_blue: "#3b82f6",
  soft_bg: "#f8faf..."
- unit_003 — paragraph / para_005 ~ para_006 — "const BLOCKS_BY_SITE_CODE = {
  "1YARD": ["A", "B", "C", "D", "E", "F", "G", "H"],
  "2YARD": ["A1", "B1", "C1", "D1", "..."
- unit_004 — paragraph / para_007 ~ para_008 — "/* ----------------------------- 작은 유틸들 ----------------------------- */
const pad2 = (n) => String(n ?? "").padStart(2,..."
- unit_005 — paragraph / para_009 ~ para_010 — "export default function EmptyOperatorConsole({
  siteCode = "1YARD", // ✅ 엠티 장비가 1부지면 기본 1YARD로
  onBack,
}) {
  /* ----..."
- unit_006 — paragraph / para_011 ~ para_012 — "const [site, setSite] = useState(null);           // {site_id, site_code, site_name, yard_row_max}
  const [tanks, setTa..."
- unit_007 — paragraph / para_013 ~ para_014 — "if (siteErr) throw siteErr;
      if (!siteRow) throw new Error("SITE_NOT_FOUND");
      if (!siteRow.is_active) console..."
- unit_008 — paragraph / para_015 ~ para_016 — "// 2) locations 로드 (해당 site_id)
      const { data: locRows, error: locErr } = await supabase
        .from("locations")..."
- unit_009 — paragraph / para_017 ~ para_018 — "// 3) tanks 좌표 뷰 로드
      // - 장비기사는 보통 "미지정"도 봐야 해서, 우선 넓게 가져오고 UI에서 필터링
      const { data: tankRows, error: tankErr }..."
- unit_010 — paragraph / para_019 ~ para_020 — "useEffect(() => {
    loadAll();
  }, [loadAll]); /* ----------------------------- 파생 데이터 ----------------------------- ..."
- unit_011 — paragraph / para_021 ~ para_022 — "const tankByLocationId = useMemo(() => {
    const map = {};
    for (const t of tanks) {
      if (t.current_location_i..."
- unit_012 — paragraph / para_023 ~ para_024 — "// Yard: 좌표 -> location_id (seed가 있으면 항상 매칭됨)
  const yardLocIdByCoord = useMemo(() => {
    const map = {};
    for (co..."
- unit_013 — paragraph / para_025 ~ para_026 — "const filteredList = useMemo(() => {
    const q = search.trim().toLowerCase();
    const base = tanks.filter((t) => {
 ..."
- unit_014 — paragraph / para_027 ~ para_028 — "return base.filter((t) => {
      const no = (t.tank_number || "").toLowerCase();
      const coord = (t.coord_label || ..."
- unit_015 — paragraph / para_029 ~ para_030 — "/* ----------------------------- RPC: Yard 좌표 배정 ----------------------------- */
  const assignYardByCoord = useCallbac..."
- unit_016 — paragraph / para_031 ~ para_032 — "/* ----------------------------- RPC: location_id로 배정 (공정 슬롯용) ----------------------------- */
  const assignByLocation..."
- unit_017 — paragraph / para_033 ~ para_034 — "/* ----------------------------- 공통: 탱크 카드 클릭 ----------------------------- */
  const handleSelectTank = (tank) => {
  ..."
- unit_018 — paragraph / para_035 ~ para_036 — "/* ----------------------------- Yard: 슬롯 클릭 ----------------------------- */
  const handlePickYardSlot = async (block,..."
- unit_019 — paragraph / para_037 ~ para_038 — "/* ----------------------------- WashBay/InspectBay: 슬롯 클릭 ----------------------------- */
  const handlePickProcessSlo..."
- unit_020 — paragraph / para_039 ~ para_040 — "<div style={styles.titleArea}>
            <div style={styles.subTitle}>EMPTY_EQUIPMENT_OPERATOR</div>
            <div ..."
- unit_021 — paragraph / para_041 ~ para_042 — "<div style={styles.navRight}>
          {!!errMsg && (
            <div style={styles.errPill}>
              <AlertTria..."
- unit_022 — paragraph / para_043 ~ para_043 — "<div style={styles.filterBar}>
              {[
                ["UNASSIGNED", "미지정", counts.UNASSIGNED],
              ..."
- unit_023 — paragraph / para_044 ~ para_045 — "<div style={styles.searchBox}>
              <Search size={16} color={UI.slate} />
              <input
                ..."
- unit_024 — paragraph / para_046 ~ para_047 — "<div style={styles.coordLine}>
                    <Layers size={14} color={selectedTank?.tank_id === t.tank_id ? "#fff"..."
- unit_025 — paragraph / para_048 ~ para_049 — "{filteredList.length === 0 && (
                <div style={styles.emptyBox}>조건에 맞는 탱크가 없습니다.</div>
              )}
   ..."
- unit_026 — paragraph / para_050 ~ para_051 — "{/* RIGHT: Workspace */}
        <section style={styles.workSection}>
          {activeTab === "YARD" && (
            <..."
- unit_027 — paragraph / para_052 ~ para_053 — "{!selectedTank && (
                <div style={styles.bigEmpty}>
                  좌측에서 탱크를 먼저 선택하세요.
                <..."
- unit_028 — paragraph / para_054 ~ para_055 — "{selectedBlock && (
                <YardSlotModal
                  block={selectedBlock}
                  onClose={()..."
- unit_029 — paragraph / para_056 ~ para_057 — "{activeTab === "INSPECT_BAY" && (
            <ProcessGrid
              title="검사베이 배치"
              icon={<ShieldChec..."
- unit_030 — paragraph / para_058 ~ para_059 — "/* -------------------------------------------------------------------------- */
/* SUB: Yard 슬롯 모달 (좌표 입력의 핵심)         ..."
- unit_031 — paragraph / para_060 ~ para_061 — "<div style={styles.gridWrap}>
          <div style={styles.gridHeaderRow}>
            <div style={styles.gridCorner}>T ..."
- unit_032 — paragraph / para_062 ~ para_063 — "return (
                  <button
                    key={`${t}-${r}`}
                    onClick={() => onPick(block..."
- unit_033 — paragraph / para_064 ~ para_064 — "/* -------------------------------------------------------------------------- */
/* SUB: 공정 슬롯 그리드 (wash_bay / inspect_b..."
- unit_034 — paragraph / para_065 ~ para_066 — "return (
    <div style={styles.workspaceCard}>
      <div style={styles.workspaceHeader}>
        {icon}
        <div>
..."
- unit_035 — paragraph / para_067 ~ para_068 — "{sorted.length === 0 ? (
        <div style={styles.bigEmpty}>{emptyHint}</div>
      ) : (
        <div style={styles.p..."
- unit_036 — paragraph / para_069 ~ para_070 — "<div style={{ marginTop: 10, fontWeight: 950, fontSize: 16 }}>
                  {isOcc ? occ.tank_number : "AVAILABLE"}..."
- unit_037 — paragraph / para_071 ~ para_072 — "/* -------------------------------------------------------------------------- */
/* STYLES                              ..."
- unit_038 — paragraph / para_073 ~ para_074 — "navLeft: { display: "flex", gap: "18px", alignItems: "center", flex: 1 },
  navRight: { display: "flex", gap: "12px", al..."
- unit_039 — paragraph / para_075 ~ para_076 — "titleArea: { display: "flex", flexDirection: "column", gap: 2 },
  subTitle: { fontSize: 11, fontWeight: 950, color: UI...."
- unit_040 — paragraph / para_077 ~ para_078 — "tabBtn: {
    border: "none",
    padding: "10px 14px",
    borderRadius: 12,
    fontSize: 13,
    fontWeight: 900,
   ..."
- unit_041 — paragraph / para_079 ~ para_080 — "errPill: {
    display: "flex",
    alignItems: "center",
    gap: 8,
    padding: "8px 10px",
    borderRadius: 12,
   ..."
- unit_042 — paragraph / para_081 ~ para_082 — "sidebar: { display: "flex", flexDirection: "column", gap: 14, overflow: "hidden" }, taskSection: {
    flex: 1,
    back..."
- unit_043 — paragraph / para_083 ~ para_084 — "hintSection: {
    background: "#fff",
    borderRadius: "22px",
    border: `1px solid ${UI.border_light}`,
    padding..."
- unit_044 — paragraph / para_085 ~ para_086 — "filterBar: { display: "flex", gap: 8, padding: 12, flexWrap: "wrap", borderBottom: `1px solid ${UI.border_light}` },
  f..."
- unit_045 — paragraph / para_087 ~ para_088 — "scrollArea: { flex: 1, overflowY: "auto", padding: 14 }, tankCard: {
    padding: 14,
    background: UI.soft_bg,
    bo..."
- unit_046 — paragraph / para_089 ~ para_090 — "emptyBox: { textAlign: "center", padding: 28, color: UI.slate, fontWeight: 900 }, workSection: {
    background: "transp..."
- unit_047 — paragraph / para_091 ~ para_092 — "workspaceCard: {
    flex: 1,
    background: "#fff",
    borderRadius: 28,
    border: `1px solid ${UI.border_light}`,
..."
- unit_048 — paragraph / para_093 ~ para_094 — "blockRow: { display: "flex", gap: 10, flexWrap: "wrap", marginTop: 10 },
  blockBtn: (active) => ({
    padding: "12px 1..."
- unit_049 — paragraph / para_095 ~ para_096 — "selectedBar: {
    marginTop: 14,
    padding: "10px 12px",
    borderRadius: 14,
    background: "rgba(59,130,246,0.08)..."
- unit_050 — paragraph / para_097 ~ para_098 — "gridWrap: { display: "flex", flexDirection: "column", gap: 10, overflowX: "auto", paddingBottom: 8 },
  gridHeaderRow: {..."
- unit_051 — paragraph / para_099 ~ para_100 — "slotBtn: (occupied, hasLoc) => ({
    width: 130,
    borderRadius: 16,
    border: `2px solid ${occupied ? UI.main_blue..."
- unit_052 — paragraph / para_101 ~ para_101 — "procGrid: {
    marginTop: 14,
    display: "grid",
    gridTemplateColumns: "repeat(auto-fill, minmax(220px, 1fr))",
  ..."

## 4. 당장 읽히는 흐름
- 입력은 중간 단위 block으로 나뉘었고, 앞/중간/뒤 흐름을 빠르게 재확인하기 좋은 분해다.

