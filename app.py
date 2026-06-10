import gradio as gr

from core.cleaner import count_words
from core.exporter import export_markdown
from core.processor import process
from config.modes import LIST_MODES, MODE_DESCRIPTIONS, DEFAULT_MODE, EXAMPLE_INPUT

APP_TITLE = "Smart Content Purifier & Summary Hub"
MIN_WORDS = 30
MAX_WORDS = 3000

UI_EXAMPLE_INPUT = """
Banyak tim membuat artikel, catatan meeting, dan materi belajar dengan bantuan AI.
Namun hasil awal sering terlalu panjang, berulang, dan belum siap dipakai langsung.
Karena itu, teks mentah perlu dibersihkan terlebih dahulu agar lebih rapi dan mudah dibaca.
Setelah teks bersih, pengguna dapat membuat ringkasan pendek atau mengambil poin penting.
Alur sederhana ini membantu konten menjadi lebih siap untuk dokumentasi, riset, dan publikasi.
""".strip() or EXAMPLE_INPUT

INTRO_TEXT = """
Bersihkan teks berantakan, buat ringkasan pendek, dan ambil poin penting dalam satu tempat.
MVP v0.1.1 ini memakai pemrosesan ringan agar tetap cepat, stabil, dan ramah untuk Hugging Face Free CPU.
"""

HELP_TEXT = """
**Cara pakai singkat:**
1. Tempel teks mentah di kolom input.
2. Pilih mode proses yang dibutuhkan.
3. Klik **Proses Teks**.
4. Klik **Export Markdown** jika ingin hasil siap salin dalam format Markdown.
"""

FOOTER_TEXT = """
---
**Smart Content Purifier & Summary Hub — MVP v0.1.1**  
Dibuat untuk portfolio AI app: sederhana, stabil, tanpa API berbayar, dan siap berjalan di Hugging Face Spaces.
"""


def validate_input(text: str) -> str | None:
    """Validate user input before processing."""
    if not text or not text.strip():
        return "⚠️ Silakan masukkan teks terlebih dahulu."

    word_count = count_words(text)

    if word_count < MIN_WORDS:
        return (
            f"⚠️ Teks terlalu pendek. Masukkan minimal {MIN_WORDS} kata "
            f"agar hasil lebih berguna. Saat ini: {word_count} kata."
        )

    if word_count > MAX_WORDS:
        return (
            f"⚠️ Teks terlalu panjang untuk MVP v0.1.1. "
            f"Gunakan maksimal {MAX_WORDS} kata. Saat ini: {word_count} kata."
        )

    return None


def run_app(text, mode):
    validation_error = validate_input(text)
    if validation_error:
        return validation_error

    try:
        result = process(text, mode)
        if not result or not result.strip():
            return "⚠️ Proses selesai, tetapi output kosong. Coba gunakan teks yang lebih jelas."
        return result
    except Exception as error:
        return (
            "⚠️ Terjadi error saat memproses teks. "
            "Aplikasi tetap aman, tetapi output belum bisa dibuat. "
            f"Detail singkat: {error}"
        )


def run_export(mode, output_text):
    if not output_text or not output_text.strip():
        return "⚠️ Jalankan proses terlebih dahulu sebelum export Markdown."

    if output_text.strip().startswith("⚠️"):
        return "⚠️ Export Markdown hanya bisa dibuat dari output proses yang valid."

    try:
        return export_markdown("Smart Content Purifier Output", output_text, mode)
    except Exception as error:
        return f"⚠️ Export Markdown gagal. Detail singkat: {error}"


def get_mode_description(mode):
    active_mode = mode or DEFAULT_MODE
    description = MODE_DESCRIPTIONS.get(active_mode, MODE_DESCRIPTIONS.get(DEFAULT_MODE, ""))
    return f"**Mode aktif:** {active_mode}\n\n{description}"


with gr.Blocks(title=APP_TITLE) as demo:
    gr.Markdown("# Smart Content Purifier & Summary Hub")
    gr.Markdown(INTRO_TEXT)
    gr.Markdown(HELP_TEXT)

    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(
                label="Input teks mentah",
                placeholder=(
                    "Tempel artikel, catatan meeting, materi belajar, atau draft konten di sini. "
                    f"Gunakan minimal {MIN_WORDS} kata dan maksimal {MAX_WORDS} kata."
                ),
                lines=12,
                value=UI_EXAMPLE_INPUT,
                show_copy_button=True,
            )
            mode_radio = gr.Radio(
                choices=LIST_MODES,
                label="Pilih jenis pemrosesan",
                value=DEFAULT_MODE,
            )
            mode_note = gr.Markdown(get_mode_description(DEFAULT_MODE))
            submit_btn = gr.Button("Proses Teks", variant="primary")

        with gr.Column():
            output_text = gr.Textbox(
                label="Hasil pemrosesan",
                placeholder="Hasil Clean Text, Short Summary, atau Key Points akan muncul di sini.",
                lines=15,
                interactive=False,
                show_copy_button=True,
            )
            export_btn = gr.Button("Export Markdown")
            export_output = gr.Textbox(
                label="Hasil export Markdown",
                placeholder="Klik Export Markdown setelah hasil pemrosesan muncul.",
                lines=10,
                interactive=False,
                show_copy_button=True,
            )

    submit_btn.click(
        fn=run_app,
        inputs=[input_text, mode_radio],
        outputs=output_text,
    )
    export_btn.click(
        fn=run_export,
        inputs=[mode_radio, output_text],
        outputs=export_output,
    )
    mode_radio.change(
        fn=get_mode_description,
        inputs=mode_radio,
        outputs=mode_note,
    )

    gr.Markdown(FOOTER_TEXT)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
