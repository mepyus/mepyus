import re
from typing import List, Dict, Optional

# Updated sample content from youtube_exam.md
YOUTUBE_EXAM_CONTENT = """최승준 참 또 하나 흥미로운 게 있었는데, 37수이 건물이 됐더라고요. AlphaGo의 그 놀라운 수라고. 인간인 이세돌 9단의 놀라운 수가 몇 수였죠? 78수였네요. 78수고 AlphaGo의 37수인데, 그 37수의 이름을 따라서 저 Google DeepMind 신사옥이 생기나 봅니다. 여름부터 입주를 한다고 하는데요.

06:40 이진원 이건 두 번째 대국이었죠.

06:54 노정석 두 번째 대국의 37수일 거예요. 아마 사람들이 다 그 해설자들이 “어, 저기는 왜 왔지”라고 하면서, 인간이라면 절대 못 둘 수였는데, 나중에

06:52 이진원 실수한 것 같다라는 얘기도 많이 했었고.

2016년 AlphaGo 대국 현장 이야기 06:54


06:58 노정석 저희가 2016년, 10년 전을 반추해 보면 저희 TensorFlow가 나오고 막 이런 거 할 때가 2015년 정도였던. TensorFlow가 나오긴 했지만 그게 뭔지 세상이 전혀 알지 못하던 때였고, 그때 막 사람들이 딥러닝이란 무엇인가, NVIDIA 키노트 보면서 softmax는 어떻고, 그다음 MNIST, 그다음에 MNIST 끝나고 나면 CNN 이런 거를 가장 기초적인 것들을 돌려보던 그런 때였기 때문에 AI라는 표현을 많이 안 썼죠. 그때는 머신러닝, 딥러닝이라는 표현을 많이 썼는데 그거에 대한 기대가 그렇게 높지 않던 때였어요.

근데 사실 2016년에 AlphaGo가 와서, AlphaGo 시작할 때만 하더라도 저도 그 행사장에도 있었는데 그리고 그 전에 전야제라고 그러죠. 갈라쇼를 할 때 가서 Eric Schmidt랑 유명한 사람들 다 모여 있고 이세돌과 Eric Schmidt와 초 VIP들이 맨 가운데 앞 테이블에 앉고 유명한 사람들이 다 뒤로 앉았었는데 그때만 하더라도 이세돌 자신만만했었어요. 인간이 이긴다. 네, 그런데 거꾸로 저는 야, 구글에서 저렇게 별들이 다 넘어올 정도면 얘들이 뭔가 확신을 갖고 넘어왔지 그냥 오진 않았을 거다라고 해서 AlphaGo가 압도적으로 이길 거다라고 저는 배팅을 했었고 그때 한참 내기를 했던 기억이 납니다. 근데 저희 1국이 끝나고 났을 때 사실 모두가 다 충격에 휩싸이긴 했죠. 압도적이었어요.

08:26 최승N라이브로 다 보셨죠? 두 분 다.

08:28 이진원 네, 봤습니다.

08:33 노정석 봤죠. 저도 바둑을 다 이해하지 못하기 때문에 그 수의 깊음이나 이런 거는 제가 이해는 못했습니다만 그 사람들, 해설해 주시는 해설자들의 탄식과 놀라움과 좌절감들을 보면서 아, 이거 엄청난 거구나라는 생각을 했었죠.

08:51 이진원 또 굉장히 재미있었던 거는 그때 유튜브 포함해서 다양한 채널에서 해설, 소위 프로바둑 기사들이 해설을 했는데 의견이 굉장히 많이 갈렸었어요. 어떤 한 수 한 수 나올 때마다 그거를 보는 것도 재미있었던 기억이 있습니다.

09:03 최승준 그 당시에는 정책망이 뭐다 가치망이 뭐다 그런 용어들을 저는 잘 몰랐던 때라 가지고 이게 무슨 소리인가 블로그 보기도 하고, 기억이 나네요.

09:13 노정석 AlphaGo 대국이 끝나고 나서 웬만한 교수님이나 유명하신 분들이 다 그게 어떻게 만들어졌는지 해설가가 되셔서 발표 자료들, 유튜브 녹화들 굉장히 많이 나왔던 생각이 납니다.
"""

