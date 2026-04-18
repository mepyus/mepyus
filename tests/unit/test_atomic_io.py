import json
import tempfile
import unittest
from pathlib import Path

from app.core.registry.atomic_io import atomic_write_json, atomic_write_text, make_idempotency_key


class AtomicIoTest(unittest.TestCase):
    def test_atomic_write_json_replaces_file_with_valid_payload(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "registry.json"

            atomic_write_json(path, {"entries": [{"doc_id": "doc_1"}]})

            payload = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(payload["entries"][0]["doc_id"], "doc_1")

    def test_atomic_write_text_replaces_file_contents(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "board.md"

            atomic_write_text(path, "alpha\n")
            atomic_write_text(path, "beta\n")

            self.assertEqual(path.read_text(encoding="utf-8"), "beta\n")

    def test_make_idempotency_key_is_stable_for_same_parts(self) -> None:
        left = make_idempotency_key("doc.md", "ingest_then_execute", "hash")
        right = make_idempotency_key("doc.md", "ingest_then_execute", "hash")

        self.assertEqual(left, right)
        self.assertEqual(len(left), 16)


if __name__ == "__main__":
    unittest.main()
