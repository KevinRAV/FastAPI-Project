from pydantic import BaseModel
from datetime import datetime


class CommandBase(BaseModel):
    product_name: str
    quantity: int
    unit_price: float
    buyer_id: int
    seller_id: int
    timestamp: datetime = datetime.utcnow()


class CommandCreate(CommandBase):
    pass


class CommandDelete(CommandBase):
    pass


class Command(CommandBase):
    id: int

    class Config:
        orm_mode = True