class ExperimentalSegmenterV2:
    def __init__(self, raw_text: str):
        self.raw_text = raw_text
        self.normalized_text = self._normalize_text(raw_text)

    def _normalize_text(self, text: str) -> str:
        # Standard normalization: replace different newlines with '\n'
        # Do not strip here to preserve paragraph breaks
        return text.replace("\r\n", "\n").replace("\r", "\n")

    def _initial_segmentation_pass(self, text: str) -> List[Dict]:
        # Marker exclusion rule: filter lines that are markers, but include them in output for merge_history
        marker_patterns = re.compile(r"^(?:\d{4}년 AlphaGo|Demis Hassabis KAIST Talk|Andrej Karpathy의 Autoresearch|\S+\s+\d{2}:\d{2})$", re.IGNORECASE)
        
        # Split by one or more blank lines, keeping the separators might be an issue.
        # Splitting by \n\s*\n+ means that the resulting paragraphs might not perfectly align with original raw_text spans if newlines are altered.
        paragraphs = re.split(r'\n\s*\n+', text)
        
        initial_candidates = []
        for p_index, p in enumerate(paragraphs):
            p_stripped = p.strip() # Stripping whitespace here can alter original alignment
            if not p_stripped:
                continue

            is_marker = bool(re.search(marker_patterns, p_stripped))
            
            # Extract time if present at the beginning of the stripped paragraph
            time_match = re.match(r"^(\d{2}:\d{2})\s", p_stripped)
            original_time_label = f"t_initial_{p_index+1:02d}"
            if time_match:
                original_time_label += f" | {time_match.group(1)}"
            
            initial_candidates.append({
                "temp_id": f"c_{p_index+1:02d}", # Candidate ID
                "text": p_stripped,
                "is_marker": is_marker,
                "original_time_label": original_time_label,
                "merge_history": [],
                "excluded_as_marker": False,
                "merge_reason": "",
                # Store original paragraph for potential index mapping later if needed, though strip() alters it.
                # For now, relying on string matching which is problematic.
            })
        
        return initial_candidates

    def _merge_pass(self, candidates: List[Dict]) -> List[Dict]:
        final_dusts = []
        
        i = 0
        while i < len(candidates):
            current_candidate = candidates[i]
            
            if current_candidate["is_marker"]:
                current_candidate["excluded_as_marker"] = True
                current_candidate["merge_reason"] = "marker exclusion rule"
                i += 1
                continue
            
            # Heuristic for question and short response
            is_question = "?" in current_candidate["text"] and len(current_candidate["text"].split()) <= 15
            
            if is_question and i + 1 < len(candidates):
                next_candidate = candidates[i+1]
                # Check for short, affirmative responses
                is_short_response_to_question = (
                    len(next_candidate["text"].split()) <= 5 and
                    any(word in next_candidate["text"] for word in ["네", "맞아요", "그렇죠", "봤습니다", "봤죠", "있었습니다"]) # Added more common Korean affirmative words
                )
                if is_short_response_to_question:
                    # Merge question and response
                    merged_text = f"{current_candidate['text']}\n{next_candidate['text']}"
                    merged_history = current_candidate["merge_history"] + [f"absorbed {next_candidate['temp_id']}"]
                    merge_reason = "forced merge: 짧은 질문 + 응답 쌍"
                    
                    final_dusts.append({
                        "temp_id": current_candidate["temp_id"],
                        "text": merged_text,
                        "is_marker": False,
                        "original_time_label": current_candidate["original_time_label"],
                        "merge_history": merged_history,
                        "excluded_as_marker": False,
                        "merge_reason": merge_reason
                    })
                    i += 2 # Skip both current and next candidate
                    continue

            # Heuristic for merging short utterances into the previous dust
            # Check if current candidate is short and not a question, and if there's a previous final dust to merge into
            if len(current_candidate["text"].split()) <= 8 and not is_question and len(final_dusts) > 0:
                prev_final_dust = final_dusts[-1] 
                final_dusts[-1]["text"] = f"{prev_final_dust['text']}\n{current_candidate['text']}"
                final_dusts[-1]["merge_history"].append(f"absorbed {current_candidate['temp_id']} (짧은 발화)")
                final_dusts[-1]["merge_reason"] = "forced merge: 짧은 발화 흡수"
            else:
                # Otherwise, add as a new dust
                final_dusts.append(current_candidate)
            i += 1
        
        return final_dusts

    def segment_and_assign_values(self) -> List[Dict]:
        candidate_dusts = self._initial_segmentation_pass(self.normalized_text)
        final_processed_candidates = self._merge_pass(candidate_dusts)
        
        segmented_output = []
        excluded_markers_output = []

        final_dusts_for_output = [d for d in final_processed_candidates if not d["excluded_as_marker"]]
        excluded_markers_output = [d for d in final_processed_candidates if d["excluded_as_marker"]]

        for i, dust_info in enumerate(final_dusts_for_output):
            dust_id = f"dust_{i+1:02d}"
            
            # clean_text is the text to be displayed and used for source_range lookup
            # It's derived from the potentially merged and stripped candidate text
            clean_text = dust_info['text'] 
            
            time_label_for_output = dust_info['original_time_label'] # This will be t_initial_xx or t_initial_xx | HH:MM
            
            # --- FIX FOR SOURCE_RANGE ---
            # Use re.search for more robust matching of clean_text within raw_text.
            # re.escape ensures special regex characters in clean_text are treated literally.
            # re.DOTALL allows '.' to match newline characters, handling multi-line matches across different newline styles.
            # Search in self.raw_text to preserve original formatting context for matching.
            source_range = "TBD_ERROR" # Default in case of error
            try:
                # Escape clean_text to ensure it's treated as a literal string in regex
                escaped_clean_text = re.escape(clean_text)
                
                # Use re.search with DOTALL to allow '.' to match newlines, and potentially handle variations in newlines (\n vs \n\n)
                # Searching within self.raw_text is crucial for accurate span calculation.
                match = re.search(escaped_clean_text, self.raw_text, re.DOTALL)
                
                if match:
                    start_index = match.start()
                    end_index = match.end()
                    source_range = f"{start_index}~{end_index}"
                else:
                    # Fallback if re.search still fails. This might happen if clean_text differs significantly from raw_text.
                    source_range = "TBD_ERROR"
                    # Log or print a warning if a match is not found, for debugging.
                    # print(f"Warning: Could not find source range for text: {clean_text[:100]}...") 
            except re.error as e:
                # Handle potential regex compilation errors
                source_range = "TBD_ERROR_REGEX"
                print(f"Regex error searching for text: {clean_text[:100]}... Error: {e}")
            # --- END FIX ---

            # Re-extract time and clean text if time label exists at the start
            final_time_match = re.match(r"^(\d{2}:\d{2})\s", clean_text)
            if final_time_match:
                # Update time_label_for_output to the more specific tXX | HH:MM format
                time_label_for_output = f"t{i+1:02d} | {final_time_match.group(1)}"
                # Remove the time prefix from clean_text for display
                clean_text = re.sub(r"^\d{2}:\d{2}\s", "", clean_text).strip()
            else:
                # If no time prefix found in the clean_text, use sequential tXX
                time_label_for_output = f"t{i+1:02d}"

            # Ensure 'merge_history' is always a list
            if 'merge_history' not in dust_info:
                dust_info['merge_history'] = []
            
            # Ensure 'merge_reason' is handled correctly, it can be empty
            merge_reason_str = dust_info.get('merge_reason', '')

            # Combine merge reasons and merge_reason for 'why_one_unit'
            why_one_unit_reasons = dust_info["merge_history"] + ([merge_reason_str] if merge_reason_str else [])
            if not why_one_unit_reasons: # Fallback if empty
                why_one_unit_reasons = ["병합/필터링 규칙을 통과하여 독립적인 의미 단위로 인정됨"]

            segmented_output.append(
                {
                    "dust_id": dust_id,
                    "source_range": source_range,
                    "text": clean_text, # Use the potentially time-prefixed clean_text
                    "unit_type": "논리 문단", # Placeholder, to be refined
                    "D": 0.50, "I": 0.50, "S": 0.50, # Placeholders, to be refined
                    "scene": "unknown", "flow": "unknown", # Placeholders, to be refined
                    "time": time_label_for_output, # Updated time label
                    "why_one_unit": why_one_unit_reasons,
                    "why_this_value": ["연습을 위한 초기 플레이스홀더 값"], # Placeholder, to be refined
                    "merge_history": dust_info["merge_history"], 
                    "confidence": "중간", # Placeholder, to be refined
                }
            )
        return segmented_output, excluded_markers_output

    def format_output(self, segmented_data: List[Dict], excluded_markers: List[Dict]) -> str:
        output_parts = []
        for data in segmented_data:
            formatted_str_lines = [
                f"[{data['dust_id']}]",
                f"source_range: {data['source_range']}",
                f"text: {data['text']}",
                f"unit_type: {data['unit_type']}",
                f"D: {data['D']:.2f}",
                f"I: {data['I']:.2f}",
                f"S: {data['S']:.2f}",
                f"scene: {data['scene']}",
                f"flow: {data['flow']}",
                f"time: {data['time']}",
                "why_one_unit:"
            ]
            formatted_str_lines.extend([f"- {reason}" for reason in data['why_one_unit']])
            
            formatted_str_lines.append("why_this_value:")
            formatted_str_lines.extend([f"- {reason}" for reason in data['why_this_value']])
            
            if data['merge_history']:
                formatted_str_lines.append("merge_history:")
                formatted_str_lines.extend([f"- {item}" for item in data['merge_history']])
            
            formatted_str_lines.append(f"confidence: {data['confidence']}")
            
            output_parts.append("\n".join(formatted_str_lines))
        
        if excluded_markers:
            output_parts.append("\n## Excluded Markers\n")
            for i, marker_data in enumerate(excluded_markers):
                output_parts.append(f"[excluded_marker_{i+1:02d}]")
                output_parts.append(f"source_range: {marker_data['source_range']}")
                output_parts.append(f"text: {marker_data['text']}")
                output_parts.append(f"reason: {marker_data['merge_reason']}")
            output_parts.append("")

        return "\n\n".join(output_parts)

