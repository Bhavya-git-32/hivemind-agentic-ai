from src.services.retrieval_service import RetrievalService


class DocumentationAgent:

    def search(self, query: str):

        matches = RetrievalService.search(
            query,
            [
                "api_architecture",
                "claims_pipeline",
                "deployment"
            ]
        )

        return {
            "agent": "Documentation Agent",
            "matches": matches
        }