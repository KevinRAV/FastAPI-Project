from datetime import datetime
import pip._internal.utils
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

    products = relationship("Product", back_populates="seller")
    carts = relationship("Cart", back_populates="owner")
    comments = relationship("Comment", back_populates="author")
    commands = relationship("Command", back_populates="buyer")
    commands = relationship("Command", back_populates="seller")


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

    seller = relationship("User", back_populates="products")
    category = relationship("Category", back_populates="products")
    products = relationship("Cart", back_populates="product")
    comments = relationship("Comment", back_populates="product")

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    products = relationship("Product", back_populates="category")

class Cart(Base):
    __tablename__ = "carts"

    owner_id = Column(Integer, ForeignKey("users.id"), primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True, index=True)
    quantity = Column(Integer)

    owner = relationship("User", back_populates="carts")
    product = relationship("Product", back_populates="carts")

class Comment(Base):
    __tablename__ = "comments"

    author_id = Column(Integer, ForeignKey("users.id"), primary_key=True, index=True)
    product_id =  Column(Integer, ForeignKey("products.id"), primary_key=True, index=True)
    stars = Column(Integer)
    message = Column(String)

    author = relationship("User", back_populates="comments")
    product = relationship("Product", back_populates="comments")

class Commands(Base):
    __tablename__ = "commands"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    quantity = Column(Integer, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    unit_price = Column(Float, index=True)

    buyer = relationship("User", back_populates="commands")
    seller = relationship("User", back_populates="commands")
