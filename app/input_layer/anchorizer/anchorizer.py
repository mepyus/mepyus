from __future__ import annotations

import re
from typing import Dict, List, Sequence, Tuple

from app.fragment.schema import FragmentAnchor, FragmentRecord


TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9_./+-]{2,}|[가-힣]{2,}")
FILE_RE = re.compile(r"([A-Za-z0-9_./-]+\.[A-Za-z0-9_]+)")
NON_WORD_RE = re.compile(r"[^a-z0-9가-힣]+")

KNOWN_OBJECTS: Dict[str, Tuple[str, str]] = {
    "비전 랭귀지 모델": ("object.model.vision_language_model", "비전 랭귀지 모델"),
    "vision language model": ("object.model.vision_language_model", "비전 랭귀지 모델"),
    "매트릭 러닝": ("object.method.metric_learning", "매트릭 러닝"),
    "metric learning": ("object.method.metric_learning", "매트릭 러닝"),
    "google deepmind": ("object.org.google_deepmind", "Google DeepMind"),
    "alphago": ("object.system.alphago", "AlphaGo"),
    "google": ("object.org.google", "Google"),
    "deepmind": ("object.org.deepmind", "DeepMind"),
    "tensorflow": ("object.framework.tensorflow", "TensorFlow"),
    "nvidia": ("object.org.nvidia", "NVIDIA"),
    "mnist": ("object.dataset.mnist", "MNIST"),
    "cnn": ("object.model.cnn", "CNN"),
    "softmax": ("object.concept.softmax", "softmax"),
    "pytorch": ("object.framework.pytorch", "PyTorch"),
    "python": ("object.language.python", "Python"),
    "chatgpt": ("object.system.chatgpt", "ChatGPT"),
    "claude": ("object.system.claude", "Claude"),
    "codex": ("object.system.codex", "Codex"),
    "deepseek": ("object.org.deepseek", "DeepSeek"),
    "deepseek-r1": ("object.model.deepseek_r1", "DeepSeek-R1"),
    "r1": ("object.model.deepseek_r1", "DeepSeek-R1"),
    "rlvr": ("object.method.rlvr", "RLVR"),
    "moe": ("object.architecture.moe", "MoE"),
    "mixture of experts": ("object.architecture.moe", "MoE"),
    "dense": ("object.architecture.dense_model", "dense model"),
    "dense model": ("object.architecture.dense_model", "dense model"),
    "llama": ("object.model.llama", "Llama"),
    "mistral": ("object.org.mistral", "Mistral"),
    "z.ai": ("object.org.z_ai", "Z.ai"),
    "minimax": ("object.org.minimax", "MiniMax"),
    "xiaomi": ("object.org.xiaomi", "Xiaomi"),
    "tencent": ("object.org.tencent", "Tencent"),
    "moonshot": ("object.org.moonshot", "Moonshot"),
    "ant": ("object.org.ant", "Ant"),
    "alibaba": ("object.org.alibaba", "Alibaba"),
    "meituan": ("object.org.meituan", "Meituan"),
    "중국": ("object.country.china", "China"),
    "cursor": ("object.tool.cursor", "Cursor"),
    "three.js": ("object.framework.three_js", "three.js"),
    "threejs": ("object.framework.three_js", "three.js"),
    "maya": ("object.tool.maya", "Maya"),
    "이세돌": ("object.person.이세돌", "이세돌"),
    "딥러닝": ("object.field.딥러닝", "딥러닝"),
    "머신러닝": ("object.field.머신러닝", "머신러닝"),
    "인공지능": ("object.field.ai", "AI"),
    "ai": ("object.field.ai", "AI"),
}

