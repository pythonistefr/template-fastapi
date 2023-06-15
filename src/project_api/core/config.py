import os
from pathlib import Path

import pydantic

from project_api.enums.logging import LogLevel

ENVIRONMENT_VARIABLES_PREFIX = "PROJECT_API_"
SECRET_ENVIRONMENT_VARIABLES_PREFIX = f"{ENVIRONMENT_VARIABLES_PREFIX}SECRET_"


def get_home_dir() -> Path:
    return Path(os.path.join(os.path.dirname(os.path.abspath(__file__)))).parent.parent.parent


class SecretSettings(pydantic.BaseSettings):
    """Pydantic settings class used specifically for secrets."""

    PGSQL_DSN: pydantic.PostgresDsn = pydantic.Field(
        default=pydantic.parse_obj_as(
            pydantic.PostgresDsn,
            "postgresql+psycopg2://project-api:project-api@localhost:5432/project-api",
        ),
        description="PostgreSQL database Data Source Name",
    )

    class Config:
        env_prefix = SECRET_ENVIRONMENT_VARIABLES_PREFIX


class Settings(pydantic.BaseSettings):
    PROJECT_NAME: str = "Project API"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = "🔥🔥 My lovely API ! 🔥🔥"

    #####
    # API
    #####
    API_HOST: str = "localhost"
    API_PORT: int = 8000

    API_ROOT_PATH: str = "/"
    API_V1_PREFIX: str = "/api/v1"
    API_MAX_RESULTS_PER_PAGE: int = pydantic.Field(
        100, description="Maximum number of results per page when listing API resources"
    )

    API_CORS_ALLOWED_ORIGINS: list[str] = [
        # API dev server
        "http://localhost:8000",
    ]
    API_CORS_ALLOWED_HEADERS: list[str] = ["*"]
    API_CORS_ALLOWED_METHODS: list[str] = ["GET", "POST", "PATCH", "DELETE", "OPTIONS"]
    API_CORS_ALLOWED_CREDENTIALS: bool = False
    API_CORS_EXPOSED_HEADERS: list[str] = ["Content-Range"]

    API_WORKERS: int = 1
    API_RELOAD: bool = True

    ####################
    # Logging
    ####################
    LOGGING_LEVEL: LogLevel = LogLevel.INFO

    ####################
    # Filesystem context
    ####################
    HOME_PATH: Path = get_home_dir()

    ####################
    # secrets
    ####################
    secrets = SecretSettings()

    class Config:
        env_prefix = ENVIRONMENT_VARIABLES_PREFIX


settings = Settings()
