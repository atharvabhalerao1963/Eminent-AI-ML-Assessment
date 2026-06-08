
# Enterprise HR Policy Assistant

## Overview

The Enterprise HR Policy Assistant is a Retrieval-Augmented Generation (RAG) application designed to help employees quickly access and understand company HR policies through natural language conversations.

Instead of manually searching through lengthy HR documents, employees can ask questions such as:

* "What is the maternity leave policy?"
* "How many sick leave days do employees receive?"
* "Am I eligible for bereavement leave after 6 months of employment?"
* "What is the work-from-home policy?"

The system retrieves relevant policy sections from an HR Policy Handbook stored in a vector database and uses a Large Language Model (LLM) to generate accurate, context-aware responses.

This project was developed as part of the Advanced AI Systems at Production Level assessment, focusing on Generative AI, Retrieval-Augmented Generation (RAG), Vector Databases, Deployment, and Production Debugging.

---

## Features

### AI-Powered HR Assistant

* Answers employee questions using natural language.
* Provides context-aware responses based on company policies.
* Reduces manual effort in searching HR documents.

### Retrieval-Augmented Generation (RAG)

* Retrieves relevant policy sections before generating responses.
* Reduces hallucinations compared to standalone LLMs.
* Grounds responses in company-approved documentation.

### Document Processing

* Loads HR policy documents in PDF format.
* Splits documents into manageable chunks.
* Generates embeddings for semantic search.

### Vector Search

* Uses ChromaDB as a local vector database.
* Stores document embeddings for efficient retrieval.
* Supports similarity-based search.

### Large Language Model Integration

* Integrates with Groq-hosted LLMs.
* Generates concise and human-readable answers.
* Restricts answers to retrieved policy context.

### API Layer

* FastAPI backend for serving AI responses.
* REST endpoints for question answering.
* Swagger UI for testing and documentation.

### Frontend Interface

* Streamlit-based user interface.
* Allows employees to interact with the HR assistant.
* Displays generated responses in a clean format.

### Containerization

* Dockerized deployment.
* Docker Compose support.
* Portable and production-ready setup.

---

## System Architecture

The application follows a modular Retrieval-Augmented Generation (RAG) architecture.

```text
User Question
      │
      ▼
FastAPI / Streamlit
      │
      ▼
Retriever
(ChromaDB)
      │
      ▼
Relevant HR Policy Chunks
      │
      ▼
Groq LLM
      │
      ▼
Final Answer
```

### Workflow

1. Employee submits a question.
2. The retriever converts the query into embeddings.
3. ChromaDB searches for the most relevant HR policy chunks.
4. Retrieved context is passed to the LLM.
5. The LLM generates a response grounded in the retrieved policy information.
6. The answer is returned through the API or Streamlit interface.



## Project Structure

