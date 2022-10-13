from __future__ import annotations

from pydantic import BaseModel

from models.category import Category


class ProductBase(BaseModel):
    name: str
    price: float
    description: str
    image: str
    stock: int


class ProductCreate(ProductBase):
    pass


class ProductDelete(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    seller_id: int
    categories: Category

    class Config:
        orm_mode = True
