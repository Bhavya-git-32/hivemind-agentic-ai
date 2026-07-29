from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    APP_NAME = os.getenv(
        "APP_NAME",
        "HiveMind AI"
    )

    APP_VERSION = os.getenv(
        "APP_VERSION",
        "1.0.0"
    )

    APP_DESCRIPTION = os.getenv(
        "APP_DESCRIPTION",
        "Enterprise Agentic AI Knowledge Platform"
    )

    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )

    API_PREFIX = os.getenv(
        "API_PREFIX",
        "/api"
    )

    ENVIRONMENT = os.getenv(
        "ENVIRONMENT",
        "development"
    )


settings = Settings()