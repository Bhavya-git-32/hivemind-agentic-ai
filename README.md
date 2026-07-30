
# 🚀 HiveMind – Enterprise Multi-Agent AI Knowledge Platform

## Overview

HiveMind is an enterprise-grade, multi-agent AI knowledge platform designed to centralize organizational knowledge and intelligently answer engineering queries. Instead of relying on a single AI assistant, HiveMind orchestrates multiple specialized agents that collaborate to retrieve documentation, source code information, incident history, and domain expertise.

The platform is built with a modular architecture using FastAPI and demonstrates concepts used in modern enterprise AI systems such as agent orchestration, knowledge retrieval, authentication, analytics, and observability.

---

# Features

### 🤖 Multi-Agent Architecture

HiveMind consists of multiple specialized AI agents:

* **Coordinator Agent** – Routes incoming requests to the appropriate agents.
* **Documentation Agent** – Retrieves enterprise documentation.
* **Git Agent** – Retrieves source code and repository knowledge.
* **Incident Agent** – Searches incident reports and RCA documents.
* **Employee Twin Agent** – Identifies domain experts and knowledge owners.

---

### 🔍 Intelligent Knowledge Search

* Enterprise document search
* Category-based retrieval
* Keyword relevance ranking
* Unified response generation

---

### 🔐 Secure Authentication

* JWT Authentication
* Protected API endpoints
* Login endpoint
* Bearer Token authorization

---

### 📊 Analytics & Observability

* Search analytics
* Search history
* Application metrics
* Logging
* Health monitoring

---

### 📚 Knowledge Management

* Markdown knowledge base
* Knowledge upload API
* Automatic indexing
* Document categorization

---

## System Architecture

```text
                    User
                      │
                      ▼
                FastAPI REST API
                      │
          JWT Authentication Layer
                      │
                      ▼
             Coordinator Agent
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
Documentation      Git Agent     Incident Agent
      │               │               │
      └───────────────┼───────────────┘
                      ▼
             Employee Twin Agent
                      │
                      ▼
             Retrieval Service
                      │
                      ▼
         Enterprise Knowledge Base
```

---

# Technology Stack

## Backend

* Python 3.14
* FastAPI
* Uvicorn
* Pydantic

## Authentication

* JWT
* OAuth2 Password Flow
* Passlib

## Knowledge Processing

* Markdown Documents
* Custom Retrieval Engine
* Index Service

## Testing

* Pytest

## Documentation

* Swagger UI
* OpenAPI

---

# Project Structure

```text
src/
│
├── agents/
│   ├── coordinator_agent.py
│   ├── documentation_agent.py
│   ├── git_agent.py
│   ├── incident_agent.py
│   └── employee_twin_agent.py
│
├── api/
├── auth/
├── models/
├── services/
├── utils/
│
├── config.py
├── middleware.py
├── exception_handler.py
└── main.py
```

---

# API Endpoints

## Authentication

| Method | Endpoint |
| ------ | -------- |
| POST   | /login   |

## Knowledge

| Method | Endpoint       |
| ------ | -------------- |
| POST   | /api/v1/search |
| POST   | /api/v1/upload |

## Analytics

| Method | Endpoint          |
| ------ | ----------------- |
| GET    | /api/v1/analytics |
| GET    | /api/v1/history   |
| GET    | /api/v1/metrics   |

## Application

| Method | Endpoint |
| ------ | -------- |
| GET    | /        |
| GET    | /health  |

---

# Running the Project

## Clone Repository

```bash
git clone https://github.com/<your-username>/hivemind-agentic-ai.git
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run

```bash
python -m uvicorn src.main:app --reload
```

---

# Swagger Documentation

After starting the server:

```
http://127.0.0.1:8000/docs
```

---

# Future Enhancements

* Semantic search using FAISS
* Vector database integration
* OpenAI / Amazon Bedrock integration
* Real-time collaboration
* React dashboard
* Docker deployment
* Kubernetes deployment
* CI/CD pipeline
* AWS cloud deployment

---

# Learning Outcomes

This project demonstrates:

* Multi-Agent AI architecture
* REST API development
* Enterprise software architecture
* Authentication & Authorization
* Knowledge retrieval systems
* Logging & observability
* Modular software design
* API documentation
* Testing with Pytest

---

# Author

**Bhavya Sri**

Associate Software Engineer

Cloud | Python | FastAPI | AWS | Agentic AI
