from pydantic import BaseModel
from pydantic.types import date


class CommandBase(BaseModel):
    product_name: str
    quantity: int
    timestamp: date
    unit_price: float


class CommandCreate(CommandBase):
    pass


class CommandDelete(CommandBase):
    pass


class Command(CommandBase):
    id: int
    buyer_id: int
    seller_id: int

    class Config:
        orm_mode = True
