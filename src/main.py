from fastapi import FastAPI

from src.api.health import router as health_router
from src.api.knowledge import router as knowledge_router

app = FastAPI(
    title="HiveMind Agentic AI",
    description="Enterprise Knowledge Platform using FastAPI and Agentic AI",
    version="1.0.0",
)

@app.get("/", tags=["Home"])
def home():
    return {
        "application": "HiveMind Agentic AI",
        "version": "1.0.0",
        "status": "Running",
        "message": "Welcome to HiveMind Enterprise Knowledge Platform"
    }

# Register API Routers
app.include_router(health_router)
app.include_router(knowledge_router)