from fastapi import APIRouter

from project_api.api.api_v1.endpoints import hello_world

api_router = APIRouter()
api_router.include_router(hello_world.router, prefix="/hello-world", tags=["hello-world"])
