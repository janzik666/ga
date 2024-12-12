from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class IngredientModel(BaseModel):
    
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    quantity = Column(String, nullable=False)

    recipe_id = Column(Integer, ForeignKey('recipes.id'), nullable=False)
    recipe = relationship("RecipeModel", back_populates="ingredients")  

