from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BIGINT, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..db.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, unique=True, nullable=False)

    orders = relationship("Order", back_populates="user")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    price = Column(BIGINT, unique=True, index=True, nullable=False)
    description = Column(String, unique=True, nullable=False)

    orders = relationship("Order", back_populates="items")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    date_created = Column(DateTime, default=datetime.now(), unique=True, index=True)
    price = Column(Integer, unique=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    item_id = Column(Integer, ForeignKey("items.id"))

    user = relationship("User", back_populates="orders")
    items = relationship("Item", back_populates="orders")
