from typing import Annotated
from fastapi import APIRouter, Depends

from app.dependencies import validate_email_and_password


router = APIRouter(
    prefix="/items",
    tags=["items"],
)


@router.get("/")
async def read_items(user: Annotated[dict, Depends(validate_email_and_password)]):
    email = user.get("email")
    password = user.get("password")

    if email != ValueError or password != ValueError:
        return {"email": email, "password": password}
