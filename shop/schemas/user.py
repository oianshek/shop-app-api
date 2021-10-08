from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    username: Optional[str]
    password: Optional[str]


class UserCreate(UserBase):
    username: str
    password: str


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
