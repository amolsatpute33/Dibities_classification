import streamlit as st
import numpy as np
import pickle
import gdown
import os


MODEL_URL = "https://drive.google.com/uc?export=download&id=1WpZKQk-UFtbTwuszxaGKmmoJRYRGrNCC"
SCALER_URL = "https://drive.google.com/uc?export=download&id=1st3SO4Imz-MJX9gYVHEcJICfiWgbVSVL"

if not os.path.exists("model.pkl"):
gdown.download(MODEL_URL, "model.pkl", quiet=False)

if not os.path.exists("scaler.pkl"):
gdown.download(SCALER_URL, "scaler.pkl", quiet=False)


model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))


st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺")

st.title("🩺 Diabetes Prediction System")

preg = st.number_input("Pregnancies", 0, 20)
glu = st.number_input("Glucose", 0, 200)
bp = st.number_input("Blood Pressure", 0, 150)
skin = st.number_input("Skin Thickness", 0, 100)
ins = st.number_input("Insulin", 0, 900)
bmi = st.number_input("BMI", 0.0, 70.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0)
age = st.number_input("Age", 1, 120)

if st.button("Predict"):

data = np.array([[preg, glu, bp, skin, ins, bmi, dpf, age]])

# 🔥 APPLY SCALING
data = scaler.transform(data)

prediction = model.predict(data)

if prediction[0] == 1:
    st.error("⚠️ Diabetic")
else:
    st.success("✅ Not Diabetic")

