""" models/tea.py """

from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel
from .comment import CommentModel
from .user import UserModel

class TeaModel(BaseModel):

    # ! This will be used directly to make a
    # ! TABLE in Postgresql
    __tablename__ = "teas"

    id = Column(Integer, primary_key=True, index=True)

    # ! Specific columns for our Tea Table.
    name = Column(String, unique=True)
    in_stock = Column(Boolean)
    rating = Column(Float)
    
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship('UserModel', back_populates='teas')
    
    comments = relationship("CommentModel", back_populates="tea")