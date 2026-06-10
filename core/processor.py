"""
Rule-based processor for Smart Content Purifier & Summary Hub MVP v0.1.1.

This module intentionally avoids heavy AI dependencies in MVP v0.1.1.
The goal is to make the first version fast, stable, and easy to deploy
on Hugging Face Spaces free CPU.
"""

from __future__ import annotations

import re
from typing import List

from core.cleaner import clean_text


IMPORTANT_KEYWORDS = (
    "penting", "utama", "kesimpulan", "masalah", "solusi", "target",
    "tujuan", "manfaat", "risiko", "hasil", "strategi", "langkah",
    "fitur", "pengguna", "produk", "konten", "ringkasan", "belajar",
)

KNOWN_ABBREVIATIONS = (
    "dr.", "prof.", "mr.", "mrs.", "ms.", "jr.", "sr.", "vs.", "etc.",
    "dll.", "dst.", "dsb.", "no.", "s.pd.", "m.pd.", "s.kom.", "m.kom.",
)

DOT_PLACEHOLDER = "<dot>"

# Split sentences after sentence-ending punctuation. This stays lightweight and
# avoids extra NLP dependencies while supporting common quotes and brackets.
_SENTENCE_SPLIT_PATTERN = re.compile(
    r"(?<=[.!?])(?:[\"'\)\]\}]*)\s+(?=[A-Z0-9\"'\(\[])",
    flags=re.MULTILINE,
)


def _protect_abbreviations(text: str) -> str:
    """Protect known abbreviations from being split as sentence endings."""
    protected = text
    for abbreviation in KNOWN_ABBREVIATIONS:
        safe_abbreviation = abbreviation.replace(".", DOT_PLACEHOLDER)
        protected = re.sub(
            re.escape(abbreviation),
            safe_abbreviation,
            protected,
            flags=re.IGNORECASE,
        )
    return protected


def _restore_abbreviations(text: str) -> str:
    """Restore protected abbreviation dots."""
    return text.replace(DOT_PLACEHOLDER, ".")


def _split_sentences(text: str) -> List[str]:
    """Split cleaned text into readable sentences using a safer regex."""
    cleaned = clean_text(text)
    if not cleaned:
        return []

    normalized = re.sub(r"\s+", " ", cleaned.replace("\n", " ")).strip()
    if not normalized:
        return []

    protected = _protect_abbreviations(normalized)
    parts = _SENTENCE_SPLIT_PATTERN.split(protected)
    sentences = []

    for part in parts:
        sentence = _restore_abbreviations(part.strip())
        if not sentence:
            continue
        if len(sentence.split()) < 4:
            continue
        sentences.append(sentence)

    if not sentences and normalized:
        sentences = [normalized]

    return sentences


def _score_sentence(sentence: str, position: int, total: int) -> float:
    """Score a sentence using simple rule-based signals."""
    words = sentence.split()
    lower = sentence.lower()

    score = 0.0

    if 8 <= len(words) <= 28:
        score += 2.0
    elif len(words) <= 40:
        score += 1.0

    for keyword in IMPORTANT_KEYWORDS:
        if keyword in lower:
            score += 1.0

    if position == 0:
        score += 1.5
    elif position == total - 1:
        score += 0.8

    if any(marker in lower for marker in ["karena", "sehingga", "agar", "untuk", "dengan"]):
        score += 0.7

    return score


def _rank_sentences(sentences: List[str]) -> List[str]:
    """Rank sentences by importance while preserving final output readability."""
    total = len(sentences)
    ranked = []

    for index, sentence in enumerate(sentences):
        ranked.append((_score_sentence(sentence, index, total), index, sentence))

    ranked.sort(key=lambda item: (-item[0], item[1]))
    return [item[2] for item in ranked]


def short_summary(text: str, max_sentences: int = 5) -> str:
    """
    Create a short summary using rule-based sentence selection.

    Args:
        text: Raw or cleaned text.
        max_sentences: Maximum number of summary sentences.

    Returns:
        Summary text containing around 3-5 important sentences.
    """
    cleaned = clean_text(text)
    if not cleaned:
        return "Tidak ada teks yang bisa diringkas."

    sentences = _split_sentences(cleaned)
    if len(sentences) <= max_sentences:
        return " ".join(sentences).strip()

    ranked = _rank_sentences(sentences)
    selected = ranked[:max(3, min(max_sentences, len(ranked)))]

    # Keep original order for easier reading.
    selected_set = set(selected)
    ordered = [sentence for sentence in sentences if sentence in selected_set]

    return " ".join(ordered).strip()


def extract_key_points(text: str, max_points: int = 8) -> str:
    """
    Extract key points from text as Markdown bullet list.

    Args:
        text: Raw or cleaned text.
        max_points: Maximum number of bullet points.

    Returns:
        Markdown bullet list.
    """
    cleaned = clean_text(text)
    if not cleaned:
        return "- Tidak ada teks yang bisa diambil poin pentingnya."

    sentences = _split_sentences(cleaned)
    if not sentences:
        return "- Tidak ada poin penting yang ditemukan."

    ranked = _rank_sentences(sentences)
    selected = ranked[:max(1, min(max_points, len(ranked)))]

    points = []
    seen = set()

    for sentence in selected:
        point = sentence.strip(" -•\t\n")
        if not point:
            continue
        normalized = point.lower()
        if normalized in seen:
            continue
        seen.add(normalized)
        if not point.endswith((".", "!", "?")):
            point += "."
        points.append(f"- {point}")

    return "\n".join(points) if points else "- Tidak ada poin penting yang ditemukan."


def process_text(text: str, mode: str) -> str:
    """
    Process text according to the selected MVP mode.

    Active MVP modes:
    - Clean Text
    - Short Summary
    - Key Points

    Unknown modes fall back to Clean Text.
    """
    selected_mode = (mode or "Clean Text").strip()

    if selected_mode == "Clean Text":
        return clean_text(text)

    if selected_mode == "Short Summary":
        return short_summary(text)

    if selected_mode == "Key Points":
        return extract_key_points(text)

    return clean_text(text)


def process(text: str, mode: str) -> str:
    """Backward-compatible alias for process_text."""
    return process_text(text, mode)


__all__ = ["short_summary", "extract_key_points", "process_text", "process"]
