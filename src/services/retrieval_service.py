from src.knowledge.documents import KNOWLEDGE_BASE


class RetrievalService:

    @staticmethod
    def search(query: str, category: str):
        query_words = query.lower().split()

        results = []

        for document in KNOWLEDGE_BASE:

            if document["category"] != category:
                continue

            searchable_text = (
                document["title"] + " " + document["content"]
            ).lower()

            score = 0

            for word in query_words:
                if word in searchable_text:
                    score += 1

            if score > 0:
                results.append(
                    {
                        "score": score,
                        "document": document
                    }
                )

        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return results