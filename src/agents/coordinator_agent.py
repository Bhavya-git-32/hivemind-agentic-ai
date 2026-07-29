from src.agents.documentation_agent import DocumentationAgent
from src.agents.git_agent import GitAgent
from src.agents.incident_agent import IncidentAgent
from src.agents.employee_twin_agent import EmployeeTwinAgent


class CoordinatorAgent:
    """
    Coordinator Agent

    Responsible for:
    - Receiving user queries
    - Determining which specialized agents should handle the request
    - Collecting responses
    - Returning a consolidated result
    """

    def __init__(self):
        self.documentation_agent = DocumentationAgent()
        self.git_agent = GitAgent()
        self.incident_agent = IncidentAgent()
        self.employee_twin_agent = EmployeeTwinAgent()

    def process_query(self, query: str):
        query_lower = query.lower()
        responses = []

        # Documentation related queries
        if (
            "document" in query_lower
            or "documentation" in query_lower
            or "architecture" in query_lower
            or "design" in query_lower
        ):
            responses.append(
                self.documentation_agent.search(query)
            )

        # Source code related queries
        if (
            "code" in query_lower
            or "api" in query_lower
            or "repository" in query_lower
            or "git" in query_lower
            or "implementation" in query_lower
        ):
            responses.append(
                self.git_agent.search(query)
            )

        # Incident related queries
        if (
            "incident" in query_lower
            or "error" in query_lower
            or "failure" in query_lower
            or "bug" in query_lower
            or "issue" in query_lower
        ):
            responses.append(
                self.incident_agent.search(query)
            )

        # Employee expertise related queries
        if (
            "expert" in query_lower
            or "owner" in query_lower
            or "sme" in query_lower
            or "engineer" in query_lower
            or "developer" in query_lower
        ):
            responses.append(
                self.employee_twin_agent.search(query)
            )

        # Default fallback
        if not responses:
            responses.append(
                self.documentation_agent.search(query)
            )

        return {
            "query": query,
            "agents_consulted": len(responses),
            "results": responses
        }