# AI-Powered Waste Classifier

## Overview
This project is an AI-based system that automatically classifies waste into categories:
- Plastic
- Paper
- Glass
- Metal
- Organic

The system suggests the correct bin for proper disposal. It can be used as a simple web app and can later be integrated into smart dustbins.

## Features
- Upload an image of waste
- Predicts the waste category using AI
- Suggests the correct disposal bin

## Requirements
- Python 3.8+
- TensorFlow
- Streamlit
- Pillow
- NumPy

## Installation
1. Clone the repository:
```bash
git clone <your-repo-link>
cd waste-classifier
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Place your trained model as `waste_classifier_model.h5` in the folder.

## Run the App
```bash
streamlit run waste_classifier_app.py
```

## Demo
Upload an image and see the predicted waste category and suggested bin instantly.

## Future Work
- Integration into smart dustbins
- Mobile app version for public use
