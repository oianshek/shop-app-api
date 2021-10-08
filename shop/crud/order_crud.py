from typing import Optional, Dict, Union, Any
from sqlalchemy.orm import Session

from shop.crud.base import CRUDBase
from shop.models import Order
from shop.schemas import OrderCreate, OrderUpdate
from shop.api import deps
from fastapi.encoders import jsonable_encoder


class CRUDOrder(CRUDBase[Order, OrderCreate, OrderUpdate]):

    def create(self, db: Session, obj_in: OrderCreate):
        obj_in_dict = obj_in.dict()
        obj_in_dict["status"] = "Active"
        db_obj = Order(**obj_in_dict)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_user_id(self, db: Session, *, user_id: int) -> Optional[Order]:
        return db.query(Order).filter(Order.user_id == user_id).first()

    def get_active(self, db: Session, user_id: int):
        # return db.execute("SELECT * FROM ORDERS WHERE user_id = :user_id AND status = 'Active'",
        #                   {'user_id': user_id}).first()
        return db.query(Order).filter(Order.user_id == user_id, Order.status == "Active").first()

    def update(
            self,
            db: Session,
            *,
            db_obj: Order,
            obj_in: Union[OrderUpdate, Dict[str, Any]]
    ) -> Order:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def update_price(self, db: Session, order_obj: Order):
        db.add(order_obj)
        db.commit()
        db.refresh(order_obj)
        return  order_obj

    def confirm_order(self, db: Session, order_obj: Order):
        db.add(order_obj)
        db.commit()
        db.refresh(order_obj)
        return order_obj

order = CRUDOrder(Order)
