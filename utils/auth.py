from models.user import User


def read_token(token: str):
    email = token
    # TODO in db get user by email
    no_user_found = (len(token) == 0)
    if no_user_found:
        # TODO status code
        return
    else:
        return User(id=0, name="John Doe", email=email, is_admin=False)
