# PIPELINE_BASELINE_REPLAY_VALIDATOR_V0

Local-only replay/integrity validator for the Phase 0.5 candidate baseline snapshot.

Run:
python3 tools/baseline_replay_validator.py

Modes:
- `python3 tools/baseline_replay_validator.py --mode frozen`
  - strict snapshot byte-identity replay
  - default mode for backward compatibility
  - checksum mismatch is FAIL
- `python3 tools/baseline_replay_validator.py --mode live-safety`
  - current DB safety invariant check only
  - does not compare file checksums
  - does not claim baseline replay PASS

Checks:
- baseline manifest exists
- checksum table exists
- all manifest files still exist
- current SHA256 matches snapshot SHA256
- DB safety invariants remain valid

Live-safety checks:
- `fail_events == 0`
- `authority_mutations == 0`
- `non_hold_reviews == 0`

Important:
- frozen replay PASS means the selected snapshot still matches byte-for-byte.
- live-safety PASS means the current live local loop still satisfies safety invariants.
- live-safety PASS is not baseline replay PASS.
- neither mode creates a new snapshot.

Boundary:
- evidence replay only
- no external execution
- no authority mutation
- no promotion
- not Phase 1 implementation
- not v1 snapshot creation
