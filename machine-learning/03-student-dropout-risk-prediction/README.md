# 📊 Student Dropout Risk Prediction

## 📌 Project Overview
This project predicts students' final exam scores (G3) to identify those at risk of academic failure, enabling schools to take preventive action early.

---

## 🎯 Business Problem
Schools need a system to identify academically at-risk students before the final exam, enabling timely interventions such as additional tutoring, mentoring, or attendance monitoring.

---

## 🎯 Objective
- Predict student's final grades (G3)
- Identify the key factors influencing academic performance
- Support early intervention decisions using model predictions after initial evaluations (G1, G2) are available

---

## 📂 Dataset
- Source: UCI Student Performance Dataset (Cortez & Silva, 2008)
- Size: 395 students, 32 features
- Dataset contains student information such as:
    - Age, school, and family background
    - Parental education and occupation
    - Study time, extracurricular activities, and health status
    - Prior grades (G1, G2) and number of past failures
- Target: G3 (final exam score, scale 0–20)
- Characteristics: Data distribution across features is fairly balanced with relatively low standard deviation. No missing values or duplicates. Roughly half the features are numeric; the rest are ordinal or binary categorical variables. Some ordinal features (e.g., Medu, Fedu, studytime) use coded integer scales that require reference to the data dictionary for interpretation.

---

## 📊 Exploratory Data Analysis (EDA)

### 🔹 Key Insights:
- Previous grades (G1, G2) have a very strong influence on the final grade (G3), indicating a strong dependency between academic evaluations.
- However, these features have the potential to cause data leakage since they directly represent prior student performance.
- Approximately 50% of the features show weak or no correlation with the target variable. This characteristic may reduce the effectiveness of distance-based models such as KNN Regressor.
- The dataset contains mixed feature types, outliers, and potential non-linear relationships, making ensemble-based models such as Random Forest and Gradient Boosting suitable candidates for experimentation.

---

## ⚙️ Modeling

### 🔹 Models Used:
- Linear Regression
- Random Forest Regressor
- Hist Gradient Boosting
- KNN regressor
- Support Vector Regressor

### 🔹 Preprocessing:
- Winsorizing to handle outliers
- Get_dummies for categorical feature transformation
- RobustScaler to normalize the scale of each feature's values
- Separate models without pipeline

---

## 📈 Model Evaluation

Since outliers have been addressed, the evaluation metrics used are:
- RMSE
- R2

---

## 📊 Performance Comparison

| Model                     |  RMSE  |  R2   |  CV Mean  |  CV Std  |
|---------------------------|--------|-------|-----------|----------|
| Random Forest regressor   |  1.95  | 0.815 |   0.89    |  0.051   |
| Hist Gradient Boosting    |  1.97  | 0.81  |   0.871   |  0.058   |
| Support Vector Regression |  2.36  | 0.727 |   0.691   |  0.086   |
| Linear Regression         |  2.37  | 0.726 |   0.817   |  0.047   |
| KNN Regressor             |  3.23  | 0.49  |   0.627   |  0.09    |

---

## 🔥 Key Findings

- Linear Regression underperforms because it is unable to capture non-linear patterns in the data
- Before fixing the random_state parameter, the best-performing model occasionally alternated between Random Forest and Hist Gradient Boosting
- Applying winsorizing (capping outliers) reduced the quality of outlier-sensitive models such as Random Forest 
- Winsorizing produced minimal impact on Linear Regression performance
- Feature G2 contributes the most to the prediction, indicating that previous academic performance strongly influences final exam scores.


---

## 💼 Business Insight

- The model can be used to detect at-risk students early
- Schools can provide interventions such as:
  - additional classes
  - academic mentoring
  - attendance monitoring
- The main focus is not only prediction, but prevention of academic failure
- The model should ideally be used after early evaluations (G1, G2) are available to improve prediction accuracy

---

## ✅ Final Decision

**Best model: Random Forest Regressor**

### Reasons:
- Lowest RMSE (1.95) on the test set, providing the most accurate grade predictions
- Highest cross-validation mean (0.890) with low variance (0.051), indicating stable generalization
- Capable of capturing non-linear patterns and interactions that Linear Regression cannot
- Naturally robust to irrelevant features through random feature subsampling at each split

---

## ⚠️ Limitations

- Potential data leakage from features G1 and G2
- Relatively small dataset limits generalizability
- Model has not been tested on external data
- Models built without a unified pipeline

---

## 🚀 Future Improvements

- Explore feature selection techniques
- Reduce potential data leakage
- Build a unified preprocessing and modeling pipeline

---

## 🛠️ Tech Stack
- Python
- Scikit-learn
- Pandas
- Matplotlib / Seaborn

---