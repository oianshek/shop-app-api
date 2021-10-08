from datetime import timedelta
from datetime import datetime
from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from ..models.item import Item
from ..schemas.item import ItemCreate, ItemUpdate
from .base import CRUDBase


class CRUDItem(CRUDBase[Item, ItemCreate, ItemUpdate]):

    def create(self, db: Session, *, obj_in: ItemCreate) -> Item:
        db_item = Item(**obj_in.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item


item = CRUDItem(Item)
