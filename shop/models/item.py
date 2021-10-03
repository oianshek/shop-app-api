# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BIGINT
# from sqlalchemy.orm import relationship
#
# from ..db.db import Base
#
#
# class Item(Base):
#     __tablename__ = "items"
#
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String,unique=True, index=True, nullable=False)
#     price = Column(BIGINT, unique=True, index=True, nullable=False)
#     description = Column(String, unique=True, nullable=False)
#
#     orders = relationship("order", back_populates="user")
#
#