if __name__ == "__main__":
    # Re-read youtube_exam.md content as it might have been truncated before
    try:
        # Using the provided YOUTUBE_EXAM_CONTENT directly for simplicity,
        # assuming it's up-to-date and representative.
        # In a real scenario, reading from 'youtube_exam.md' file would be preferred.
        youtube_content = YOUTUBE_EXAM_CONTENT 
        # If reading from file is preferred, uncomment below:
        # with open("youtube_exam.md", "r", encoding='utf-8') as f:
        #     youtube_content = f.read()
    except FileNotFoundError:
        print("Error: youtube_exam.md not found or content not loaded. Please ensure the file exists or content is available.")
        exit(1)

    segmenter_v2 = ExperimentalSegmenterV2(youtube_content)
    final_dusts, excluded_markers = segmenter_v2.segment_and_assign_values()
    
    # Calculate source_range for excluded markers using the same robust search method
    for marker in excluded_markers:
        try:
            escaped_marker_text = re.escape(marker['text'])
            match = re.search(escaped_marker_text, segmenter_v2.raw_text, re.DOTALL)
            if match:
                start_index = match.start()
                end_index = match.end()
                marker['source_range'] = f"{start_index}~{end_index}"
            else:
                marker['source_range'] = "TBD_ERROR_MARKER"
        except re.error as e:
            marker['source_range'] = "TBD_ERROR_REGEX_MARKER"
            print(f"Regex error searching for marker text: {marker['text'][:100]}... Error: {e}")
            

    print(segmenter_v2.format_output(final_dusts, excluded_markers))