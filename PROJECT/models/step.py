# models/step.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class StepModel(BaseModel):

    __tablename__ = "steps"

    id = Column(Integer, primary_key=True, index=True)
    step_order = Column(Integer, nullable=False)
    step_details = Column(String, nullable=False)

    recipe_id = Column(Integer, ForeignKey('recipes.id'), nullable=False)
    recipe = relationship("RecipeModel", back_populates="steps")
    
    

