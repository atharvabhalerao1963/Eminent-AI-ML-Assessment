# Eminent AI/ML Assessment Solutions

## Overview

This repository contains solutions for the **Eminent AI/ML Practical Assessment**, covering Machine Learning, Production-Grade Python Engineering, and Advanced Retrieval-Augmented Generation (RAG) Systems.

The assessment demonstrates skills in:

* Machine Learning Pipelines
* Imbalanced Classification Problems
* Model Evaluation & Threshold Optimization
* Python Software Engineering
* Object-Oriented Programming
* FastAPI Development
* Production Logging & Error Handling
* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Docker Containerization
* Production Debugging Strategies

---

# Repository Structure

```text
Eminent-AI-ML-Assessment/
│
├── problem_1_predictive_maintenance/
│
├── Problem_2_Legacy_code/
│
├── Problem_3_HR_AiAssistance/
│
└── README.md
```

---

# Problem 1 – Predictive Maintenance

## Objective

Build an end-to-end machine learning pipeline for predictive maintenance using a highly imbalanced dataset where machine failures represent only 0.5% of all observations.

## Features

* Synthetic dataset generation using `make_classification`
* Data preprocessing pipeline
* Feature scaling
* Outlier treatment
* Imbalanced data handling
* Model training and comparison
* Hyperparameter tuning
* Evaluation using imbalance-aware metrics
* Technical memo explaining business trade-offs

## Models Implemented

* Logistic Regression
* Random Forest Classifier

## Imbalance Handling Techniques

* SMOTE Oversampling
* Class Weight Adjustment

## Evaluation Metrics

* Precision
* Recall
* F1 Score
* ROC-AUC
* PR-AUC

## Project Location

```text
problem_1_predictive_maintenance/
```

---

# Problem 2 – Legacy Code Refactoring

## Objective

Refactor a memory-inefficient log-processing script into a production-ready FastAPI application.

## Features

* Object-Oriented Design
* Generator-Based Processing
* Memory-Efficient File Handling
* Production Logging
* Robust Exception Handling
* Async FastAPI Endpoint
* Unit Testing
* Clean Project Architecture

## API Endpoint

### Analyze Logs

```http
POST /analyze-logs
```

Accepts a transaction log file and returns flagged transactions.

## Engineering Improvements

### Legacy Version

* Reads entire file into memory
* High memory consumption
* Poor error handling
* No logging
* No modularity

### Refactored Version

* Stream-based processing
* Generator architecture
* Structured logging
* FastAPI integration
* Production-ready design

## Project Location

```text
Problem_2_Legacy_code/
```

---

# Problem 3 – Enterprise HR Policy Assistant

## Objective

Build a Retrieval-Augmented Generation (RAG) system that answers employee HR policy questions using document retrieval and Large Language Models.

## Architecture

Employee Query
↓
Retriever
↓
ChromaDB Vector Store
↓
Relevant HR Policy Chunks
↓
LLM (Groq)
↓
Final Answer

## Technologies Used

* LangChain
* ChromaDB
* HuggingFace Embeddings
* Groq LLM
* FastAPI
* Streamlit
* Docker

## Features

* PDF ingestion pipeline
* Embedding generation
* Vector search
* Context retrieval
* LLM-based answer generation
* Modular RAG architecture
* Retrieval testing
* Production debugging analysis

## Project Location

```text
Problem_3_HR_AiAssistance/
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd Eminent-AI-ML-Assessment
```

---

# Running Problem 1

```bash
cd problem_1_predictive_maintenance
```

Open:

```text
notebooks/predictive_maintenance.ipynb
```

Run all notebook cells to reproduce results.

---

# Running Problem 2

```bash
cd Problem_2_Legacy_code

pip install -r requirements.txt

uvicorn app.main:app --reload
```

API Documentation:

```text
http://localhost:8000/docs
```

---

# Running Problem 3

```bash
cd Problem_3_HR_AiAssistance

pip install -r requirements.txt
```

Create Vector Database:

```bash
python rag/ingest.py
```

Start Backend:

```bash
uvicorn backend.api:app --reload
```

Run Streamlit Frontend:

```bash
streamlit run frontend/app.py
```

---

# Docker Support

Problem 3 includes:

* Dockerfile
* docker-compose.yml

To start services:

```bash
docker-compose up --build
```

---

# Testing

## Problem 2

```bash
cd Problem_2_Legacy_code

pytest
```

## Problem 3

```bash
cd Problem_3_HR_AiAssistance

pytest
```

---

# Assessment Coverage

| Requirement                   | Status |
| ----------------------------- | ------ |
| End-to-End ML Pipeline        | ✅      |
| Imbalanced Learning           | ✅      |
| Model Evaluation              | ✅      |
| Technical Memo                | ✅      |
| OOP Refactoring               | ✅      |
| Memory Optimization           | ✅      |
| FastAPI Development           | ✅      |
| Logging & Error Handling      | ✅      |
| RAG Architecture              | ✅      |
| ChromaDB Integration          | ✅      |
| HuggingFace Embeddings        | ✅      |
| Docker Containerization       | ✅      |
| Production Debugging Analysis | ✅      |


# Author

**Atharva Bhalerao**


