from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCredentials(UserBase):
    password: str


class UserCreate(UserCredentials):
    name: str
    is_admin: bool = False


class User(UserBase):
    id: int
    name: str
    is_admin: bool

    class Config:
        orm_mode = True
