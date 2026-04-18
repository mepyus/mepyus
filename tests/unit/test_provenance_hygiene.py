import unittest

from app.core.registry.provenance_hygiene import build_compaction_preview


class ProvenanceHygieneTest(unittest.TestCase):
    def test_build_compaction_preview_classifies_safe_and_manual_groups(self) -> None:
        links = [
            {
                "source_doc_ref": "doc_a.md",
                "derived_target_ref": "runtime/manifests/structured_internal_docs_registry_v1.json",
                "ticket_ref": "",
                "relationship": "registered_in_structured_doc_registry",
                "run_id": "run_1",
                "idempotency_key": "idem_a",
            },
            {
                "source_doc_ref": "doc_a.md",
                "derived_target_ref": "runtime/manifests/structured_internal_docs_registry_v1.json",
                "ticket_ref": "",
                "relationship": "registered_in_structured_doc_registry",
                "run_id": "run_2",
                "idempotency_key": "idem_a",
            },
            {
                "source_doc_ref": "doc_a.md",
                "derived_target_ref": "generated/out_run_1.json",
                "ticket_ref": "tkt_1",
                "relationship": "generated_by_structured_doc_routing",
                "run_id": "run_1",
                "idempotency_key": "idem_a",
            },
            {
                "source_doc_ref": "doc_a.md",
                "derived_target_ref": "generated/out_run_2.json",
                "ticket_ref": "tkt_1",
                "relationship": "generated_by_structured_doc_routing",
                "run_id": "run_2",
                "idempotency_key": "idem_a",
            },
            {
                "source_doc_ref": "doc_a.md",
                "derived_target_ref": "generated/out_run_3.json",
                "ticket_ref": "tkt_1",
                "relationship": "generated_by_structured_doc_routing",
                "run_id": "run_3",
                "idempotency_key": "idem_a",
            },
            {
                "source_doc_ref": "doc_a.md",
                "derived_target_ref": "generated/out_run_4.json",
                "ticket_ref": "tkt_1",
                "relationship": "generated_by_structured_doc_routing",
                "run_id": "run_4",
                "idempotency_key": "idem_a",
            },
            {
                "source_doc_ref": "doc_a.md",
                "derived_target_ref": "generated/out_run_5.json",
                "ticket_ref": "tkt_1",
                "relationship": "generated_by_structured_doc_routing",
                "run_id": "run_5",
                "idempotency_key": "idem_a",
            },
            {
                "source_doc_ref": "doc_a.md",
                "derived_target_ref": "generated/out_run_6.json",
                "ticket_ref": "tkt_1",
                "relationship": "generated_by_structured_doc_routing",
                "run_id": "run_6",
                "idempotency_key": "idem_a",
            },
            {
                "source_doc_ref": "doc_a.md",
                "derived_target_ref": "generated/out_run_7.json",
                "ticket_ref": "tkt_1",
                "relationship": "generated_by_structured_doc_routing",
                "run_id": "run_7",
                "idempotency_key": "idem_a",
            },
        ]

        preview = build_compaction_preview(links)

        self.assertEqual(preview["scan_summary"]["total_rows"], 9)
        self.assertEqual(preview["candidate_summary"]["safe_group_count"], 1)
        self.assertEqual(preview["candidate_summary"]["manual_review_group_count"], 1)
        classifications = preview["candidate_summary"]["classification_counts"]
        self.assertEqual(classifications["same_idempotency_context_repeated_append"], 1)
        self.assertEqual(classifications["same_document_reingest_accumulation"], 1)


if __name__ == "__main__":
    unittest.main()
