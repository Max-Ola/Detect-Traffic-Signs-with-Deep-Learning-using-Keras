import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

model = tf.keras.models.load_model("traffic_sign_model.h5")

st.title("🚦 Traffic Sign Classifier")
uploaded_file = st.file_uploader("Upload a traffic sign image...", type=["jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).resize((32, 32))
    img_array = np.expand_dims(np.array(image) / 255.0, axis=0)
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction)
    st.image(image, caption=f"Prediction: {predicted_class} (Confidence: {np.max(prediction):.2f})")