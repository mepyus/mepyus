from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Dict, List
import json


BASE_DIR = Path(__file__).resolve().parent
DICT_DIR = BASE_DIR / "dictionaries"


def _load_json(name: str):
    with (DICT_DIR / name).open(encoding="utf-8") as handle:
        return json.load(handle)


@lru_cache(maxsize=1)
def discourse_stopwords() -> List[str]:
    return list(_load_json("discourse_stopwords_ko.json"))


@lru_cache(maxsize=1)
def weak_generic_nouns() -> List[str]:
    return list(_load_json("weak_generic_nouns_ko.json"))


@lru_cache(maxsize=1)
def particle_suffixes() -> List[str]:
    values = list(_load_json("particle_suffixes_ko.json"))
    return sorted(values, key=len, reverse=True)


@lru_cache(maxsize=1)
def ending_suffixes() -> List[str]:
    values = list(_load_json("ending_suffixes_ko.json"))
    return sorted(values, key=len, reverse=True)


@lru_cache(maxsize=1)
def alias_entries() -> List[Dict[str, object]]:
    return list(_load_json("alias_dictionary.json"))


@lru_cache(maxsize=1)
def alias_lookup() -> Dict[str, Dict[str, object]]:
    rows: Dict[str, Dict[str, object]] = {}
    for entry in alias_entries():
        for alias in entry.get("aliases", []):
            rows[str(alias).strip().lower()] = entry
    return rows


@lru_cache(maxsize=1)
def anchor_type_lookup() -> Dict[str, str]:
    return dict(_load_json("anchor_type_dictionary.json"))


@lru_cache(maxsize=1)
def acronym_whitelist() -> List[str]:
    return list(_load_json("acronym_whitelist.json"))

