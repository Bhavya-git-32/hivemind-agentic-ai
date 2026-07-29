from src.services.document_loader import DocumentLoader


class RetrievalService:
    """
    Retrieves the most relevant documents from the knowledge base
    using simple keyword matching and scoring.
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

        # Load all markdown documents
        documents = DocumentLoader.load_documents()

        # Convert a single category to a list
        if isinstance(categories, str):
            categories = [categories]

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

            # Simple keyword matching
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

        # Sort by highest score first
        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return results