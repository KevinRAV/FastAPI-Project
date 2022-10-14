from fastapi import APIRouter, Header

from utils.auth import read_token

router = APIRouter()


@router.get("/users/me")
def get_active_user(auth_token: str = Header(min_length=1, max_length=50)):
    return read_token(auth_token)


@router.get("/commands")
def get_active_user(auth_token: str = Header(min_length=1, max_length=50)):
    # TODO in db
    return read_token(auth_token)
