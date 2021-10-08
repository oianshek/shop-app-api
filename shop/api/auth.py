from typing import Any, List
from datetime import datetime, timedelta

from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from shop import crud, schemas, models
from shop.api.deps import get_db, get_current_user

router = APIRouter()


@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = crud.user.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=crud.user_crud.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crud.user.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# FIXME: alter double g
@router.get("/get_current_user", response_model=schemas.User)
async def get_current(current_user: schemas.User = Depends(get_current_user)):
    return current_user
