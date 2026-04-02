Diabetes Prediction using Decision Tree Classifier
Project Type: Classification | Algorithm: Decision Tree | Language: Python Dataset: diabetes.csv Toolkits: pandas, scikit-learn ,seaborn, matplotlib

💡 Problem Statement
Predict whether a person is diabetic based on medical attributes like glucose level, blood pressure, BMI, and age using a decision tree classifier.

Dataset Overview:
There are 8 features and one target variable in dataset,involving 768 rows × 9 columns.

🧠 Domain Analysis
This project lies in the domain of healthcare analytics, targeting early detection of diabetes through clinical and demographic features. It leverages decision tree modeling to classify patients as diabetic or non-diabetic based on measurable parameters.

🔍 Exploratory Data Analysis
Histograms: Visualized the distribution of continuous variables to understand skewness, central tendency, and spread.
Countplots: Examined target variable balance or not.
Boxplots: Used boxplots to visually detect outliers and compare distributions across survival status.
Scatter Plots: Explored relationships between pairs of variables .
🧼 Data Preprocessing
Replaced biologically invalid zeroes with median values. Handled outliers using IQR and replaced with median. Applied logarithmic transformation to skewed columns. Scaled features using MinMaxScaler.

⚙️ Modeling Building
Model Used: DecisionTreeClassifier Sampling: Applied SMOTE to balance the class distribution. Train-Test Split: 80–20 ratio Evaluation Metrics: Accuracy,Confusion Matrix, Classification Report

Model Evaluation :
The training accurasy of model is 72% and testing accurasy is 1%.i.e.model is overfitting.so we have done hyperparameter tuning to increase the performance of model.

Hyperparameter tuning:
Doing bY using two ways

Grid search cv
Random search cv
After hyperparameter tuning the training accurasy of model is 74% & the testing accurasy of model is 81%.

🏆 Model Performance
Model Training Accuracy Testing Accuracy

Decision Tree : 100% : 71.4%

GridSearchCV Tuned Model :84.2% : 72.1%

RandomizedSearchCV Tuned : 84.2% : 72.7%

Cost Complexity Pruning : 77.0% : 77.2%

	



