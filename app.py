import streamlit as st
import numpy as np
import pickle
import gdown
import os

# ================= GOOGLE DRIVE LINKS =================

MODEL_URL = "https://drive.google.com/uc?export=download&id=1WpZKQk-UFtbTwuszxaGKmmoJRYRGrNCC"
SCALER_URL = "https://drive.google.com/uc?export=download&id=1st3SO4Imz-MJX9gYVHEcJICfiWgbVSVL"

# ================= DOWNLOAD FILES =================

try:
if not os.path.exists("model.pkl"):
gdown.download(MODEL_URL, "model.pkl", quiet=False, fuzzy=True)

```
if not os.path.exists("scaler.pkl"):
    gdown.download(SCALER_URL, "scaler.pkl", quiet=False, fuzzy=True)
```

except Exception as e:
st.error(f"Download Error: {e}")

# ================= LOAD FILES =================

if os.path.exists("model.pkl") and os.path.exists("scaler.pkl"):
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
else:
st.error("❌ Model or Scaler file not found!")
st.stop()

# ================= PAGE CONFIG =================

st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺", layout="centered")

# ================= TITLE =================

st.title("🩺 Diabetes Prediction System")
st.markdown("Predict whether a person is diabetic based on medical data")

# ================= INPUT FIELDS =================

preg = st.number_input("Pregnancies", 0, 20)
glu = st.number_input("Glucose", 0, 200)
bp = st.number_input("Blood Pressure", 0, 150)
skin = st.number_input("Skin Thickness", 0, 100)
ins = st.number_input("Insulin", 0, 900)
bmi = st.number_input("BMI", 0.0, 70.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0)
age = st.number_input("Age", 1, 120)

# ================= PREDICTION =================

if st.button("🔍 Predict"):

```
data = np.array([[preg, glu, bp, skin, ins, bmi, dpf, age]])

# APPLY SCALING
data = scaler.transform(data)

prediction = model.predict(data)

st.subheader("Result")

if prediction[0] == 1:
    st.error("⚠️ Diabetic")
else:
    st.success("✅ Not Diabetic")
```

# ================= FOOTER =================

st.markdown("---")
st.markdown(
"<center>👨‍💻 Created by <b>Amol Satpute</b></center>",
unsafe_allow_html=True
)