SEMANTIC_RULES: Sequence[Tuple[str, str, str]] = (
    ("semantic.embedding_space_distance", "embedding space distance", "인베딩 공간"),
    ("semantic.embedding_space_distance", "embedding space distance", "거리"),
    ("semantic.contrastive_learning", "contrastive learning", "네거티브"),
    ("semantic.contrastive_learning", "contrastive learning", "파지티브"),
    ("semantic.contrastive_learning", "contrastive learning", "레이블 없이"),
    ("semantic.label_classification", "label classification", "레이블은"),
    ("semantic.label_classification", "label classification", "분류도"),
    ("semantic.class_token_classification", "class token classification", "클래스 토큰"),
    ("semantic.class_token_classification", "class token classification", "이미지 분류"),
    ("semantic.retrieval_ranking_clustering", "retrieval ranking clustering", "클러스터링"),
    ("semantic.retrieval_ranking_clustering", "retrieval ranking clustering", "리트리벌"),
    ("semantic.retrieval_ranking_clustering", "retrieval ranking clustering", "랭킹"),
    ("semantic.topic_similarity", "topic similarity", "주제 이미지"),
    ("semantic.topic_similarity", "topic similarity", "가장 가까운 거"),
    ("semantic.match.signature_move", "signature move", "37수"),
    ("semantic.match.signature_move", "signature move", "78수"),
    ("semantic.public_shock", "public shock", "놀라운 수"),
    ("semantic.public_shock", "public shock", "인간이라면 절대"),
    ("semantic.historical.context", "historical context", "반추해"),
    ("semantic.historical.context", "historical context", "10년 전"),
    ("semantic.historical.context", "historical context", "그때"),
    ("semantic.framework.early_adoption", "framework early adoption", "TensorFlow가 나오"),
    ("semantic.framework.early_adoption", "framework early adoption", "세상이 전혀 알지 못하던"),
    ("semantic.learning.basics", "learning basics", "기초적인 것들을 돌려보던"),
    ("semantic.ai.naming_shift", "AI naming shift", "AI라는 표현을 많이 안 썼"),
    ("semantic.expectation.low", "low expectation", "기대가 그렇게 높지 않"),
    ("semantic.error_speculation", "error speculation", "실수한 것 같다"),
    ("semantic.future_of_work", "future of work", "연금 받고"),
    ("semantic.future_of_work", "future of work", "일은 다"),
    ("semantic.platform_shift", "platform shift", "플랫폼 시프트"),
    ("semantic.platform_shift", "platform shift", "distribution 채널"),
    ("semantic.verification.difficulty", "verification difficulty", "verifiable"),
    ("semantic.verification.difficulty", "verification difficulty", "verify"),
    ("semantic.verification.difficulty", "verification difficulty", "metric"),
    ("semantic.no_playbook", "no playbook", "플레이북에 정답이 없습니다"),
    ("semantic.fast_follower_risk", "fast follower risk", "market share"),
    ("semantic.fast_follower_risk", "fast follower risk", "먼저 가서 순교"),
    ("semantic.fast_follower_risk", "fast follower risk", "다 가져가 버리는"),
    ("semantic.paradigm_shift", "paradigm shift", "패러다임이 확 전환"),
    ("semantic.posttraining_shift", "posttraining shift", "에이전트 포스트트레이닝"),
    ("semantic.open_frontier_boom", "open frontier boom", "수많은 오픈 프런티어 모델"),
    ("semantic.frontier_model_push", "frontier model push", "프런티어 혹은 준 프런티어"),
    ("semantic.frontier_model_push", "frontier model push", "모두가 더 큰 모델"),
    ("semantic.china_open_frontier", "china open frontier leadership", "100% 다 중국"),
    ("semantic.china_open_frontier", "china open frontier leadership", "중국이 다 주도"),
    ("semantic.compute_constraint", "compute constraint", "제약된 컴퓨팅 파워"),
    ("semantic.compute_constraint", "compute constraint", "제한된 연산 자원"),
    ("semantic.frontier_under_constraint", "frontier under constraint", "프런티어를 노릴 수 있다는 것이 증명"),
    ("semantic.deepseek_trigger", "DeepSeek trigger", "가장 큰 역할을 한 게 여전히 DeepSeek"),
    ("semantic.compute_multiplier", "compute multiplier", "연산 배수"),
    ("semantic.compute_multiplier", "compute multiplier", "7배 이상"),
    ("semantic.compute_multiplier", "compute multiplier", "compute multiplier"),
    ("semantic.sparsity", "sparsity", "sparsity"),
    ("semantic.sparsity", "sparsity", "희소성"),
    ("semantic.routing_modularity", "routing modularity", "모듈화되어 있고"),
    ("semantic.routing_modularity", "routing modularity", "expert 라우팅"),
    ("semantic.moe_mainstream_shift", "MoE mainstream shift", "거의 대부분 MoE 모델"),
    ("semantic.moe_mainstream_shift", "MoE mainstream shift", "MoE가 아닌 모델들이 굉장히 드문"),
    ("semantic.deepseek_recipe_diffusion", "DeepSeek recipe diffusion", "DeepSeek의 굉장히 큰 기여"),
    ("semantic.deepseek_recipe_diffusion", "DeepSeek recipe diffusion", "그대로 채택해 버리는"),
)

