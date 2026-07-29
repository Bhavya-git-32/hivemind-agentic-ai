from src.services.retrieval_service import RetrievalService


class DocumentationAgent:

    def search(self, query: str):

        matches = RetrievalService.search(
            query,
            "documentation"
        )

        return {
            "agent": "Documentation Agent",
            "matches": matches
        }