from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.user import UserCredentials
from models.user import UserCreate
from sql_app import crud, models
from sql_app.database import get_db

router = APIRouter()


@router.post("/auths/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user using data sent in request body and returns an auth token for this user

    :param user: new user infos
    :param db: optional, where to store the account
    :return: auth_token: str
    """
    db_user = crud.read(models.User, [["email", user.email]], db)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    row = models.User(name=user.name, email=user.email, hashed_password=user.password)
    account = crud.create(row, db)
    auth_token = account.email
    return {"auth_token": auth_token}


@router.post("/auths/login")
def login(credentials: UserCredentials, db: Session = Depends(get_db)):
    db_account = crud.read(models.User, [["email", credentials.email], ["hashed_password", credentials.password]], db)
    if len(db_account):
        auth_token = db_account[0].email
        return {"auth_token": auth_token}
    else:
        # TODO status code
        return
