import re
from typing import List, Dict, Optional, Tuple

# Sample content from youtube_exam.md
YOUTUBE_EXAM_CONTENT = """최승준 참 또 하나 흥미로운 게 있었는데, 37수이 건물이 됐더라고요. AlphaGo의 그 놀라운 수라고. 인간인 이세돌 9단의 놀라운 수가 몇 수였죠? 78수였네요. 78수고 AlphaGo의 37수인데, 그 37수의 이름을 따라서 저 Google DeepMind 신사옥이 생기나 봅니다. 여름부터 입주를 한다고 하는데요.

06:40 이진원 이건 두 번째 대국이었죠.

06:41 노정석 두 번째 대국의 37수일 거예요. 아마 사람들이 다 그 해설자들이 “어, 저기는 왜 왔지”라고 하면서, 인간이라면 절대 못 둘 수였는데, 나중에

06:52 이진원 실수한 것 같다라는 얘기도 많이 했었고.

2016년 AlphaGo 대국 현장 이야기 06:54


06:58 노정석 저희가 2016년, 10년 전을 반추해 보면 저희 TensorFlow가 나오고 막 이런 거 할 때가 2015년 정도였던. TensorFlow가 나오긴 했지만 그게 뭔지 세상이 전혀 알지 못하던 때였고, 그때 막 사람들이 딥러닝이란 무엇인가, NVIDIA 키노트 보면서 softmax는 어떻고, 그다음 MNIST, 그다음에 MNIST 끝나고 나면 CNN 이런 거를 가장 기초적인 것들을 돌려보던 그런 때였기 때문에 AI라는 표현을 많이 안 썼죠. 그때는 머신러닝, 딥러닝이라는 표현을 많이 썼는데 그거에 대한 기대가 그렇게 높지 않던 때였어요.

근데 사실 2016년에 AlphaGo가 와서, AlphaGo 시작할 때만 하더라도 저도 그 행사장에도 있었는데 그리고 그 전에 전야제라고 그러죠. 갈라쇼를 할 때 가서 Eric Schmidt랑 유명한 사람들 다 모여 있고 이세돌과 Eric Schmidt와 초 VIP들이 맨 가운데 앞 테이블에 앉고 유명한 사람들이 다 뒤로 앉았었는데 그때만 하더라도 이세돌 자신만만했었어요. 인간이 이긴다. 네, 그런데 거꾸로 저는 야, 구글에서 저렇게 별들이 다 넘어올 정도면 얘들이 뭔가 확신을 갖고 넘어왔지 그냥 오진 않았을 거다라고 해서 AlphaGo가 압도적으로 이길 거다라고 저는 배팅을 했었고 그때 한참 내기를 했던 기억이 납니다. 근데 저희 1국이 끝나고 났을 때 사실 모두가 다 충격에 휩싸이긴 했죠. 압도적이었어요.

08:26 최승준 라이브로 다 보셨죠? 두 분 다.

08:28 이진원 네, 봤습니다.

08:33 노정석 봤죠. 저도 바둑을 다 이해하지 못하기 때문에 그 수의 깊음이나 이런 거는 제가 이해는 못했습니다만 그 사람들, 해설해 주시는 해설자들의 탄식과 놀라움과 좌절감들을 보면서 아, 이거 엄청난 거구나라는 생각을 했었죠.

08:51 이진원 또 굉장히 재미있었던 거는 그때 유튜브 포함해서 다양한 채널에서 해설, 소위 프로바둑 기사들이 해설을 했는데 의견이 굉장히 많이 갈렸었어요. 어떤 한 수 한 수 나올 때마다 그거를 보는 것도 재미있었던 기억이 있습니다.

09:03 최승준 그 당시에는 정책망이 뭐다 가치망이 뭐다 그런 용어들을 저는 잘 몰랐던 때라 가지고 이게 무슨 소리인가 블로그 보기도 하고, 기억이 나네요.

09:13 노정석 AlphaGo 대국이 끝나고 나서 웬만한 교수님이나 유명하신 분들이 다 그게 어떻게 만들어졌는지 해설가가 되셔서 발표 자료들, 유튜브 녹화들 굉장히 많이 나왔던 생각이 납니다.


Demis Hassabis KAIST Talk youtube.com
09:32 최승준 어떻게 보면 한국이 그 덕을 좀 봤다고도 볼 수 있지 않을까요? 일찌감치 세게 맞아 가지고 당사자성을 가지고서 좀 보게 됐는데, 이게 아마 Demis Hassabis가 대국 끝나고서 KAIST에서 했던 강연 영상이에요. 그래서 여기에서 DQN 같은 거 보여주고 실제로 그게 어떤 맥락에 있는가 같은 것들을 짚었던 얘기들 같은 것들도 해주고 그런 것들을 조금 실감 나게 볼 수 있었던 2016년의 경험이었던 것 같습니다.

09:57 노정석 14년, 15년, 16년 이때 하면 사실 DQN만 하더라도 엄청난 첨단 기술이었고 그리고 OpenAI Gym에서 RL스러운 것들 조금씩 해보던 그런 때였던 것 같아요.

10:15 최승준 저도 그때 소회 같은 것들을 소셜미디어에 감정을 담아서 썼던 기억들이 나고요. 그래서 저희가 오늘 조금 역사를, 10년을 돌아보는 이야기를 하기 전에 최근에 이게 관련이 있다고 저는 느껴졌는데 Autoresearch가 핫하더라고요. Andrej Karpathy가 작년에는 vibe coding이라고 코딩으로 밈을 선점하더니, 올해는 Autoresearch로 뭐랄까 딱 이렇게 쥐어 잡은 느낌인데 어떻게 보셨나요?

Andrej Karpathy의 Autoresearch와 검증 가능한 신호의 반복 10:24


10:40 노정석 이거 Ralph loop랑 뭐가 다른 거예요?

10:46 최승준 Ralph loop죠. 하지만 작동하는 딱 도메인, 딱 영역에서 평가 가능한 validation, 그것만 한 거죠. 테스트까지 아니고 그냥 validation 점수만 가지고서 그거를 낮출 수 있는 쪽으로 온갖 아이디어를 내서 실험하고 실험하고 계속 그거를 할 수 있게 하는 그런 느낌이었죠.

11:07 노정석 컨셉으로는 RLVR하고 사실 비슷한 거죠. 그러나 레이어가 다른 거죠. RLVR을 학습 과정에서 어떤 그 verifiable한, 검증 가능한 신호를 줄 수만 있다면 그 도메인에서 학습을 계속할 수 있다라는 얘기를 한 거고 얘는 실질적으로 응용하는 과정에 끌고 와서, 그렇죠. 연구나 이런 것들도 결국은 굉장히 뛰어난 모델에게 보상 신호, 좋아지는 방향에 대해서 어떤 목표 설정을 할 수 있다면 자율적으로 걔가 그 목표를 향해서 나아갈 수 있다라는 거를 보여준 거죠.


Alif Munim on Autoresearch for Interpretability x.com

Simon Willison on Liquid Performance Improvements simonwillison.net
autoresearch 진행 그래프(83회 실험, 15개 개선 유지)와 Karpathy의 2026년 3월 글 '자율 AI 에이전트 군단이 코드베이스를 10,205세대 진화시켰다'는 내용이 표시된 화면

11:48 최승준 보상 신호가 RL에서의 보상 신호가 아니라 미분 가능하지 않은데도 그냥 어떤 되고 안 되고만 판정을 해 줬는데 굉장히 간단한 몇 개의 파일, prepare.py, 이거는 별로 중요하지 않고 train.py, program.md 이렇게 있으면 그 조건을 달성하는 거를 될 때까지 낮추는 쪽으로 리서치를 하는 건데 MD 파일이 별로 길지도 않아요. 맨 끝에 재미있는 게 있는데, never stop. 멈추지 말고 만약에 막히면, 아이디어가 막히면 페이퍼 읽고 오고 이 가설 세우고 실험해보고 저 가설 실험해보고, 나한테 계속 갈 거냐 물어보지 말고 계속해라라는 거가 마지막 주문인 것 같은데 그거를 실제로 성과를 보고 있는 것들이 여기에 그래프로 보이고 있죠.

그런 건데 여기 그 Andrej Karpathy하고 Yuchen Jin라는 분이 최근에 이분도 CEO였다가 지금 다른 거 하려고 내려오신 분인 것 같은데 이런 아이디어까지 얘기를 하더라고요. 이게 지금 하나의 스쿼드를 돌리거나 그냥 에이전트 하나가 쭉 이렇게 깊게 들어가는 느낌이라면 그런 연구자들의 소셜미디어를 moltbook처럼 만들면 어떠냐 그런 얘기까지 하는 소셜미디어 포스팅을 좀 재미있게 봤고요.

파생 작업들이 있는데 이거는 그 TinyStories를 어떻게 최적화하는가, 또 TinyStories도 데이터가 작은 셋에 잘 정제되어 있어서 그거 낮추는 거를 통해서 이 사람이 배운 거. 그다음에 이거는 Sparse Autoencoder라고 기계론적 해석 가능성 연구에서 쓰는 것들을 잘 할 수 있게 하는 거를 Autoresearch 방식으로 하는 거. 그리고 이거는 Simon Willison이 사례를 공유해 줬는데 Shopify의 CEO, 이 Tobias라는 분이 자기가 예전에 만들었던 어떤 것을 53% 빠르게 하는 그런 거에 Autoresearch를 응용해서 해냈다. 그러니까 작동하는 영역에서는 이게 다 된다는 거죠.

안 되는 것들도 물론 있겠지만 안 되는 영역이 훨씬 더 많겠지만 작동하는 영역에서 심플하고 우아하게 이거를 토큰을 제대로 태워서 할 수 있는 그런 경로들이 발견되고 있는 중입니다. 근데 그 잘 작동하는 영역이 공교롭게도 AI 훈련하는 그거죠.

14:08 노정석 네, 목표를 명확하게 했던 거가 evaluation metric을 명확하게 정의할 수만 있으면 벤치마크가 존재하면 거기는 무조건 된다.
"""

class ExperimentalSegmenter:
    def __init__(self, raw_text: str):
        self.raw_text = raw_text
        self.normalized_text = self._normalize_text(raw_text)

    def _normalize_text(self, text: str) -> str:
        # Standard normalization: replace different newlines with '\n'
        # Do not strip here to preserve paragraph breaks
        return text.replace("\r\n", "\n").replace("\r", "\n")

    def _split_meaningful_units(self, text: str) -> List[str]:
        # Split by one or more blank lines (robust paragraph detection)
        # Each resulting unit is then stripped individually
        paragraphs = [p.strip() for p in re.split(r'\n\s*\n+', text) if p.strip()]
        return paragraphs or [text] # Fallback to original text if no paragraphs found

    def segment_and_assign_values(self) -> List[Dict]:
        dusts_raw = self._split_meaningful_units(self.normalized_text)
        
        segmented_output = []
        for i, text_unit in enumerate(dusts_raw):
            # Placeholder values and explanations
            dust_id = f"dust_{i+1:02d}"
            
            # Extract timestamp if available at the beginning of the unit
            time_match = re.match(r"^(\d{2}:\d{2})\s", text_unit)
            time_value = f"t{i+1:02d}"
            if time_match:
                time_value += f" | {time_match.group(1)}"
                # Remove timestamp from text_unit for cleaner dust content
                text_unit = text_unit[len(time_match.group(0)):].strip()
            
            # Calculate source_range using find method. This is a simplification.
            # A more robust solution would track offsets during splitting.
            start_index = self.raw_text.find(text_unit)
            end_index = start_index + len(text_unit) if start_index != -1 else -1
            source_range = f"{start_index}~{end_index}" if start_index != -1 else "TBD_ERROR"

            segmented_output.append(
                {
                    "dust_id": dust_id,
                    "source_range": source_range,
                    "text": text_unit,
                    "unit_type": "논리 문단", # Placeholder
                    "D": 0.50, # Placeholder
                    "I": 0.50, # Placeholder
                    "S": 0.50, # Placeholder
                    "scene": "unknown", # Placeholder
                    "flow": "unknown", # Placeholder
                    "time": time_value,
                    "why_one_unit": [
                        "현재 단락 단위로 분절되었으며, 하나의 주된 의미를 포함할 것으로 가정" # Placeholder
                    ],
                    "why_this_value": [
                        "연습을 위한 초기 플레이스홀더 값" # Placeholder
                    ],
                    "confidence": "중간", # Placeholder
                }
            )
        return segmented_output

    def format_output(self, segmented_data: List[Dict]) -> str:
        formatted_str = []
        for data in segmented_data:
            formatted_str.append(f"[{data['dust_id']}]")
            formatted_str.append(f"source_range: {data['source_range']}")
            formatted_str.append(f"text: {data['text']}")
            formatted_str.append(f"unit_type: {data['unit_type']}")
            formatted_str.append(f"D: {data['D']:.2f}")
            formatted_str.append(f"I: {data['I']:.2f}")
            formatted_str.append(f"S: {data['S']:.2f}")
            formatted_str.append(f"scene: {data['scene']}")
            formatted_str.append(f"flow: {data['flow']}")
            formatted_str.append(f"time: {data['time']}")
            formatted_str.append("why_one_unit:")
            for reason in data['why_one_unit']:
                formatted_str.append(f"- {reason}")
            formatted_str.append("why_this_value:")
            for reason in data['why_this_value']:
                formatted_str.append(f"- {reason}")
            formatted_str.append(f"confidence: {data['confidence']}")
            formatted_str.append("") # Blank line between dusts
        return "\n".join(formatted_str)


if __name__ == "__main__":
    segmenter = ExperimentalSegmenter(YOUTUBE_EXAM_CONTENT)
    output_data = segmenter.segment_and_assign_values()
            
    print(segmenter.format_output(output_data))