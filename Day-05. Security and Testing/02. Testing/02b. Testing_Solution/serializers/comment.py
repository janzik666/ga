""" serializers/comment.py """
from pydantic import BaseModel

class CommentSchema(BaseModel):
  id: int
  content: str

  class ConfigDict:
    from_attributes = True