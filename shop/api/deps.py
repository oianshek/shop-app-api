from fastapi import Depends, HTTPException, status, Security
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, SecurityScopes

from shop.db.db_base import SessionLocal
from shop import crud, models, schemas

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, crud.user_crud.SECRET_KEY, algorithms=[crud.user_crud.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)

    except JWTError:
        raise credentials_exception
    user = crud.user.get_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user
