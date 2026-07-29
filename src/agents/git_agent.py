from src.services.retrieval_service import RetrievalService


class GitAgent:

    def search(self, query: str):

        matches = RetrievalService.search(
            query,
            [
                "claims_pipeline"
            ]
        )

        return {
            "agent": "Git Agent",
            "matches": matches
        }