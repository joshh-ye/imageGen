from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

client = InferenceClient(
    provider="nebius",
    api_key=os.getenv('API_KEY_3')
)


def image_gen(prompt: str):
    # output is a PIL.Image object
    image = client.text_to_image(
        prompt,
        model="black-forest-labs/FLUX.1-dev",
    )
    return image
