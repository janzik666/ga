# Serializers/ingredient.py
from pydantic import BaseModel, Field
from typing import Optional, List

class IngredientSchema(BaseModel):
    id: Optional[int] = Field(None) 
    name: str
    quantity: str
    recipe_id: int

    class Config:
        orm_mode = True