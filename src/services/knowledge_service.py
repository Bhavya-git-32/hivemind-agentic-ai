from src.agents.coordinator_agent import CoordinatorAgent
from src.exceptions import HiveMindException
from src.services.response_service import ResponseService
from src.utils.logger import logger


class KnowledgeService:

    coordinator = CoordinatorAgent()

    @classmethod
    def search(cls, query: str):

        try:

            logger.info(f"Knowledge search started: {query}")

            results = cls.coordinator.process_query(query)

            return ResponseService.generate(
                query,
                results["results"]
            )

        except HiveMindException as ex:

            logger.error(str(ex))

            return {
                "status": "error",
                "message": str(ex)
            }

        except Exception as ex:

            logger.exception(ex)

            return {
                "status": "error",
                "message": "Unexpected server error."
            }