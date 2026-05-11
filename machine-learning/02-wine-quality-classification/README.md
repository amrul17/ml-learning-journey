# 📊 Wine Classification Prediction

## 📌 Project Overview
This project aims to classify wine classes based on their chemical characteristics.

---

## 🎯 Business Problem
The company wants consistent quality across all its products to ensure customer satisfaction.

---

## 🎯 Objective
- Build a classification model to predict wine classes based on chemical features
- Identify the most influential features in wine class classification
- Provide data-driven recommendations for production quality control

---

## 📂 Dataset
- Dataset contains information related to wine compounds and characteristics, such as:
  - Alcohol
  - Ash
  - Phenols
  - Flavanoids
  - Color
  - Etc.
- Target: Class
- Characteristics: The dataset has a relatively small number of instances but a fairly large number of features, good data distribution (low std), outliers in only one or two features, no duplicates, and only requires header correction. All features are numerical.

---

## 📊 Exploratory Data Analysis (EDA)

### 🔹 Key Insights:
- There are features with both positive and negative correlations to the class label (Class), which can serve as a basis for important feature selection.
- The `Proline` feature contains outliers. Since this feature has a strong correlation with the target, the outliers were not removed. Instead, models that are robust to outliers such as Random Forest and Gradient Boosting were used. Decision Tree was also included as a baseline comparison model.

---

## ⚙️ Modeling

### 🔹 Models Used:
- Random Forest Classifier
- Hist Gradient Boosting
- Support Vector Classifier
- Decision Tree

### 🔹 Preprocessing:
- `RobustScaler` to rescale numerical features
- `Pipeline` for process efficiency across each model

---

## 📈 Model Evaluation

Evaluation metrics used:
- `classification_report` (Precision, Recall, F1-Score, Accuracy)
- Confusion Matrix
- ROC AUC Score
- Cross-Validation Score (Stratified K-Fold)

---

## 📊 Performance Comparison

|          Model              | Precision | Recall |  F1  | Accuracy | ROC AUC |   CV Score        |
|-----------------------------|-----------|--------|------|----------|---------|-------------------|
| Random Forest Classifier    |   1.00    |  1.00  | 1.00 |   1.00   |  1.00   | 0.9889 ± 0.0222   |
| Hist Gradient Boosting      |   0.97    |  0.97  | 0.97 |   0.97   |  1.00   | 0.9722 ± 0.0512   |
| Support Vector Classifier   |   1.00    |  1.00  | 1.00 |   1.00   |  1.00   | 0.9778 ± 0.0369   |
| Decision Tree               |   0.95    |  0.94  | 0.94 |   0.94   |  0.95   | 0.8997 ± 0.0776   |

---

## 🔥 Key Findings

- Random Forest is the best model in this case.
- All models produced good results. This is not an indication of overfitting or data leakage, but rather because this dataset has fairly clear and well-separated patterns. This is evidenced by consistently high cross-validation scores and the use of Stratified K-Fold, which ensures data is always shuffled proportionally during training.
- SVC performed well because this model is well-suited for small datasets with many features.
- Hist Gradient Boosting struggled slightly on class 3 (1 misclassified sample), which is understandable given that class 3 has the smallest support (8 samples).
- Decision Tree showed lower performance with a ROC AUC of 0.9521 and the lowest CV score with the highest std (±0.0776), indicating this model is less stable compared to ensemble models.
- Hyperparameter tuning was also performed to ensure the model does not overfit, by constraining the value of each parameter. Results still showed good performance.

---

## 💼 Business Insight

- This model can be used to automatically predict wine classes based on their chemical profiles, supporting the quality control process on the production line.
- Features with strong correlations to the class label (such as `Proline`, `Flavanoids`, and `Total_phenols`) can serve as reference points for monitoring the production process — features with high correlation to a specific class need to be kept consistent.
- The correlation analysis in this dataset reflects the relationship between features and **wine varietal classes** (not a high-low quality scale). Therefore, quality improvement recommendations should refer to **feature importance** results and oenological domain knowledge, not solely from correlation values.
- As a next step, feature importance analysis from Random Forest can provide a more accurate picture of which features most determine wine class classification.

---

## ✅ Final Decision

**Best Model: Random Forest Classifier**

### Reasons:
- Delivers perfect results on the classification report (Precision, Recall, F1, Accuracy = 1.00) with a ROC AUC of 1.00.
- Highest cross-validation score (0.9889) with the lowest std (±0.0222), indicating stable and consistent performance.
- Robust to outliers (such as in the `Proline` feature).
- Capable of handling high feature complexity without performance degradation.
- Provides `feature_importances_` which is useful for model interpretation.

---

## ⚠️ Limitations

- Dataset is relatively small, so generalization to new data needs further testing.
- Model has not been tested on wine data from different varietals or regions.
- Feature importance analysis has not been explicitly performed.

---

## 🚀 Future Improvements

- Add feature importance analysis for better model interpretability
- Perform additional feature engineering if needed
- Test the model on new datasets from different varietals or regions
- Consider using SHAP values for deeper explainability

---

## 🛠️ Tech Stack
- Python
- Scikit-learn
- Pandas
- Matplotlib
- Seaborn