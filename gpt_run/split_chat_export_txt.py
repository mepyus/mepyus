#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
split_chat_marked_txt.py

규칙
- 사용자 턴 시작: []
- 어시스턴트 턴 시작: [[A]]

예시
[] 오늘은 테스트 먼저
[[A]] 좋습니다. a.txt부터 보겠습니다.
[] 오케이 나눠지긴 한다
[[A]] 그럼 이제 경계만 더 단단히 잡으면 됩니다.

실행 예시
python3 split_chat_marked_txt.py --input ./a.txt --output-dir ./out_chat_split --max-chars 1200
"""

from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import dataclass, asdict
from typing import List, Optional, Tuple


USER_MARKER_RE = re.compile(r"^\s*\[\](.*)$")
ASSISTANT_MARKER_RE = re.compile(r"^\s*\[\[A\]\](.*)$")


@dataclass
class Turn:
    turn_index: int
    speaker: str
    text: str


@dataclass
class Chunk:
    chunk_id: str
    turn_index: int
    speaker: str
    chunk_index_in_turn: int
    text: str
    char_count: int


def detect_marker(line: str) -> Optional[Tuple[str, str]]:
    """
    줄 맨 앞의 [] / [[A]] 마커를 인식한다.
    반환:
      ("user", 나머지텍스트) or ("assistant", 나머지텍스트)
    """
    m = USER_MARKER_RE.match(line)
    if m:
        return "user", m.group(1).lstrip()

    m = ASSISTANT_MARKER_RE.match(line)
    if m:
        return "assistant", m.group(1).lstrip()

    return None


def parse_turns(raw_text: str) -> List[Turn]:
    """
    raw txt를 턴 단위로 분리한다.

    규칙:
    - [] 가 나오면 user 새 턴 시작
    - [[A]] 가 나오면 assistant 새 턴 시작
    - 마커 없는 줄은 현재 화자 턴에 이어붙임
    - 파일 첫머리에 마커 없는 일반 텍스트가 나오면 user로 간주
    """
    lines = raw_text.splitlines()
    turns: List[Turn] = []

    current_speaker: Optional[str] = None
    current_lines: List[str] = []

    def flush() -> None:
        nonlocal current_speaker, current_lines, turns
        if current_speaker is None:
            current_lines = []
            return

        text = "\n".join(current_lines).strip()
        if text:
            turns.append(
                Turn(
                    turn_index=len(turns) + 1,
                    speaker=current_speaker,
                    text=text,
                )
            )
        current_lines = []

    for line in lines:
        detected = detect_marker(line)
        if detected:
            speaker, remainder = detected
            flush()
            current_speaker = speaker
            current_lines = [remainder] if remainder else []
            continue

        # 빈 줄
        if not line.strip():
            if current_speaker is None:
                continue
            current_lines.append("")
            continue

        # 아직 speaker가 없는데 일반 텍스트가 나오면 user로 시작
        if current_speaker is None:
            current_speaker = "user"

        current_lines.append(line.rstrip())

    flush()
    return turns


def split_paragraphs(text: str) -> List[str]:
    parts = re.split(r"\n\s*\n", text.strip())
    return [p.strip() for p in parts if p.strip()]


def split_sentences_safe(text: str) -> List[str]:
    text = text.strip()
    if not text:
        return []

    # 한국어/영어 혼합 대응용 느슨한 분리
    parts = re.split(r"(?<=[\.\!\?。！？])\s+|\n+", text)
    return [p.strip() for p in parts if p.strip()]


def split_long_text(text: str, max_chars: int) -> List[str]:
    if len(text) <= max_chars:
        return [text]

    chunks: List[str] = []
    paragraphs = split_paragraphs(text)
    current = ""

    def push_current() -> None:
        nonlocal current
        if current.strip():
            chunks.append(current.strip())
        current = ""

    for para in paragraphs:
        if len(para) <= max_chars:
            candidate = f"{current}\n\n{para}".strip() if current else para
            if len(candidate) <= max_chars:
                current = candidate
            else:
                push_current()
                current = para
            continue

        # 문단이 너무 길면 문장 기준 분해
        sentences = split_sentences_safe(para)
        if not sentences:
            sentences = [para]

        for sent in sentences:
            if len(sent) <= max_chars:
                candidate = f"{current}\n\n{sent}".strip() if current else sent
                if len(candidate) <= max_chars:
                    current = candidate
                else:
                    push_current()
                    current = sent
                continue

            # 문장도 너무 길면 강제 절단
            if current:
                push_current()

            start = 0
            while start < len(sent):
                piece = sent[start:start + max_chars].strip()
                if piece:
                    chunks.append(piece)
                start += max_chars

    push_current()
    return chunks


def build_chunks(turns: List[Turn], max_chars: int) -> List[Chunk]:
    chunks: List[Chunk] = []
    global_idx = 1

    for turn in turns:
        pieces = split_long_text(turn.text, max_chars=max_chars)
        for i, piece in enumerate(pieces, start=1):
            chunks.append(
                Chunk(
                    chunk_id=f"chunk_{global_idx:04d}",
                    turn_index=turn.turn_index,
                    speaker=turn.speaker,
                    chunk_index_in_turn=i,
                    text=piece,
                    char_count=len(piece),
                )
            )
            global_idx += 1

    return chunks


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def save_outputs(chunks: List[Chunk], output_dir: str) -> None:
    ensure_dir(output_dir)
    chunks_dir = os.path.join(output_dir, "chunks")
    ensure_dir(chunks_dir)

    manifest = []

    for chunk in chunks:
        filename = (
            f"{chunk.chunk_id}_{chunk.speaker}"
            f"_turn{chunk.turn_index:04d}_part{chunk.chunk_index_in_turn:02d}.txt"
        )
        file_path = os.path.join(chunks_dir, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"[speaker] {chunk.speaker}\n")
            f.write(f"[turn_index] {chunk.turn_index}\n")
            f.write(f"[chunk_index_in_turn] {chunk.chunk_index_in_turn}\n")
            f.write(f"[char_count] {chunk.char_count}\n\n")
            f.write(chunk.text.strip())
            f.write("\n")

        item = asdict(chunk)
        item["file_name"] = filename
        manifest.append(item)

    manifest_path = os.path.join(output_dir, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    jsonl_path = os.path.join(output_dir, "chunks.jsonl")
    with open(jsonl_path, "w", encoding="utf-8") as f:
        for item in manifest:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"[OK] chunk_count={len(chunks)}")
    print(f"[OK] output_dir={output_dir}")
    print(f"[OK] manifest={manifest_path}")
    print(f"[OK] jsonl={jsonl_path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="입력 txt 파일 경로")
    parser.add_argument("--output-dir", required=True, help="출력 디렉토리")
    parser.add_argument("--max-chars", type=int, default=1200, help="청크 최대 길이")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        raw_text = f.read()

    turns = parse_turns(raw_text)
    if not turns:
        raise RuntimeError("턴을 하나도 찾지 못했습니다. 입력 형식을 확인하세요.")

    chunks = build_chunks(turns, max_chars=args.max_chars)
    save_outputs(chunks, output_dir=args.output_dir)


if __name__ == "__main__":
    main()