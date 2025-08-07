from openai import OpenAI
import streamlit as st

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["API_KEY_2"]
)

def extract_data(full_transcript: str) -> str:
    completion = client.chat.completions.create(
        extra_body={},
        model="mistralai/mistral-small-3.2-24b-instruct:free",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a creative AI that reads a transcript and distills a single, "
                    "evocative image description. Your job is:\n"
                    "1. Identify only the passage where one speaker describes how they see the world.\n"
                    "2. From that passage, generate a concise image description (no more than 20 words) "
                    "that could be fed into an image‐generation model. "
                    "Output only the image description—no extra text."
                )
            },
            {
                "role": "user",
                "content": (
                        "Here is the full conversation transcript:\n\n" + full_transcript
                )
            }
        ]
    )

    return completion.choices[0].message.content