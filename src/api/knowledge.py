from src.agents.coordinator_agent import CoordinatorAgent
from src.services.response_service import ResponseService
from src.utils.logger import logger


class KnowledgeService:

    coordinator = CoordinatorAgent()

    @classmethod
    def search(cls, query: str):

        logger.info(f"Searching knowledge for: {query}")

        results = cls.coordinator.process_query(query)

        return ResponseService.generate(
            query,
            results["results"]
        )