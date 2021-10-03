# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship
#
# from ..db.db import Base
#
#
# class User(Base):
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True, nullable=False)
#     password = Column(String, unique=True, nullable=False)
#
#     orders = relationship("order", back_populates="user")
#
#
