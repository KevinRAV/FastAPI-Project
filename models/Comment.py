from pydantic import BaseModel


class CommentBase(BaseModel):
    stars: int | None = None
    message: str | None = None


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
