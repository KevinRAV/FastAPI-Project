from sqlalchemy.orm import Session

from models.Product import ProductCreate
from models.User import UserCreate
from . import models
from models import *


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(name=user.name, email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def create_seller_product(db: Session, product: ProductCreate, user_id: int):
    db_item = models.Product(**product.dict(), seller_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
