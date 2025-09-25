# waste_classifier_app.py
import os
import streamlit as st
from tensorflow.keras.models import load_model, Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
import numpy as np

# -----------------------------
# Constants
# -----------------------------
MODEL_PATH = "waste_classifier_model.h5"
IMAGE_SIZE = (128, 128)
BATCH_SIZE = 4
CATEGORIES = ["Plastic", "Paper", "Glass", "Metal", "Organic"]
SAMPLE_DATA_DIR = "sample_images"  # small dataset folder pushed to GitHub

# -----------------------------
# Train model function (small demo)
# -----------------------------
def train_model():
    st.info("Training small demo model. This may take a minute...")
    
    datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
    
    train_gen = datagen.flow_from_directory(
        SAMPLE_DATA_DIR,
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="categorical",
        subset="training",
        shuffle=True
    )
    
    val_gen = datagen.flow_from_directory(
        SAMPLE_DATA_DIR,
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="categorical",
        subset="validation",
        shuffle=True
    )
    
    model = Sequential([
        Flatten(input_shape=(128,128,3)),
        Dense(64, activation='relu'),
        Dense(len(CATEGORIES), activation='softmax')
    ])
    
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(train_gen, validation_data=val_gen, epochs=5)  # small epochs for demo
    model.save(MODEL_PATH)
    st.success("Model trained and saved!")
    return model

# -----------------------------
# Load or train model
# -----------------------------
if os.path.exists(MODEL_PATH):
    model = load_model(MODEL_PATH)
else:
    model = train_model()

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("AI-Powered Waste Classifier ♻️")
st.write("Upload an image of waste and the AI will classify it.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    image = load_img(uploaded_file, target_size=IMAGE_SIZE)
    image_array = img_to_array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    prediction = model.predict(image_array)
    class_index = np.argmax(prediction)
    st.image(image, caption=f"Predicted: {CATEGORIES[class_index]}", use_column_width=True)
