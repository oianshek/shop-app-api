from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class OrderBase(BaseModel):
    date_created: Optional[datetime]
    price: Optional[int]
    status: Optional[str]
    user_id: Optional[int]


class OrderCreate(OrderBase):
    date_created: datetime


class OrderUpdate(OrderBase):
    pass


class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True
