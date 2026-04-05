# 🩺 Diabetes Prediction using Decision Tree Classifier

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![ML](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

---

## 📌 Project Overview

This project predicts whether a person is diabetic or not using a **Decision Tree Classifier** based on medical attributes such as glucose level, blood pressure, BMI, and age.

---

## 💡 Problem Statement

The goal of this project is to build a machine learning model that can **predict diabetes early** using patient health data.

---

## 📊 Dataset Information

* 📁 Dataset: `diabetes.csv`
* 📏 Shape: **768 rows × 9 columns**
* 🎯 Target Variable: `Outcome` (0 = Non-Diabetic, 1 = Diabetic)
* 🔢 Features:

  * Pregnancies
  * Glucose
  * Blood Pressure
  * Skin Thickness
  * Insulin
  * BMI
  * Diabetes Pedigree Function
  * Age

---

## 🧠 Domain Analysis

This project falls under **Healthcare Analytics**, focusing on early detection of diabetes using clinical data and predictive modeling techniques.

---

## 🔍 Exploratory Data Analysis (EDA)

* 📉 **Histograms** → Distribution of features
* 📊 **Countplots** → Class balance
* 📦 **Boxplots** → Outlier detection
* 🔗 **Scatter Plots** → Feature relationships

---

## 🧼 Data Preprocessing

* Replaced invalid zero values with median
* Handled outliers using IQR method
* Applied log transformation for skewed features
* Feature scaling using **MinMaxScaler**

---

## ⚙️ Model Building

* 🤖 Algorithm: **Decision Tree Classifier**
* ⚖️ Handling Imbalance: **SMOTE**
* 🔀 Train-Test Split: **80:20**
* 📏 Evaluation Metrics:

  * Accuracy
  * Confusion Matrix
  * Classification Report

---

## 📉 Model Evaluation

| Model                    | Training Accuracy | Testing Accuracy |
| ------------------------ | ----------------- | ---------------- |
| Decision Tree            | 100%              | 71.4%            |
| GridSearchCV Tuned       | 84.2%             | 72.1%            |
| RandomizedSearchCV Tuned | 84.2%             | 72.7%            |
| Cost Complexity Pruning  | 77.0%             | 77.2%            |

---

## ⚠️ Overfitting Issue

Initially, the model showed:

* Training Accuracy: **72%**
* Testing Accuracy: **1%**

👉 This indicated **overfitting**.

### ✅ Solution

* Applied **Hyperparameter Tuning**
* Used **GridSearchCV & RandomizedSearchCV**
* Applied **Cost Complexity Pruning**

---

## 🏆 Final Result

* ✅ Best Testing Accuracy: **77.2%**
* 📈 Improved Generalization
* 🔍 Reduced Overfitting

---

## 🚀 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Seaborn
* Matplotlib
* Streamlit

---

## 🌐 Live Demo

🔗 https://dibitiesclassification-rkxhhaufqpw4t46iyzunc6.streamlit.app/

---

## 📂 Project Structure

```
diabetes_prediction/
│
├── app.py
├── model.pkl
├── diabetes.csv
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/diabetes-prediction.git

# Go to project folder
cd diabetes-prediction

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

---

## 📌 Future Improvements

* 🔥 Add more ML models (Random Forest, XGBoost)
* 📊 Add visualization dashboard
* 🌍 Deploy with advanced UI
* 📱 Mobile responsive UI

---

## 👨‍💻 Author

**Amol Satpute**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!
