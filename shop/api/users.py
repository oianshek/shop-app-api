from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session

from shop import crud, schemas, models
from shop.api.deps import get_db

router = APIRouter()


@router.get("/test_get/{some_id}")
def root(some_id: int):
    return {"some_id": some_id}


@router.get("/", response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    users = crud.user.get_multi(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.user.get(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/", response_model=schemas.User)
def create_user(*, db: Session = Depends(get_db), user_in: schemas.UserCreate) -> Any:
    user = crud.user.get_by_username(db, username=user_in.username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud.user.create(db, obj_in=user_in)
    return user


@router.put("/{user_id}", response_model=schemas.User)
def update_user(*, db: Session = Depends(get_db), user_id: int, user_in: schemas.UserUpdate) -> Any:
    user = crud.user.get_by_id(db, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this user_id does not exist in the system",
        )
    user = crud.user.update(db, db_obj=user, obj_in=user_in)
    return user

