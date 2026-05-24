# PIPELINE_TRANSITION_TABLE_HARDENING_V0

Local-only validator for Phase 0.5 state/depth/status vocabulary and transition evidence.

Run:
python3 tests/transition_table_validator.py

Guarantees checked:
- request state enum is explicit
- depth enum is explicit
- execution status enum is explicit
- guardrail result vocabulary is normalized
- promotion remains HOLD
- authority remains NO
- MATURED_OR_HELD has review + maturation
- open residue states are explained only by G1/G6/G8 probe events

Boundary:
- no external execution
- no authority mutation
- no promotion
- not Phase 1 implementation