STRUCTURAL_RULES: Sequence[Tuple[str, str, float]] = (
    ("structural.role.open_question", "몇 수였죠", 0.92),
    ("structural.role.quote", "라고 하면서", 0.84),
    ("structural.role.background", "반추해", 0.86),
    ("structural.role.background", "10년 전", 0.82),
    ("structural.role.background", "그때", 0.72),
    ("structural.role.evidence", "기억", 0.74),
    ("structural.role.evidence", "봤", 0.72),
    ("structural.role.evidence", "느꼈", 0.74),
    ("structural.role.failure_mode", "실수한 것 같다", 0.9),
    ("structural.role.failure_mode", "절대 못 둘", 0.82),
    ("structural.role.bridge", "하지만", 0.7),
    ("structural.role.bridge", "근데", 0.7),
    ("structural.role.bridge", "그런데", 0.7),
    ("structural.role.definition", "무엇인가", 0.82),
)

STOP_TERMS = {
    "그리고",
    "하지만",
    "그러나",
    "이건",
    "저희가",
    "그때",
    "정도",
    "이제",
    "있다",
    "했다",
    "합니다",
    "있는데",
    "이야기",
    "현장",
    "참",
    "하나",
    "같다",
    "생기나",
    "봅니다",
    "여름부터",
    "입주를",
    "llama",
    "mistral",
    "deepseek",
    "dense",
    "model",
    "legend",
    "compute",
    "multiplier",
    "expert",
    "experts",
    "activation",
    "hyperparameter",
    "minimax",
    "xiaomi",
    "tencent",
    "moonshot",
    "ant",
    "alibaba",
    "meituan",
    "대국이었죠",
    "나중에",
    "반추해",
    "보면",
    "나오고",
    "정도였던",
    "나오긴",
    "하지만",
    "세상이",
    "전혀",
    "모르던",
    "표현을",
    "많이",
    "썼는데",
    "기대가",
    "높지",
    "됐더라고요",
    "수였네요",
    "신사옥이",
    "있었는데",
    "그다음에",
    "정도였던",
    "표현을",
    "사람들이",
    "최승준",
    "노정석",
    "이진원",
    "인간이라면",
    "같다라는",
    "무엇인가",
    "흥미로운",
    "하는데요",
    "설명서가",
    "아닙니다",
    "프로젝트의",
    "에이전트의",
    "설계하다",
    "매니페스트",
    "접근하라",
    "개발자를",
    "시나리오",
    "연결하는",
    "인터페이스를",
    "심리학적",
    "어디인가",
    "context",
    "layer",
    "elon",
    "musk",
    "optimus",
    "tesla",
    "advantage",
    "market",
    "share",
    "distribution",
    "metric",
    "verifiable",
    "verify",
    "gemini",
}

