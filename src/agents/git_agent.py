from src.services.retrieval_service import RetrievalService


class GitAgent:

    def search(self, query: str):

        matches = RetrievalService.search(
            query,
            "git"
        )

        return {
            "agent": "Git Agent",
            "matches": matches
        }