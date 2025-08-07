import streamlit as st
import os, tempfile
import time

from audioToTextInput import transcribe_file
from textDataExtraction import extract_data
from image_gen import image_gen
from driveUpload import upload_to_folder

st.title("Transcribe audio, image generator")

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
            with tempfile.NamedTemporaryFile(suffix=".txt", delete=False, mode="w", encoding="utf-8") as tmp:
                tmp.write(text)
                tmp.flush()
                upload_to_folder(folder_id="1l_FSxH89e9iR6C32PcLWdqpJ3cdnEDPi", picPath=tmp.name)

        except Exception as err:
            st.error(str(err))

    os.remove(tmpFileAddress)

    with st.spinner("Extracting data"):
        image_prompt = extract_data(text)
        st.write("Done")

    if st.button("Generate image"):
        with st.spinner("Generating image"):
            pic = image_gen(image_prompt)
            st.image(pic, caption=image_prompt, use_container_width=True)

            with tempfile.NamedTemporaryFile(suffix='.jpg',
                                             delete=False) as tmp:
                pic.save(tmp.name, format="JPEG")

                with st.spinner("Uploading..."):
                    upload_to_folder(folder_id="1l_FSxH89e9iR6C32PcLWdqpJ3cdnEDPi", picPath=tmp.name)

                # this looks cool
                progress_text = "Uploading..."
                my_bar = st.progress(0, text=progress_text)
                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1, text=progress_text)
                time.sleep(1)
                my_bar.empty()

                st.write("All generated images can be found here: https://drive.google.com/drive/folders/1l_FSxH89e9iR6C32PcLWdqpJ3cdnEDPi?usp=sharing")
else:
    st.write("Awaiting audio")
