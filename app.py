import gradio as gr
from core.processor import process
from core.exporter import export_markdown
from config.modes import LIST_MODES, MODE_DESCRIPTIONS, DEFAULT_MODE, EXAMPLE_INPUT

APP_TITLE = "Smart Content Purifier & Summary Hub"


def run_app(text, mode):
    if not text or not text.strip():
        return "Silakan masukkan teks terlebih dahulu."
    return process(text, mode)


def run_export(mode, output_text):
    if not output_text or not output_text.strip():
        return "Jalankan proses terlebih dahulu sebelum export Markdown."
    return export_markdown("Smart Content Purifier Output", output_text, mode)


def get_mode_description(mode):
    return MODE_DESCRIPTIONS.get(mode, MODE_DESCRIPTIONS.get(DEFAULT_MODE, ""))


with gr.Blocks(title=APP_TITLE) as demo:
    gr.Markdown("# Smart Content Purifier & Summary Hub")
    gr.Markdown("Alat sederhana untuk membersihkan, meringkas, dan mengambil poin penting dari teks Anda.")

    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(
                label="Input Teks",
                placeholder="Tempelkan teks Anda di sini...",
                lines=10,
                value=EXAMPLE_INPUT,
            )
            mode_radio = gr.Radio(
                choices=LIST_MODES,
                label="Pilih Mode",
                value=DEFAULT_MODE,
            )
            mode_note = gr.Markdown(get_mode_description(DEFAULT_MODE))
            submit_btn = gr.Button("Proses Teks", variant="primary")

        with gr.Column():
            output_text = gr.Textbox(
                label="Hasil",
                lines=15,
                interactive=False,
                show_copy_button=True,
            )
            export_btn = gr.Button("Export Markdown")
            export_output = gr.Textbox(
                label="Hasil Export Markdown",
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

    gr.Markdown("---")
    gr.Markdown("MVP v0.1 - Dibuat untuk kecepatan dan stabilitas.")

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
