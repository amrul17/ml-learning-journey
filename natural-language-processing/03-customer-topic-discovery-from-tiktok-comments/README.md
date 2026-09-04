# Customer Topic Discovery from TikTok Comments

---

## Business Problem

The client wants to understand **what customers discuss in the comments** and identify the recurring topics they are talking about.

Manually reviewing hundreds of comments can be time-consuming and makes it difficult to identify common discussion patterns.

---

## Objective

* Automatically discover recurring topics from customer comments.
* Identify representative keywords and comments for each topic.
* Analyze the distribution of discovered topics.
* Evaluate the model output and topic interpretability.

---

## Dataset

The raw dataset was collected from comments on a randomly selected TikTok video.

Only the **main comments** were collected; replies to those comments were not included.

### Dataset Characteristics

* **910 comments** collected in total.
* 4 columns: `User`, `Comment`, `Date`, and `Reply`.
* **885 comments** had non-null `Comment` values.
* 25 rows with missing comments were removed.
* 100% user-generated comments.
* Contains noisy and unstructured text.
* Includes slang, informal language, and variations commonly found in social media comments.
* Contains comments from a global audience with multiple languages.

---

## Exploratory Data Analysis (EDA)

### Key Insights

* The dataset contains a wide variety of opinions and perspectives about the product.
* Comments come from viewers around the world, with multiple languages represented.
* Social media comments contain informal and noisy language, making preprocessing important for topic modeling.
* Many comments are very short and provide limited contextual information.
* Some comments do not clearly represent a specific discussion topic.

---

## Preprocessing

The following preprocessing steps were applied:

1. **Handle missing values**

   * Removed rows with missing `Comment`.
   * 910 → **885 comments**.

2. **Short-text filtering**

   * Removed comments containing fewer than **5 words**.
   * 885 → **493 comments** used for topic modeling.

3. **Vectorizer configuration**

   * English stopword removal.
   * `ngram_range=(1, 2)` to capture both single words and two-word phrases.
   * `min_df=2` to remove terms appearing in fewer than two comments.



---

## Modeling

### Architecture Used

BERTopic, was used as an **unsupervised topic modeling framework** to automatically discover discussion topics without predefined topic labels.

---

## Evaluation Metric

Since this is an **unsupervised topic modeling** task, there is no manually labeled ground-truth dataset in the current experiment.

Therefore, accuracy, precision, recall, and F1-score were not used.

The experiment was evaluated using:

* Number of discovered topics.
* Topic size/distribution.
* Topic keywords.
* Representative comments.
* Topic probability.
* Outlier proportion.

### Topic Probability

The notebook calculates the maximum probability across the topic probability distribution for each comment.

A higher probability indicates that the model assigns the comment more strongly to its selected topic.

> **Important:** Topic probability does not prove that a topic assignment is objectively correct. Human interpretation is still required because no ground-truth topic labels were available.

---

## Model Result

The model discovered **24 non-outlier topics** and **1 outlier bucket (`-1`)** from the 493 comments used for modeling.

### Topic Summary

| Topic ID | Topic Label            | Representation                             | Count |
| -------: | ---------------------- | ------------------------------------------ | ----: |
|       -1 | Outlier                | mayo, add, bro, love, burger, time, sauces |    75 |
|        0 | Egg Burger             | egg burger, egg, eggs, burger, burgers     |    48 |
|        1 | Egg Yolk               | egg, yolk, runny, lost, prefer, want       |    35 |
|        2 | Tomato / Salt / Pepper | tomato, salt, salt pepper, pepper, hard    |    29 |
|        3 | Lettuce / Tomato       | lettuce, lettuce tomato, veggies, tomato   |    27 |
|        4 | Cheese                 | cheese, cheeseburger, american, slice      |    27 |
|        5 | Mustard                | mustard, mustard burger, sandwich, hot     |    26 |
|        6 | Perfect Burger         | burger, perfect burger, burger dont        |    21 |
|        7 | Krabby Patty           | krabby, krabby patty, patty, looks like    |    19 |
|        8 | Pickles / Temperature  | pickles, cold, hot, heat                   |    19 |
|        9 | Onion Ring             | onion, egg onion, onion ring               |    19 |
|       10 | Ketchup                | ketchup, mayo ketchup, bottle              |    18 |
|       11 | Mayo Bottle            | 20, come, 10, mayo, burger                 |    17 |
|       12 | Mayo Bottle Color      | mayo, mayo looks, bottle, red bottle       |    14 |
|       13 | Hot Pickle Request     | yes, ill, need, hot pickle                 |    14 |
|       14 | Gloves / Hygiene       | gloves, using, meat, left, raw             |    12 |
|       15 | Looks Delicious        | delicious, looks delicious, looks          |    11 |
|       16 | Smash Burger           | smash, love, im, fact                      |    10 |
|       17 | Pickles + Mustard      | pickles, pickle, mustard, mustard pickles  |     9 |
|       18 | Seasoning              | seasoning, people, grill, burger           |     9 |
|       19 | Bun / Sesame Seeds     | bun, sesame, seeds, half                   |     8 |
|       20 | Burger Patty           | burger, burger thing, burger patty         |     7 |
|       21 | Making Cheeseburger    | cheeseburger, making cheeseburger          |     7 |
|       22 | Negative Comments      | people, theres, reason, dont like          |     7 |
|       23 | Bun / Lettuce / Tomato | bun, lettuce, tomatoes, order              |     5 |

