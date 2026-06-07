# Log Analyzer API

## Overview

This project is a production-ready refactoring of a legacy Python log processing script.

The original implementation worked for small files but failed when processing large log files (50GB+) due to excessive memory consumption and poor code structure.

This solution introduces:
¸
* Object-Oriented Programming (OOP)
* Generator-based processing
* Memory-efficient file handling
* Production-grade logging
* Exception handling
* FastAPI integration
* Unit testing

---

## Problem Statement

The legacy code loaded the entire log file into memory using:

```python
data = f.readlines()
```

This approach caused Out Of Memory (OOM) failures when processing large files.

The goal was to:

1. Refactor the code using OOP principles.
2. Improve memory efficiency using generators.
3. Add robust exception handling and logging.
4. Expose functionality through a FastAPI endpoint.
5. Analyze time and space complexity.

---

## Legacy Code Issues

### 1. Memory Inefficiency

The entire file was loaded into memory.

```python
data = f.readlines()
```

Space Complexity:

```text
O(n)
```

---

### 2. Poor Error Handling

Invalid records could crash the application.

---

### 3. No Logging

No visibility into processing failures.

---

### 4. Lack of Modularity

All logic existed inside a single function.

---

## Solution Architecture

```text
Client
   │
   ▼
POST /analyze-logs
   │
   ▼
FastAPI Route
   │
   ▼
LogAnalyzer Service
   │
   ├── parse_line()
   ├── validate()
   └── yield Transaction
   │
   ▼
Response Schema
   │
   ▼
JSON Response
```

---

## Project Structure

```text
app/
├── api/
├── core/
├── models/
├── schemas/
├── services/
└── main.py

tests/
sample_data/
logs/
```

---

## Key Features

### OOP Design

Business logic is encapsulated within the `LogAnalyzer` service.

---

### Generator-Based Processing

Uses:

```python
yield
```

to process one record at a time.

Benefits:

* Constant memory usage
* Suitable for very large log files

---

### Structured API Responses

Implemented using Pydantic response models.

---

### Production Logging

Implemented using Python's logging module.

---

### Unit Testing

Implemented using pytest.

---

## Complexity Analysis

### Legacy Solution

Time Complexity:

```text
O(n)
```

Space Complexity:

```text
O(n)
```

because the entire file is loaded into memory.

---

### Refactored Solution

Time Complexity:

```text
O(n)
```

every line must still be processed.

Space Complexity:

```text
O(1)
```

because generator-based processing reads one line at a time.

---

## API Endpoint

### Analyze Logs

```http
POST /analyze-logs
```

Upload a transaction log file.

---

### Sample Input

```text
2026-06-01,user123,15000,ERROR
2026-06-01,user456,5000,ERROR
2026-06-01,user999,18000,ERROR
```

---

### Sample Response

```json
{
  "total_flagged": 2,
  "flagged_users": [
    {
      "user_id": "user123",
      "amount": 15000,
      "status": "flagged"
    },
    {
      "user_id": "user999",
      "amount": 18000,
      "status": "flagged"
    }
  ]
}
```

---

## Challenges Faced

### FastAPI UploadFile Returns Bytes

During testing, an issue occurred:

```text
TypeError:
a bytes-like object is required, not 'str'
```

Cause:

FastAPI's UploadFile streams bytes while the parser expected strings.

Solution:

Each incoming line was decoded using UTF-8 before processing.

```python
if isinstance(line, bytes):
    line = line.decode("utf-8")
```

---

## Testing

Run tests:

```bash
pytest
```

Current Result:

```text
4 passed
```

---

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start server:

```bash
uvicorn app.main:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## Technologies Used

* Python
* FastAPI
* Pydantic
* Pytest
* Logging
* Dataclasses
