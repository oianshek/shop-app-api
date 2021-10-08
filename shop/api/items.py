from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session

from shop import crud, schemas, models
from shop.api.deps import get_db

router = APIRouter()


@router.post("/add_item")
def create_item(*, db: Session = Depends(get_db), item_in: schemas.ItemCreate):
    return crud.item.create(db, obj_in=item_in)
