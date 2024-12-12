# serializers/recipe.py
from pydantic import BaseModel, Field
from typing import Optional, List
from .step import StepSchema
from .ingredient import IngredientSchema
from .user import UserSchema

class RecipeSchema(BaseModel):
  id: Optional[int] = Field(None) # This makes sure you don't have to explicitly add an id when sending json data
  title: str
  recipe_type: str
  cuisine_tags: str
  serves: int
  notes: str
  user: UserSchema
  
  ingredients: List[IngredientSchema] = []
  steps: List[StepSchema] = []

  class Config:
    orm_mode = True

class RecipeCreate(BaseModel):
  title:str
  recipe_type: str
  cuisine_tags: str
  serves: int
  notes: str    
  


