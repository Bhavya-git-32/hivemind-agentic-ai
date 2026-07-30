class QueryAnalyzer:
    """
    Determines which agents should handle a query.
    """

    @staticmethod
    def analyze(query: str):

        query = query.lower()

        selected_agents = set()

        documentation_keywords = [
            "architecture",
            "design",
            "documentation",
            "document",
            "flow",
            "overview",
            "explain",
            "xml",
            "validation"
        ]

        git_keywords = [
            "api",
            "code",
            "repository",
            "implementation",
            "class",
            "method",
            "function",
            "python",
            "lambda"
        ]

        incident_keywords = [
            "incident",
            "error",
            "failure",
            "bug",
            "issue",
            "timeout",
            "exception",
            "root cause"
        ]

        employee_keywords = [
            "owner",
            "expert",
            "developer",
            "engineer",
            "sme",
            "who"
        ]

        for word in documentation_keywords:
            if word in query:
                selected_agents.add("documentation")

        for word in git_keywords:
            if word in query:
                selected_agents.add("git")

        for word in incident_keywords:
            if word in query:
                selected_agents.add("incident")

        for word in employee_keywords:
            if word in query:
                selected_agents.add("employee")

        if len(selected_agents) == 0:
            selected_agents.add("documentation")

        return list(selected_agents)