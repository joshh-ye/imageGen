from huggingface_hub import InferenceClient
import streamlit as st

client = InferenceClient(
    provider="nebius",
    api_key=st.secrets["API_KEY_3"]
)


def image_gen(prompt: str):
    # output is a PIL.Image object
    image = client.text_to_image(
        prompt,
        model="black-forest-labs/FLUX.1-dev",
    )
    return image
