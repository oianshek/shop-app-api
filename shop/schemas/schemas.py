from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    date_created: datetime


class OrderCreate(OrderBase):
    date_created: datetime
    user_id: int
    item_id: int


class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True


class ItemBase(BaseModel):
    name: str
    price: int
    description: str


class ItemCreate(ItemBase):
    name: str
    price: int
    description: str


class Item(ItemBase):
    id: int

