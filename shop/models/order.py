from ..db.db_base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, BIGINT, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    date_created = Column(DateTime, default=datetime.now(), index=True)
    price = Column(Integer, index=True)
    status = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="orders")