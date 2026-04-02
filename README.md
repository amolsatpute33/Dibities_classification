🩺 Diabetes Prediction using Decision Tree Classifier

Project Type: Classification
Algorithm: Decision Tree
Language: Python
Dataset: diabetes.csv
Libraries: pandas, scikit-learn, seaborn, matplotlib

⸻

💡 Problem Statement

Predict whether a person is diabetic or non-diabetic based on medical attributes such as:
	•	Glucose Level
	•	Blood Pressure
	•	BMI
	•	Insulin
	•	Age
	•	Pregnancies
	•	Skin Thickness
	•	Diabetes Pedigree Function

⸻

📊 Dataset Overview
	•	Rows: 768
	•	Columns: 9
	•	Features: 8
	•	Target: Outcome (0 = Non-Diabetic, 1 = Diabetic)

⸻

🧠 Domain Analysis

This project falls under Healthcare Analytics.
The goal is early detection of diabetes using machine learning.

Decision Tree Classifier is used to:
	•	Learn patterns from medical data
	•	Classify diabetic vs non-diabetic patients
	•	Improve prediction accuracy

⸻

🔍 Exploratory Data Analysis (EDA)

📈 Histograms
	•	Checked distribution of numerical features
	•	Identified skewed columns

📊 Countplot
	•	Checked class imbalance in target variable

📦 Boxplots
	•	Detected outliers
	•	Compared feature spread

🔗 Scatter Plots
	•	Analyzed relationship between features

⸻

🧼 Data Preprocessing

✔ Replaced invalid zero values with median
✔ Handled outliers using IQR method
✔ Applied log transformation
✔ Feature scaling using MinMaxScaler
✔ Balanced data using SMOTE

⸻

⚙️ Model Building

Model Used: DecisionTreeClassifier

Train-Test Split: 80% Train — 20% Test

Evaluation Metrics:
	•	Accuracy
	•	Confusion Matrix
	•	Classification Report

⸻

📉 Initial Model Performance

Training Accuracy: 72%
Testing Accuracy: 1%

⚠️ Model was overfitting

⸻

🔧 Hyperparameter Tuning

Applied:

✅ GridSearchCV

✅ RandomizedSearchCV

✅ Cost Complexity Pruning
