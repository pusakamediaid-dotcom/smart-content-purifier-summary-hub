"""
Rule-based text cleaner for Smart Content Purifier & Summary Hub.

This module is intentionally lightweight for MVP v0.1.
It uses only Python standard library modules, so it can run easily
on Hugging Face Spaces free CPU environments.
"""

import re
import unicodedata


_ALLOWED_CHARS_PATTERN = re.compile(
    r"[^A-Za-z0-9\s\.,!?;:\-\(\)\[\]\{\}\"'/%@#&+=_\n]"
)

_WORD_PATTERN = re.compile(r"\b[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)?\b")
_SENTENCE_PATTERN = re.compile(r"[^.!?]+[.!?]*")


_TRANSLATION_MAP = str.maketrans({
    "\u2018": "'",
    "\u2019": "'",
    "\u201c": '"',
    "\u201d": '"',
    "\u2013": " - ",
    "\u2014": " - ",
    "\u2212": "-",
    "\u2026": "...",
    "\u2022": "-",
    "\u00a0": " ",
})


def _to_text(value) -> str:
    """Convert any input value into a safe string."""
    if value is None:
        return ""
    return str(value)


def _normalize_newlines(text: str) -> str:
    """Normalize Windows/Mac line breaks into Unix-style line breaks."""
    return text.replace("\r\n", "\n").replace("\r", "\n")


def _normalize_unicode_to_ascii(text: str) -> str:
    """
    Convert common Unicode punctuation to ASCII and remove non-ASCII chars.

    Example:
    - smart quotes become normal quotes
    - long dashes become hyphen
    - emoji and unsupported symbols are removed
    """
    text = text.translate(_TRANSLATION_MAP)
    text = unicodedata.normalize("NFKD", text)
    return text.encode("ascii", "ignore").decode("ascii")


def _remove_unwanted_symbols(text: str) -> str:
    """Remove symbols that are not useful for plain text processing."""
    return _ALLOWED_CHARS_PATTERN.sub(" ", text)


def _fix_spacing_around_punctuation(text: str) -> str:
    """Fix common spacing issues around punctuation marks."""
    text = re.sub(r"\s+([,.!?;:])", r"\1", text)
    text = re.sub(r"([,.!?;:])([^\s\n,.!?;:])", r"\1 \2", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _reduce_repeated_punctuation(text: str) -> str:
    """Reduce excessive punctuation to a cleaner form."""
    text = re.sub(r"!{2,}", "!", text)
    text = re.sub(r"\?{2,}", "?", text)
    text = re.sub(r",{2,}", ",", text)
    text = re.sub(r"\.{4,}", "...", text)
    return text


def _remove_repeated_words(text: str) -> str:
    """
    Remove the same word repeated three or more times in a row.

    Example:
    "penting penting penting" becomes "penting".
    """
    pattern = re.compile(r"\b([A-Za-z0-9]+)(?:\s+\1\b){2,}", flags=re.IGNORECASE)
    previous = None

    while previous != text:
        previous = text
        text = pattern.sub(r"\1", text)

    return text


def _clean_paragraph(paragraph: str) -> str:
    """Clean a single paragraph while preserving readable sentence flow."""
    paragraph = re.sub(r"[\t ]+", " ", paragraph)
    paragraph = _reduce_repeated_punctuation(paragraph)
    paragraph = _fix_spacing_around_punctuation(paragraph)
    paragraph = _remove_repeated_words(paragraph)
    return paragraph.strip()


def clean_text(text) -> str:
    """
    Clean raw text using lightweight rule-based processing.

    Cleaning steps:
    1. Normalize newlines.
    2. Convert Unicode text to ASCII-safe text.
    3. Remove unnecessary symbols.
    4. Remove excessive blank lines.
    5. Trim and normalize paragraph spacing.
    6. Fix spacing around punctuation.
    7. Remove simple repeated words.

    Args:
        text: Raw text input from the user.

    Returns:
        A cleaned string. Returns an empty string if input is empty.
    """
    text = _to_text(text)
    if not text.strip():
        return ""

    text = _normalize_newlines(text)
    text = _normalize_unicode_to_ascii(text)
    text = _remove_unwanted_symbols(text)

    text = re.sub(r"\n\s*\n+", "\n\n", text)

    raw_paragraphs = re.split(r"\n\s*\n", text)
    cleaned_paragraphs = []

    for paragraph in raw_paragraphs:
        paragraph = " ".join(line.strip() for line in paragraph.split("\n") if line.strip())
        cleaned = _clean_paragraph(paragraph)
        if cleaned:
            cleaned_paragraphs.append(cleaned)

    return "\n\n".join(cleaned_paragraphs).strip()


def count_words(text) -> int:
    """
    Count words in the given text.

    Args:
        text: Text input from the user.

    Returns:
        Number of detected words.
    """
    text = _to_text(text)
    if not text.strip():
        return 0

    text = _normalize_unicode_to_ascii(text)
    return len(_WORD_PATTERN.findall(text))


def count_sentences(text) -> int:
    """
    Count sentences in the given text.

    Args:
        text: Text input from the user.

    Returns:
        Number of detected sentences. If text has words but no punctuation,
        it is counted as one sentence.
    """
    text = clean_text(text)
    if not text:
        return 0

    sentences = [s.strip() for s in _SENTENCE_PATTERN.findall(text) if s.strip()]
    return len(sentences) if sentences else 1


__all__ = ["clean_text", "count_words", "count_sentences"]
