from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from uvicorn import run

from project_api.api.api_v1.api import api_router
from project_api.core.config import settings
from project_api.core.logging import configure_logging

configure_logging()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description=settings.PROJECT_DESCRIPTION,
    root_path=settings.API_ROOT_PATH,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.API_CORS_ALLOWED_ORIGINS,
    allow_credentials=settings.API_CORS_ALLOWED_CREDENTIALS,
    allow_methods=settings.API_CORS_ALLOWED_METHODS,
    allow_headers=settings.API_CORS_ALLOWED_HEADERS,
    expose_headers=settings.API_CORS_EXPOSED_HEADERS,
)

app.include_router(api_router, prefix=settings.API_V1_PREFIX)

if __name__ == "__main__":
    run(
        "main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        workers=settings.API_WORKERS,
        reload=settings.API_RELOAD,
    )
