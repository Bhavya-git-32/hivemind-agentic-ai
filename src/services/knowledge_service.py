from src.agents.coordinator_agent import CoordinatorAgent
from src.services.response_service import ResponseService

coordinator = CoordinatorAgent()


def search_knowledge(query: str):

    results = coordinator.process_query(query)

    return ResponseService.generate(
        query,
        results["results"]
    )