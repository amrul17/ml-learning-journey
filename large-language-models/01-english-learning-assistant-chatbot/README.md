# English Learning Assistant Chatbot

---

## Business Problem

The client wants a private tutor that can answer questions about English.

---

## Objective

* Build a model that can teach someone English.
* Evaluate the model's output.

---

## Data / Knowledge Source

No custom dataset was curated for this experiment. The model relies entirely on the parametric knowledge learned during Qwen's pretraining, including vocabulary, translation, grammar rules, and other language knowledge.

No fine-tuning or retrieval-augmented grounding was applied.

### Model Characteristics

* Using the 0.5 billion parameter version (`Qwen2.5-0.5B-Instruct`).

---

## Resource & Deployment Constraints

* The small-parameter version can run on both CPU and GPU.
* It can run on the client's machine without requiring a paid API or subscription.
* Local inference avoids per-request API costs and allows the client to use the assistant without depending on an external API service.

*Note: Since no custom dataset was built, there is no exploratory data analysis (EDA) to perform in the traditional sense. This section instead documents deployment feasibility.*

---

## Preprocessing

1. Install dependencies:

   * `transformers` to load and run the open-source model.
   * `torch`, the deep learning backend.
   * `accelerate`, which helps efficiently load the model on CPU/GPU.
   * `sentencepiece`, a tokenizer dependency required by many models.

2. Import libraries:

   * `AutoTokenizer` and `AutoModelForCausalLM` from `transformers`, which can load open-source language models by name.
   * `torch`, used for tensor operations and model inference.
   * `json` and `datetime`, used later to save conversation logs.

3. Prompt the model to act as an English teacher. The system prompt can be adjusted depending on the intended use case.

4. Write code that prioritizes GPU usage for faster inference when a compatible GPU is available.

---

## Modeling

### Architecture Used

Qwen2.5-0.5B-Instruct — an open-source instruction-tuned language model that can run locally without requiring an external API.

---

## Evaluation Metric

* **Current approach:** Human judgment based on a single sample response (n = 1). This is anecdotal and not yet a reliable evaluation method.
* **Recommended next step:** Build a small evaluation set containing 10–20 grammar and vocabulary questions with known correct answers.

Each response can be evaluated using a simple rubric:

1. Factual correctness of the grammar or vocabulary explanation.
2. Validity of the example sentence.
3. Tone and clarity relative to the system prompt.

This would turn qualitative judgment into a more reproducible evaluation instead of relying on a single example.

---

## Model Result

Test prompt (intentionally written with incorrect grammar):

> *"what is the different between either and neither?"*

Model response:

```text
Tutor: Hi there! Great question! Let's think about the word "either" and "neither."

- Either: This phrase typically refers to two options or choices. It often comes before a conjunction like "or" or "but". For example:
  - "He likes either ice cream or pizza."
  - "We should choose either option."

- Neither: This phrase usually refers to only one choice or option. It often comes before a conjunction like "nor" or "and". For example:
  - "She doesn't like neither ice cream nor pizza."
  - "They chose neither option."

In sentences like "Either he likes ice cream or pizza," "neither he likes ice cream nor pizza," or "Neither she likes ice cream nor pizza," "he" is referring to the person who likes ice cream, "she" is referring to the person who likes pizza, and "ice cream" and "pizza" are the two options available.
```

The response follows the system prompt correctly in tone and structure: it provides a clear answer and examples.

However, the explanation itself contains factual grammatical errors and misconceptions. For example, the model incorrectly describes "neither" as referring to "only one choice or option" and produces the nonstandard sentence:

> "She doesn't like neither ice cream nor pizza."

This demonstrates an important distinction between **instruction following** and **factual correctness**: the model can follow the requested response style while still producing an incorrect explanation.

System prompt used:

```text
"You are Amy, a friendly and patient English language tutor. When the student writes something with a grammar or vocabulary mistake, gently point it out, explain the correct form in simple terms, and give one clear example sentence. If the student asks a question about English (grammar rules, vocabulary, pronunciation, or usage), answer clearly and give an example. Keep your answers short, warm, and encouraging. Avoid overly technical linguistic terms unless the student asks for them."
```

---

## Key Findings

* The model follows the system prompt's instructions well: the answer is clear, warm, and includes examples as requested.
* However, the explanation contains factual grammatical errors and misconceptions.
* Instruction-following quality and factual correctness are separate evaluation dimensions.
* Lowering the temperature did not resolve the observed factual error, suggesting that temperature alone was insufficient to address the problem.
* The 0.5B model may have insufficient capability for reliable grammar reasoning in this use case.
* This conclusion is based on a single test case; additional samples and model comparisons are required before confirming the cause.

---

## Business Insight

* This model cannot be sent to the client in its current state. The response style is appropriate, but the factual content is unreliable, which is unacceptable for an English-learning application.
* A different model, a larger parameter size, or a grounding strategy such as retrieval from a curated grammar reference should be evaluated.
* The positive takeaway is that the existing notebook pipeline — model loading, prompting, GPU handling, and logging — is reusable. Swapping the model requires relatively small changes.

---

## Final Decision

### Recommended Approach: Test Alternative Models and Grounding Strategies

### Reasons

* Need to experiment with other models before deployment.
* The 0.5B model was not reliable enough for the tested grammar explanation task.
* Lowering the temperature did not resolve the observed factual error.
* A larger or more capable instruction-tuned model should be evaluated.
* A grounding strategy such as RAG could be tested to reduce reliance on the model's parametric knowledge.
* The current local inference pipeline can be reused for further experiments.

---

## Limitations

* The model cannot be considered reliable for reasoning-based English questions based on the current evidence.
* Temperature tuning alone did not resolve the observed error.
* The evaluation is currently based on a single example rather than a systematic test set.
* The experiment does not establish that parameter size alone caused the observed error.
* No comparison with larger models or grounding approaches has been performed yet.

---

## Future Improvements

* Test a larger Qwen variant on the same evaluation questions to investigate whether model capacity affects performance.
* Try other instruction-tuned models and compare their responses using the same evaluation rubric.
* Test a grounding approach by retrieving answers from a small curated set of English grammar references.
* Build a proper evaluation set containing 10–20 grammar and vocabulary questions.
* Increase model parameter size if the client's computational resources allow it.

---

## Tech Stack

* Python 3.13.3
* `torch==2.14.0`
* `transformers==5.15.10`

---

## What I Learned (1% Improvement)

* Learned how an LLM works, from tokenization, embedding, self-attention/multi-head attention, to detokenization.
* Understood the functions of `AutoTokenizer` and `AutoModelForCausalLM`.
* Understood why GPUs use float16 rather than float32 like CPUs.
* Learned about `max_new_tokens`, `top_p`, and temperature parameters.
