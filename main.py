import streamlit as st
import os, tempfile

from audioToTextInput import transcribe_file
from textDataExtraction import extract_data
from image_gen import image_gen

st.title("Transcribe audio, image generator. 转录音频、图像生成器")

st.subheader("Data collection here")
recordedAudio = st.audio_input("Option 1: Click to record")

uploadedWav = st.file_uploader("option 2: Upload own .wav file or use an example file below")

with open('firstConvo.wav', 'rb') as f:
    exampleConvo = f.read()

with open('secondConvo(chinese).wav', 'rb') as f:
    exampleConvo2 = f.read()

st.download_button(
    label="Download example to test",
    data=exampleConvo,
    file_name="firstConvo.wav",
    mime="audio/wav",
)

st.download_button(
    label="下载示例",
    data=exampleConvo2,
    file_name="secondConvo(chinese).wav",
    mime="audio/wav",
)

audioWav = recordedAudio if recordedAudio is not None else uploadedWav

if audioWav:
    st.audio(audioWav)

    # create tmpFile
    with (tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as af):
        af.write(audioWav.read())
        tmpFileAddress = af.name

    with st.spinner("Transcribing"):
        try:
            text = transcribe_file(tmpFileAddress)
            st.text_area("Your conversation transcribed", text)
        except Exception as err:
            st.error(str(err))

    os.remove(tmpFileAddress)

    with st.spinner("Extracting data"):
        image_prompt = extract_data(text)
        st.write("Done")

    if st.button("Generate image"):
        with st.spinner("Generating image"):
            st.image(image_gen(image_prompt), caption=image_prompt, use_container_width=True)

else:
    st.write("Awaiting audio")
