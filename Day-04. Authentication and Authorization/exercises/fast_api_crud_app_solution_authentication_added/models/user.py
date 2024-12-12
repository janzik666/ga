from datetime import datetime, timedelta
# from passlib.context import CryptContext    # optional password hashing
import jwt
from sqlalchemy import Column, Integer, String
from .base import Base

# Import the secret from the environment file
from config.environment import secret

class UserModel(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, nullable=False, unique=True)
  email = Column(String, nullable=False, unique=True)


  def generate_token(self):
    # Create a token for this user.
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
  


##### OPTIONAL PASSWORD HASHING CODE ADDED BELOW!!
##### THE CODE BELOW WOULD BE INTEGRATED WITH THE USER MODEL ABOVE!

# ## Stretch goal
# The goal here is to walk through what authentication and password management *could* look like. In a real world scenario, these operations would likely be managed be an entirely separate department that is responsible for identity management.

# ### Password hashing with Passlib

# The gold standard for dealing with passwords is to hash them before storing them in the database. There are many Python libraries we can use to help us with this. Most use `passlib[bcrypt]`.

# Install passlib as follows:
# `pipenv install passlib`

# ### Updating a user model

# Here's what a possible implementation could look like. First you would have a field on the user model called `password_hash`. This will be what actually gets stored in the database. Also, there would be a function on our user model to set the password.

# **models/user.py**
# ```py
# from passlib.context import CryptContext
# from sqlalchemy import Column, Integer, String
# from .base import Base

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# class UserModel(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, nullable=False, unique=True)
#     email = Column(String, nullable=False, unique=True)
#     password_hash = Column(String, nullable=True) # We're storing a hashed version of our password here

#     # We'll create this method to to set the hashed password
#     def set_password(self, password):
#         self.password_hash = pwd_context.hash(password)
# ```

# If you see above the `set_password` function uses the `pwd_context` to hash the password and sets the hash to the user's `password_hash` property.
