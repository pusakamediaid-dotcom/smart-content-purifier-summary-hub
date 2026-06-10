from core.cleaner import clean_text, count_sentences, count_words


def test_clean_text_removes_extra_spaces():
    result = clean_text("  This    text   has   extra   spaces .  ")

    assert result == "This text has extra spaces."


def test_clean_text_handles_empty_input():
    assert clean_text("") == ""
    assert clean_text(None) == ""


def test_count_words_counts_words():
    assert count_words("Clean text helps users work faster.") == 6


def test_count_sentences_counts_sentences():
    assert count_sentences("First sentence. Second sentence! Third sentence?") == 3
