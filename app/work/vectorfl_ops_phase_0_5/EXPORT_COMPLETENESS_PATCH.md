# PIPELINE_EXPORT_COMPLETENESS_PATCH_V0

Adds structured local exports for every Phase 0.5 request.

Run:
python3 tools/structured_export.py

Outputs:
- exports/structured/request_XXX_*_structured_export.md
- exports/structured/request_XXX_*_structured_export.json
- receipts/pipeline_export_completeness_patch_receipt.md
- exports/pipeline_export_completeness_index.md

Boundary:
- local SQLite read/export only
- no external execution
- no authority mutation
- no promotion
- not Phase 1 implementation
