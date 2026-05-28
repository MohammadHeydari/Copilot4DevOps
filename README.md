# AI-Powered RAG Chat System (FastAPI + FAISS + Ollama)

A production-style Retrieval-Augmented Generation (RAG) system built with FastAPI, FAISS, and local LLMs via Ollama.

This project demonstrates how to build a scalable backend for AI-powered question answering using custom knowledge bases.

---

## Features

* **Semantic Search (FAISS)**

  * Efficient vector similarity search
  * Supports multilingual embeddings (Persian + English)

* **LLM Integration (Ollama)**

  * Local inference (no OpenAI dependency required)
  * Streaming responses

* **FastAPI Backend**

  * REST + WebSocket endpoints
  * Real-time streaming responses

* **Custom Knowledge Base**

  * Supports `.md`, `.json`, `.log`
  * Chunking + preprocessing pipeline

* **RAG Pipeline**

  * Query → Embedding → Retrieval → LLM → Answer

* **Metrics Endpoint (Prometheus-ready)**

  * `/metrics` endpoint for observability

---

## Architecture

```
User Query - > FastAPI API - > Embedding Model - > FAISS Vector Search - > Top-K Context Retrieval - > LLM (Ollama) - > Final Answer
```

---

## Setup

### 1. Clone repo

```bash
git clone https://github.com/MohammadHeydari/Copilot4DevOps
cd Copilot4DevOps
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run Ollama

Make sure Ollama is running locally:

```bash
ollama run llama3
```

---

### 4. Build FAISS index

```bash
python ingestion/run_ingestion.py
```

---

### 5. Run API

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## API Usage

### Ask a question

```
GET /ask?q=Your question
```

Example:

```
/ask?q=Why payment is failing?
```

---

### Response

```json
{
  "question": "...",
  "answer": "...",
  "contexts": [...]
}
```

---

## Metrics

```
GET /metrics
```

Prometheus-compatible metrics endpoint.

---

## Example Use Case

Query:

```
TimeoutError bank API not responding
```

Output:

```
Retry + fallback
```

---

## Tech Stack

* FastAPI
* FAISS
* SentenceTransformers
* Ollama (LLM)
* Python

---

## Future Improvements

* Grafana dashboards
* Alerting system
* RAG evaluation (accuracy / hallucination detection)
* Caching layer (Redis)
* Deployment (Docker / Kubernetes)

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first.


