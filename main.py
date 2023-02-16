from routers import auths
from routers import products
from routers import categories
from routers import carts
from routers import commands
from routers import users
from sql_app import crud

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from models.cart import Cart, CartCreate
from models.category import Category, CategoryCreate
from models.command import Command, CommandCreate
from models.comment import Comment, CommentCreate
from models.product import Product, ProductCreate
from models.user import User, UserCreate
from sql_app.database import get_db

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.delete("/categories/{id}", response_model=Category)
def delete_category_product(id: int, db: Session = Depends(get_db)):
    return crud.delete_category(db, id)


# Products

@app.post("/products/{seller_id}", response_model=Product)
def create_seller_product(
        seller_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product, seller_id=seller_id)


@app.get("/products/", response_model=list[Product])
def read_product(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products


@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    return crud.delete_product(db, id)


@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    return crud.update_product(db, id, product)


# Comment

@app.post("/comment/{user_id}/{product_id}", response_model=Comment)
def create_comment_for_user(
        user_id: int, product_id: int, comment: CommentCreate, db: Session = Depends(get_db)):
    return crud.create_comment(db, comment, user_id, product_id)


@app.get("/comments", response_model=list[Comment])
def read_comments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    comments = crud.get_comments(db, skip=skip, limit=limit)
    return comments


@app.delete("/comment/{user_id}/{product_id}", response_model=Comment)
def delete_comment_for_user(user_id: int, product_id: int, db: Session = Depends(get_db)):
    return crud.delete_comment(db, user_id, product_id)


@app.put("/comment/{user_id}/{product_id}")
def update_comment_for_user(user_id: int, product_id: int, comment: Comment, db: Session = Depends(get_db)):
    return crud.update_comment(db, user_id, product_id, comment)


@app.delete("/carts/{product_id}")
def delete_cart_by_id(product_id: int, db: Session = Depends(get_db)):
    return crud.delete_cart_by_id(db, product_id)


@app.patch("/carts/{product_id}")
def update_cart(product_id: int, cart: Cart, db: Session = Depends(get_db)):
    return crud.update_cart(db, product_id, cart)


app.include_router(auths.router)
app.include_router(products.router)
app.include_router(categories.router)
app.include_router(carts.router)
app.include_router(commands.router)
app.include_router(users.router)
