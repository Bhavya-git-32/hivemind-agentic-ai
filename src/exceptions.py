class HiveMindException(Exception):
    """
    Base exception for HiveMind.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class KnowledgeBaseException(HiveMindException):
    """
    Raised when the knowledge base cannot be loaded.
    """
    pass


class RetrievalException(HiveMindException):
    """
    Raised when retrieval fails.
    """
    pass


class ValidationException(HiveMindException):
    """
    Raised when validation fails.
    """
    pass