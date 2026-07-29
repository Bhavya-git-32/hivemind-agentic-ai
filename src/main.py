from fastapi import FastAPI, APIRouter

from src.config import settings
from src.exception_handler import register_exception_handlers
from src.middleware import log_requests
from src.models.request_models import QueryRequest
from src.models.response_models import SearchResponse
from src.services.knowledge_service import KnowledgeService


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=getattr(
        settings,
        "APP_DESCRIPTION",
        "Enterprise Agentic AI Knowledge Platform"
    ),
    contact={
        "name": "Bhavya Sri",
        "url": "https://github.com/Bhavya-git-32",
    },
    license_info={
        "name": "MIT License",
    },
)

# Register Global Exception Handlers
register_exception_handlers(app)

# Register Middleware
app.middleware("http")(log_requests)

# API Router
router = APIRouter(
    prefix="/api/v1",
    tags=["Knowledge Search"]
)


@app.get(
    "/",
    tags=["Application"],
    summary="Application Information",
    description="Returns application information and current status."
)
def home():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "status": "Running"
    }


@app.get(
    "/health",
    tags=["Application"],
    summary="Health Check",
    description="Checks whether the HiveMind API is healthy."
)
def health():
    return {
        "status": "healthy",
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION
    }


@router.post(
    "/search",
    response_model=SearchResponse,
    summary="Search Enterprise Knowledge",
    description="Searches enterprise documentation, Git repositories, incident knowledge, and employee digital twins."
)
def search(request: QueryRequest):
    return KnowledgeService.search(request.query)


# Register API Routes
app.include_router(router)