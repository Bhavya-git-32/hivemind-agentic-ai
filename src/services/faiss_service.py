import faiss
import numpy as np

from src.services.embedding_service import EmbeddingService
from src.services.index_service import IndexService


class FaissService:
    """
    Creates and manages the FAISS vector index.
    """

    _index = None
    _documents = []

    @classmethod
    def build_index(cls):

        documents = IndexService.get_documents()

        cls._documents = documents

        if not documents:
            return

        embeddings = []

        for document in documents:

            text = f"{document['title']}\n{document['content']}"

            embedding = EmbeddingService.encode(text)

            embeddings.append(embedding)

        embeddings = np.array(
            embeddings,
            dtype="float32"
        )

        dimension = embeddings.shape[1]

        cls._index = faiss.IndexFlatL2(dimension)

        cls._index.add(embeddings)

        print(f"Indexed {len(documents)} documents.")

    @classmethod
    def search(cls, query, top_k=3):

        if cls._index is None:
            cls.build_index()

        query_embedding = EmbeddingService.encode(query)

        query_embedding = np.array(
            [query_embedding],
            dtype="float32"
        )

        distances, indices = cls._index.search(
            query_embedding,
            top_k
        )

        results = []

        for idx in indices[0]:

            if idx == -1:
                continue

            results.append(cls._documents[idx])

        return results