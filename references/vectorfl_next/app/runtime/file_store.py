import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


class JsonlEventStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.touch(exist_ok=True)

    def append(self, record: Dict[str, Any]) -> None:
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=True) + "\n")

    def read_all(self) -> List[Dict[str, Any]]:
        rows: List[Dict[str, Any]] = []
        with self.path.open("r", encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if not line:
                    continue
                rows.append(json.loads(line))
        return rows


class JsonDirectoryStore:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)

    def put(self, object_id: str, record: Dict[str, Any]) -> Path:
        path = self.root / f"{object_id}.json"
        with path.open("w", encoding="utf-8") as handle:
            json.dump(record, handle, ensure_ascii=True, indent=2, sort_keys=True)
            handle.write("\n")
        return path

    def get(self, object_id: str) -> Optional[Dict[str, Any]]:
        path = self.root / f"{object_id}.json"
        if not path.exists():
            return None
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)

    def list_ids(self) -> Iterable[str]:
        for path in sorted(self.root.glob("*.json")):
            yield path.stem

    def read_all(self) -> List[Dict[str, Any]]:
        rows: List[Dict[str, Any]] = []
        for object_id in self.list_ids():
            record = self.get(object_id)
            if record is not None:
                rows.append(record)
        return rows
