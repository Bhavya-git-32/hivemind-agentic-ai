from pathlib import Path

from src.exceptions import KnowledgeBaseException


class DocumentLoader:

    KNOWLEDGE_PATH = Path("knowledge")

    @classmethod
    def load_documents(cls):

        if not cls.KNOWLEDGE_PATH.exists():
            raise KnowledgeBaseException(
                "Knowledge directory not found."
            )

        documents = []

        for file in cls.KNOWLEDGE_PATH.glob("*.md"):

            category = file.stem

            with open(file, "r", encoding="utf-8") as f:

                content = f.read()

            documents.append(
                {
                    "title": file.stem.replace("_", " ").title(),
                    "category": category,
                    "content": content,
                }
            )

        return documents