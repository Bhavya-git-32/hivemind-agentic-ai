from datetime import datetime


class AnalyticsService:

    _history = []

    @classmethod
    def record_search(cls, query: str, agents: list):

        cls._history.append(
            {
                "query": query,
                "agents": agents,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        )

    @classmethod
    def get_statistics(cls):

        total = len(cls._history)

        frequency = {}

        for item in cls._history:

            query = item["query"]

            frequency[query] = frequency.get(query, 0) + 1

        most_searched = None

        if frequency:

            most_searched = max(
                frequency,
                key=frequency.get
            )

        return {
            "total_searches": total,
            "most_searched": most_searched
        }

    @classmethod
    def get_history(cls):

        return {
            "total_searches": len(cls._history),
            "history": cls._history
        }