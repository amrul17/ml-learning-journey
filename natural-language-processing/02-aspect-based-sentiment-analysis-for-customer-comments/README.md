# Aspect-Based Sentiment Analysis for Customer Comments

---

## Business Problem

The client wants to understand customer opinions about their product in more detail, rather than relying only on overall positive or negative sentiment.

By identifying both the **aspect being discussed** and the **sentiment expressed**, the client can determine which parts of the product should be improved and which aspects should be maintained.

---

## Objective

- Build a model that identifies the aspect discussed in each customer comment.
- Classify the sentiment associated with each aspect.
- Generate more specific insights from unstructured customer comments.
- Evaluate the model predictions and analyze the resulting customer feedback.

---

## Dataset

The raw dataset was collected from comments on a randomly selected TikTok video.

Only the **main comments** were collected; replies to those comments were not included.

### Dataset Characteristics

- **910 comments** in total.
- 100% user-generated comments.
- Contains noisy and unstructured text.
- Contains missing values.
- Includes slang, informal language, and other variations commonly found in social media comments.

---

## Exploratory Data Analysis (EDA)

### Key Insights

- The dataset contains a high variety of opinions and perspectives, providing multiple points of view about the product.
- Several relevant aspects were identified based on the business objective:
  - Taste
  - Price
  - Appearance
  - Ingredients
- Social media comments contain a significant amount of informal and noisy language, making preprocessing important before applying the model.
- Some comments do not provide clear information about a specific aspect, which can make aspect classification more challenging.

---

## Preprocessing

- Handled missing values in the dataset.
- Standardized text values to maintain consistent formatting.
- Converted text to lowercase using `lower()` to reduce differences caused by capitalization.
- Defined the aspect categories based on the client's information needs.
- Prepared the comments for transformer-based classification.

---

## Modeling

### Architecture Used

The project uses a pretrained transformer model from **CardiffNLP** for sentiment-related text classification.

The transformer-based approach was selected because it can capture contextual relationships within text more effectively than traditional keyword-based approaches.

The model was used to analyze customer comments and generate:

- Aspect classification
- Sentiment label
- Prediction confidence score

---

## Evaluation Metric

The current experiment primarily analyzes the model's prediction output:

- **Predicted aspect**
- **Sentiment label**
- **Confidence score**

> **Note:** The confidence score represents the model's certainty about its prediction. It does not directly measure prediction accuracy. A proper quantitative evaluation would require manually labeled ground-truth data for both aspect and sentiment.

---

## Model Result

The model generated aspect and sentiment predictions for the collected comments.

| Index | Comment | Aspect | Sentiment | Confidence |
| ---: | --- | --- | --- | ---: |
| 346 | You better bring back the mayo bottle and sque... | Ingredients | Neutral | 0.537 |
| 347 | You cracked an egg there, buddy. You’re not ma... | Ingredients | Negative | 0.863 |
| 348 | You know its going to be expensive when the ch... | Price | Negative | 0.554 |
| 349 | You lost me at the toxic-chemical American cheese | Ingredients | Negative | 0.946 |
| 350 | Yummy | Taste | Positive | 0.448 |

### Aspect Distribution

The analysis identified **ingredients** as the most frequently discussed aspect, with **143 comments**.

Appearance also received a notable number of positive comments, with **45 positive comments**.

### Sentiment Insight

Approximately **60% of the comments related to taste were positive**, indicating that taste was generally perceived favorably in this sample.

### Price Insight

The selected TikTok video did not provide significant price-related information, resulting in relatively fewer comments discussing price.

---

## Key Findings

- The transformer model was able to classify customer comments into relevant aspects and sentiment categories.
- Prediction confidence varied between comments, indicating that some comments were more difficult for the model to interpret than others.
- **Ingredients** was the most discussed aspect, making it an important area for further analysis.
- Negative comments were particularly concentrated around the ingredients aspect.
- **Appearance** received a relatively positive response, suggesting that the visual presentation of the product should be maintained.
- **Taste** received predominantly positive feedback, with approximately 60% of comments classified as positive.
- The model demonstrates the potential of ABSA to extract more actionable information than simply classifying comments as positive or negative.

---

## Business Insight

- **Ingredients** should receive the highest attention because it generated the largest amount of discussion and negative feedback.
- Positive feedback regarding **appearance** can be used as an indicator of an aspect that should be maintained.
- The generally positive sentiment toward **taste** suggests that the current product taste is well received, while negative comments can still be reviewed for specific improvement opportunities.
- Aspect-level analysis allows the client to prioritize product improvements based on specific customer concerns rather than treating all negative reviews equally.

---

## Final Decision

### Recommended Architecture: CardiffNLP Transformer

### Reasons

- Suitable for analyzing natural-language customer comments.
- Able to generate contextual sentiment predictions.
- Provides aspect-level analysis that can produce more actionable business insights.
- Can process informal customer-generated text better than simple keyword-based approaches.

---

## Limitations

- The dataset contains only **910 comments**, which limits the amount of data available for analysis.
- The dataset contains noisy social media language, including slang and informal expressions.
- Only main comments were collected; replies were not included.
- Aspect categories were manually defined based on the business objective and may not cover every topic discussed by customers.
- No manually labeled ground-truth dataset was created for aspect and sentiment classification.
- Therefore, confidence scores cannot be interpreted as actual model accuracy.
- Some comments may contain multiple aspects, but the current approach focuses on assigning a primary aspect.

---

## Future Improvements

- Increase the dataset size by collecting comments from multiple videos.
- Include replies to capture deeper customer discussions.
- Add more aspect categories based on recurring customer feedback.
- Create a manually labeled validation dataset to calculate accuracy, precision, recall, and F1-score.
- Improve handling of slang, abbreviations, emojis, and other social-media-specific language.
- Explore multi-aspect classification for comments that discuss more than one product aspect.
- Build an automated dashboard to summarize aspect-level sentiment and identify the most important improvement areas.

---

## Tech Stack

- `pandas==3.0.5`
- `transformers==5.15.1`

---

## What I Learned (1% Improvement)

- Learned how to extract customer feedback into multiple aspect categories.
- Learned why text normalization, such as using `lower()`, is important for consistent text processing.
- Learned how transformer models can be applied to customer-generated text.
- Learned how aspect-based sentiment analysis can provide more actionable insights than overall sentiment classification.
- Learned that model confidence is not the same as model accuracy and that proper evaluation requires ground-truth labels.