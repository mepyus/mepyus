[dust_01]
  source_range: 1-1
  text: 최승준
  unit_type: text
  D: 0.50
  I: 0.20
  S: 0.50
  scene: self
  flow: contract
  why_one_unit:
   - Separating the speaker's name as an independent unit.
  why_this_value:
   - D/I/S are set to neutral or low values to minimize perceived direction or intensity.
   - Scene is 'self' as it's the speaker's name.
   - Flow is 'contract' because it's a minimal unit.
  confidence: 0.85


  [dust_02]
  source_range: 1-3
  text: 참 또 하나 흥미로운 게 있었는데, 37수이 건물이 됐더라고요.
  unit_type: text
  D: 0.70
  I: 0.50
  S: 0.70
  scene: evidence
  flow: expand
  why_one_unit:
   - Segmented a phrase introducing a topic and stating a fact.
  why_this_value:
   - D is moderately positive, pushing the narrative.
   - I is moderate, reflecting some interest in the "interesting thing."
   - S is moderate-high, as it's a factual statement.
   - Scene is 'evidence' as it reports on a factual development.
   - Flow is 'expand' to introduce new information.
  confidence: 0.90


  [dust_03]
  source_range: 3-3
  text: AlphaGo의 그 놀라운 수라고.
  unit_type: text
  D: 0.60
  I: 0.60
  S: 0.70
  scene: evidence
  flow: bridge
  why_one_unit:
   - Isolated the specific reference to AlphaGo's "amazing move."
  why_this_value:
   - D is slightly positive, acknowledging the move's notable quality.
   - I is moderate-high, reflecting the word "놀라운" (amazing).
   - S is moderate-high, a descriptive phrase.
   - Scene is 'evidence' as it refers to a specific event/element.
   - Flow is 'bridge' to connect this to the building.
  confidence: 0.90


  [dust_04]
  source_range: 3-4
  text: 인간인 이세돌 9단의 놀라운 수가 몇 수였죠?
  unit_type: text
  D: 0.40
  I: 0.50
  S: 0.70
  scene: meta
  flow: tension
  why_one_unit:
   - Separated a question posed for clarification.
  why_this_value:
   - D is low-leaning, as questions don't strongly push forward.
   - I is moderate, reflecting curiosity.
   - S is moderate-high, a clear question.
   - Scene is 'meta' as it's seeking information.
   - Flow is 'tension' to create a pause for an answer.
  confidence: 0.90


  [dust_05]
  source_range: 4-4
  text: 78수였네요.
  unit_type: text
  D: 0.50
  I: 0.30
  S: 0.60
  scene: meta
  flow: bridge
  why_one_unit:
   - Isolated the short answer to the previous question.
  why_this_value:
   - D is neutral.
   - I is low, a simple factual answer.
   - S is moderate, a short statement.
   - Scene is 'meta' as it provides the answer.
   - Flow is 'bridge' to connect the answer to the next piece of info.
  confidence: 0.85


  [dust_06]
  source_range: 4-5
  text: 78수고 AlphaGo의 37수인데,
  unit_type: text
  D: 0.50
  I: 0.40
  S: 0.60
  scene: meta
  flow: bridge
  why_one_unit:
   - Fragmented the comparison of the two move counts.
  why_this_value:
   - D is neutral.
   - I is low-moderate.
   - S is moderate, short factual comparison.
   - Scene is 'meta' as it's comparing facts.
   - Flow is 'bridge' to link these numbers to the building.
  confidence: 0.85


  [dust_07]
  source_range: 5-6
  text: 그 37수의 이름을 따라서 저 Google DeepMind 신사옥이 생기나 봅니다.
  unit_type: text
  D: 0.70
  I: 0.50
  S: 0.80
  scene: evidence
  flow: expand
  why_one_unit:
   - Isolated the core statement about the building's naming origin.
  why_this_value:
   - D is moderately positive, reporting on a new development.
   - I is moderate, conveying interest.
   - S is moderate-high, a clear factual statement.
   - Scene is 'evidence' as it reports on a specific event/naming.
   - Flow is 'expand' to add detail to the building's origin.
  confidence: 0.95


  [dust_08]
  source_range: 6-6
  text: 여름부터 입주를 한다고 하는데요.
  unit_type: text
  D: 0.50
  I: 0.30
  S: 0.60
  scene: meta
  flow: expand
  why_one_unit:
   - Separated the detail about the move-in date.
  why_this_value:
   - D is neutral.
   - I is low, a simple factual detail.
   - S is moderate, a short piece of information.
   - Scene is 'meta' as it's additional factual info.
   - Flow is 'expand' to add more detail.
  confidence: 0.85


  [dust_09]
  source_range: 7-7
  text: 06:40
  unit_type: text
  D: 0.00
  I: 0.00
  S: 0.20
  scene: marker
  flow: contract
  why_one_unit:
   - Treated the timestamp as a separate, minimal unit.
  why_this_value:
   - D/I are 0.00 as markers have no direction or intensity.
   - S is low, as it's a transient marker.
   - Scene is 'marker' as it's purely metadata.
   - Flow is 'contract' due to its minimal nature.
  confidence: 0.70


  [dust_10]
  source_range: 7-7
  text: 이진원
  unit_type: text
  D: 0.50
  I: 0.20
  S: 0.50
  scene: self
  flow: contract
  why_one_unit:
   - Isolated the speaker's name.
  why_this_value:
   - Standard neutral/low values for a name.
  confidence: 0.85


  [dust_11]
  source_range: 7-8
  text: 이건 두 번째 대국이었죠.
  unit_type: text
  D: 0.50
  I: 0.40
  S: 0.70
  scene: meta
  flow: bridge
  why_one_unit:
   - Isolated a clarifying statement about the match.
  why_this_value:
   - D is neutral.
   - I is low-moderate.
   - S is moderate-high, a factual clarification.
   - Scene is 'meta' as it's providing context.
   - Flow is 'bridge' to link to the next point.
  confidence: 0.90


  [dust_12]
  source_range: 9-9
  text: 06:41
  unit_type: text
  D: 0.00
  I: 0.00
  S: 0.20
  scene: marker
  flow: contract
  why_one_unit:
   - Isolated timestamp marker.
  why_this_value:
   - Minimal values for a marker.
  confidence: 0.70


  [dust_13]
  source_range: 9-9
  text: 노정석
  unit_type: text
  D: 0.50
  I: 0.20
  S: 0.50
  scene: self
  flow: contract
  why_one_unit:
   - Isolated speaker's name.
  why_this_value:
   - Standard neutral/low values.
  confidence: 0.85


  [dust_14]
  source_range: 9-11
  text: 두 번째 대국의 37수일 거예요.
  unit_type: text
  D: 0.70
  I: 0.50
  S: 0.70
  scene: evidence
  flow: expand
  why_one_unit:
   - Segmented the statement about the specific move in the second game.
  why_this_value:
   - D is moderately positive, stating a fact about the move.
   - I is moderate.
   - S is moderate-high, a specific statement.
   - Scene is 'evidence' as it refers to a specific game event.
   - Flow is 'expand' to add detail.
  confidence: 0.90


  [dust_15]
  source_range: 11-12
  text: 아마 사람들이 다 그 해설자들이 “어, 저기는 왜 왔지”라고 하면서,
  unit_type: text
  D: 0.60
  I: 0.60
  S: 0.70
  scene: evidence
  flow: bridge
  why_one_unit:
   - Isolated the observation of commentators' reactions and surprise.
  why_this_value:
   - D is moderately positive, reporting on reactions.
   - I is moderate-high, reflecting the surprise ("어, 저기는 왜 왔지").
   - S is moderate-high, describing an observation.
   - Scene is 'evidence' as it reports on external reactions.
   - Flow is 'bridge' to connect this reaction to the nature of the move.
  confidence: 0.90


  [dust_16]
  source_range: 12-13
  text: 인간이라면 절대 못 둘 수였는데,
  unit_type: text
  D: 0.70
  I: 0.70
  S: 0.80
  scene: meta
  flow: expand
  why_one_unit:
   - Isolated the description of the move as one a human couldn't make.
  why_this_value:
   - D is positive, emphasizing the move's quality.
   - I is high, due to the strong assertion "절대 못 둘" (absolutely couldn't make).
   - S is moderate-high, a clear descriptive statement.
   - Scene is 'meta' as it's an evaluation/analysis of the move's nature.
   - Flow is 'expand' to explain the significance.
  confidence: 0.95


  [dust_17]
  source_range: 13-13
  text: 나중에
  unit_type: text
  D: 0.00
  I: 0.00
  S: 0.10
  scene: marker
  flow: contract
  why_one_unit:
   - Separated this trailing, incomplete word.
  why_this_value:
   - Minimal values, reflecting its status as a dangling fragment.
  confidence: 0.70


  [dust_18]
  source_range: 14-14
  text: 06:52
  unit_type: text
  D: 0.00
  I: 0.00
  S: 0.20
  scene: marker
  flow: contract
  why_one_unit:
   - Isolated timestamp marker.
  why_this_value:
   - Minimal values.
  confidence: 0.70


  [dust_19]
  source_range: 15-15
  text: 이진원
  unit_type: text
  D: 0.50
  I: 0.20
  S: 0.50
  scene: self
  flow: contract
  why_one_unit:
   - Isolated speaker's name.
  why_this_value:
   - Standard neutral/low values.
  confidence: 0.85


  [dust_20]
  source_range: 15-16
  text: 실수한 것 같다라는 얘기도 많이 했었고.
  unit_type: text
  D: 0.40
  I: 0.50
  S: 0.70
  scene: evidence
  flow: bridge
  why_one_unit:
   - Isolated the statement about initial perceptions of the move being a mistake.
  why_this_value:
   - D is low-leaning, focusing on past, incorrect perceptions.
   - I is moderate, reflecting the reporting of opinions.
   - S is moderate-high, a factual statement about what was said.
   - Scene is 'evidence' as it reports on opinions/reactions.
   - Flow is 'bridge' to link this to the overall discussion of the move.
  confidence: 0.90


  [dust_21]
  source_range: 17-17
  text: 2016년 AlphaGo 대국 현장 이야기 06:54
  unit_type: text
  D: 0.00
  I: 0.00
  S: 0.20
  scene: marker
  flow: contract
  why_one_unit:
   - Treated section title and timestamp as a marker.
  why_this_value:
   - Minimal values.
  confidence: 0.70


  [dust_22]
  source_range: 18-18
  text: 06:58
  unit_type: text
  D: 0.00
  I: 0.00
  S: 0.20
  scene: marker
  flow: contract
  why_one_unit:
   - Isolated timestamp marker.
  why_this_value:
   - Minimal values.
  confidence: 0.70


  [dust_23]
  source_range: 19-19
  text: 노정석
  unit_type: text
  D: 0.50
  I: 0.20
  S: 0.50
  scene: self
  flow: contract
  why_one_unit:
   - Isolated speaker's name.
  why_this_value:
   - Standard neutral/low values.
  confidence: 0.85


  [dust_24]
  source_range: 19-20
  text: 저희가 2016년, 10년 전을 반추해 보면
  unit_type: text
  D: 0.50
  I: 0.50
  S: 0.70
  scene: meta
  flow: expand
  why_one_unit:
   - Isolated the introductory phrase about reflecting on the past.
  why_this_value:
   - D is neutral, as it's a reflection.
   - I is moderate, as reflection can carry some weight.
   - S is moderate-high, a statement about the act of reflection.
   - Scene is 'meta' as it sets up a historical context.
   - Flow is 'expand' to introduce the historical discussion.
  confidence: 0.90


  [dust_25]
  source_range: 20-21
  text: 저희 TensorFlow가 나오고 막 이런 거 할 때가 2015년 정도였던.
  unit_type: text
  D: 0.70
  I: 0.50
  S: 0.70
  scene: evidence
  flow: expand
  why_one_unit:
   - Isolated the mention of TensorFlow's release.
  why_this_value:
   - D is moderately positive, discussing technological advancement.
   - I is moderate.
   - S is moderate-high, a factual statement about tech history.
   - Scene is 'evidence' as it reports on a past tech event.
   - Flow is 'expand' to add historical detail.
  confidence: 0.90


  [dust_26]
  source_range: 21-22
  text: TensorFlow가 나오긴 했지만 그게 뭔지 세상이 전혀 알지 못하던 때였고,
  unit_type: text
  D: 0.40
  I: 0.60
  S: 0.70
  scene: meta
  flow: tension
  why_one_unit:
   - Isolated the statement about public ignorance of TensorFlow.
  why_this_value:
   - D is low-leaning, emphasizing the lack of awareness.
   - I is moderate-high, reflecting the strong statement "전혀 알지 못하던" (knew nothing at all).
   - S is moderate-high, a descriptive statement.
   - Scene is 'meta' as it describes the general state of knowledge.
   - Flow is 'tension' to contrast the release with the lack of understanding.
  confidence: 0.90


  [dust_27]
  source_range: 22-25
  text: 그때 막 사람들이 딥러닝이란 무엇인가, NVIDIA 키노트 보면서 softmax는 어떻고, 그다음에 MNIST, 그다음에 MNIST 끝나고 나면 CNN 이런 거를 가장 기초적인 것들을 돌려보던 그런
  때였기 때문에
  unit_type: text
  D: 0.70
  I: 0.60
  S: 0.80
  scene: meta
  flow: expand
  why_one_unit:
   - Isolated the description of early ML/DL learning activities.
  why_this_value:
   - D is moderately positive, describing active learning.
   - I is moderate-high, reflecting the engaged learning process.
   - S is moderate-high, a detailed description of common practices.
   - Scene is 'meta' as it describes the learning activities.
   - Flow is 'expand' to detail what people were doing.
  confidence: 0.95


  [dust_28]
  source_range: 25-26
  text: AI라는 표현을 많이 안 썼죠.
  unit_type: text
  D: 0.50
  I: 0.40
  S: 0.60
  scene: meta
  flow: bridge
  why_one_unit:
   - Isolated the statement about the infrequent use of "AI."
  why_this_value:
   - D is neutral.
   - I is low-moderate.
   - S is moderate, a short factual statement.
   - Scene is 'meta' as it discusses terminology.
   - Flow is 'bridge' to contrast with other terms.
  confidence: 0.85


  [dust_29]
  source_range: 26-27
  text: 그때는 머신러닝, 딥러닝이라는 표현을 많이 썼는데
  unit_type: text
  D: 0.50
  I: 0.40
  S: 0.70
  scene: meta
  flow: bridge
  why_one_unit:
   - Isolated the statement about the prevalent use of "Machine Learning" and "Deep Learning."
  why_this_value:
   - D is neutral.
   - I is low-moderate.
   - S is moderate-high, a factual statement about terminology.
   - Scene is 'meta' as it discusses terminology.
   - Flow is 'bridge' to clarify the preceding statement.
  confidence: 0.90


  [dust_30]
  source_range: 27-28
  text: 그거에 대한 기대가 그렇게 높지 않던 때였어요.
  unit_type: text
  D: 0.40
  I: 0.50
  S: 0.70
  scene: meta
  flow: bridge
  why_one_unit:
   - Isolated the statement about low expectations.
  why_this_value:
   - D is low-leaning, emphasizing the lack of high expectations.
   - I is moderate, reflecting the sentiment.
   - S is moderate-high, a descriptive statement.
   - Scene is 'meta' as it describes general sentiment.
   - Flow is 'bridge' to conclude the discussion on expectations.
  confidence: 0.90


  [dust_31]
  source_range: 28-29
  text: 근데 사실 2016년에 AlphaGo가 와서,
  unit_type: text
  D: 0.70
  I: 0.50
  S: 0.70
  scene: evidence
  flow: bridge
  why_one_unit:
   - Isolated the re-introduction of AlphaGo's arrival in 2016.
  why_this_value:
   - D is moderately positive, introducing a key event.
   - I is moderate.
   - S is moderate-high, a factual statement.
   - Scene is 'evidence' as it sets the stage for a key event.
   - Flow is 'bridge' to transition to the personal experience.
  confidence: 0.90


  [dust_32]
  source_range: 29-30
  text: AlphaGo 시작할 때만 하더라도 저도 그 행사장에도 있었는데
  unit_type: text
  D: 0.70
  I: 0.50
  S: 0.80
  scene: self
  flow: expand
  why_one_unit:
   - Isolated the speaker's personal presence at the event.
  why_this_value:
   - D is moderately positive, reporting personal involvement.
   - I is moderate.
   - S is moderate-high, a stable personal statement.
   - Scene is 'self' as it's a personal account.
   - Flow is 'expand' to add personal context.
  confidence: 0.95


  [dust_33]
  source_range: 30-31
  text: 그리고 그 전에 전야제라고 그러죠.
  unit_type: text
  D: 0.50
  I: 0.40
  S: 0.60
  scene: meta
  flow: bridge
  why_one_unit:
   - Isolated the explanation of the term "전야제" (eve party).
  why_this_value:
   - D is neutral.
   - I is low-moderate.
   - S is moderate, a short clarification.
   - Scene is 'meta' as it defines a term.
   - Flow is 'bridge' to connect to the description of the gala.
  confidence: 0.85


  [dust_34]
  source_range: 31-32
  text: 갈라쇼를 할 때 가서 Eric Schmidt랑 유명한 사람들 다 모여 있고
  unit_type: text
  D: 0.70
  I: 0.60
  S: 0.80
  scene: evidence
  flow: expand
  why_one_unit:
   - Isolated the description of the gala event and its attendees.
  why_this_value:
   - D is moderately positive, reporting on a significant gathering.
   - I is moderate-high, describing a high-profile event.
   - S is moderate-high, a detailed description.
   - Scene is 'evidence' as it describes the event setting.
   - Flow is 'expand' to add more detail.
  confidence: 0.95


  [dust_35]
  source_range: 32-33
  text: 이세돌과 Eric Schmidt와 초 VIP들이 맨 가운데 앞 테이블에 앉고
  unit_type: text
  D: 0.70
  I: 0.50
  S: 0.70
  scene: evidence
  flow: expand
  why_one_unit:
   - Isolated the specific detail about VIP seating arrangements.
  why_this_value:
   - D is moderately positive, reporting specific event details.
   - I is moderate.
   - S is moderate-high, a factual detail.
   - Scene is 'evidence' as it describes the event setup.
   - Flow is 'expand' to add more granular detail.
  confidence: 0.90


  [dust_36]
  source_range: 33-34
  text: 유명한 사람들이 다 뒤로 앉았었는데
  unit_type: text
  D: 0.70
  I: 0.50
  S: 0.70
  scene: evidence
  flow: expand
  why_one_unit:
   - Isolated the detail about other famous people sitting further back.
  why_this_value:
   - D is moderately positive, reporting specific event details.
   - I is moderate.
   - S is moderate-high, a factual detail.
   - Scene is 'evidence' as it describes the event setup.
   - Flow is 'expand' to add more granular detail.
  confidence: 0.90


  [dust_37]
  source_range: 34-35
  text: 그때만 하더라도 이세돌 자신만만했었어요.
  unit_type: text
  D: 0.70
  I: 0.60
  S: 0.80
  scene: evidence
  flow: bridge
  why_one_unit:
   - Isolated the statement about Lee Sedol's confidence.
  why_this_value:
   - D is moderately positive, describing confidence.
   - I is moderate-high, reflecting the strong term "자신만만" (very confident).
   - S is moderate-high, a stable statement about emotional state.
   - Scene is 'evidence' as it reports on an observed state.
   - Flow is 'bridge' to lead into his prediction.
  confidence: 0.95


  [dust_38]
  source_range: 35-35
  text: 인간이 이긴다.
  unit_type: text
  D: 0.70
  I: 0.70
  S: 0.70
  scene: self
  flow: expand
  why_one_unit:
   - Isolated Lee Sedol's expressed belief as a separate unit.
  why_this_value:
   - D is moderately positive, an assertive statement.
   - I is high, reflecting the strong conviction.
   - S is moderate-high, a clear declaration.
   - Scene is 'self' as it's a direct statement of belief.
   - Flow is 'expand' to emphasize this belief.
  confidence: 0.90


  [dust_39]
  source_range: 35-35
  text: 네,
  unit_type: text
  D: 0.50
  I: 0.30
  S: 0.40
  scene: meta
  flow: bridge
  why_one_unit:
   - Isolated the short affirmation "네".
  why_this_value:
   - D is neutral.
   - I is low.
   - S is moderate, as it's very short and less stable.
   - Scene is 'meta' as it's an acknowledgement.
   - Flow is 'bridge' to connect to the next speaker's thought.
  confidence: 0.80


  [dust_40]
  source_range: 35-38
  text: 그런데 거꾸로 저는 야, 구글에서 저렇게 별들이 다 넘어올 정도면 얘들이 뭔가 확신을 갖고 넘어왔지 그냥 오진 않았을 거다라고 해서
  unit_type: text
  D: 0.80
  I: 0.70
  S: 0.80
  scene: meta
  flow: expand
  why_one_unit:
   - Isolated the speaker's reasoning for their prediction.
  why_this_value:
   - D is strongly positive, detailing the reasoning for a confident prediction.
   - I is high, reflecting strong conviction and reasoning.
   - S is moderate-high, a stable explanation of thought process.
   - Scene is 'meta' as it describes the speaker's reasoning.
   - Flow is 'expand' to elaborate on the prediction.
  confidence: 0.95


  [dust_41]
  source_range: 38-40
  text: AlphaGo가 압도적으로 이길 거다라고 저는 배팅을 했었고 그때 한참 내기를 했던 기억이 납니다.
  unit_type: text
  D: 0.90
  I: 0.80
  S: 0.80
  scene: evidence
  flow: expand
  why_one_unit:
   - Isolated the speaker's prediction and personal action (betting).
  why_this_value:
   - D is very high, representing a strong, confident prediction and action.
   - I is high, conveying the intensity of the bet and memory.
   - S is moderate-high, a stable report of action and memory.
   - Scene is 'evidence' as it reports on a past action and prediction.
   - Flow is 'expand' to further detail the speaker's personal involvement.
  confidence: 0.95


  [dust_42]
  source_range: 40-41
  text: 근데 저희 1국이 끝나고 났을 때
  unit_type: text
  D: 0.70
  I: 0.50
  S: 0.70
  scene: evidence
  flow: bridge
  why_one_unit:
   - Isolated the context of the first game ending.
  why_this_value:
   - D is moderately positive, moving the narrative forward to the outcome.
   - I is moderate.
   - S is moderate-high, a factual statement of context.
   - Scene is 'evidence' as it sets the stage for the result.
   - Flow is 'bridge' to transition to the outcome.
  confidence: 0.90


  [dust_43]
  source_range: 41-42
  text: 사실 모두가 다 충격에 휩싸이긴 했죠.
  unit_type: text
  D: 0.60
  I: 0.80
  S: 0.80
  scene: evidence
  flow: expand
  why_one_unit:
   - Isolated the statement about collective shock.
  why_this_value:
   - D is moderately positive, acknowledging the impact of the event.
   - I is very high, reflecting the strong emotion of "충격에 휩싸" (engulfed in shock).
   - S is moderate-high, a stable description of a collective state.
   - Scene is 'evidence' as it reports on the collective reaction.
   - Flow is 'expand' to elaborate on the impact.
  confidence: 0.95


  [dust_44]
  source_range: 42-42
  text: 압도적이었어요.
  unit_type: text
  D: 0.80
  I: 0.80
  S: 0.70
  scene: evidence
  flow: bridge
  why_one_unit:
   - Isolated the single word emphasizing the overwhelming nature of the outcome.
  why_this_value:
   - D is high, strongly pushing the narrative of dominance.
   - I is high, reflecting the intensity of "overwhelming."
   - S is moderate-high, a definitive statement.
   - Scene is 'evidence' as it describes the outcome.
   - Flow is 'bridge' to reinforce the previous statement.
  confidence: 0.95


  [dust_45]
  source_range: 45-45
  text: 08:26
  unit_type: text
  D: 0.00
  I: 0.00
  S: 0.20
  scene: marker
  flow: contract
  why_one_unit:
   - Isolated timestamp marker.
  why_this_value:
   - Minimal values.
  confidence: 0.70


  [dust_46]
  source_range: 46-46
  text: 최승준
  unit_type: text
  D: 0.50
  I: 0.20
  S: 0.50
  scene: self
  flow: contract
  why_one_unit:
   - Isolated speaker's name.
  why_this_value:
   - Standard neutral/low values.
  confidence: 0.85


  [dust_47]
  source_range: 47-48
  text: 라이브로 다 보셨죠?
  unit_type: text
  D: 0.40
  I: 0.50
  S: 0.70
  scene: meta
  flow: tension
  why_one_unit:
   - Isolated the question about watching live.
  why_this_value:
   - D is low-leaning, seeking confirmation rather than pushing forward.
   - I is moderate, reflecting curiosity.
   - S is moderate-high, a clear question.
   - Scene is 'meta' as it's seeking shared experience confirmation.
   - Flow is 'tension' to create anticipation for an answer.
  confidence: 0.90


  [dust_48]
  source_range: 48-48
  text: 두 분 다.
  unit_type: text
  D: 0.50
  I: 0.30
  S: 0.50
  scene: meta
  flow: bridge
  why_one_unit:
   - Isolated the clarifying phrase "both of you."
  why_this_value:
   - D is neutral.
   - I is low.
   - S is moderate, a short clarifying phrase.
   - Scene is 'meta' as it clarifies the question's scope.
   - Flow is 'bridge' to add detail to the question.
  confidence: 0.85


  [dust_49]
  source_range: 49-49
  text: 08:28
  unit_type: text
  D: 0.00
  I: 0.00
  S: 0.20
  scene: marker
  flow: contract
  why_one_unit:
   - Isolated timestamp marker.
  why_this_value:
   - Minimal values.
  confidence: 0.70


  [dust_50]
  source_range: 50-50
  text: 이진원
  unit_type: text
  D: 0.50
  I: 0.20
  S: 0.50
  scene: self
  flow: contract
  why_one_unit:
   - Isolated speaker's name.
  why_this_value:
   - Standard neutral/low values.
  confidence: 0.85


  [dust_51]
  source_range: 51-51
  text: 네, 봤습니다.
  unit_type: text
  D: 0.50
  I: 0.30
  S: 0.40
  scene: meta
  flow: bridge
  why_one_unit:
   - Isolated the short confirmation.
  why_this_value:
   - D is neutral.
   - I is low.
   - S is moderate, as it's very short and less stable.
   - Scene is 'meta' as it's an acknowledgement.
   - Flow is 'bridge' to transition to the next speaker.
  confidence: 0.80


  [dust_52]
  source_range: 52-52
  text: 08:33
  unit_type: text
  D: 0.00
  I: 0.00
  S: 0.20
  scene: marker
  flow: contract
  why_one_unit:
   - Isolated timestamp marker.
  why_this_value:
   - Minimal values.
  confidence: 0.70


  [dust_53]
  source_range: 53-53
  text: 노정석
  unit_type: text
  D: 0.50
  I: 0.20
  S: 0.50
  scene: self
  flow: contract
  why_one_unit:
   - Isolated speaker's name.
  why_this_value:
   - Standard neutral/low values.
  confidence: 0.85


  [dust_54]
  source_range: 54-54
  text: 봤죠.
  unit_type: text
  D: 0.50
  I: 0.30
  S: 0.40
  scene: meta
  flow: bridge
  why_one_unit:
   - Isolated the short acknowledgement.
  why_this_value:
   - D is neutral.
   - I is low.
   - S is moderate, as it's very short.
   - Scene is 'meta' as it's an acknowledgement.
   - Flow is 'bridge' to continue the narrative.
  confidence: 0.80


  [dust_55]
  source_range: 54-55
  text: 저도 바둑을 다 이해하지 못하기 때문에
  unit_type: text
  D: 0.40
  I: 0.50
  S: 0.70
  scene: meta
  flow: bridge
  why_one_unit:
   - Isolated the statement about not fully understanding Go.
  why_this_value:
   - D is low-leaning, emphasizing the lack of understanding.
   - I is moderate, reflecting the weight of the statement.
   - S is moderate-high, a stable admission of limitation.
   - Scene is 'meta' as it's a personal limitation.
   - Flow is 'bridge' to explain how understanding was gained despite this.
  confidence: 0.90


  [dust_56]
  source_range: 55-56
  text: 그 수의 깊음이나 이런 거는 제가 이해는 못했습니다만
  unit_type: text
  D: 0.40
  I: 0.50
  S: 0.70
  scene: meta
  flow: bridge
  why_one_unit:
   - Isolated the specific detail about not understanding the depth of moves.
  why_this_value:
   - D is low-leaning, reiterating the lack of understanding.
   - I is moderate, reflecting the qualifier "but."
   - S is moderate-high, a stable statement of limitation.
   - Scene is 'meta' as it's a personal limitation.
   - Flow is 'bridge' to contrast with gained insight.
  confidence: 0.90


  [dust_57]
  source_range: 57-58
  text: 그 사람들, 해설해 주시는 해설자들의 탄식과 놀라움과 좌절감들을 보면서
  unit_type: text
  D: 0.70
  I: 0.70
  S: 0.80
  scene: evidence
  flow: bridge
  why_one_unit:
   - Isolated the observation of commentators' emotional reactions.
  why_this_value:
   - D is moderately positive, observing reactions that signal importance.
   - I is high, reflecting the strong emotions described ("탄식과 놀라움과 좌절감").
   - S is moderate-high, a stable description of observed phenomena.
   - Scene is 'evidence' as it reports on observable reactions.
   - Flow is 'bridge' to lead to the conclusion drawn from these observations.
  confidence: 0.95


  [dust_58]
  source_range: 58-59
  text: 아, 이거 엄청난 거구나라는 생각을 했었죠.
  unit_type: text
  D: 0.70
  I: 0.70
  S: 0.80
  scene: meta
  flow: expand
  why_one_unit:
   - Isolated the speaker's realization of the event's significance.
  why_this_value:
   - D is moderately positive, reflecting a positive realization.
   - I is high, due to the strong exclamation "엄청난 거구나" (it's something huge).
   - S is moderate-high, a stable statement of realization.
   - Scene is 'meta' as it's a personal conclusion/reflection.
   - Flow is 'expand' to detail the speaker's derived understanding.
  confidence: 0.95


  [dust_59]
  source_range: 60-60
  text: 08:51
  unit_type: text
  D: 0.00
  I: 0.00
  S: 0.20
  scene: marker
  flow: contract
  why_one_unit:
   - Isolated timestamp marker.
  why_this_value:
   - Minimal values.
  confidence: 0.70


  [dust_60]
  source_range: 60-60
  text: 이진원
  unit_type: text
  D: 0.50
  I: 0.20
  S: 0.50
  scene: self
  flow: contract
  why_one_unit:
   - Isolated speaker's name.
  why_this_value:
   - Standard neutral/low values.
  confidence: 0.85


  [dust_61]
  source_range: 60-62
  text: 또 굉장히 재미있었던 거는 그때 유튜브 포함해서 다양한 채널에서 해설,
  unit_type: text
  D: 0.70
  I: 0.60
  S: 0.80
  scene: evidence
  flow: expand
  why_one_unit:
   - Isolated the statement about the interesting aspect of varied commentary.
  why_this_value:
   - D is moderately positive, highlighting an interesting facet.
   - I is moderate-high, reflecting "재미있었던" (was very interesting).
   - S is moderate-high, a stable description.
   - Scene is 'evidence' as it reports on an observed phenomenon.
   - Flow is 'expand' to detail this phenomenon.
  confidence: 0.95


  [dust_62]
  source_range: 62-63
  text: 소위 프로바둑 기사들이 해설을 했는데
  unit_type: text
  D: 0.70
  I: 0.50
  S: 0.70
  scene: evidence
  flow: expand
  why_one_unit:
   - Isolated the description of professional commentators.
  why_this_value:
   - D is moderately positive, reporting on experts.
   - I is moderate.
   - S is moderate-high, a factual description.
   - Scene is 'evidence' as it describes the commentators.
   - Flow is 'expand' to add detail to the commentary aspect.
  confidence: 0.90


  [dust_63]
  source_range: 63-64
  text: 의견이 굉장히 많이 갈렸었어요.
  unit_type: text
  D: 0.60
  I: 0.70
  S: 0.80
  scene: evidence
  flow: expand
  why_one_unit:
   - Isolated the statement about divided opinions among commentators.
  why_this_value:
   - D is moderately positive, highlighting a dynamic aspect.
   - I is high, reflecting "굉장히 많이 갈렸었어요" (were very divided).
   - S is moderate-high, a stable observation.
   - Scene is 'evidence' as it reports on the nature of the commentary.
   - Flow is 'expand' to detail the diversity of opinions.
  confidence: 0.95


  [dust_64]
  source_range: 64-66
  text: 어떤 한 수 한 수 나올 때마다 그거를 보는 것도 재미있었던 기억이 있습니다.
  unit_type: text
  D: 0.70
  I: 0.60
  S: 0.80
  scene: evidence
  flow: expand
  why_one_unit:
   - Isolated the memory of finding the commentary itself enjoyable.
  why_this_value:
   - D is moderately positive, reflecting enjoyment.
   - I is moderate-high, due to "재미있었던 기억" (memorable and fun).
   - S is moderate-high, a stable statement of memory.
   - Scene is 'evidence' as it reports on a personal memory of enjoyment.
   - Flow is 'expand' to elaborate on the viewing experience.
  confidence: 0.95


  [dust_65]
  source_range: 67-67
  text: 09:03
  unit_type: text
  D: 0.00
  I: 0.00
  S: 0.20
  scene: marker
  flow: contract
  why_one_unit:
   - Isolated timestamp marker.
  why_this_value:
   - Minimal values.
  confidence: 0.70


  [dust_66]
  source_range: 67-67
  text: 최승준
  unit_type: text
  D: 0.50
  I: 0.20
  S: 0.50
  scene: self
  flow: contract
  why_one_unit:
   - Isolated speaker's name.
  why_this_value:
   - Standard neutral/low values.
  confidence: 0.85


  [dust_67]
  source_range: 67-69
  text: 그 당시에는 정책망이 뭐다 가치망이 뭐다 그런 용어들을 저는 잘 몰랐던 때라 가지고
  unit_type: text
  D: 0.40
  I: 0.50
  S: 0.70
  scene: meta
  flow: bridge
  why_one_unit:
   - Isolated the statement about not understanding technical terms.
  why_this_value:
   - D is low-leaning, emphasizing the lack of knowledge.
   - I is moderate, reflecting the phrase "잘 몰랐던 때라" (was a time when I didn't know well).
   - S is moderate-high, a stable statement of personal limitation.
   - Scene is 'meta' as it's a personal confession of ignorance.
   - Flow is 'bridge' to explain how they learned.
  confidence: 0.90


  [dust_68]
  source_range: 69-70
  text: 이게 무슨 소리인가 블로그 보기도 하고,
  unit_type: text
  D: 0.70
  I: 0.50
  S: 0.70
  scene: meta
  flow: expand
  why_one_unit:
   - Isolated the detail about consulting blogs for information.
  why_this_value:
   - D is moderately positive, describing an active learning method.
   - I is moderate.
   - S is moderate-high, a stable detail about learning.
   - Scene is 'meta' as it describes a learning process.
   - Flow is 'expand' to add more detail to the learning experience.
  confidence: 0.90


  [dust_69]
  source_range: 70-70
  text: 기억이 나네요.
  unit_type: text
  D: 0.50
  I: 0.40
  S: 0.60
  scene: self
  flow: bridge
  why_one_unit:
   - Isolated the phrase "I remember."
  why_this_value:
   - D is neutral.
   - I is low-moderate.
   - S is moderate, a short statement of memory.
   - Scene is 'self' as it's a personal reflection.
   - Flow is 'bridge' to conclude the thought.
  confidence: 0.85


  [dust_70]
  source_range: 71-71
  text: 09:13
  unit_type: text
  D: 0.00
  I: 0.00
  S: 0.20
  scene: marker
  flow: contract
  why_one_unit:
   - Isolated timestamp marker.
  why_this_value:
   - Minimal values.
  confidence: 0.70


  [dust_71]
  source_range: 71-71
  text: 노정석
  unit_type: text
  D: 0.50
  I: 0.20
  S: 0.50
  scene: self
  flow: contract
  why_one_unit:
   - Isolated speaker's name.
  why_this_value:
   - Standard neutral/low values.
  confidence: 0.85


  [dust_72]
  source_range: 71-74
  text: AlphaGo 대국이 끝나고 나서 웬만한 교수님이나 유명하신 분들이 다 그게 어떻게 만들어졌는지 해설가가 되셔서 발표 자료들, 유튜브 녹화들 굉장히 많이 나왔던 생각이 납니다.
  unit_type: text
  D: 0.70
  I: 0.50
  S: 0.80
  scene: meta
  flow: expand
  why_one_unit:
   - Isolated the description of the widespread expert analysis and content creation post-event.
  why_this_value:
   - D is moderately positive, highlighting the dissemination of knowledge.
   - I is moderate, describing a significant educational effort.
   - S is moderate-high, a stable description of widespread activity.
   - Scene is 'meta' as it describes the academic and public response.
   - Flow is 'expand' to detail the impact and legacy through content creation.
  confidence: 0.95