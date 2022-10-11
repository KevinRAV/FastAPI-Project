from fastapi import APIRouter

router = APIRouter()


@router.post("/auth/signup")
def auth_signup():
    auth_token = "a"
    return {"auth_token": auth_token}


@router.post("/auth/login")
def auth_login():
    auth_token = "a"
    return {"auth_token": auth_token}
