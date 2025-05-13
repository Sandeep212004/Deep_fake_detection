import streamlit as st

st.set_page_config(page_title="About", layout="centered")

st.markdown("""
<h2 style='text-align: center;'>ℹ️ About This App</h2>

<p style='text-align: justify;'>
The <strong>DeepFake Detector</strong> is a user-friendly web application built to help individuals verify the authenticity of images and videos. With the increasing use of digitally manipulated content, this tool plays an important role in identifying altered or fake faces. It is ideal for journalists, researchers, educators, and everyday users who wish to check visual content for signs of tampering.
</p>

---

### 🔍 What Does It Do?

This app analyzes uploaded media to detect whether the faces present are real or potentially manipulated. It does this using a pre-trained Convolutional Neural Network (CNN) model trained on a dataset of both authentic and deepfake samples.

---

### ⚙️ Key Features

- **📷 Upload Media**: Supports both image and video uploads.
- **🧠 Face Detection & Classification**: Automatically detects faces and checks for signs of manipulation.
- **📊 Visual Feedback**: Displays results clearly by marking each detected face as “Real” or “DeepFake.”
- **📁 History Tracking**: Keeps a record of all analyses with time, file type, and results for easy reference.

---

### 🛠️ Technologies Used

- **Python** – The core programming language behind the app.
- **Streamlit** – Used to build an interactive, browser-based interface.
- **CNN Model (H5)** – For face analysis and classification.
- **PIL & OpenCV** – For image and video processing.
- **NumPy & JSON** – For data handling and result storage.

---

### 👨‍💻 Developer Note

This project was created out of a growing need to detect misinformation in visual content. It’s a simple tool with powerful functionality, built with care using open-source technologies.

Developed with ❤️ using Python, Streamlit, and Machine Learning.

""", unsafe_allow_html=True)
