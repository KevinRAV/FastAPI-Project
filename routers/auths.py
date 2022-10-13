from fastapi import APIRouter

from models.user import UserCredentials
from models.user import UserCreate

router = APIRouter()


@router.post("/auths/signup")
def signup(account: UserCreate):
    """
    Create a new user using data sent in request body and returns an auth token for this user
    :param account: new user infos
    :return: auth_token: str
    """
    # TODO in db add account
    auth_token = account.email
    return {"auth_token": auth_token}


@router.post("/auths/login")
def login(credentials: UserCredentials):
    # TODO in db get account
    db_account = credentials
    if db_account.password == credentials.password:
        auth_token = db_account.email
        return {"auth_token": auth_token}
    else:
        # TODO status code
        return
