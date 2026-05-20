# 📊 Sales & Engagement Clustering Analysis

## 📌 Project Overview
This project aims to identify customer behavior patterns using clustering techniques to support sales and engagement strategies

---

## 🎯 Business Problem
The company wants to maximize conversion opportunities from website visitors by understanding customer behavior patterns

---

## 🎯 Objective
- Build a clustering model to segment customer behavior
- Discover behavioral patterns from website activity data
- Support customer segmentation strategies

---

## 📂 Dataset
- Dataset contains information about activity in the website, such as:
  - click_in_site
  - product_category
  - payment_method
  - value [USD]
  - date
  - etc.
- Target: Sales (value USD)
- Characteristics: The dataset contains 24,999 observations and 7 features, with no missing values, right skewness, multiple types, valid outliers no need to remove.

---

## 📊 Exploratory Data Analysis (EDA)

### 🔹 Key Insights:
- Sales activity is highest on Friday and lowest on Saturday
- Product category 505 generated the highest sales volume
- Valid outliers in sales, time on site, clicks in site, because every person have different behavior and needs
- Among the numerical features, clicks_in_site shows the strongest correlation with sales value
- KMeans was selected because the objective is to group customers based on behavioral similarity

---

## ⚙️ Modeling

### 🔹 Models Used:
- KMeans, with sequential process to find best k, start with elbow method, silhouette score, and the last one is silhouette diagrams

### 🔹 Preprocessing:
- StandardScaler` to rescale numerical features


---

## 📈 Model Evaluation

Evaluation metrics used:
- Silhouette score
- Davies-Bouldin
- Calinski-Harabasz

---

## 📊 Performance Comparison


Model Evaluation
|    |   K |   Silhouette (↑) |   Davies-Bouldin (↓) |   Calinski-Harabasz (↑) |   Inertia (↓) |
|---:|----:|-----------------:|---------------------:|------------------------:|--------------:|
|  1 |   3 |           0.6494 |               0.6554 |                 26538.5 |       24011.2 |
|  2 |   4 |           0.561  |               0.696  |                 30541.4 |       16074.1 |

---

## 🔥 Key Findings

- K=3 outperformed K=4 across most evaluation metrics, achieving higher silhouette score and better cluster separation
- K=4 achieved lower inertia values, which is expected because inertia generally decreases as the number of clusters increases
- The sequential evaluation approach — elbow method → silhouette score → silhouette diagram — consistently pointed to K=3 as the optimal number of clusters
- Using RobustScaler reduced cluster separation quality in this case, likely because extreme values contained important behavioral information

---

## 💼 Business Insight

Cluster Profile:
|           |   sales |   time_on_site [Minutes] |   clicks_in_site |
|:----------|--------:|-------------------------:|-----------------:|
| Cluster 0 |  135.21 |                    23.86 |            11.72 |
| Cluster 1 |  174.43 |                   559.21 |            14.31 |
| Cluster 2 |  570.46 |                    50.32 |            39.31 |

- The model show different behavior of customer, 
  1. Cluster 0 — Balanced Customers
  Customers in this cluster show moderate engagement and moderate spending behavior. They appear to visit the website with relatively clear purchase intent.
  2. Cluster 1 — Passive Browsers
  These customers spend a long time on the website but generate relatively low sales and low interaction activity. This may indicate uncertainty, low purchase intent, or ineffective product discovery.
  3. Cluster 2 — High-Value Customers
  This cluster generates the highest sales with strong interaction activity and efficient browsing behavior. These customers are likely repeat buyers or highly familiar with the platform.

- Recommendation action each cluster:
|  Cluster  |        Type          |             Recommended Action                |
|-----------|----------------------|-----------------------------------------------|
| Cluster 0 | Balanced Customers   | Upselling & cross-selling campaigns           |
| Cluster 1 | Passive Browsers     | Retargeting ads, improve UX/product discovery |
| Cluster 2 | High-Value Customers | Loyalty program, exclusive offers             |

---

## ✅ Final Decision

**Best Model: Kmeans With K=3**

### Reasons:
- Achieved the best balance between cluster separation, compactness, and interpretability
- Provides clear separation between customer behavior groups

---

## ⚠️ Limitations

- Limited number of behavioral features may reduce cluster richness
- Clustering results may change with additional demographic or transactional data

---

## 🚀 Future Improvements

- Incorporate demographic features (age, gender, location) to enrich cluster profiles
- Develop targeted marketing strategies per cluster (e.g., retargeting for Cluster 1, loyalty rewards for Cluster 2)
- Test DBSCAN or Gaussian Mixture Models as alternative clustering approaches

---

## 🛠️ Tech Stack
- Python
- Scikit-learn
- Pandas
- Matplotlib
- Seaborn