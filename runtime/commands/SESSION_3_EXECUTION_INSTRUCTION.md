# SESSION_3_EXECUTION_INSTRUCTION.md

## 1. Goal
Create `TOOL_READABLE_SURFACE_V0` set (README, CURRENT_MODE, BOUNDARY_RULES, AUTHORITY_LEVELS, SPACE_INDEX, INTERPRETATION_GUIDE, MISSION_PACKET_TEMPLATE, RETURN_RECOVERY_RULES) and define the tool interaction protocol.

## 2. Search First
- Surface-related definitions, CURRENT_MODE, BOUNDARY_RULES.
- Space Index mapping, Interpretation Guide (4-Lens logic).
- Mission Packet Template, Return Recovery Rules.
- Existing tool error logs (Codex drift, Gemini drift).
- Boundary/Authority hierarchical rules.

## 3. Tool-Readable Surface Set (Requirement: 8 docs)
1. README (Entry point, Read-Interpret-Propose order)
2. CURRENT_MODE (Tool-readable adapter, manual-triggered)
3. BOUNDARY_RULES (No mutation, No automation, No broad scan)
4. AUTHORITY_LEVELS (User > Baseline > Candidate > Tool Output)
5. SPACE_INDEX (Material Activation routes linkage)
6. INTERPRETATION_GUIDE (Line/Axis/Camera/Lens usage)
7. MISSION_PACKET_TEMPLATE (Bounded task input structure)
8. RETURN_RECOVERY_RULES (Judgment Card, Recovery classification)

## 4. Key Artifacts
- `SURFACE_READ_ORDER_V0`: Hierarchical entry instruction.
- `SURFACE_TO_ACTIVATION_LINKS_V0`: Linking surface rules to Activation Map.

## 5. Constraints
- **Not a Controller.**
- No implementation, No automation, No file modification.
- Keep focus on "Read-Interpret-Propose" workflow.
- Log non-blocking issues.

## 6. Next Handoff
Prepare `SESSION_4_HANDOFF.md` for Context Bundle Template session.