**Total: 493 comments**

### Sample Predictions

| Comment                                                 | Topic ID | Topic Label       | Topic Probability |
| ------------------------------------------------------- | -------: | ----------------- | ----------------: |
| You ruined it with the mustard and pickles              |       17 | Pickles + Mustard |             1.000 |
| Your ingredients are so well behaved and cooperative... |       -1 | Outlier           |             0.010 |
| You're supposed to use butter                           |       -1 | Outlier           |             0.025 |
| YUCK TOO MUCH MUSTARD BRO THAT IS NOT A FREAKI...       |        5 | Mustard           |             1.000 |
| Yummmmmm I feel like they learned how to make...        |       -1 | Outlier           |             0.024 |

### Topic Interpretation

Several discovered topics have clear and interpretable themes:

* **Egg-related topics** — customer opinions about adding eggs to burgers.
* **Mustard and pickle topics** — preferences regarding condiments and preparation.
* **Ingredient topics** — discussions about cheese, lettuce, tomatoes, onions, mayo, and ketchup.
* **Hygiene topic** — comments related to gloves, raw meat, and food preparation.
* **Positive reaction topics** — comments describing the burger as delicious or visually appealing.

---

## Key Findings

* The model discovered **24 non-outlier topics** from the 493 comments used for modeling.
* **75 comments** were assigned to the outlier bucket (`-1`), making it the largest individual assignment.
* Ingredient-related discussions appear across many of the discovered topics, particularly eggs, mustard, cheese, pickles, tomatoes, lettuce, mayo, and ketchup.
* Some comments assigned to the outlier bucket still appear semantically related to the overall discussion.
* High topic probability indicates stronger model assignment, but it does **not guarantee that the discovered topic is correct**.
* The discovered topics provide a useful first-pass summary of recurring customer discussions without requiring predefined topic categories.

---

## Business Insight

* BERTopic can help summarize hundreds of customer comments into a smaller number of understandable discussion themes.
* The topic distribution can reveal what customers frequently talk about, such as **ingredients, condiments, burger preparation, and food hygiene**.
* Recurring topics can help the client identify areas that may require further investigation.
* Outlier comments can be treated as candidates for **human review** because they do not strongly fit the discovered clusters.

---

## Final Decision

### Recommended Architecture: BERTopic

### Reasons

* Suitable for unsupervised topic discovery.
* Automatically discovers discussion topics without predefined categories.
* Works with natural-language customer comments.
* Provides representative keywords and documents for interpreting discovered topics.
* Provides topic probabilities that can be used as a signal for identifying uncertain assignments.
* Suitable as a first-pass exploratory tool for large collections of customer comments.

---

## Limitations

* The dataset contains comments from only **one TikTok video**.
* Only main comments were collected; replies were not included.
* **392 of 885 usable comments were removed** because they contained fewer than 5 words.
* Short reactions, emojis, and very brief comments are therefore not represented in the final topic model.
* The dataset contains noisy social media language, slang, and multiple languages.
* **75 comments were assigned to the outlier bucket.**
* Some outlier comments may still contain meaningful information.
* No manually labeled ground-truth topic dataset was created.
* No topic coherence metric was used.
* Topic probability does not guarantee topic correctness.
* Human interpretation is still required before using the results for business decisions.

---

## Future Improvements

* Increase the dataset size by collecting comments from multiple TikTok videos.
* Include replies to capture deeper customer discussions.
* Revisit the `MIN_WORDS=5` threshold and test whether shorter comments can be retained without significantly reducing topic quality.
* Tune BERTopic parameters to reduce unnecessary outliers and improve topic separation.
* Merge or reduce redundant topics when multiple topics represent similar discussions.
* Add topic coherence metrics such as **C_v or NPMI**.
* Create a small manually labeled validation dataset to evaluate topic quality.
* Test a multilingual embedding model because the dataset contains comments in multiple languages.
* Improve topic labeling to make the results easier for business users to interpret.

---

## Tech Stack

* Python 3.13.3
* pandas
* bertopic==0.17.4
* scikit-learn==1.9.0

---

## What I Learned (1% Improvement)

* Learned what `stop_words` does in a text vectorizer.
* Learned the basic mechanism of **BERTopic**.
* Learned how `ngram_range` affects topic representation.
* Learned how `min_df` helps filter low-frequency terms.
* Learned the difference between **topic probability and prediction correctness**.
* Learned how to interpret discovered topics using keywords and representative comments.
