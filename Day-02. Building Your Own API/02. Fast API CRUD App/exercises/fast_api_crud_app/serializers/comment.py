# serializers/comment.py
from pydantic import BaseModel, Field
from typing import Optional, List

class CommentSchema(BaseModel):
  id: Optional[int] = Field(None) 
  content: str
  tea_id: int
  
  class Config:
    orm_mode = True