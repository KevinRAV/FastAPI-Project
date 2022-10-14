from sql_app.crud import read
from sql_app import models
from models.user import User


def read_token(token: str, db):
    # TODO in db get user by email
    users = read(models.User, [["email", token]], db)
    if len(users) == 0:
        # TODO status code
        return
    else:
        db_user = users[0]
        user = User(
            id=db_user.id,
            email=db_user.email,
            name=db_user.name,
            is_admin=db_user.is_admin
        )
        return user