```text
Problem_3_HR_AiAssistance
│
├── backend/
│   ├── api.py
│   └── schemas.py
│
├── frontend/
│   └── app.py
│
├── rag/
│   ├── ingest.py
│   ├── retriever.py
│   ├── generator.py
│   ├── prompts.py
│   ├── chain.py
│   ├── test_retrieval.py
│   └── test_rag.py
│
├── data/
│   └── hr_policy.pdf
│
├── vectorstore/
│   └── chroma_db/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

### Directory Explanation

#### backend/

Contains the FastAPI application and API schemas.

* `api.py` → FastAPI endpoints
* `schemas.py` → Request and response models

#### frontend/

Contains the Streamlit user interface.

* `app.py` → Frontend application

#### rag/

Contains the complete Retrieval-Augmented Generation pipeline.

* `ingest.py` → PDF ingestion and vector database creation
* `retriever.py` → Retrieves relevant document chunks
* `generator.py` → Generates responses using Groq LLM
* `prompts.py` → Prompt templates
* `chain.py` → End-to-end RAG orchestration
* `test_retrieval.py` → Retriever testing
* `test_rag.py` → Full RAG pipeline testing

#### data/

Stores source HR policy documents.

#### vectorstore/

Stores ChromaDB embeddings and indexes.

#### Dockerfile

Containerizes the application.

#### docker-compose.yml

Simplifies deployment and service management.

---

## Technology Stack

| Component            | Technology       |
| -------------------- | ---------------- |
| Programming Language | Python           |
| Backend Framework    | FastAPI          |
| Frontend             | Streamlit        |
| RAG Framework        | LangChain        |
| Embedding Model      | all-MiniLM-L6-v2 |
| Vector Database      | ChromaDB         |
| LLM Provider         | Groq             |
| Document Loader      | PyPDF            |
| Containerization     | Docker           |
| Orchestration        | Docker Compose   |

---

## RAG Pipeline

The project follows a Retrieval-Augmented Generation workflow.

### Step 1: Document Ingestion

The HR Policy Handbook is loaded using PyPDF and converted into LangChain documents.

### Step 2: Text Chunking

The document is split using RecursiveCharacterTextSplitter.

Configuration:

* Chunk Size: 1500
* Chunk Overlap: 200

This ensures policy sections remain semantically meaningful while fitting within model context limits.

### Step 3: Embedding Generation

Each chunk is converted into vector embeddings using:

```python
sentence-transformers/all-MiniLM-L6-v2
```

These embeddings capture semantic meaning rather than simple keyword matching.

### Step 4: Vector Storage

Embeddings are stored in ChromaDB for efficient similarity search.

### Step 5: Retrieval

When a user asks a question:

1. The question is embedded.
2. Similarity search is performed.
3. Top-k relevant chunks are retrieved.

### Step 6: Response Generation

Retrieved context is provided to the Groq-hosted LLM.

The model is instructed to:

* Answer only from retrieved context.
* Avoid making assumptions.
* Return a fallback response if information is unavailable.

### Step 7: Final Response

The generated answer is returned through:

* FastAPI endpoint
* Streamlit frontend


## Production Debugging

### Problem Scenario

During production testing, users reported that questions related to **Maternity Leave** occasionally returned information from the **Sick Leave Policy**.

This indicates a retrieval quality issue where the retriever selects semantically similar but incorrect document chunks.

Example:

**User Question**

```text
What is the maternity leave policy?
```

**Incorrect Retrieval**

```text
Sick Leave Policy:
Employees are entitled to 12 paid sick leave days annually.
```

**Expected Retrieval**

```text
Maternity Leave Policy:
Eligible employees are entitled to 26 weeks of paid maternity leave.
```

---

### Step 1: Evaluate Retrieval Quality

The first step is to inspect the retrieved chunks before they are sent to the LLM.

Debugging actions:

* Print retrieved chunks to logs.
* Review top-k search results.
* Verify that relevant policy sections appear among retrieved documents.
* Create a benchmark set of HR-related questions and expected policy sections.

Example test questions:

| Question                                | Expected Policy  |
| --------------------------------------- | ---------------- |
| What is maternity leave?                | Maternity Leave  |
| How many sick leave days are available? | Sick Leave       |
| What is the remote work policy?         | Work From Home   |
| What is the probation period?           | Probation Policy |

---

### Step 2: Root Cause Analysis

Possible causes include:

#### Large Chunk Sizes

Chunks may contain multiple HR policies in a single document segment.

#### Poor Semantic Separation

Different leave policies may use similar language, causing embedding overlap.

#### Insufficient Retrieval Configuration

A low-quality retrieval strategy may rank partially related chunks higher than the correct section.

#### Missing Metadata

Document chunks currently lack section-level metadata such as:

* Leave Policy
* Remote Work Policy
* Benefits Policy
* Code of Conduct

Metadata could improve retrieval precision.

---

### Step 3: Improve Chunking Strategy

Several improvements can increase retrieval accuracy.

#### Section-Aware Chunking

Split the document according to policy headings instead of fixed character counts.

Example:

```text
Maternity Leave
--------------------------------

Sick Leave
--------------------------------

