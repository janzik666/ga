# controllers/steps.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.step import StepModel
#from models.step import StepModel
from serializers.step import StepSchema
from typing import List
from models.database import get_db
from models.user import UserModel # import user model
from dependencies.get_current_user import get_current_user
from models.recipe import RecipeModel

router = APIRouter()

@router.get("/steps", response_model=List[StepSchema])
def get_steps(db: Session = Depends(get_db)):
    steps = db.query(StepModel).all()  
    return steps

@router.post("/steps", response_model=StepSchema)
def create_step(step: StepSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    db_recipe = db.query(RecipeModel).filter(RecipeModel.id == step.recipe_id).first()
    
    #This checks who created the recipe and only allows recipe creatore to perform action
    if db_recipe.user_id !=current_user.id:
        raise HTTPException(status_code=403, detail="Operation forbidden")    
    
    new_step = StepModel(**step.dict())
    db.add(new_step)
    db.commit()
    db.refresh(new_step)
    return new_step

@router.put("/steps/{step_id}", response_model=StepSchema)
def update_step(step_id: int, step: StepSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    # find the step to update
    db_step = db.query(StepModel).filter(StepModel.id == step_id).first()
    db_recipe = db.query(RecipeModel).filter(RecipeModel.id == db_step.recipe_id).first()
    if not db_step:
        raise HTTPException(status_code=404, detail="Step not found")
    #This checks who created the recipe and only allows recipe creatore to perform action
    if db_recipe.user_id !=current_user.id:
        raise HTTPException(status_code=403, detail="Operation forbidden")
    
    # update the step
    step_data = step.dict(exclude_unset=True)
    for key, value in step_data.items():
        try:
            setattr(db_step, key, value)
        except:
            pass
    db.commit()
    db.refresh(db_step)
    return db_step    

@router.delete("/steps/{step_id}")
def delete_step(step_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    # find the step to delete
    db_step = db.query(StepModel).filter(StepModel.id == step_id).first()
    db_recipe = db.query(RecipeModel).filter(RecipeModel.id == db_step.recipe_id).first()    
    if not db_step:
        raise HTTPException(status_code=404, detail="Step not found")
    
    if db_recipe.user_id !=current_user.id:
        raise HTTPException(status_code=403, detail="Operation forbidden")      

    db.delete(db_step)
    db.commit()
    return {"message": f"Step {step_id} deleted successfully"}