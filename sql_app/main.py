from fastapi import Depends, FastAPI, HTTPException, Path, Query
from sqlalchemy.orm import Session
from typing import Union

from models.cart import Cart
from models.user import User, UserCreate
from models.product import Product, ProductCreate
from models.category import Category, CategoryCreate
from . import crud
from . import models

from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# post un nouveau user

@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


# get tous les users sous forme de liste

@app.get("/users/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


# @app.post(f"/{User.id}/products/", response_model=Product)
# def create_product(product: ProductCreate, user_id: User, db: Session = Depends(get_db)):
#    db_product = crud.get_products(db, skip=0, limit=100)
#    if db_product:
#        raise HTTPException(status_code=400, detail="Product already registered")
#   return crud.create_product(db=db, product=product, user_id=User.id)

# get la liste de tous les produits

@app.post("/categories/", response_model=Category)
def create_categories(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = crud.get_category_name(db, name=category.name)
    if db_category:
        raise HTTPException(status_code=400, detail="Category already registered")
    return crud.create_category(db=db, category=category)


@app.get("/categories/", response_model=list[Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = crud.get_category(db, skip=skip, limit=limit)
    return categories
