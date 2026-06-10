from core.processor import extract_key_points, process_text, short_summary


SAMPLE_TEXT = """
Smart Content Purifier helps users clean messy text before they reuse it.
The main problem is that raw notes, drafts, and AI outputs are often too long and repetitive.
This project provides a lightweight solution for cleaning text, creating summaries, and extracting key points.
The goal is to keep the MVP simple, stable, and easy to deploy on Hugging Face Spaces.
The result is useful for portfolio documentation, study notes, and content preparation.
""".strip()


def test_short_summary_returns_non_empty_output():
    result = short_summary(SAMPLE_TEXT)

    assert isinstance(result, str)
    assert result.strip()


def test_extract_key_points_returns_bullet_list():
    result = extract_key_points(SAMPLE_TEXT)

    assert isinstance(result, str)
    assert result.strip()
    assert result.lstrip().startswith("-")


def test_process_text_clean_text_mode_runs():
    result = process_text("Messy     text   with   extra spaces.", "Clean Text")

    assert result == "Messy text with extra spaces."


def test_process_text_short_summary_mode_runs():
    result = process_text(SAMPLE_TEXT, "Short Summary")

    assert isinstance(result, str)
    assert result.strip()


def test_process_text_key_points_mode_runs():
    result = process_text(SAMPLE_TEXT, "Key Points")

    assert isinstance(result, str)
    assert result.strip()
    assert result.lstrip().startswith("-")


def test_unknown_mode_falls_back_to_clean_text():
    result = process_text("Messy     text   with   extra spaces.", "Unknown Mode")

    assert result == "Messy text with extra spaces."
