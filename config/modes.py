"""
Mode configuration for Smart Content Purifier & Summary Hub MVP v0.1.

Only active MVP modes are shown to users to avoid disappointing them with
features that are not ready yet.
"""

LIST_MODES = [
    "Clean Text",
    "Short Summary",
    "Key Points",
]

MODE_DESCRIPTIONS = {
    "Clean Text": "Membersihkan teks berantakan agar lebih rapi dan mudah dibaca.",
    "Short Summary": "Membuat ringkasan pendek 3-5 kalimat dari teks panjang.",
    "Key Points": "Mengambil poin-poin penting dalam bentuk daftar bullet.",
}

DEFAULT_MODE = "Clean Text"

EXAMPLE_INPUT = """
Banyak orang membuat konten dengan bantuan AI, tetapi hasil awalnya sering terlalu panjang,
berulang, dan belum siap dipakai. Karena itu, teks mentah perlu dibersihkan terlebih dahulu,
dirangkum, lalu diubah menjadi poin penting agar lebih mudah dipahami dan digunakan kembali.
""".strip()


__all__ = [
    "LIST_MODES",
    "MODE_DESCRIPTIONS",
    "DEFAULT_MODE",
    "EXAMPLE_INPUT",
]
