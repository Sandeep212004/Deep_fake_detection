# app.py
import streamlit as st
from utils.face_utils import process_image
from utils.video_utils import process_video
from PIL import Image
import numpy as np
import tempfile
import json
import os
from datetime import datetime

st.set_page_config(page_title="DeepFake Detector", layout="centered", page_icon="🕵️")

st.markdown(
    """
    <h1 style='text-align: center;'>DeepFake Detector</h1>
    <p style='text-align: center; color: gray;'>Upload an image or video to detect possible deepfakes using our AI model.</p>
    """, 
    unsafe_allow_html=True
)

model_path = "cnn_model(2).h5"
history_file = "history.json"

def save_history(entry):
    if os.path.exists(history_file):
        with open(history_file, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(entry)
    with open(history_file, "w") as f:
        json.dump(data, f, indent=4)

option = st.radio("Select Input Type:", ("Image", "Video"), horizontal=True)

if option == "Image":
    uploaded_file = st.file_uploader("📷 Upload an Image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        with st.spinner("Processing Image..."):
            img = Image.open(uploaded_file).convert("RGB")
            img_np = np.array(img)

            st.image(img, caption="🖼️ Original Image", use_container_width=True)
            output_img, results = process_image(img_np, model_path)
            st.image(output_img, caption="📊 Prediction Result", use_container_width=True)

            if results:
                st.subheader("🔍 Detected Faces & Prediction:")
                for i, label in enumerate(results):
                    st.markdown(f"- **Face {i+1}**: {label}")
            else:
                st.warning("⚠️ No faces detected in the image.")

            save_history({
                "type": "Image",
                "filename": uploaded_file.name,
                "result": results,
                "timestamp": str(datetime.now())
            })

elif option == "Video":
    uploaded_video = st.file_uploader("🎥 Upload a Video", type=["mp4", "avi", "mov"])
    if uploaded_video:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())

        with st.spinner("Processing video... This may take a few moments ⏳"):
            result_path = process_video(tfile.name, model_path)

        st.success("✅ Video processed successfully!")
        st.video(result_path)

        save_history({
            "type": "Video",
            "filename": uploaded_video.name,
            "result": "Processed",
            "timestamp": str(datetime.now())
        })
