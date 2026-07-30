from datetime import datetime

from src.config import settings
from src.services.analytics_service import AnalyticsService
from src.services.index_service import IndexService


class MetricsService:
    """
    Provides application metrics.
    """

    started_at = datetime.now()

    @classmethod
    def get_metrics(cls):

        uptime = datetime.now() - cls.started_at

        documents = IndexService.get_documents()

        analytics = AnalyticsService.get_statistics()

        return {
            "application": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "environment": settings.ENVIRONMENT,
            "status": "Running",
            "uptime": str(uptime).split(".")[0],
            "documents_loaded": len(documents),
            "total_searches": analytics["total_searches"],
            "registered_agents": [
                "Coordinator Agent",
                "Documentation Agent",
                "Git Agent",
                "Incident Agent",
                "Employee Twin Agent"
            ]
        }