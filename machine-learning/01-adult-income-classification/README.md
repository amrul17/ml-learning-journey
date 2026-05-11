# Adult Income Classification


## 📌 Project Overview
This project aims to predict whether a resident's income is less than $50,000 (0) or more than $50,000 (1) based on the correlation of several features such as education, age, relationship, and so on

---

## 🎯 Business Objective
Helps identify individuals with high income potential (>50K) to support:
- marketing targeting
- customer segmentation
- data-driven decision making

---

## 📂 Dataset
- Dataset contains resident information such as:
  - Age
  - Income
  - Marital Status
  - Gender
  - Race
- Target: ** > $50k (Yes = 1, No = 0)**
- Characteristics: Imbalanced dataset, Several features contain many zero values (e.g., capital_gain, capital_loss). However, these zeros are not missing data, a value of 0 in capital_gain simply means the individual had no capital gain that year. Therefore, no imputation was performed to preserve the original distribution.

---

## 📊 Exploratory Data Analysis (EDA)

### 🔹 Key Insights:
- Individuals with higher education levels have a significantly greater probability of having an income >50K
- Features such as capital_gain and hours_per_week show high variance, which contributes to income differences

---

## ⚙️ Modeling

### 🔹 Models Used:
- Random Forest Classifier
- Hist Gradient Boosting
- Linear Support Vector Classifier

### 🔹 Preprocessing:
- OrdinalEncoder for categorical features with ranking
- OneHotEncoder for regular categorical features
- StandardScaler to normalize the scale of each numerical feature

---

## 📈 Model Evaluation

Since the data is imbalanced, accuracy alone is not a reliable metric. Therefore, Precision, Recall, and F1-score are used to better evaluate model performance on both classes.

---

## 📊 Performance Comparison

### 🔹 Evaluation for target < $50.000

|       Model       | Accuracy | Precision | Recall |  F1  |
|-------------------|----------|-----------|--------|------|
| Random Forest     |   0.86   |   0.89    |  0.93  | 0.91 |
| Gradient Boosting |   0.87   |   0.89    |  0.95  | 0.92 |
| Linear SVC        |   0.86   |   0.88    |  0.94  | 0.91 |

---

### 🔹 Evaluation for target > $50.000

|       Model       | Accuracy | Precision | Recall |  F1  |
|-------------------|----------|-----------|--------|------|
| Random Forest     |   0.86   |    0.75   |  0.64  | 0.69 |
| Gradient Boosting |   0.87   |    0.8    |  0.62  | 0.7  |
| Linear SVC        |   0.86   |    0.75   |  0.6   | 0.67 |

---

## 🔥 Key Findings

- Gradient Boosting slightly outperforms other models
- The model tends to give more weight to the dominant target
- The model performs significantly better on the majority class (<50K)
- The cross-validation results are close to the test accuracy, indicating stable model performance
- LinearSVC did not outperform ensemble models, likely because the dataset contains many categorical features and complex feature interactions. LinearSVC was chosen over kernel SVC due to its scalability with large datasets

---

## ✅ Final Decision

Best model: Gradient Boosting

Reasons:
- Has the highest F1-score on both classes
- More stable in handling imbalanced data and outliers
- Recall on the >50K class remains maintained compared to other models

---

## 💼 Business Insight

- The model is better at detecting individuals with low income (<50K)
- However, for business cases, the >50K class is more important as it holds higher value
- Therefore, improving recall on the >50K class becomes a priority

👉 The model can be used for:
- premium customer targeting
- demographic analysis of high-value customers

---

## ⚠️ Limitations

- The model is still biased toward the majority class
- Recall on the >50K class is still relatively low
- Some features have imbalanced distributions

---

## 🚀 Future Improvements

- Apply SMOTE or class_weight balancing to improve recall on the >50K class
- Explore XGBoost or LightGBM
- Threshold optimization for business use case

---

## 🛠️ Tech Stack
- Python
- Scikit-learn
- Pandas
- Matplotlib 
- Seaborn