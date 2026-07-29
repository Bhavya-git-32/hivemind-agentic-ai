from pathlib import Path


class DocumentLoader:

    KNOWLEDGE_PATH = Path("knowledge")

    @staticmethod
    def load_documents():

        documents = []

        print(f"Looking for knowledge in: {DocumentLoader.KNOWLEDGE_PATH.resolve()}")

        if not DocumentLoader.KNOWLEDGE_PATH.exists():
            print("Knowledge folder NOT found!")
            return documents

        files = list(DocumentLoader.KNOWLEDGE_PATH.glob("*.md"))
        print(f"Found {len(files)} markdown files")

        for file in files:
            print(f"Loading: {file.name}")

            content = file.read_text(encoding="utf-8")

            documents.append(
                {
                    "title": file.stem.replace("_", " ").title(),
                    "category": file.stem,
                    "content": content,
                }
            )

        return documents