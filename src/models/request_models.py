from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    """
    User search request model.
    """

    query: str = Field(
        ...,
        min_length=3,
        max_length=500,
        description="Natural language search query.",
        examples=["Explain the Claims API architecture"]
    )