# 📊 Low-Cost Sensor Calibration for CO Prediction Using Machine Learning

## 📌 Project Overview
This project aims to calibrate low-cost air quality sensors by predicting CO concentrations using correlated environmental sensor data and machine learning models.

---

## 🎯 Business Problem
The company wants low-cost sensors to produce measurements comparable to expensive reference sensors in order to reduce operational costs.

---

## 🎯 Objective
- Build a regression model to predict the target (CO)
- Identify the feature that have a high correlation with the CO feature
- Use this models to save more budget

---

## 📂 Dataset
- Dataset contains information many compounds in the air and the sensor used, such as:
  - CO(GT)
  - PT08.S1(CO)
  - NO2(GT)
  - Time
  - Date
  - Etc.
- Target: CO(GT)
- Characteristics: The dataset has a relatively small number of instances (9357) and have 15 features, many valid outliers caused by natural air-quality fluctuations, missing values, right-skewed feature distributions, high variance across several sensor readings, and all of them is numerical with 2 feature timestamps.

---

## 📊 Exploratory Data Analysis (EDA)

### 🔹 Key Insights:
- Approximately 73% of the features show moderate to strong correlation with the target variable.
- All the feature that have outliers is valid, because air quality always fluctuative, and we can't remove it. So we use robust scaler or tree based and gradient boosting that can handle outliers
- Linear Regression was included as a baseline to benchmark performance against tree-based and boosting models

---

## ⚙️ Modeling

### 🔹 Models Used:
- Random Forest Regression
- Hist Gradient Boosting Regression
- Cat Boost Regressor
- Linear Regression

### 🔹 Preprocessing:
- `RobustScaler` to rescale numerical features and outliers handling for linear regression model
- `Pipeline` for process efficiency across each model

---

## 📈 Model Evaluation

Evaluation metrics used:
- MAE (because dataset has many outliers)
- R2 (to see how good is it the model)

---

## 📊 Performance Comparison

|    | Model                   |    MAE |     R2 |
|---:|:------------------------|-------:|-------:|
|  1 | Random Forest Regressor | 0.2933 | 0.8867 |
|  2 | Hist Gradient Boosting  | 0.3037 | 0.8834 |
|  3 | Cat Boost Regressor     | 0.2913 | 0.8923 |
|  4 | Linear Regression       | 0.3823 | 0.827  |

---

## 🔥 Key Findings

- Cat booster regressor is the best model for this case 
- As expected, tree-based and boosting models outperformed Linear Regression due to their ability to capture non-linear relationships and handle outliers effectively
- Strong correlations between several features and the target contributed to the high R2 scores (~0.88)
- Log transformation was also tested to reduce skewness, but it did not improve performance compared to RobustScaler

---

## 💼 Business Insight

- The model achieved a low MAE of 0.291, indicating relatively small prediction errors
- The model has the potential to significantly reduce monitoring costs by minimizing dependence on expensive reference sensors
- The model can be integrated into a real-time monitoring dashboard to flag abnormal CO levels automatically

---

## ✅ Final Decision

**Best Model: CatBoost Regressor**

### Reasons:
- Given the best result with MAE 0.2913 and R2 score 89.23%
- Performs well on structured tabular datasets with mixed distributions and outliers
- Robust to outliers
- Good with dataset that have many features

---

## ⚠️ Limitations

- The model has not been tested on external sensor environments
- Missing values handling may still affect generalization
- Temporal patterns from timestamp features were not fully explored

---

## 🚀 Future Improvements

- Explore timestamp features for time-series modeling (e.g., hourly/daily patterns)
- Hyperparameter tuning for CatBoost to further reduce MAE
- Test model generalization on external sensor environments

---

## 🛠️ Tech Stack
- Python
- Scikit-learn
- Pandas
- Matplotlib
- Seaborn