from fastapi import HTTPException

from sql_app.crud import read
from sql_app import models
from models.user import User


def read_token(token: str, db):
    """
    This authtoken who passed in header, this function:

    Read the authtoken of user who is an email

    :param token: str

    :param db:

    :return: user

    """
    users = read(models.User, [["email", token]], db)
    if len(users) == 0:
        raise HTTPException(status_code=401, detail="Unauthorized : The auth_token is wrong !")
    else:
        db_user = users[0]
        user = User(
            id=db_user.id,
            email=db_user.email,
            name=db_user.name,
            is_admin=db_user.is_admin
        )
        return user
