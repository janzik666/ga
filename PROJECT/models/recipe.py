# models/recipe.py

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel
#from models.ingredient import IngredientModel
from .ingredient import IngredientModel
from .user import UserModel

class RecipeModel(BaseModel):
    
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, unique=True)
    recipe_type = Column(String)
    cuisine_tags = Column(String)
    serves = Column(Integer)
    notes = Column(String)
    # Foreign key for User
    user_id = Column(Integer, ForeignKey('users.id'))

  # Many (TeaModel) to One (UserModel) relationship
    user = relationship('UserModel', back_populates='recipes')
    
    ingredients = relationship("IngredientModel", back_populates="recipe", cascade="all, delete-orphan")
    steps = relationship("StepModel", back_populates="recipe", cascade="all, delete-orphan")
    
    

