import os
import gradio as gr
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def transcribe_audio(audio_file):
    """
    Transcribes uploaded or recorded audio using Whisper Large V3
    """
    if audio_file is None:
        return "Please upload or record an audio file."

    with open(audio_file, "rb") as audio:
        transcription = client.audio.transcriptions.create(
            file=audio,
            model="whisper-large-v3",
            response_format="verbose_json"
        )

    return transcription.text

# Gradio UI
with gr.Blocks(title="Speech-to-Text with Whisper Large V3") as demo:
    gr.Markdown(
        """
        # 🎙️ Speech-to-Text Application
        **Powered by Whisper Large V3 & Groq**
        
        Upload an audio file or record your voice to get real-time transcription.
        """
    )

    audio_input = gr.Audio(
        sources=["upload", "microphone"],
        type="filepath",
        label="Upload or Record Audio"
    )

    text_output = gr.Textbox(
        label="Transcribed Text",
        placeholder="Your transcription will appear here...",
        lines=6
    )

    transcribe_btn = gr.Button("Transcribe")

    transcribe_btn.click(
        fn=transcribe_audio,
        inputs=audio_input,
        outputs=text_output
    )

# Run app
if __name__ == "__main__":
    demo.launch(inbrowser=True)
