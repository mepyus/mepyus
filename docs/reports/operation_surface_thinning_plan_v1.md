# operation_surface_thinning_plan_v1

## 1. Current Problem
- latest board still carries copied output lists and recent event summaries
- latest commands still behave like a mini content surface rather than a pointer surface
- per-run artifacts already exist, so latest does not need to duplicate them

## 2. Thinning Direction
- move rich detail to per-run board / per-run commands
- keep latest board / latest commands as pointer-first
- add provenance compacted pointer where available

## 3. Expected Result
- latest surface becomes fast to scan
- per-run surface remains the source of detailed run evidence
- long-horizon readability improves without deleting trace detail

## 4. Patch Scope
- [scripts/process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py)
- [runtime/views/operation_board_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/operation_board_latest.md)
- [runtime/commands/structured_doc_routing_commands_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/commands/structured_doc_routing_commands_v1.md)

## 5. Guardrail
- do not thin per-run artifacts
- do not hide receipt or provenance pointers
- do not break latest -> per-run navigability
