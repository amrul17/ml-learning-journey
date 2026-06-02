# Retail Customer Segmentation with Clustering

## Project Overview

This project aims to identify hidden customer segments from online retail transaction data using unsupervised machine learning techniques. The resulting segments can support targeted marketing strategies, customer retention programs, and revenue optimization initiatives.

---

## Business Problem

The company wants to maximize conversion opportunities and improve customer engagement by understanding purchasing patterns across different customer groups.

Without segmentation, marketing campaigns are applied uniformly, which may reduce effectiveness and increase customer acquisition costs.

---

## Objective

- Build clustering models to segment retail transactions
- Discover hidden patterns in customer purchasing behavior
- Compare multiple clustering algorithms
- Generate actionable business recommendations for each segment

---

## Dataset

Dataset: `online_retail.xlsx`

The dataset contains online retail transaction records including:

- Quantity
- UnitPrice
- Country
- Sales (engineered feature: Quantity × UnitPrice)

The following features were removed during preprocessing:

- InvoiceNo
- StockCode
- Description
- CustomerID
- InvoiceDate

### Dataset Characteristics

- Transactional retail dataset
- Missing values found in `Description` and `CustomerID`
- Negative values in `Quantity` and `UnitPrice` removed
- Strong right-skewed distribution in sales-related variables
- Valid business outliers retained
- Mixed numerical and categorical features

### Goal

Discover hidden customer segments based on transaction value and geographic information.

---

## Exploratory Data Analysis (EDA)

### Key Insights

- Sales distribution is heavily right-skewed, which is common in retail transaction data
- Large transactions were retained because they represent valid business behavior rather than data errors
- Sales was engineered as:

```python
sales = Quantity - UnitPrice
```

- Country information may contribute significantly to cluster formation

---

## Modeling

### Algorithms Evaluated

#### KMeans (MiniBatchKMeans)

- Scalable for large datasets
- K determined using Elbow Method, Silhouette Score, and Silhouette Diagram

#### Agglomerative Clustering

- Hierarchical clustering approach
- Evaluated using the same K-selection process

#### Spectral Clustering

- Graph-based clustering using nearest-neighbor affinity

#### DBSCAN

- Density-based clustering
- Automatically determines cluster count

---

## Preprocessing

- OneHotEncoder for `Country`
- StandardScaler for numerical features
- PCA (10 components) applied after encoding to reduce dimensionality and sparsity
- Random sampling of 5,000 observations used during evaluation for computational efficiency

---

## Model Evaluation

The following internal clustering metrics were used:

- Silhouette Score (higher is better)
- Davies-Bouldin Index (lower is better)
- Calinski-Harabasz Score (higher is better)
- Inertia (KMeans only)
- Training Time

---

## K Selection

K-selection was applied only to K-based algorithms.

### Silhouette Score and Inertia

| K  | Silhouette | Inertia |
| -- | ---------- | ------- |
| 2  | 0.82       | 49,000  |
| 3  | 0.62       | 44,000  |
| 4  | 0.84       | 39,800  |
| 5  | 0.80       | 34,000  |
| 6  | 0.79       | 32,500  |
| 7  | 0.51       | 32,500  |
| 8  | 0.51       | 27,500  |
| 9  | 0.46       | 24,500  |
| 10 | 0.51       | 24,500  |

### Best K = 4

Confirmed through:

- Elbow Method
- Silhouette Score
- Silhouette Diagram

The silhouette score reached its global maximum at K=4, indicating the best cluster separation.

---

## Model Comparison

| Model                    | Clusters | Silhouette | Davies-Bouldin | Calinski-Harabasz | Time (s) |
| ------------------------ | -------- | ---------- | -------------- | ----------------- | -------- |
| KMeans (MiniBatch)       | 4        | 0.9263     | 1.3375         | 1009.6            | 0.6      |
| Agglomerative Clustering | 4        | 0.9201     | 1.2032         | 1239.0            | 0.2      |
| Spectral Clustering      | 4        | -0.8552    | 4.0836         | 19.5              | 0.4      |
| DBSCAN                   | 18       | 0.9898     | 0.1017         | 333804.6          | 0.1      |

### Note

DBSCAN generated 18 clusters automatically.

Although DBSCAN achieved the highest metric scores, the resulting segmentation was highly fragmented and less interpretable from a business perspective.

---

## Key Findings

- K=4 was consistently identified as the optimal number of clusters
- Agglomerative Clustering delivered the strongest balance between separation quality and interpretability
- KMeans produced comparable performance while offering higher scalability
- Spectral Clustering was not suitable for the structure of this dataset
- DBSCAN likely over-segmented the data despite its excellent internal metrics

---

## Business Insight

Cluster profiling was performed using Agglomerative Clustering (K=4).

Since `Country` is one of the primary clustering features, geographic information strongly influences cluster formation. Therefore, the resulting segments should be interpreted as a combination of spending patterns and geographic distribution rather than pure customer behavior profiles.

### Cluster Profile

| Cluster | Transactions | Total Sales (USD) | Avg Sales (USD) | Top Country     |
| ------- | ------------ | ----------------- | --------------- | --------------- |
| 0       | 276          | 10,332.03         | 37.43           | Germany         |
| 1       | 4,582        | 81,264.70         | 17.74           | United Kingdom  |
| 2       | 78           | 1,575.61          | 20.20           | France          |
| 3       | 64           | 1,110.86          | 17.36           | Mixed Countries |

### Segment Interpretation

| Cluster | Label                     | Description                                                                             |
| ------- | ------------------------- | --------------------------------------------------------------------------------------- |
| 0       | High-Value German Segment | Highest average transaction value with strong revenue contribution                      |
| 1       | High-Volume UK Segment    | Largest customer group with high transaction volume but lower average transaction value |
| 2       | Mid-Value French Segment  | Moderate spending customers with growth potential                                       |
| 3       | Mixed Regional Segment    | Smaller customer group with moderate spending behavior                                  |

### Recommended Actions

| Segment                   | Recommendation                                            |
| ------------------------- | --------------------------------------------------------- |
| High-Value German Segment | Loyalty programs, personalized offers, premium membership |
| High-Volume UK Segment    | Bundle promotions and cross-selling campaigns             |
| Mid-Value French Segment  | Regional marketing campaigns and upselling                |
| Mixed Regional Segment    | Customer engagement and retention campaigns               |

---

## Final Decision

### Best Model: Agglomerative Clustering (K=4)

Reasons:

- Strong silhouette score (0.9201)
- Lowest Davies-Bouldin score among fixed-K models
- More interpretable than DBSCAN
- Fast training time
- Produces meaningful business segments

---

## Limitations

- Only sales and Country were used as clustering features
- Clustering was performed at the transaction level rather than the customer level
- Results are based on a 5,000-sample subset
- Geographic information strongly influences segmentation
- Business value of clusters has not yet been validated through marketing experiments

---

## Future Improvements

- Build customer-level segmentation using CustomerID
- Create RFM (Recency, Frequency, Monetary) features
- Explore Gaussian Mixture Models
- Tune DBSCAN hyperparameters systematically
- Validate clusters through A/B testing and marketing performance metrics

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn




