from fastapi import APIRouter, Header, Depends, HTTPException
from sqlalchemy.orm import Session

from models.command import Command, CommandCreate
from sql_app import crud, models
from sql_app.database import get_db
from utils.auth import read_token
from typing import List

router = APIRouter()


@router.get("/commands", response_model=List[Command])
def get_my_buys(auth_token: str = Header(min_length=1, max_length=50), db: Session = Depends(get_db)):
    user = read_token(auth_token, db)
    return crud.read(models.Commands, [["buyer_id", user.id]], db)


@router.get("/commands/{user_id}", response_model=List[Command])
def get_my_sells(user_id, auth_token: str = Header(min_length=1, max_length=50), db: Session = Depends(get_db)):
    user = read_token(auth_token, db)
    if user.id == user_id or user.is_admin:
        return crud.read(models.Commands, [["buyer_id", user.id]], db)
    else:
        raise HTTPException(status_code=401, detail="User_id in url does not match account from token sent")


@router.post("/commands", response_model=List[Command])
def order_my_cart(auth_token: str = Header(min_length=1, max_length=50), db: Session = Depends(get_db)):
    commands = []
    user = read_token(auth_token, db)
    carts = crud.read(models.Cart, [["owner_id", user.id]], db)
    for cart in carts:
        product = crud.read(models.Product, [["id", cart.product_id]], db)[0]
        command = CommandCreate(product_name=product.name,
                                quantity=cart.quantity,
                                unit_price=product.price,
                                buyer_id=user.id,
                                seller_id=product.seller_id
                                )
        row = models.Commands(**command.dict())
        # TODO supprimer cart
        commands.append(crud.create(row, db))
    return commands
