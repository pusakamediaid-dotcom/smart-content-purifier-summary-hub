"""
Markdown exporter for Smart Content Purifier & Summary Hub.

MVP v0.1 returns export content as strings so users can copy the result
directly from the interface. File download can be added in later versions.
"""

from __future__ import annotations

from datetime import datetime


def _safe_text(value) -> str:
    """Convert any value into a safe string."""
    if value is None:
        return ""
    return str(value).strip()


def _timestamp() -> str:
    """Return timestamp in Indonesian-friendly format."""
    return datetime.now().strftime("%d-%m-%Y %H:%M")


def export_markdown(title: str, content: str, mode: str) -> str:
    """
    Return a clean Markdown export string.

    Format follows MVP v0.1 standard:
    # Smart Content Purifier Output
    Mode:
    [Nama Mode]
    Tanggal:
    [Tanggal Proses]
    Hasil:
    [Output]
    """
    try:
        safe_title = _safe_text(title) or "Smart Content Purifier Output"
        safe_content = _safe_text(content) or "Tidak ada hasil untuk diekspor."
        safe_mode = _safe_text(mode) or "Clean Text"

        return "\n".join([
            f"# {safe_title}",
            "",
            "Mode:",
            safe_mode,
            "",
            "Tanggal:",
            _timestamp(),
            "",
            "Hasil:",
            safe_content,
            "",
        ]).strip()
    except Exception as error:
        return f"Gagal membuat export Markdown: {error}"


def export_plain(content: str) -> str:
    """Return plain text content for copy-paste usage."""
    try:
        return _safe_text(content)
    except Exception:
        return ""


__all__ = ["export_markdown", "export_plain"]
