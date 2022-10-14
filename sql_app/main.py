from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from models.cart import Cart, CartCreate
from models.category import Category, CategoryCreate
from models.command import Command, CommandCreate
from models.comment import Comment, CommentCreate
from models.product import Product, ProductCreate
from models.user import User, UserCreate
from . import crud, models
from .database import get_db
from .database import SessionLocal, engine

app = FastAPI()


# post un nouveau user

@app.post("/users", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


# get tous les users sous forme de liste

@app.get("/users", response_model=list[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


# @app.post("/{user_id}/products/", response_model=Product)
# def create_product(product: ProductCreate, user_id: User, db: Session = Depends(get_db)):
#    db_product = crud.get_products(db, skip=0, limit=100)
#    if db_product:
#        raise HTTPException(status_code=400, detail="Product already registered")
#    return crud.create_product(db=db, product=product, user_id=User.id)

# get la liste de tous les produits

@app.post("/categories", response_model=Category)
def create_categories(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = crud.get_category_name(db, name=category.name)
    if db_category:
        raise HTTPException(status_code=400, detail="Category already registered")
    return crud.create(models.User(**category.dict()))


@app.get("/categories", response_model=list[Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = crud.get_category(db, skip=skip, limit=limit)
    return categories


@app.get("/categories/{categorie_id}")
def read_categories_id(categorie_id: int, db: Session = Depends(get_db)):
    category = crud.get_category_by_id(db, categorie_id)
    if category:
        return category
    else:
        raise HTTPException(status_code=400, detail=f"No Category with id {categorie_id}")


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


@app.post("/carts/", response_model=Cart)
def create_user_cart(
        owner_id: int, product_id: int, cart: CartCreate, db: Session = Depends(get_db)):
    return crud.create_cart(db=db, cart=cart, owner_id=owner_id, product_id=product_id)


@app.get("/carts/", response_model=list[Cart])
def read_cart(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    carts = crud.get_carts(db, skip=skip, limit=limit)
    return carts


@app.delete("/carts/{product_id}")
def delete_cart_by_id(product_id: int, db: Session = Depends(get_db)):
    return crud.delete_cart_by_id(db, product_id)


@app.patch("/carts/{product_id}")
def update_cart(product_id: int, cart: Cart, db: Session = Depends(get_db)):
    return crud.update_cart(db, product_id, cart)


@app.post("/commands/", response_model=Command)
def create_user_command(
        buyer_id: int, command: CommandCreate, db: Session = Depends(get_db)):
    return crud.create_command(db=db, command=command, buyer_id=buyer_id)
