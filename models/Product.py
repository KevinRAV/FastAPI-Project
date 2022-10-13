from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    price: float
    description: str | None = None
    image: str | None = None
    stock: int


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    seller_id: int
    categories: Category

    class Config:
        orm_mode = True
