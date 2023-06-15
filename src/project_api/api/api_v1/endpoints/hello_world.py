from fastapi import APIRouter
from starlette.status import HTTP_200_OK

router = APIRouter()


@router.get(
    "/",
    status_code=HTTP_200_OK,
    description="Hello World.",
    response_model=dict[str, str],
)
def hello_world() -> dict[str, str]:
    """Say you : Hello world.

    Returns:
        A Json which say you : Hello World.
    """
    return {"message": "Hello World."}
