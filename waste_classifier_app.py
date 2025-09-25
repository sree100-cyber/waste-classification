import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

model = load_model("waste_classifier_model.h5")

categories = ['Plastic', 'Paper', 'Glass', 'Metal', 'Organic']
bin_suggestions = {
    'Plastic': 'Blue Bin',
    'Paper': 'Green Bin',
    'Glass': 'Yellow Bin',
    'Metal': 'Red Bin',
    'Organic': 'Brown Bin'
}

st.title("AI-Powered Waste Classifier")
st.write("Upload an image of waste, and the system will suggest the correct bin.")

uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_column_width=True)
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)
    predicted_category = categories[class_index]
    st.success(f"Predicted Category: {predicted_category}")
    st.info(f"Suggested Bin: {bin_suggestions[predicted_category]}")
