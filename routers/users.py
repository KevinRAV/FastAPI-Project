from fastapi import APIRouter, Header

from utils.auth import read_token

router = APIRouter()


@router.get("/users/me")
def get_active_user(auth_token: str = Header()):
    return read_token(auth_token)
