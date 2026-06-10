import gradio as gr
from core.processor import process
from config.modes import LIST_MODES, MODE_DESCRIPTIONS, DEFAULT_MODE, EXAMPLE_INPUT

def run_app(text, mode):
    if not text or not text.strip():
        return "Silakan masukkan teks terlebih dahulu."
    return process(text, mode)

# UI Layout
with gr.Blocks(title="Smart Content Purifier & Summary Hub") as demo:
    gr.Markdown("# Smart Content Purifier & Summary Hub")
    gr.Markdown("Alat sederhana untuk membersihkan, meringkas, dan mengambil poin penting dari teks Anda.")
    
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(
                label="Input Teks", 
                placeholder="Tempelkan teks Anda di sini...", 
                lines=10,
                value=EXAMPLE_INPUT
            )
            mode_radio = gr.Radio(
                choices=LIST_MODES, 
                label="Pilih Mode", 
                value=DEFAULT_MODE
            )
            submit_btn = gr.Button("Proses Teks", variant="primary")
        
        with gr.Column():
            output_text = gr.Textbox(
                label="Hasil", 
                lines=15, 
                interactive=False
            )

    submit_btn.click(
        fn=run_app,
        inputs=[input_text, mode_radio],
        outputs=output_text
    )

    gr.Markdown("---")
    gr.Markdown("MVP v0.1 - Dibuat untuk kecepatan dan stabilitas.")

if __name__ == "__main__":
    demo.launch()
