import unittest

from app.work.input_layer.axis_input_parser import parse_axis_material_drafts


class AxisInputParserTest(unittest.TestCase):
    def test_parser_splits_labelled_blocks_and_keeps_axis_hints(self) -> None:
        drafts = parse_axis_material_drafts(
            """
문제:
겉으로 많이 바뀌어 보여도 실제 구조는 거의 안 바뀌었을 수 있고,
겉보기 변화가 적어도 물리는 크게 흔들렸을 수 있다.

대응:
- semantic diff와 presentation diff 분리
- invariant change를 중심으로 비교
- quiet persistence 변화는 별도 확인

위험:
- node count 변화만 보고 scale effect를 과장
- wording 변화만 보고 law shift로 오독
- UI 변화와 runtime 변화를 혼동
""".strip()
        )

        self.assertEqual(len(drafts), 3)
        self.assertEqual(drafts[0].block_label, "문제")
        self.assertEqual(drafts[0].axes.direction, "divergent_tension")
        self.assertEqual(drafts[1].axes.direction, "corrective_flow")
        self.assertEqual(drafts[2].axes.direction, "divergent_tension")
        self.assertTrue(all(draft.connectivity_keys for draft in drafts))

    def test_parser_marks_quiet_and_time_hints(self) -> None:
        drafts = parse_axis_material_drafts(
            """
어떤 존재는 오랫동안 quiet하게 버틴다.

어떤 존재는 빠르게 나타나 사라진다.
""".strip()
        )

        self.assertEqual(len(drafts), 2)
        self.assertEqual(drafts[0].axes.stability, "stable")
        self.assertEqual(drafts[0].axes.time, "durational")
        self.assertEqual(drafts[0].axes.intensity, "low")
        self.assertEqual(drafts[1].axes.time, "rapid")

    def test_parser_splits_single_statement_into_condition_and_risk(self) -> None:
        drafts = parse_axis_material_drafts(
            "컨텍스트 엔지니어링은 구조적 안정성과 이해도가 바탕이 되지 않으면 ai에게 흔들릴 가능성이 높다"
        )

        self.assertEqual(len(drafts), 3)
        self.assertEqual(drafts[0].block_label, "condition")
        self.assertEqual(drafts[0].axes.direction, "structural_grounding")
        self.assertEqual(drafts[1].block_label, "basis")
        self.assertIn("바탕", drafts[1].source_text)
        self.assertEqual(drafts[2].block_label, "risk")
        self.assertEqual(drafts[2].axes.direction, "divergent_tension")
        self.assertEqual(drafts[2].axes.stability, "unstable")

    def test_parser_splits_long_paragraph_by_sentence_axis_shift(self) -> None:
        drafts = parse_axis_material_drafts(
            "어떤 존재는 빠르게 나타나 사라진다. 어떤 존재는 오랫동안 quiet하게 버틴다. 어떤 존재는 사라진 듯하다 다시 돌아온다."
        )

        self.assertEqual(len(drafts), 3)
        self.assertEqual(drafts[0].axes.time, "rapid")
        self.assertEqual(drafts[1].axes.time, "durational")
        self.assertEqual(drafts[1].axes.stability, "stable")
        self.assertEqual(drafts[2].axes.time, "reentry")


if __name__ == "__main__":
    unittest.main()
