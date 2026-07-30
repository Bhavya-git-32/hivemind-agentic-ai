from fastapi import (
    FastAPI,
    APIRouter,
    Depends,
    HTTPException
)

from src.config import settings
from src.exception_handler import register_exception_handlers
from src.middleware import log_requests
from src.services.metrics_service import MetricsService

from src.services.knowledge_service import KnowledgeService
from src.services.analytics_service import AnalyticsService
from src.services.upload_service import UploadService

from src.models.request_models import (
    QueryRequest,
    UploadRequest
)

from src.models.response_models import SearchResponse
from src.models.auth_models import (
    LoginRequest,
    TokenResponse
)

from src.auth.auth_service import AuthService
from src.auth.auth import get_current_user


# --------------------------------------------------
# FastAPI Application
# --------------------------------------------------

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
        "url": "https://github.com/Bhavya-git-32"
    },
    license_info={
        "name": "MIT License"
    }
)


# --------------------------------------------------
# Middleware
# --------------------------------------------------

app.middleware("http")(log_requests)


# --------------------------------------------------
# Exception Handlers
# --------------------------------------------------

register_exception_handlers(app)


# --------------------------------------------------
# API Router
# --------------------------------------------------

router = APIRouter(
    prefix="/api/v1"
)


# --------------------------------------------------
# Home Endpoint
# --------------------------------------------------

@app.get(
    "/",
    tags=["Application"],
    summary="Application Information"
)
def home():

    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "status": "Running"
    }


# --------------------------------------------------
# Health Endpoint
# --------------------------------------------------

@app.get(
    "/health",
    tags=["Application"],
    summary="Health Check"
)
def health():

    return {
        "status": "healthy",
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION
    }


# --------------------------------------------------
# Login Endpoint
# --------------------------------------------------

@app.post(
    "/login",
    response_model=TokenResponse,
    tags=["Authentication"],
    summary="User Login"
)
def login(request: LoginRequest):

    token = AuthService.login(
        request.username,
        request.password
    )

    if token is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    return token


# --------------------------------------------------
# Search Endpoint
# --------------------------------------------------

@router.post(
    "/search",
    response_model=SearchResponse,
    tags=["Knowledge"],
    summary="Search Enterprise Knowledge"
)
def search(
    request: QueryRequest,
    current_user: str = Depends(get_current_user)
):

    return KnowledgeService.search(
        request.query
    )


# --------------------------------------------------
# Analytics Endpoint
# --------------------------------------------------

@router.get(
    "/analytics",
    tags=["Analytics"],
    summary="Search Analytics"
)
def analytics(
    current_user: str = Depends(get_current_user)
):

    return AnalyticsService.get_statistics()
@router.get(
    "/history",
    tags=["Analytics"],
    summary="Search History"
)

@router.get(
    "/metrics",
    tags=["Analytics"],
    summary="Application Metrics"
)
def metrics(
    current_user: str = Depends(get_current_user)
):

    return MetricsService.get_metrics()
def history(
    current_user: str = Depends(get_current_user)
):

    return AnalyticsService.get_history()


# --------------------------------------------------
# Upload Knowledge Endpoint
# --------------------------------------------------

@router.post(
    "/upload",
    tags=["Knowledge"],
    summary="Upload Knowledge Document"
)
def upload_document(
    request: UploadRequest,
    current_user: str = Depends(get_current_user)
):

    return UploadService.upload_document(
        request.filename,
        request.content
    )


# --------------------------------------------------
# Register Router
# --------------------------------------------------

app.include_router(router)