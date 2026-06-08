# Customer Churn Prediction

## Project Overview

This project aims to identify the likelihood of customers churning and to support the business in taking proactive retention actions.

---

## Business Problem

The company wants to take preventive actions to keep customers subscribed to their products.

---

## Objective

- Build classification models to predict whether a customer will churn or stay
- Discover hidden patterns in customer charges and behavior
- Compare multiple classification algorithms
- Derive actionable business insights from the data

---

## Dataset

Dataset: telco_cust.csv

The dataset contains transaction records and service subscription details including:

- Total charges
- Monthly charges
- Tech support subscription
- Contract type, payment method, and other service features

### Dataset Characteristics

The dataset has 7,043 instances and 21 features, with no missing values but contains non-numeric string values in features that should be numeric (cleaned during preprocessing). No duplicated records were found. Some features have high variance, total charges shows right skewness, and the target feature (churn) is imbalanced.

---

## Exploratory Data Analysis (EDA)

### Key Insights

- Total charges shows right skewness, which is handled naturally by the ensemble and boosting methods used in this project.
- The class imbalance in the target variable is addressed using StratifiedKFold to ensure each fold maintains the original class distribution during cross-validation.
- The majority of customers are low spenders (around $20/month). The highest churn rate occurs in the $70–$100/month range, suggesting that mid-to-high spenders are the most at-risk segment.

---

## Modeling

### Algorithms Evaluated

- Logistic Regression, used as a simple baseline model to establish a performance floor before testing more complex approaches
- Hist Gradient Boosting,handles skewed data well, ideal for small-to-medium datasets, and is generally faster and more accurate than standard Gradient Boosting
- Random Forest Classifier, uses a different aggregation strategy (bagging) compared to boosting methods, providing a strong ensemble baseline for tabular data
- CatBoost Classifier, efficient with high-dimensional categorical features, making it well-suited for this dataset's structure
- SVC, effective for non-linear decision boundaries when combined with appropriate kernel and regularization via hyperparameter tuning
- Gaussian Process Classifier and Bernoulli Naive Bayes, included as experimental methods; Bernoulli NB is appropriate here because the features were binarized, making it a better fit than Multinomial or Gaussian variants

---

## Preprocessing

- OneHotEncoder, appropriate for this case because categorical columns have few unique values, avoiding high-dimensional sparse representations
- RobustScaler, applied for Logistic Regression and SVC; reduces sensitivity to outliers compared to StandardScaler
- StratifiedKFold, preserves class distribution across folds to ensure fair evaluation under class imbalance

---

## Model Evaluation

Metrics used:

- Classification report (accuracy, precision, F1-score, and recall)
- Cross-validation score (mean accuracy)

---

## Model Comparison

### Without Hyperparameter Tuning

| Model                       | CV Accuracy         | Accuracy | Precision | Recall |  F1  |
| :-------------------------- | :------------------ | :------: | :-------: | :----: | :--: |
| Logistic Regression         |   0.8027 (±0.0095)  |   0.79   |    0.63   |  0.51  | 0.56 |
| Random Forest               |   0.7916 (±0.0086)  |   0.78   |    0.62   |  0.48  | 0.54 |
| Hist Gradient Boosting      |   0.7991 (±0.0055)  |   0.78   |    0.61   |  0.50  | 0.55 |
| Cat Booster                 |   0.7995 (±0.0080)  |   0.79   |    0.62   |  0.50  | 0.55 |
| SVC                         |   0.7977 (±0.0065)  |   0.79   |    0.63   |  0.48  | 0.54 |
| Gaussian Process Classifier |   0.7938 (±0.0091)  |   0.78   |    0.62   |  0.47  | 0.54 |
| Bernoulli NB                |   0.7278 (±0.0138)  |   0.71   |    0.47   |  0.80  | 0.60 |


### With Hyperparameter Tuning

| Model                       | CV Accuracy         | Accuracy | Precision | Recall |  F1  |
| :-------------------------- | :------------------ | :------: | :-------: | :----: | :--: |
| Logistic Regression         |   0.8050 (±0.0120)  |   0.79   |    0.63   |  0.51  | 0.56 |
| Random Forest               |   0.8053 (±0.0092)  |   0.79   |    0.63   |  0.49  | 0.55 |
| Hist Gradient Boosting      |   0.8036 (±0.0083)  |   0.79   |    0.66   |  0.43  | 0.52 |
| Cat Booster                 |   0.8069 (±0.0070)  |   0.79   |    0.64   |  0.48  | 0.55 |
| SVC                         |   0.8002 (±0.0068)  |   0.72   |    0.48   |  0.74  | 0.58 |
| Gaussian Process Classifier |   0.7938 (±0.0091)  |   0.78   |    0.62   |  0.47  | 0.54 |
| Bernoulli NB                |   0.7278 (±0.0138)  |   0.71   |    0.47   |  0.80  | 0.60 |

---

## Key Findings

- Hyperparameter tuning improved the performance of several models, though gains were modest, in some cases (e.g., Hist Gradient Boosting), precision improved while recall dropped, highlighting a trade-off worth considering per business context
- Logistic Regression remained highly competitive despite being the simplest model tested, demonstrating that simpler models can generalize well on small datasets with relatively linear patterns
- CatBoost achieved the highest cross-validation accuracy and delivered stable performance across evaluation metrics
- Bernoulli Naive Bayes achieved the highest recall (0.80), making it the most effective model for catching churners, though at the cost of lower precision and accuracy; this trade-off may be acceptable depending on the business's tolerance for false positives
- Gaussian Process Classifier outperformed Naive Bayes in overall accuracy but required significantly higher computational resources

---

## Business Insight

- CatBoost can be used as a practical churn prediction model due to its balanced performance and strong generalization capability; running it periodically as a scoring system can help prioritize outreach to high-risk customers
- Customers with MonthlyCharges between approximately $70 and $100 exhibit a relatively higher churn rate, this segment is a priority target for loyalty rewards or personalized value-added offers
- Customers with higher TotalCharges tend to remain subscribed longer, suggesting that early-tenure customers are the most vulnerable; retention programs should focus on the first few months of a customer's lifecycle
- Retention campaigns such as loyalty rewards, personalized offers, or proactive customer support may be particularly effective for customers within the high-risk spending segments

## Final Decision

### Best Model: CatBoost Classifier

Reasons:

- Achieved the highest cross-validation accuracy (0.8069)
- Delivered a strong balance between precision and recall
- Demonstrated stable performance after hyperparameter tuning
- Well-suited for tabular customer data with mixed feature interactions
- Provides strong generalization capability compared to simpler models

---

## Limitations

- The dataset contains limited behavioral and customer engagement features
- Class imbalance remains a challenge; StratifiedKFold preserves distribution during evaluation but does not resample training data, techniques such as SMOTE or class weighting were not applied in this iteration
- Model performance has not yet been validated on external datasets or real-world production data

---

## Future Improvements

- Explore advanced hyperparameter optimization techniques
- Investigate whether CustomerID-derived behavioral features can improve predictive performance
- Apply feature selection and regularization techniques
- Evaluate resampling methods such as SMOTE or class weighting to further address class imbalance
- Test model performance on external validation datasets

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn

---

## What I Learned (1% Improvement)

- Learned hyperparameter tuning and applied it across multiple algorithms
- Explored new algorithms such as Bernoulli Naive Bayes and Gaussian Process Classifier