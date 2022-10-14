from fastapi import APIRouter, Header, Depends, HTTPException
from sqlalchemy.orm import Session

from sql_app.database import get_db
from models.cart import CartCreate, Cart
from utils.auth import read_token
from sql_app import crud, models

router = APIRouter()


@router.get("/carts", response_model=list[Cart])
def get_my_carts(auth_token: str = Header(min_length=1, max_length=50), db: Session = Depends(get_db)):
    user = read_token(auth_token, db)
    return crud.read(models.Cart, [["owner_id", user.id]], db)


@router.post("/carts", response_model=Cart)
def new_cart(
        cart: CartCreate,
        auth_token: str = Header(min_length=1, max_length=50),
        db: Session = Depends(get_db)
):
    user = read_token(auth_token, db)
    if len(crud.read(models.Cart, [["owner_id", user.id], ["product_id", cart.product_id]], db)) > 0:
        raise HTTPException(status_code=400, detail="Already in cart")
    row = models.Cart(owner_id=user.id, product_id=cart.product_id, quantity=cart.quantity)
    return crud.create(row, db)
