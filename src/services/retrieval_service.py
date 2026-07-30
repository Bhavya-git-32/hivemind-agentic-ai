from src.services.index_service import IndexService


class RetrievalService:
    """
    Retrieves the most relevant documents from the knowledge base
    using keyword-based relevance scoring.
    """

    @staticmethod
    def search(query: str, categories):
        """
        Search documents by query and category/categories.

        Args:
            query (str): User search query.
            categories (str | list): One category or multiple categories.

        Returns:
            list: Ranked matching documents.
        """

        documents = IndexService.get_documents()

        # Convert single category into a list
        if isinstance(categories, str):
            categories = [categories]

        query_words = set(query.lower().split())

        results = []

        for document in documents:

            # Skip unrelated categories
            if document["category"] not in categories:
                continue

            searchable_text = (
                document["title"] + " " + document["content"]
            ).lower()

            searchable_words = set(searchable_text.split())

            # Calculate relevance score
            score = len(query_words.intersection(searchable_words))

            # Bonus if the full query exists
            if query.lower() in searchable_text:
                score += 3

            # Bonus if query words appear in title
            title_words = set(document["title"].lower().split())
            score += len(query_words.intersection(title_words)) * 2

            if score > 0:
                results.append(
                    {
                        "score": score,
                        "document": document
                    }
                )

        # Highest score first
        results.sort(
            key=lambda item: (
                item["score"],
                len(item["document"]["content"])
            ),
            reverse=True
        )

        return results