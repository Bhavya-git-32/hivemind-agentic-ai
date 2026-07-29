KNOWLEDGE_BASE = [
    {
        "title": "Claims API Architecture",
        "category": "documentation",
        "content": (
            "The Claims API is built using FastAPI and AWS Lambda. "
            "It receives XML claim files from Amazon S3, validates the "
            "input, transforms the data, and stores the processed records "
            "in Amazon Redshift."
        )
    },
    {
        "title": "Claims API Source Code",
        "category": "git",
        "content": (
            "The implementation uses Python, FastAPI, AWS Lambda, "
            "API Gateway, and reusable service classes."
        )
    },
    {
        "title": "Production Incident RCA",
        "category": "incident",
        "content": (
            "A production issue occurred due to an invalid XML schema. "
            "The validation layer was updated to reject malformed XML "
            "before processing."
        )
    },
    {
        "title": "Claims Domain Expert",
        "category": "employee",
        "content": (
            "The Claims platform is primarily maintained by the Claims "
            "Engineering Team. Complex business-rule questions should be "
            "reviewed with the designated domain experts."
        )
    }
]