from pydantic import BaseModel


class CartBase(BaseModel):
    quantity: int


class CartCreate(CartBase):
    product_id: int


class CartDelete(CartBase):
    pass


class CartUpdate(CartBase):
    pass


class Cart(CartBase):
    owner_id: int
    product_id: int

    class Config:
        orm_mode = True
