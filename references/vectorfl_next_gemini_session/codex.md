
  [dust_01]
  source_range: 1-5
  text: 최승준 참 또 하나 흥미로운 게 있었는데, 37수이 건물이 됐더라고요. AlphaGo의 그 놀라운 수라고. 인간인 이세돌 9단의 놀라운 수가 몇 수였죠? 78수였네요. 78수고 AlphaGo의
  37수인데, 그 37수의 이름을 따라서 저 Google DeepMind 신사옥이 생기나 봅니다. 여름부터 입주를 한다고 하는데요.
  unit_type: text
  D: 0.70
  I: 0.50
  S: 0.80
  scene: evidence
  flow: expand
  time: t01
  why_one_unit:
   - This dust describes a specific event: the naming of a new Google DeepMind building after AlphaGo's 37th move.
   - It connects a past event (AlphaGo game) with a present development (new building).
  why_this_value:
   - D: 0.70 (Positive push forward, expanding on the event's significance)
   - I: 0.50 (Moderate intensity, factual reporting with a hint of interest)
   - S: 0.80 (Stable unit, clearly presenting a single piece of information)
   - scene: evidence (Reporting on a factual event and its historical context)
   - flow: expand (Expanding on the initial mention of the building and its name origin)
  confidence: 0.95


  [dust_02]
  source_range: 7-8
  text: 이진원 이건 두 번째 대국이었죠.
  unit_type: text
  D: 0.50
  I: 0.30
  I: 0.30
  S: 0.70
  scene: meta
  flow: bridge
  time: t02
  why_one_unit:
   - This dust clarifies the context of the previous statement by specifying which game the 37th move belonged to.
  why_this_value:
   - D: 0.50 (Neutral, simply clarifying a fact)
   - I: 0.30 (Low intensity, stating a factual clarification)
   - S: 0.70 (Stable unit, providing a specific clarifying detail)
   - scene: meta (Providing meta-information to contextualize the previous statement)
   - flow: bridge (Bridging the information from the previous dust to the next clarification)
  confidence: 0.90


  [dust_03]
  source_range: 9-13
  text: 노정석 두 번째 대국의 37수일 거예요. 아마 사람들이 다 그 해설자들이 “어, 저기는 왜 왔지”라고 하면서, 인간이라면 절대 못 둘 수였는데, 나중에
  unit_type: text
  D: 0.60
  I: 0.70
  S: 0.70
  scene: evidence
  flow: expand
  time: t03
  why_one_unit:
   - This dust elaborates on the significance of the 37th move, mentioning that commentators were surprised by it and that it was a move a human would not typically make.
  why_this_value:
   - D: 0.60 (Leaning towards positive/forward, highlighting the move's uniqueness)
   - I: 0.70 (High intensity, conveying surprise and the extraordinary nature of the move)
   - S: 0.70 (Stable unit, describing a specific aspect of the move and reactions to it)
   - scene: evidence (Describing reactions and commentary on a specific event)
   - flow: expand (Expanding on the details and implications of the move)
  confidence: 0.90


  [dust_04]
  source_range: 14-15
  text: 이진원 실수한 것 같다라는 얘기도 많이 했었고.
  unit_type: text
  D: 0.40
  I: 0.40
  S: 0.70
  scene: meta
  flow: bridge
  time: t04
  why_one_unit:
   - This dust adds a detail about the initial perception of the move: some thought it was a mistake.
  why_this_value:
   - D: 0.40 (Low/negative side, indicating a past, possibly incorrect, judgment)
   - I: 0.40 (Moderate-low intensity, reporting on a past sentiment)
   - S: 0.70 (Stable unit, providing a specific detail about the initial reaction)
   - scene: meta (Providing context about the reception of the move)
   - flow: bridge (Connecting the previous statement about the move to the subsequent discussion about it being perceived as a mistake)
  confidence: 0.90


  [dust_05]
  source_range: 17-27
  text: 2016년 AlphaGo 대국 현장 이야기 06:54


  06:58 노정석 저희가 2016년, 10년 전을 반추해 보면 저희 TensorFlow가 나오고 막 이런 거 할 때가 2015년 정도였던. TensorFlow가 나오긴 했지만 그게 뭔지 세상이 전혀 알지 못하던
  때였고, 그때 막 사람들이 딥러닝이란 무엇인가, NVIDIA 키노트 보면서 softmax는 어떻고, 그다음에 MNIST, 그다음에 MNIST 끝나고 나면 CNN 이런 거를 가장 기초적인 것들을 돌려보던
  그런 때였기 때문에 AI라는 표현을 많이 안 썼죠. 그때는 머신러닝, 딥러닝이라는 표현을 많이 썼는데 그거에 대한 기대가 그렇게 높지 않던 때였어요.
  unit_type: text
  D: 0.70
  I: 0.60
  S: 0.80
  scene: meta
  flow: expand
  time: t05 | 06:58
  why_one_unit:
   - This dust sets the historical context by discussing the state of AI/ML (TensorFlow, Deep Learning, MNIST, CNN) in 2015-2016, noting the low expectations and limited use of
     the term "AI".
  why_this_value:
   - D: 0.70 (Forward-looking, discussing the evolution and early stages of AI)
   - I: 0.60 (Moderately high intensity, describing a period of significant technological emergence with notable user interest but not widespread adoption)
   - S: 0.80 (Stable unit, detailing the technological landscape and sentiment of the era)
   - scene: meta (Discussing the historical context and development of AI/ML)
   - flow: expand (Expanding on the timeline and the nascent state of AI/ML technologies)
  confidence: 0.95


  [dust_06]
  source_range: 28-32
  text: 근데 사실 2016년에 AlphaGo가 와서, AlphaGo 시작할 때만 하더라도 저도 그 행사장에도 있었는데 그리고 그 전에 전야제라고 그러죠. 갈라쇼를 할 때 가서 Eric Schmidt랑 유명한
  사람들 다 모여 있고 이세돌과 Eric Schmidt와 초 VIP들이 맨 가운데 앞 테이블에 앉고 유명한 사람들이 다 뒤로 앉았었는데 그때만 하더라도 이세돌 자신만만했었어요. 인간이 이긴다.
  네, 그런데 거꾸로 저는 야, 구글에서 저렇게 별들이 다 넘어올 정도면 얘들이 뭔가 확신을 갖고 넘어왔지 그냥 오진 않았을 거다라고 해서 AlphaGo가 압도적으로 이길 거다라고 저는
  배팅을 했었고 그때 한참 내기를 했던 기억이 납니다.
  unit_type: text
  D: 0.80
  I: 0.70
  S: 0.80
  scene: evidence
  flow: expand
  time: t06
  why_one_unit:
   - This dust describes the speaker's personal experience attending the AlphaGo event, the atmosphere, and their prediction that AlphaGo would win, based on the caliber of
     people present.
  why_this_value:
   - D: 0.80 (Strongly forward-looking, making a confident prediction and recalling a significant past event)
   - I: 0.70 (High intensity, conveying personal involvement, strong conviction in the prediction, and the notable atmosphere)
   - S: 0.80 (Stable unit, detailing a personal account and reasoning for a prediction)
   - scene: evidence (Recounting a personal experience at a significant event)
   - flow: expand (Expanding on the personal perspective and prediction during the AlphaGo event)
  confidence: 0.95


  [dust_07]
  source_range: 32-34
  text: 근데 저희 1국이 끝나고 났을 때 사실 모두가 다 충격에 휩싸이긴 했죠. 압도적이었어요.
  unit_type: text
  D: 0.60
  I: 0.80
  S: 0.70
  scene: evidence
  flow: bridge
  time: t07
  why_one_unit:
   - This dust describes the immediate aftermath of the first game, highlighting the shock and the overwhelming nature of AlphaGo's performance.
  why_this_value:
   - D: 0.60 (Leaning positive, but the shock and overwhelming nature imply a shift in expectations)
   - I: 0.80 (Very high intensity, conveying the strong emotional impact of the event)
   - S: 0.70 (Stable unit, describing the reaction to the first game's outcome)
   - scene: evidence (Describing the immediate impact and reception of a game outcome)
   - flow: bridge (Bridging the prediction to the actual outcome and the resulting shock)
  confidence: 0.95


  [dust_08]
  source_range: 35-36
  text: 최승준 라이브로 다 보셨죠? 두 분 다.
  unit_type: text
  D: 0.50
  I: 0.30
  S: 0.70
  scene: meta
  flow: bridge
  time: t08
  why_one_unit:
   - A question directed to the other speakers, checking if they also watched the event live.
  why_this_value:
   - D: 0.50 (Neutral, seeking confirmation)
   - I: 0.30 (Low intensity, a simple question)
   - S: 0.70 (Stable unit, posing a clear question)
   - scene: meta (Asking for confirmation about shared experience)
   - flow: bridge (Bridging to the next speaker's reflection)
  confidence: 0.90


  [dust_09]
  source_range: 37-38
  text: 이진원 네, 봤습니다.
  unit_type: text
  D: 0.50
  I: 0.30
  S: 0.70
  scene: meta
  flow: bridge
  time: t09
  why_one_unit:
   - A simple affirmation from another speaker.
  why_this_value:
   - D: 0.50 (Neutral affirmation)
   - I: 0.30 (Low intensity, simple confirmation)
   - S: 0.70 (Stable unit, direct answer)
   - scene: meta (Simple confirmation)
   - flow: bridge (Responding to the question and allowing the conversation to continue)
  confidence: 0.90


  [dust_10]
  source_range: 39-44
  text: 노정석 봤죠. 저도 바둑을 다 이해하지 못하기 때문에 그 수의 깊음이나 이런 거는 제가 이해는 못했습니다만 그 사람들, 해설해 주시는 해설자들의 탄식과 놀라움과 좌절감들을
  보면서 아, 이거 엄청난 거구나라는 생각을 했었죠.
  unit_type: text
  D: 0.70
  I: 0.70
  S: 0.80
  scene: meta
  flow: expand
  time: t10
  why_one_unit:
   - The speaker acknowledges watching the match, admits not fully understanding the game's depth, but felt the significance through the commentators' reactions.
  why_this_value:
   - D: 0.70 (Leaning positive, acknowledging the significance and learning from it)
   - I: 0.70 (High intensity, conveying the impact of the commentators' reactions and the realization of something "huge")
   - S: 0.80 (Stable unit, describing personal experience and inferred understanding)
   - scene: meta (Reflecting on the experience and understanding the event's magnitude indirectly)
   - flow: expand (Expanding on the personal experience and how understanding was gained)
  confidence: 0.95


  [dust_11]
  source_range: 45-50
  text: 이진원 또 굉장히 재미있었던 거는 그때 유튜브 포함해서 다양한 채널에서 해설, 소위 프로바둑 기사들이 해설을 했는데 의견이 굉장히 많이 갈렸었어요. 어떤 한 수 한 수 나올
  때마다 그거를 보는 것도 재미있었던 기억이 있습니다.
  unit_type: text
  D: 0.70
  I: 0.60
  S: 0.80
  scene: evidence
  flow: expand
  time: t11
  why_one_unit:
   - This dust highlights an interesting aspect of the event: the diverse and often conflicting opinions from professional commentators on YouTube and other channels.
  why_this_value:
   - D: 0.70 (Positive, focusing on the interesting and engaging aspect of varied commentary)
   - I: 0.60 (Moderately high intensity, describing a dynamic and engaging element of the broadcast)
   - S: 0.80 (Stable unit, detailing a specific observation about the commentary)
   - scene: evidence (Reporting on an observed phenomenon during the event broadcast)
   - flow: expand (Expanding on the viewing experience by detailing the commentary aspect)
  confidence: 0.95


  [dust_12]
  source_range: 51-53
  text: 최승준 그 당시에는 정책망이 뭐다 가치망이 뭐다 그런 용어들을 저는 잘 몰랐던 때라 가지고 이게 무슨 소리인가 블로그 보기도 하고, 기억이 나네요.
  unit_type: text
  D: 0.50
  I: 0.40
  S: 0.70
  scene: meta
  flow: bridge
  time: t12
  why_one_unit:
   - The speaker recalls their personal lack of understanding of technical terms like "policy network" and "value network" at the time, and how they sought information through
     blogs.
  why_this_value:
   - D: 0.50 (Neutral, reflecting on a past state of knowledge)
   - I: 0.40 (Low-moderate intensity, describing a personal learning process)
   - S: 0.70 (Stable unit, detailing personal unfamiliarity with technical terms and learning methods)
   - scene: meta (Reflecting on personal knowledge and learning process during a past event)
   - flow: bridge (Connecting the previous discussion about commentary to the speaker's personal understanding of the technical aspects)
  confidence: 0.90


  [dust_13]
  source_range: 54-56
  text: 노정석 AlphaGo 대국이 끝나고 나서 웬만한 교수님이나 유명하신 분들이 다 그게 어떻게 만들어졌는지 해설가가 되셔서 발표 자료들, 유튜브 녹화들 굉장히 많이 나왔던 생각이
  납니다.
  unit_type: text
  D: 0.70
  I: 0.50
  S: 0.80
  scene: meta
  flow: expand
  time: t13
  why_one_unit:
   - This dust describes the extensive aftermath of the AlphaGo match, where many experts and academics created presentations and YouTube recordings explaining its creation.
  why_this_value:
   - D: 0.70 (Forward-looking, highlighting the widespread dissemination of knowledge following the event)
   - I: 0.50 (Moderate intensity, describing a significant educational/dissemination effort)
   - S: 0.80 (Stable unit, detailing the widespread expert analysis and content creation post-event)
   - scene: meta (Describing the scholarly and public response to the technological event)
   - flow: expand (Expanding on the impact and legacy of the AlphaGo match through post-event analysis)
  confidence: 0.95