# HiveMind Project Structure

## Overview

HiveMind follows a modular, layered architecture that separates API routing, business logic, agent orchestration, services, authentication, and utilities into independent components. This structure improves maintainability, scalability, and testability.

---

# Project Directory

```text
hivemind-agentic-ai/
│
├── src/
│   ├── agents/
│   ├── api/
│   ├── auth/
│   ├── models/
│   ├── services/
│   ├── utils/
│   ├── config.py
│   ├── main.py
│   ├── middleware.py
│   ├── exceptions.py
│   └── exception_handler.py
│
├── knowledge/
│
├── tests/
│
├── README.md
├── ARCHITECTURE.md
├── API_DOCUMENTATION.md
├── PROJECT_STRUCTURE.md
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .gitignore
```

---

# Source Folder (`src/`)

The `src` directory contains the complete application source code.

---

## `agents/`

Contains the AI agent implementations responsible for different knowledge domains.

### coordinator_agent.py

Central orchestration component.

Responsibilities:

* Receives user queries
* Determines which agents should participate
* Collects responses
* Returns a unified result

---

### documentation_agent.py

Searches documentation such as:

* Architecture documents
* Technical specifications
* User guides
* Markdown documentation

---

### git_agent.py

Responsible for source-code-related knowledge.

Examples:

* API implementations
* Repository documentation
* Code ownership

---

### incident_agent.py

Searches operational knowledge.

Examples:

* Incident reports
* Root Cause Analysis (RCA)
* Production issues

---

### employee_twin_agent.py

Represents organizational expertise.

Provides:

* Subject Matter Expert (SME) lookup
* Component ownership
* Team knowledge mapping

---

# `api/`

Contains optional API routers.

Examples:

* Health APIs
* Knowledge APIs

Keeping routes separated simplifies maintenance as the application grows.

---

# `auth/`

Authentication and authorization components.

Includes:

* JWT token generation
* Token validation
* Password hashing
* Login service
* Security utilities

---

# `models/`

Contains Pydantic models.

Examples:

* Request models
* Response models
* Authentication models
* Validation schemas

These models provide automatic validation and OpenAPI documentation.

---

# `services/`

Business logic layer.

Major services include:

### KnowledgeService

Coordinates knowledge retrieval.

---

### RetrievalService

Ranks and filters documents.

---

### ResponseService

Generates the final API response.

---

### IndexService

Caches enterprise knowledge.

---

### DocumentLoader

Loads Markdown knowledge files.

---

### AnalyticsService

Tracks:

* Search history
* Query frequency
* Agent usage

---

### MetricsService

Provides:

* Uptime
* Application status
* Registered agents
* Loaded documents
* Search statistics

---

### UploadService

Allows enterprise knowledge to be uploaded and indexed.

---

# `utils/`

Reusable utilities.

Currently includes:

* Logger configuration
* Shared helper functions

---

# Configuration Files

## config.py

Application configuration.

Stores:

* Application name
* Version
* Environment
* JWT configuration
* Other global settings

---

## middleware.py

Contains FastAPI middleware.

Responsibilities include:

* Request logging
* Execution timing
* Middleware pipeline

---

## exception_handler.py

Registers global exception handlers.

Ensures consistent API error responses.

---

## exceptions.py

Defines custom application exceptions.

---

## main.py

Application entry point.

Responsibilities:

* Creates FastAPI application
* Registers middleware
* Registers exception handlers
* Defines API endpoints
* Configures authentication
* Starts the application

---

# Knowledge Folder

Stores enterprise knowledge documents.

Typical files include:

* Architecture documents
* Incident reports
* Git documentation
* Employee knowledge
* API documentation

Markdown is used because it is lightweight, version-controlled, and easy to maintain.

---

# Tests

Contains automated tests.

Examples:

* Health endpoint tests
* Coordinator tests
* Search tests
* Authentication tests

The project uses **pytest** for testing.

---

# Documentation Files

## README.md

Project overview.

---

## ARCHITECTURE.md

Explains the system architecture and request flow.

---

## API_DOCUMENTATION.md

Describes every REST endpoint with request and response examples.

---

## PROJECT_STRUCTURE.md

Explains the responsibility of every major folder and file.

---

# Dependency Files

## requirements.txt

Lists all Python dependencies.

---

## Dockerfile

Defines the container image used for deployment.

---

## docker-compose.yml

Defines multi-container local development.

---

## .gitignore

Prevents unnecessary files from being committed.

Examples:

* Virtual environments
* Python cache
* IDE configuration
* Log files

---

# Design Principles

HiveMind is designed using modern software engineering principles.

* Modular architecture
* Separation of concerns
* Single Responsibility Principle (SRP)
* Loose coupling
* High cohesion
* Reusable services
* Extensible agent framework
* Testable components

---

# Extending HiveMind

Adding a new AI agent typically requires only:

1. Creating a new agent inside `agents/`
2. Updating the `CoordinatorAgent`
3. Adding knowledge documents (if required)
4. Writing tests

No major architectural changes are required.

---

# Summary

HiveMind is organised into clearly defined layers that separate API handling, business logic, orchestration, authentication, analytics, and knowledge retrieval. This structure makes the project easier to understand, maintain, test, and extend as new enterprise capabilities are introduced.
