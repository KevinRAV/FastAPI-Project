from __future__ import annotations

from pydantic import BaseModel


class CommentBase(BaseModel):
    stars: int
    message: str


class CommentCreate(CommentBase):
    pass


class CommentDelete(CommentBase):
    pass


class CommentUpdate(CommentBase):
    pass


class Comment(CommentBase):
    author_id: int
    product_id: int

    class Config:
        orm_mode = True
