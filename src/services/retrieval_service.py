from src.services.index_service import IndexService
from src.utils.logger import logger


class RetrievalService:
    """
    Retrieves the most relevant documents from the knowledge base
    using keyword matching and document scoring.
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

        logger.info(f"Starting search for query: '{query}'")

        # Load indexed documents
        documents = IndexService.get_documents()

        logger.info(f"Knowledge base contains {len(documents)} documents.")

        # Convert single category to list
        if isinstance(categories, str):
            categories = [categories]

        logger.info(f"Searching categories: {categories}")

        query_words = query.lower().split()

        results = []

        for document in documents:

            # Skip unrelated categories
            if document["category"] not in categories:
                continue

            searchable_text = (
                document["title"] + " " + document["content"]
            ).lower()

            score = 0

            # Keyword matching
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

        # Highest score first
        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        logger.info(f"Retrieved {len(results)} matching documents.")

        return results