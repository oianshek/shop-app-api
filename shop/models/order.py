# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
# from sqlalchemy.orm import relationship
# from datetime import datetime
#
# from ..db.db import Base
#
#
# class Order(Base):
#     __tablename__ = "orders"
#
#     id = Column(Integer, primary_key=True, index=True)
#     date_created = Column(DateTime, default=datetime.now(), unique=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     item_id = Column(Integer, ForeignKey("items.id"))
#
#     user = relationship("user", back_populates="orders")
