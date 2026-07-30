from pathlib import Path

from src.services.index_service import IndexService


class UploadService:

    KNOWLEDGE_PATH = Path("knowledge_base")

    @classmethod
    def upload_document(cls, filename: str, content: str):

        cls.KNOWLEDGE_PATH.mkdir(exist_ok=True)

        file_path = cls.KNOWLEDGE_PATH / filename

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

        # Refresh the knowledge index
        IndexService.refresh()

        return {
            "message": "Document uploaded successfully.",
            "filename": filename
        }