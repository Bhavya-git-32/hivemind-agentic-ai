from src.agents.documentation_agent import DocumentationAgent
from src.agents.git_agent import GitAgent
from src.agents.incident_agent import IncidentAgent
from src.agents.employee_twin_agent import EmployeeTwinAgent

from src.services.query_analyzer import QueryAnalyzer


class CoordinatorAgent:
    """
    Coordinator Agent

    Responsibilities:
    - Receive user query
    - Determine which agents should handle it
    - Collect responses
    - Return consolidated results
    """

    def __init__(self):

        self.documentation_agent = DocumentationAgent()
        self.git_agent = GitAgent()
        self.incident_agent = IncidentAgent()
        self.employee_twin_agent = EmployeeTwinAgent()

    def process_query(self, query: str):

        selected_agents = QueryAnalyzer.analyze(query)

        responses = []

        if "documentation" in selected_agents:
            responses.append(
                self.documentation_agent.search(query)
            )

        if "git" in selected_agents:
            responses.append(
                self.git_agent.search(query)
            )

        if "incident" in selected_agents:
            responses.append(
                self.incident_agent.search(query)
            )

        if "employee" in selected_agents:
            responses.append(
                self.employee_twin_agent.search(query)
            )

        return {
            "query": query,
            "agents_consulted": len(responses),
            "selected_agents": selected_agents,
            "results": responses
        }