SEMANTIC_TOKEN_ALLOW = {
    "대국",
    "해설자들",
    "기계학습",
    "머신러닝",
    "딥러닝",
    "알파고",
    "텐서플로",
}

KOREAN_ENDING_BLOCKLIST = (
    "는데",
    "더라고요",
    "였네요",
    "였죠",
    "했죠",
    "했고",
    "같다",
    "같은",
    "했다",
    "하고",
    "하는데",
    "입니다",
    "예요",
    "이에요",
)


def enrich_fragment_with_anchors(fragment: FragmentRecord) -> FragmentRecord:
    anchors = extract_fragment_anchors(fragment.raw_text)
    primary = anchors[0] if anchors else fragment.anchor
    return FragmentRecord(
        fragment_id=fragment.fragment_id,
        source_id=fragment.source_id,
        source_type=fragment.source_type,
        source_path=fragment.source_path,
        raw_text=fragment.raw_text,
        unit_scale=fragment.unit_scale,
        created_at=fragment.created_at,
        source_range=fragment.source_range,
        page_ref=fragment.page_ref,
        paragraph_index=fragment.paragraph_index,
        anchor=primary,
        anchors=anchors,
        D=fragment.D,
        I=fragment.I,
        S=fragment.S,
        scene=fragment.scene,
        flow=fragment.flow,
        time=fragment.time,
        confidence=fragment.confidence,
        provenance_log=fragment.provenance_log,
        metadata=fragment.metadata,
    )


def extract_fragment_anchors(text: str) -> List[FragmentAnchor]:
    anchors: List[FragmentAnchor] = []
    seen = set()
    tokens = TOKEN_RE.findall(text)

    def add(
        anchor_type: str,
        value: str,
        label: str = "",
        *,
        key: str = "",
        evidence_text: str = "",
        confidence: float = 0.7,
        aliases: Sequence[str] = (),
        origin: str = "rule",
    ) -> None:
        normalized = value.strip()
        if not normalized:
            return
        canonical = key or _canonical_key(anchor_type, normalized)
        dedupe = (anchor_type, canonical)
        if dedupe in seen:
            return
        seen.add(dedupe)
        anchors.append(
            FragmentAnchor(
                key=canonical,
                canonical_key=canonical,
                label=label or normalized,
                value=normalized,
                anchor_type=anchor_type,
                evidence_text=evidence_text or normalized,
                confidence=confidence,
                origin=origin,
                aliases=list(aliases),
                status="active",
            )
        )

    for file_name in FILE_RE.findall(text):
        add("source", file_name, key=_canonical_key("source", file_name), confidence=0.9, origin="source_rule")

    for key, label, evidence in _extract_object_candidates(text, tokens):
        add(
            "object",
            label,
            label=label,
            key=key,
            evidence_text=evidence,
            confidence=0.86,
            origin="object_rule",
        )
        if _count_type(anchors, "object") >= 3:
            break

    for key, label, evidence in _extract_semantic_candidates(text, tokens):
        add(
            "semantic",
            label,
            label=label,
            key=key,
            evidence_text=evidence,
            confidence=0.76,
            origin="semantic_rule" if key.startswith("semantic.") and label != evidence else "semantic_rule",
        )
        if _count_type(anchors, "semantic") >= 3:
            break

    for key, label, evidence, confidence in _infer_structural_anchors(text):
        add(
            "structural",
            key,
            label=label,
            key=key,
            evidence_text=evidence,
            confidence=confidence,
            origin="structural_rule",
        )
        if _count_type(anchors, "structural") >= 2:
            break

    return _order_anchors(anchors, text)


def _canonical_key(anchor_type: str, value: str) -> str:
    token = value.strip().lower()
    token = NON_WORD_RE.sub("_", token).strip("_")
    if anchor_type == "source":
        return f"source.{token}"
    if anchor_type == "structural":
        return value
    return f"{anchor_type}.{token}"


