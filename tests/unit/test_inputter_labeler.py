import unittest

from app.runtime.inputter import build_dust_inputs_for_material
from app.runtime.labeler import label_dust_inputs


class InputterLabelerTest(unittest.TestCase):
    def test_text_material_is_split_into_sentence_level_dust_and_labeled(self) -> None:
        material = {
            "material_id": "mat_demo",
            "source_type": "memo",
            "source_ref": "memo-demo",
            "raw_payload": "파서를 실행했다. 에러가 났다. 조건을 완화했다.",
            "created_at": "2026-03-17T00:00:00+00:00",
        }

        dust_inputs = build_dust_inputs_for_material(material)
        labeled = label_dust_inputs(dust_inputs)

        self.assertEqual(len(dust_inputs), 3)
        self.assertEqual([row.text for row in dust_inputs], [
            "파서를 실행했다.",
            "에러가 났다.",
            "조건을 완화했다.",
        ])
        self.assertEqual(len(labeled), 3)
        self.assertEqual(labeled[0].flow, "run")
        self.assertEqual(labeled[1].flow, "break")
        self.assertEqual(labeled[2].flow, "fix")
        self.assertTrue(all(row.scene in {"review", "spec", "evidence", "impl", "unknown"} for row in labeled))

    def test_code_material_is_split_by_function(self) -> None:
        material = {
            "material_id": "mat_code",
            "source_type": "code",
            "source_ref": "demo.py",
            "raw_payload": "def alpha():\n    return 1\n\ndef beta():\n    return 2\n",
            "created_at": "2026-03-17T00:00:00+00:00",
        }

        dust_inputs = build_dust_inputs_for_material(material)
        labeled = label_dust_inputs(dust_inputs)

        self.assertEqual(len(dust_inputs), 2)
        self.assertEqual(labeled[0].scene, "impl")
        self.assertEqual(labeled[1].scene, "impl")
        anchor_values = [anchor.value for anchor in labeled[0].anchors]
        self.assertIn("alpha", anchor_values)
        self.assertEqual(labeled[0].flow, "run")

    def test_review_like_text_defaults_flow_to_compare_instead_of_unknown(self) -> None:
        material = {
            "material_id": "mat_review",
            "source_type": "note",
            "source_ref": "memo-review",
            "raw_payload": "Observe whether engine-self and observer materials stay distinct before any point-first pull.",
            "created_at": "2026-03-17T00:00:00+00:00",
        }

        dust_inputs = build_dust_inputs_for_material(material)
        labeled = label_dust_inputs(dust_inputs)

        self.assertEqual(len(labeled), 1)
        self.assertEqual(labeled[0].scene, "review")
        self.assertEqual(labeled[0].flow, "compare")


if __name__ == "__main__":
    unittest.main()
