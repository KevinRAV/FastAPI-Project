from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=True)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float, index=True)
    description = Column(String)
    stock = Column(Integer, index=True)
    image = Column(String, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    seller_id = Column(Integer, ForeignKey("users.id"))



class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


class Cart(Base):
    __tablename__ = "carts"

    owner_id = Column(Integer, ForeignKey("users.id"), primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True, index=True)
    quantity = Column(Integer)

    owner = Column(Integer, ForeignKey("users.id"))
    product = Column(Integer, ForeignKey("products.id"))


class Comment(Base):
    __tablename__ = "comments"

    author_id = Column(Integer, ForeignKey("users.id"), primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True, index=True)
    stars = Column(Integer)
    message = Column(String)

    author = Column(Integer, ForeignKey("products.id"))
    product = Column(Integer, ForeignKey("users.id"))


class Commands(Base):
    __tablename__ = "commands"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    quantity = Column(Integer, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    unit_price = Column(Float, index=True)
    buyer_id = Column(Integer, ForeignKey("users.id"))

    buyer = Column(Integer, ForeignKey("users.id"))
    seller = Column(Integer, ForeignKey("users.id"))
