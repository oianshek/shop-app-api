from datetime import timedelta
from datetime import datetime
from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from ..models.user import User
from ..schemas.user import UserUpdate, UserCreate
from ..core.security import get_password_hash, verify_password
from .base import CRUDBase

from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):

    def get_by_id(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    def get_by_username(self, db: Session, *, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        obj_in_dict = obj_in.dict()
        hashed_password = get_password_hash(obj_in.password)
        del obj_in_dict["password"]
        db_obj = User(**obj_in_dict, password=hashed_password)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
            self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if "password" in update_data and update_data["password"]:
            update_data["password"] = get_password_hash(update_data["password"])
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate_user(self, db: Session, username: str, password: str):
        user = self.get_by_username(db, username=username)
        if not user:
            return False
        if not verify_password(password, user.password):
            return False
        return user

    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt


user = CRUDUser(User)
# from typing import Any, Dict, Optional, Union
# from sqlalchemy.orm import Session
#
# from ..models.models import User, Item, Order
# from ..schemas.schemas import UserCreate, UserUpdate
#
# from passlib.context import CryptContext
#
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
#
#

#
#
# def get_password_hash(password: str) -> str:
#     return pwd_context.hash(password)
#
#
# def get_user_by_username(db: Session, username: str):
#     return db.query(User).filter(User.username == username).first()
#
#
# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(User).offset(skip).limit(limit).all()
#
#
# def create_user(db: Session, user: UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = User(username=user.username, password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
#
#     def update(
#             self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
#     ) -> User:
#         if isinstance(obj_in, dict):
#             update_data = obj_in
#         else:
#             update_data = obj_in.dict(exclude_unset=True)
#         if update_data["password"]:
#             hashed_password = get_password_hash(update_data["password"])
#             del update_data["password"]
#             update_data["hashed_password"] = hashed_password
#         return super().update(db, db_obj=db_obj, obj_in=update_data)
#
#
# def update_user(db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]):
#     if isinstance(obj_in, dict):
#         update_data = obj_in
#     else:
#         update_data = obj_in.dict(exclude_unset=True)
#     if update_data["password"]:
#         hashed_password = get_password_hash(update_data["password"])
#         del update_data["password"]
#         update_data["password_hash"] = hashed_password
#     return
