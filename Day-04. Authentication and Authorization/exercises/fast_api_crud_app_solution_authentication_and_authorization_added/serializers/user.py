from pydantic import BaseModel
from typing import Optional, List

class UserSchema(BaseModel):
  username: str
  email: str

class UserLogin(BaseModel):
  username: str

class UserToken(BaseModel):
  token: str

  class Config:
    orm_mode = True