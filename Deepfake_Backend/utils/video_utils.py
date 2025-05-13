import os
import cv2
import numpy as np
import tensorflow as tf
import tempfile

model = None

# Load the DNN face detection model from ../models
base_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(base_dir, "../models")
prototxt_path = os.path.join(model_dir, "deploy.prototxt")
weights_path = os.path.join(model_dir, "res10_300x300_ssd_iter_140000.caffemodel")
face_net = cv2.dnn.readNetFromCaffe(prototxt_path, weights_path)

def load_model_once(model_path):
    global model
    if model is None:
        model = tf.keras.models.load_model(model_path)

def preprocess_image(face):
    face = cv2.resize(face, (128, 128), interpolation=cv2.INTER_AREA)
    face = face / 255.0
    return np.expand_dims(face, axis=0)

def process_video(video_path, model_path, conf_threshold=0.5):
    load_model_once(model_path)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise Exception("Failed to open video file.")

    # Video properties
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = int(cap.get(cv2.CAP_PROP_FPS))

    # Output video file
    temp_output = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    out = cv2.VideoWriter(temp_output.name,
                          cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Face detection on frame
        blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300),
                                     (104.0, 177.0, 123.0), swapRB=False, crop=False)
        face_net.setInput(blob)
        detections = face_net.forward()

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > conf_threshold:
                (h, w) = frame.shape[:2]
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (x1, y1, x2, y2) = box.astype("int")

                pad = 20
                x1 = max(0, x1 - pad)
                y1 = max(0, y1 - pad)
                x2 = min(w, x2 + pad)
                y2 = min(h, y2 + pad)

                face = frame[y1:y2, x1:x2]
                if face.shape[0] < 50 or face.shape[1] < 50:
                    continue

                processed = preprocess_image(face)
                pred = model.predict(processed, verbose=0)[0][0]
                label = "Deepfake" if pred > 0.5 else "Real"
                color = (0, 0, 255) if label == "Deepfake" else (0, 255, 0)

                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, f"{label} ({confidence:.2f})", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        out.write(frame)

    cap.release()
    out.release()
    return temp_output.name

def extract_frames(video_path, max_frames=10):
    cap = cv2.VideoCapture(video_path)
    frames = []
    frame_count = 0

    while cap.isOpened() and frame_count < max_frames:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
        frame_count += 1

    cap.release()
    return frames
