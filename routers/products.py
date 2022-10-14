from fastapi import APIRouter, Header, Depends
from sqlalchemy.orm import Session

from sql_app.database import get_db
from utils.auth import read_token

router = APIRouter()


@router.get("/users/me")
def get_active_user(auth_token: str = Header(min_length=1, max_length=50), db: Session = Depends(get_db)):
    return read_token(auth_token, db)
