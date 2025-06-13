# Conversation Image Generator - access website [here](https://imagegen-jzaskmdzugdt3xrmvsakna.streamlit.app/)

A Streamlit‐powered tool that lets you **record live conversations** or **upload existing transcripts** (in virtually any language), **extract the speaker’s key ideas**, and **turn them into evocative images** using an AI image‐generation model.

---

## Features

- **Live recording**: Capture audio from your microphone and transcribe in real time.  
- **File upload**: Drop in an audio or text transcript (MP3, WAV, TXT, etc.) and process it immediately.  
- **Multi‐language support**: Works out of the box with English, Chinese, Spanish, and most other languages.  
- **Key‐idea extraction**: Uses an LLM to distill the most important user insights from free‐form conversation.  
- **Image generation**: Feeds distilled prompts into an AI image‐generation backend to produce a shareable visual.  
- **Configurable backends**: Swap between OpenAI, Hugging Face, or your own hosted model.

---

## Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/conversation-image-generator.git
   cd conversation-image-generator
   python3 -m venv .venv
   source .venv/bin/activate    # Mac/Linux
   .\.venv\Scripts\activate     # Windows PowerShell
   pip install -r requirements.txt

### Create the .streamlit/secrets.toml and plug in your own API key
API_KEY_1={assembly-AI_API_key}  
API_KEY_2={deepseek-v3_API_key}  
API_KEY_3={huggingFaceAPI_key}  

