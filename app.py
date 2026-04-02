import streamlit as st
import numpy as np
import pickle

# ================= LOAD MODEL =================
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ================= PAGE CONFIG =================
st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺", layout="wide")

# ================= SIDEBAR =================
st.sidebar.title("📌 Project Info")
st.sidebar.info("""
Diabetes Prediction using Decision Tree

✔ SMOTE Applied  
✔ Hyperparameter Tuned  
✔ Pruned Model  
✔ Accuracy: ~77%
""")

# ================= TITLE =================
st.title("🩺 Diabetes Prediction System")
st.markdown("Enter patient details to predict diabetes")

# ================= INPUT =================
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Pregnancies", 0, 20)
    glucose = st.number_input("Glucose", 0, 200)
    bp = st.number_input("Blood Pressure", 0, 150)
    skin = st.number_input("Skin Thickness", 0, 100)

with col2:
    insulin = st.number_input("Insulin", 0, 900)
    bmi = st.number_input("BMI", 0.0, 70.0)
    dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0)
    age = st.number_input("Age", 1, 120)

# ================= PREPROCESS FUNCTION =================
def preprocess(data):
    data = np.array(data).reshape(1, -1)

    # Log transform (same as training)
    cols_to_log = [2,3,4,5,6,7]  # index based (BloodPressure → Age)
    for i in cols_to_log:
        data[0][i] = np.log1p(data[0][i])

    # Scale
    data_scaled = scaler.transform(data[:,1:])  # excluding pregnancies

    # Combine back
    final_data = np.concatenate((data[:,0].reshape(-1,1), data_scaled), axis=1)

    return final_data

# ================= PREDICTION =================
if st.button("🔍 Predict"):
    input_data = [pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]

    processed = preprocess(input_data)

    prediction = model.predict(processed)

    st.subheader("Result")

    if prediction[0] == 1:
        st.error("⚠️ Diabetic")
    else:
        st.success("✅ Not Diabetic")

# ================= FOOTER =================
st.markdown("---")
st.markdown("<center>👨‍💻 Created by <b>Amol Satpute</b></center>", unsafe_allow_html=True)
