from sqlalchemy.orm import Session

from models.product import ProductCreate
from models.user import UserCreate
from models.category import CategoryCreate
from . import models

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


def create_product(db: Session, product: ProductCreate, seller_id: int):
    db_product = models.Product(
        name=product.name,
        price=product.price,
        description=product.description,
        image=product.image,
        stock=product.stock,
        category_id=product.category_id,
        seller_id=seller_id
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


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


def get_category_by_id(db: Session, id: int) -> object:
    return db.query(models.Category).filter(models.Category.id == id).first()