Remote Work Policy
--------------------------------
```

#### Smaller Chunks

Reduce chunk size to improve topic separation.

Current:

```text
Chunk Size = 1500
Chunk Overlap = 200
```

Potential Improvement:

```text
Chunk Size = 800
Chunk Overlap = 100
```

#### Metadata Tagging

Store metadata for each chunk:

```python
{
    "section": "Maternity Leave"
}
```

This enables metadata filtering during retrieval.

---

### Step 4: Retriever Improvements

#### Increase Retrieval Quality

Retrieve more candidate chunks and rerank them.

Example:

```python
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 5}
)
```

#### Similarity Score Inspection

Track retrieval scores to identify weak matches.

Low-confidence results should be treated carefully.

#### Hybrid Retrieval

Combine:

* Semantic Search
* Keyword Search

This improves accuracy for policy-specific questions.

---

### Step 5: Fallback Mechanisms

If retrieval confidence is low, the system should avoid generating uncertain answers.

Example response:

```text
I could not find sufficient information in the HR policy document to answer this question.
```

Benefits:

* Reduces hallucinations.
* Improves user trust.
* Prevents policy misinformation.

---

### Step 6: Guardrails

To ensure reliability:

#### Context-Only Responses

The LLM should answer only from retrieved context.

#### Source Attribution

Display supporting policy sections alongside answers.

#### Hallucination Prevention

If supporting evidence is unavailable:

* Do not guess.
* Return a fallback response.

---

### Step 7: Monitoring and Observability

A production deployment should continuously monitor retrieval quality.

Metrics to track:

* Retrieval accuracy
* Top-k relevance
* User feedback
* Failed queries
* Hallucination rate

Useful logs:

* User question
* Retrieved chunks
* Similarity scores
* Generated answer

These metrics help identify retrieval failures before they impact users.

---

### Summary

To address incorrect retrievals such as returning Sick Leave information for Maternity Leave questions, the recommended production strategy is:

1. Evaluate retrieval quality.
2. Improve chunking methodology.
3. Add metadata-based retrieval.
4. Increase retrieval precision using reranking.
5. Introduce fallback mechanisms.
6. Enforce strict guardrails.
7. Monitor retrieval performance continuously.

These improvements significantly reduce hallucinations and improve the reliability of the HR Policy Assistant in production environments.
## Installation & Setup

### Clone the Repository

```bash
git clone <repository-url>
cd Problem_3_HR_AiAssistance
```

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Running the Application

### Run Locally

#### Create Vector Database

```bash
python rag/ingest.py
```

#### Start FastAPI

```bash
uvicorn backend.api:app --reload
```

API available at:

```text
http://localhost:8000
```

Swagger UI:

```text
http://localhost:8000/docs
```

#### Start Streamlit Frontend

```bash
streamlit run frontend/app.py
```

---

### Run with Docker

Build and start containers:

```bash
docker compose up --build
```

Application available at:

```text
http://localhost:8000/docs
```

---

## API Endpoints

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

---

### Ask Question

```http
POST /ask
```

Request:

```json
{
  "question": "What is maternity leave?"
}
```

Response:

```json
{
  "answer": "Eligible employees are entitled to 26 weeks of paid maternity leave.",
  "sources": []
}
```

---

## Example Questions

* What is the maternity leave policy?
* How many sick leave days are available?
* What is the work-from-home policy?
* What is the probation period?
* What benefits do full-time employees receive?
* What is the bereavement leave policy?
* How does the remote work approval process work?

---

## Future Improvements

* Metadata-aware retrieval
* Hybrid search (semantic + keyword)
* Reranking models
* Multi-document support
* User authentication
* HR analytics dashboard
* Retrieval evaluation framework
* Feedback collection system

---

## Author

Atharva Bhalerao


<img width="1470" height="956" alt="Screenshot 2026-06-08 at 2 38 04 PM" src="https://github.com/user-attachments/assets/aed564c8-0160-48de-8c31-ad41508a2440" />
<img width="1470" height="956" alt="Screenshot 2026-06-08 at 2 37 30 PM" src="https://github.com/user-attachments/assets/05d50f9f-000b-48ca-9f95-df5dfe4bc435" />


