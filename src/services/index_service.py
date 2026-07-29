from src.services.document_loader import DocumentLoader
from src.utils.logger import logger


class IndexService:
    """
    Loads and caches enterprise knowledge documents.
    """

    _documents = None

    @classmethod
    def get_documents(cls):
        """
        Load documents into memory only once.
        """

        if cls._documents is None:

            logger.info("Loading enterprise knowledge base...")

            cls._documents = DocumentLoader.load_documents()

            logger.info(
                f"Successfully loaded {len(cls._documents)} knowledge documents."
            )

        return cls._documents

    @classmethod
    def refresh(cls):
        """
        Reload all knowledge documents.
        """

        logger.info("Refreshing enterprise knowledge base...")

        cls._documents = DocumentLoader.load_documents()

        logger.info(
            f"Knowledge base refreshed successfully. Loaded {len(cls._documents)} documents."
        )

        return cls._documents