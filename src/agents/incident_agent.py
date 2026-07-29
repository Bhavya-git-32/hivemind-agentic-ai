from src.services.retrieval_service import RetrievalService


class IncidentAgent:
    """
    Searches production incidents, root cause analysis (RCA),
    and troubleshooting documentation.
    """

    def search(self, query: str):

        matches = RetrievalService.search(
            query,
            [
                "incident_rca"
            ]
        )

        return {
            "agent": "Incident Agent",
            "matches": matches
        }