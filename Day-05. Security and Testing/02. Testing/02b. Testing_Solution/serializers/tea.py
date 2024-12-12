""" serializers/tea.py """
from pydantic import BaseModel
from typing import Optional, List
from .comment import CommentSchema
from .user import UserSchema

class TeaSchema(BaseModel):
  id: int
  name: str
  in_stock: bool
  rating: float
  user: UserSchema
  
  comments: List[CommentSchema] = []

class TeaCreate(BaseModel):
  name: str
  in_stock: bool
  rating: int

class ConfigDict:
  from_attributes = True