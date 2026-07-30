# HiveMind API Documentation

## Overview

HiveMind exposes a RESTful API built with FastAPI. The API provides authentication, enterprise knowledge search, analytics, metrics, and knowledge management capabilities.

**Base URL (Local Development)**

```text
http://127.0.0.1:8000
```

---

# Authentication

Most endpoints require a JWT Bearer Token.

## Login

**Endpoint**

```http
POST /login
```

### Request

```json
{
  "username": "admin",
  "password": "admin123"
}
```

### Successful Response

```json
{
  "access_token": "<jwt-token>",
  "token_type": "bearer"
}
```

---

## Using the Token

Include the token in the Authorization header.

```http
Authorization: Bearer <jwt-token>
```

---

# Application APIs

## Home

**Endpoint**

```http
GET /
```

### Response

```json
{
  "application": "HiveMind",
  "version": "1.0.0",
  "environment": "development",
  "status": "Running"
}
```

---

## Health Check

**Endpoint**

```http
GET /health
```

### Response

```json
{
  "status": "healthy",
  "application": "HiveMind",
  "version": "1.0.0"
}
```

---

# Knowledge APIs

## Enterprise Search

**Endpoint**

```http
POST /api/v1/search
```

**Authentication Required**

Yes

### Request

```json
{
  "query": "Explain Claims API architecture"
}
```

### Example Response

```json
{
  "query": "Explain Claims API architecture",
  "summary": "Architecture information retrieved successfully.",
  "results": [
    {
      "agent": "Documentation Agent",
      "documents_found": 2
    },
    {
      "agent": "Git Agent",
      "documents_found": 1
    }
  ]
}
```

---

## Upload Knowledge

**Endpoint**

```http
POST /api/v1/upload
```

**Authentication Required**

Yes

### Request

```json
{
  "filename": "incident_rca.md",
  "content": "# RCA\nRoot cause analysis..."
}
```

### Response

```json
{
  "status": "success",
  "message": "Document uploaded successfully."
}
```

---

# Analytics APIs

## Analytics

**Endpoint**

```http
GET /api/v1/analytics
```

### Response

```json
{
  "total_searches": 15,
  "most_searched_query": "Claims API",
  "most_used_agent": "documentation",
  "agent_usage": {
    "documentation": 10,
    "git": 8,
    "incident": 4,
    "employee": 3
  }
}
```

---

## Search History

**Endpoint**

```http
GET /api/v1/history
```

### Response

```json
{
  "total_searches": 3,
  "history": [
    {
      "query": "Claims API",
      "agents": [
        "documentation",
        "git"
      ],
      "timestamp": "2026-07-30 10:15:20"
    }
  ]
}
```

---

## Metrics

**Endpoint**

```http
GET /api/v1/metrics
```

### Response

```json
{
  "application": "HiveMind",
  "version": "1.0.0",
  "environment": "development",
  "status": "Running",
  "uptime": "00:18:42",
  "documents_loaded": 15,
  "total_searches": 22,
  "registered_agents": [
    "Coordinator Agent",
    "Documentation Agent",
    "Git Agent",
    "Incident Agent",
    "Employee Twin Agent"
  ]
}
```

---

# Authentication Errors

## Invalid Credentials

```http
401 Unauthorized
```

```json
{
  "detail": "Invalid username or password"
}
```

---

## Missing Token

```http
401 Unauthorized
```

```json
{
  "detail": "Not authenticated"
}
```

---

## Invalid Token

```http
401 Unauthorized
```

```json
{
  "detail": "Could not validate credentials"
}
```

---

# HTTP Status Codes

| Status Code | Meaning                           |
| ----------- | --------------------------------- |
| 200         | Request completed successfully    |
| 201         | Resource created successfully     |
| 400         | Invalid request                   |
| 401         | Authentication required or failed |
| 404         | Resource not found                |
| 422         | Request validation failed         |
| 500         | Internal server error             |

---

# API Security

HiveMind secures protected endpoints using JWT Bearer Authentication.

Security features include:

* JWT access tokens
* Protected API endpoints
* Authorization header validation
* Request model validation using Pydantic
* Structured exception handling

---

# Supported Content

HiveMind currently supports knowledge stored as Markdown documents.

Example document categories:

* Documentation
* Source Code
* Incident Reports
* Employee Knowledge
* Architecture Documents

---

# Testing

The API can be tested using:

* Swagger UI (`/docs`)
* FastAPI OpenAPI specification
* Postman
* cURL
* Python requests library

---

# Future API Enhancements

Planned improvements include:

* Semantic vector search
* Batch document upload
* User management
* Role-Based Access Control (RBAC)
* Streaming AI responses
* WebSocket support
* Audit logging
* Cloud storage integration
