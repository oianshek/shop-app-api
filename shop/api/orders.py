from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from shop import crud, schemas, models
from shop.api.deps import get_db, get_current_user

router = APIRouter()


@router.post("/add_to_cart/{item_id}")
def add_to_cart(*, item_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user),
                order_in: schemas.OrderCreate):
    active_order = crud.order.get_active(db, current_user.id)
    if active_order is None:
        order_in.price = crud.item.get(db, id=item_id).price
        order_in.user_id = current_user.id
        order = crud.order.create(db, obj_in=order_in)
        crud.order_item_crud.create_order_item(db, item_id=item_id, order_id=order.id)

        return order

    crud.order_item_crud.create_order_item(db, item_id, active_order.id)
    active_order.price += crud.item.get(db, item_id).price

    return crud.order.update_price(db, active_order)


@router.post("/confirm_order")
def confirm_order(*, db: Session = Depends(get_db),
                  current_user: schemas.User = Depends(get_current_user)):
    active_order = crud.order.get_active(db, current_user.id)

    if active_order is None:
        return "No orders!"

    active_order.status = "Closed"

    # confirmed_order = crud.order.confirm_order(db, active_order)
    crud.order_item_crud.delete_order_item(db, active_order.id)

    return crud.order.confirm_order(db, active_order)


@router.delete("/remove_from_cart/{item_id}")
def remove_from_cart(item_id: int, db: Session = Depends(get_db),
                     current_user: schemas.User = Depends(get_current_user)):
    active_order = crud.order.get_active(db, current_user.id)

    if active_order is None:
        return "No orders!"

    crud.order_item_crud.delete_item_from_order(db, active_order.id, item_id)
    active_order.price -= crud.item.get(db,item_id).price

    return crud.order.update_price(db, active_order)
