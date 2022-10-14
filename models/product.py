from __future__ import annotations

from pydantic import BaseModel

from models.category import Category


class ProductBase(BaseModel):
    name: str
    price: float
    description: str = ""
    image: str = "https://cdn-icons-png.flaticon.com/512/8043/8043427.png"
    stock: int
    category_id: int


class ProductCreate(ProductBase):
    pass


class ProductDelete(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    seller_id: int

    class Config:
        orm_mode = True
