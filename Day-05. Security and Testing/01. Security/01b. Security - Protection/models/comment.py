# models/comment.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class CommentModel(BaseModel):

  __tablename__ = "comments"

  id = Column(Integer, primary_key=True, index=True)
  content = Column(String, nullable=False)

  # ForeignKey points to the primary key of the teas table
  tea_id = Column(Integer, ForeignKey('teas.id'), nullable=False)
  tea = relationship("TeaModel", back_populates="comments")