def _extract_object_candidates(text: str, tokens: Sequence[str]) -> List[Tuple[str, str, str]]:
    lowered_text = text.lower()
    results: List[Tuple[str, str, str]] = []
    seen = set()

    phrase_entries = sorted(KNOWN_OBJECTS.items(), key=lambda item: len(item[0]), reverse=True)
    for phrase, (key, label) in phrase_entries:
        phrase_lower = phrase.lower()
        if phrase_lower in lowered_text and key not in seen:
            if key == "object.org.deepmind" and "object.org.google_deepmind" in seen:
                continue
            if key == "object.org.google" and "object.org.google_deepmind" in seen:
                continue
            seen.add(key)
            results.append((key, label, phrase))

    for token in tokens:
        lowered = token.lower()
        if lowered in KNOWN_OBJECTS:
            key, label = KNOWN_OBJECTS[lowered]
            if key == "object.org.deepmind" and "object.org.google_deepmind" in seen:
                continue
            if key == "object.org.google" and "object.org.google_deepmind" in seen:
                continue
            if key not in seen:
                seen.add(key)
                results.append((key, label, token))
    return results


def _extract_semantic_candidates(text: str, tokens: Sequence[str]) -> List[Tuple[str, str, str]]:
    lowered_text = text.lower()
    results: List[Tuple[str, str, str]] = []
    seen = set()

    for key, label, evidence in SEMANTIC_RULES:
        if evidence.lower() in lowered_text and key not in seen:
            seen.add(key)
            results.append((key, label, evidence))

    for token in tokens:
        if not _semantic_token_allowed(token):
            continue
        canonical = _canonical_key("semantic", token)
        if canonical in seen:
            continue
        seen.add(canonical)
        results.append((canonical, token, token))
        if len(results) >= 3:
            break
    return results


def _semantic_token_allowed(token: str) -> bool:
    lowered = token.lower()
    if lowered in STOP_TERMS or lowered in KNOWN_OBJECTS:
        return False
    if len(token) < 3:
        return False
    if any(lowered.endswith(ending) for ending in KOREAN_ENDING_BLOCKLIST):
        return False
    if _looks_like_korean_name(token):
        return False
    if token in SEMANTIC_TOKEN_ALLOW:
        return True
    if re.fullmatch(r"[A-Za-z][A-Za-z0-9_+-]{3,}", token):
        return True
    return False


def _looks_like_korean_name(token: str) -> bool:
    return bool(re.fullmatch(r"[가-힣]{3}", token))


def _infer_structural_anchors(text: str) -> List[Tuple[str, str, str, float]]:
    lowered = text.lower()
    anchors: List[Tuple[str, str, str, float]] = []
    seen = set()
    for key, evidence, confidence in STRUCTURAL_RULES:
        if evidence.lower() in lowered and key not in seen:
            seen.add(key)
            anchors.append((key, key.replace("structural.", ""), evidence, confidence))
    return anchors[:2]


def _count_type(anchors: Sequence[FragmentAnchor], anchor_type: str) -> int:
    return sum(1 for anchor in anchors if anchor.anchor_type == anchor_type)


def _order_anchors(anchors: Sequence[FragmentAnchor], text: str) -> List[FragmentAnchor]:
    text_lower = text.lower()
    document_like = "claude.md" in text_lower or "manifest" in text_lower or "발표문" in text_lower

    def score(anchor: FragmentAnchor) -> tuple:
        base = {
            "object": 0,
            "semantic": 1,
            "structural": 2,
            "source": 3,
        }.get(anchor.anchor_type, 4)

        if document_like and anchor.anchor_type == "source":
            base += 3
        if document_like and anchor.key == "object.system.claude":
            base += 1
        if anchor.origin == "semantic_rule":
            base -= 1
        if anchor.anchor_type == "semantic" and anchor.origin == "rule":
            base += 2

        return (base, -float(anchor.confidence), anchor.key)

    return sorted(list(anchors), key=score)
