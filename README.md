# Deep Fake Detection

## Overview

This project aims to detect deepfake videos by analyzing facial features and inconsistencies using deep learning techniques. It includes a Python-based backend and a simple frontend for uploading videos and viewing results.

## Features

- 🔍 Deepfake Detection using deep learning
- 🌐 User-friendly Streamlit frontend
- 🔧 Modular backend for video processing and face analysis
- 🧠 Ready for future model integration and improvements

## Directory Structure

Deep_fake_detection/
- Deepfake_Backend/ # Backend code for detection and processing
- deepfake_frontend/ # Frontend interface using Streamlit
─ requirements.txt # Python dependencies
─ README.md # Project documentation

markdown
Copy
Edit

## Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package installer)
- Optional: virtualenv for isolated environments

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sandeep212004/Deep_fake_detection.git
   cd Deep_fake_detection
Set up a virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Usage
Run Backend
Navigate to backend:

bash
Copy
Edit
cd Deepfake_Backend
python app.py
This will start the backend on http://localhost:5000/.

Run Frontend
Open a new terminal and run:

bash
Copy
Edit
cd deepfake_frontend
streamlit run app.py
Access the frontend at http://localhost:8501/
