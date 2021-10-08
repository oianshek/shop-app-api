from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    name: Optional[str]
    price: Optional[int]
    description: Optional[str]


class ItemCreate(ItemBase):
    name: str
    price: int
    description: str


class ItemUpdate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
