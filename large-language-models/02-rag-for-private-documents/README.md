# RAG for Private Documents

---

## Business Problem

The client wants a private system that can understand information from confidential documents. Because the documents contain sensitive information, using public AI services or external APIs may not be appropriate.

---

## Objective

- Build a RAG system based on private company documents.
- Evaluate the model's output and verify whether the system can provide grounded answers from the document.

---

## Data / Knowledge Source

A PDF document was used as the knowledge source for the RAG pipeline.

The document was processed locally and split into **339 chunks** before being converted into embeddings.

No custom model training or fine-tuning was performed.

---

## Key Insight

- Using an 8B parameter LLM provides a more capable generation model for this use case, but building a complete RAG pipeline requires multiple components.
- The pipeline was designed to run locally, allowing the document and inference process to remain offline without depending on external APIs.
- Running the entire pipeline locally requires downloading and storing multiple model and software dependencies.

---

## Preprocessing

Dependencies and components used:

- **Text extraction:** `pypdf` to extract text from the PDF document.
- **Chunking:** `langchain-text-splitters` using `RecursiveCharacterTextSplitter`.
- **Embedding:** SentenceTransformer using `BAAI/bge-small-en-v1.5`.
- **Vector store:** FAISS using an `IndexFlatIP` index.
- **Retrieval:** Retrieve the top `k=5` candidate chunks based on vector similarity.
- **Reranking:** CrossEncoder using `cross-encoder/ms-marco-MiniLM-L-6-v2` to rerank the retrieved candidates.
- **Generation:** Llama 3.1 8B running fully locally through Ollama.

---

## Modeling

### Architecture Used

A fully local RAG architecture using:

- **Embedding model:** `BAAI/bge-small-en-v1.5`
- **Vector store:** FAISS
- **Reranker:** `cross-encoder/ms-marco-MiniLM-L-6-v2`
- **LLM:** Llama 3.1 8B via Ollama

The LLM is instructed to answer using only the retrieved context and return *"I don't know"* when the answer is not available in the provided context.

---

## Evaluation Metric

The current evaluation uses qualitative testing rather than formal retrieval or generation metrics.

Two test cases were used:

1. **In-context question:** a question whose answer is available in the document.
2. **Out-of-context question:** a randomly selected question that is unrelated to the document.

No formal metrics such as Recall@k, Precision@k, faithfulness score, or answer accuracy were calculated.

---

## Model Result

Two test cases were used to evaluate the RAG pipeline.

### Test Case 1 — Information Available in the Document

The question was related to information contained in the document.

Model response:

> "The main topic appears to be the analysis of the relationship between density and capacitance, and the factors that influence it, likely in the context of materials science or electrochemistry."

The model was able to generate an answer based on the retrieved document context.

### Test Case 2 — Information Not Available in the Document

A randomly selected question unrelated to the document was used.

Model response:

> "I don't know."

The model correctly followed the instruction to avoid generating an answer when the information was not available in the retrieved context.

---

## Key Findings

- The RAG pipeline successfully retrieved document context and generated an answer for the tested in-context question.
- For the out-of-context question, the model returned **"I don't know"**, following the grounding instruction instead of generating an unrelated answer.
- The tested results demonstrate that the current pipeline can distinguish between questions supported by the provided context and questions outside the document's scope.
- FAISS is suitable for this use case because it can run locally without requiring a managed cloud vector database.
- The retrieval function uses `k=5` to retrieve five candidate chunks, which are then reranked and reduced to the top 3 chunks before being passed to the LLM.
- Using `k=5` does not mean retrieving five documents. The source is one document, but the document has been divided into multiple chunks, so `k` refers to the number of retrieved chunks.
- The current `k=5` and `top_n=3` settings were used for the experiment, but a systematic comparison with other values would be required before calling them an optimal configuration.

---

## Business Insight

- The current pipeline demonstrates a promising proof of concept for private document question answering.
- Running the system locally provides an important privacy advantage because confidential documents do not need to be sent to an external AI API.
- However, the current two-test evaluation is not sufficient to confirm production readiness.
- More documents and a larger evaluation set are required before deploying the system in a production environment.

---

## Final Decision

### Recommended Approach: Fully Local RAG with Llama 3.1 8B

### Reasons

- The tested model was able to answer a question related to the document.
- The model returned "I don't know" for an unrelated question in the tested case.
- The 8B model provides a more capable generation model than the previously tested 0.5B model.
- The entire pipeline can run locally without relying on external AI APIs.
- FAISS provides a simple local vector-store solution suitable for the current proof of concept.
- A larger model may provide better generation quality, but it also requires more computational resources and storage.

---

## Limitations

- The current experiment uses only one PDF document.
- Only two test cases were used for evaluation.
- No formal retrieval or generation metrics were calculated.
- The system has not been evaluated across multiple documents.
- The current results do not establish production readiness.
- The retrieval parameters (`k=5` and `top_n=3`) have not been systematically benchmarked.
- Local deployment requires sufficient storage and computational resources for the LLM and supporting models.

---

## Future Improvements

- Test the RAG pipeline with multiple documents.
- Build a larger evaluation dataset containing questions with known answers.
- Evaluate retrieval performance using metrics such as Recall@k.
- Evaluate answer quality and faithfulness against the retrieved context.
- Compare different values of `k` and `top_n` to determine their effect on retrieval and generation quality.
- Customize the system prompt depending on the client's requirements.
- Experiment with larger or alternative LLMs if computational resources allow.

---

## Tech Stack

- `faiss==1.5.3`
- `langchain_text_splitters==1.1.2`
- `numpy==2.5.3`
- `ollama==0.6.2`
- `pypdf==6.18.1`
- `sentence_transformers==6.0.1`

---

## What I Learned (1% Improvement)

- Learned how parameter `k` and `top_n` work.
- Learned that `k=1` is not the same as the number of documents.
- Understood how `RecursiveCharacterTextSplitter` works.
- Understood the difference between SentenceTransformer for embedding and CrossEncoder for re-ranking, and that both are from the same library.
- Learned that retrieval requires transforming the query into a vector first.
