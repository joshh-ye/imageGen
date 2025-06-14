from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("API_KEY_2")
)


def extract_data(full_transcript: str) -> str:
    messages = [
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

    completion = client.chat.completions.create(
        model="deepseek/deepseek-chat:free",
        messages=messages,  # type: ignore[arg-type]
    )

    return completion.choices[0].message.content