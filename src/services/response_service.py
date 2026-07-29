class ResponseService:

    @staticmethod
    def generate(query: str, agent_results: list):

        answer = f"Query: {query}\n\n"

        for result in agent_results:

            answer += f"{result['agent']}:\n"

            matches = result.get("matches", [])

            if not matches:
                answer += "No relevant information found.\n\n"
                continue

            for item in matches:

                document = item["document"]

                answer += (
                    f"- {document['title']}: "
                    f"{document['content']}\n"
                )

            answer += "\n"

        return {
            "query": query,
            "summary": answer
        }