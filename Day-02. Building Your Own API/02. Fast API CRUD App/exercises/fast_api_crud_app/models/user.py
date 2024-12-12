# models/user.py
from datetime import datetime, timedelta
import jwt
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import BaseModel

from config.environment import secret

class UserModel(BaseModel):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, nullable=False, unique=True)
  email = Column(String, nullable=False, unique=True)

  # One (UserModel) to Many (TeaModel) relationship
  teas = relationship('TeaModel', back_populates='user')

  def generate_token(self):
    payload = {
      "exp": datetime.utcnow() + timedelta(days=1),
      "iat": datetime.utcnow(),
      "sub": self.id,
    }

    token = jwt.encode(
      payload,
      secret,
      algorithm="HS256",
    )
    
    return token