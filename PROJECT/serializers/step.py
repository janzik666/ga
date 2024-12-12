# Serializers/step.py
from pydantic import BaseModel, Field
from typing import Optional, List

class StepSchema(BaseModel):
    id: Optional[int] = Field(None) 
    step_order: int
    step_details: str
    recipe_id: int

    class Config:
        orm_mode = True