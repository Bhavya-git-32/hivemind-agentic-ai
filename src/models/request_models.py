from pydantic import BaseModel


class QueryRequest(BaseModel):
    query: str


class UploadRequest(BaseModel):
    filename: str
    content: str