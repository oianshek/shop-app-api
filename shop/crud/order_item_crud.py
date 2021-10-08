from sqlalchemy.orm import Session


def create_order_item(db: Session, item_id: int, order_id: int):
    db.execute("INSERT INTO order_item VALUES(:order_id, :item_id)", {'order_id': order_id, 'item_id': item_id})
    db.commit()


def delete_order_item(db: Session, order_id: int):
    db.execute("DELETE FROM order_item WHERE order_id = :order_id", {'order_id': order_id})
    db.commit()


def delete_item_from_order(db: Session, order_id: int, item_id: int):
    db.execute("DELETE FROM order_item WHERE order_id = :order_id AND item_id = :item_id",{'order_id': order_id, 'item_id': item_id})
    db.commit()
