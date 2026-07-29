from src.services.retrieval_service import RetrievalService


class IncidentAgent:

    def search(self, query: str):

        matches = RetrievalService.search(
            query,
            "incident"
        )

        return {
            "agent": "Incident Agent",
            "matches": matches
        }