from pydantic import BaseModel


class SearchResponse(BaseModel):
    """
    Search response model.
    """

    query: str
    summary: str