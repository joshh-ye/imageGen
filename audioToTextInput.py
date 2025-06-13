# Install the assemblyai package by executing the command "pip install assemblyai"

import assemblyai as aai
import streamlit as st

aai.settings.api_key = st.secrets["API_KEY_1"]

# audio_file = "./local_file.mp3"

##for international convertion
config = aai.TranscriptionConfig(
    speech_model=aai.SpeechModel.universal
    , language_detection=True
)


# For us (cheaper)
# config = aai.TranscriptionConfig(
#     speech_model=aai.SpeechModel.nano
# )

def transcribe_file(path: str) -> str:
    """
    Send the file at `path` to AssemblyAI and return the transcript text.
    Raises RuntimeError if AssemblyAI returns an error.
    """
    audio_file = path
    transcript = aai.Transcriber(config=config).transcribe(audio_file)

    if transcript.status == "error":
        raise RuntimeError(f"Transcription failed: {transcript.error}")
    return transcript.text
