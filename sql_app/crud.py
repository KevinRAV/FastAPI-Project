from sqlalchemy.orm import Session

from models.product import ProductCreate
from models.user import UserCreate
from models.category import Category, CategoryCreate
from . import models
from models import *

import hashlib
import os

salt = os.urandom(32)


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> object:
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    password = hashlib.pbkdf2_hmac('sha256', user.password.encode('utf-8'), salt, 100000)
    db_user = models.User(name=user.name, email=user.email, hashed_password=str(password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: ProductCreate, user_id: int):
    db_item = models.Product(**product.dict(), seller_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_category(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()


def create_category(db: Session, category: CategoryCreate):
    db_category = models.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_category_name(db: Session, name: str) -> object:
    return db.query(models.Category).filter(models.Category.name == name).first()
