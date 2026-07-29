from src.services.retrieval_service import RetrievalService


class EmployeeTwinAgent:

    def search(self, query: str):

        matches = RetrievalService.search(
            query,
            [
                "employee_expertise"
            ]
        )

        return {
            "agent": "Employee Twin Agent",
            "matches": matches
        }