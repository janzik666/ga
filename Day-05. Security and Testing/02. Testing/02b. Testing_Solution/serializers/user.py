""" serializers/user.py """
from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    email: str
    
class UserLogin(BaseModel):
    username: str
    
class UserToken(BaseModel):
    token: str
    
class ConfigDict:
    from_attributes = True