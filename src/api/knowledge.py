from fastapi import APIRouter

from src.models.schemas import SearchRequest
from src.services.knowledge_service import search_knowledge

router = APIRouter(prefix="/knowledge", tags=["Knowledge"])


@router.post("/search")
def search(request: SearchRequest):
    return search_knowledge(request.query)