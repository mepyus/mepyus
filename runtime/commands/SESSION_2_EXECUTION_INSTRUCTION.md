# SESSION_2_EXECUTION_INSTRUCTION.md

## 1. Goal
Create `SPACE_MATERIAL_ACTIVATION_MAP_V0`, `MATERIAL_FAMILY_INDEX_V0`, and `CONTEXT_BUNDLE_REQUIREMENTS_V0` to formalize how existing VectorFL records are triggered, retrieved, and packaged for external tools.

## 2. Search First (Critical Records)
- Pipeline Harness Records, Package Digest, Recovery Records.
- Tool-Readable Surface discussions, Space Index, Mission Packet structure.
- Line/Axis/Camera/Lens records in `docs/architecture` and `references/`.
- External Tool patterns (Codex, OmX, Hermes).
- Drift/Failure records (Gemini/Codex).
- User Operating Principles (No implementation, Search-first, SSOT).

## 3. Activation Routes (Requirement: 8+)
1. External Material Intake
2. Codex/OmX Attachment Review
3. Gemini Output Review
4. Boundary Risk Detection
5. Tool-Readable Surface Revision
6. Context Bundle Creation
7. Review & Recovery Gate
8. Post-Session Issue Review

## 4. Material Families (Requirement: 10+)
1. Pipeline Harness Records
2. Tool-Readable Surface Records
3. Boundary Risk Records
4. Gemini Drift Records
5. Codex/OmX Workflow Records
6. Hermes Interface Records
7. OpenClaw Gateway Watch Records
8. Digest / Recovery Records
9. User Operating Principles
10. Program-Level Setup Records

## 5. Constraints
- No Implementation, No Automation, No Runner/Script, No Controller/Router/Registry, No DB/Schema.
- Keep program-level focus. Use the 4-Lens (Line/Axis/Camera/Lens) logic.
- Log non-blocking issues in Issue Log; don't stop.
- **Do not modify files or execute commands without user approval.**

## 6. Next Handoff
Prepare `SESSION_3_HANDOFF.md` for Tool-Readable Surface session.
