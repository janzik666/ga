# controllers/recipes.py

from fastapi import APIRouter, Depends, HTTPException, Security
from sqlalchemy.orm import Session
from models.recipe import RecipeModel
from models.step import StepModel
from models.ingredient import IngredientModel
from models.user import UserModel # import user model
from serializers.recipe import RecipeSchema, RecipeCreate as RecipeCreateSchema
from typing import List
from models.database import get_db
from dependencies.get_current_user import get_current_user


router = APIRouter()

@router.get("/recipes", response_model=List[RecipeSchema])
def get_recipes(db: Session = Depends(get_db)):
    recipes = db.query(RecipeModel).all()  
    return recipes

@router.get("/recipes/{recipe_id}", response_model=RecipeSchema)
def get_single_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = db.query(RecipeModel).filter(RecipeModel.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@router.post("/recipes", response_model=RecipeSchema)
def create_recipe(recipe: RecipeCreateSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    new_recipe = RecipeModel(**recipe.dict(), user_id=current_user.id)
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe

@router.put("/recipes/{recipe_id}", response_model=RecipeSchema)
def update_recipe(recipe_id: int, recipe: RecipeSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
#def update_recipe(recipe_id: int, recipe: RecipeSchema, db: Session = Depends(get_db)):    
    # find the recipe to update
    divider = "*******************************************************************"
    db_recipe = db.query(RecipeModel).filter(RecipeModel.id == recipe_id).first()
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    if db_recipe.user_id !=current_user.id:
        raise HTTPException(status_code=403, detail="Operation forbidden")

    # update the recipe
    recipe_data = recipe.dict(exclude_unset=True)
    # print(divider)
    # print(recipe_data)
    # print(f"4{divider}")
    for key, value in recipe_data.items():
        try:
            setattr(db_recipe, key, value)
        except:
            pass
    db.commit()
    db.refresh(db_recipe)
    return db_recipe    

@router.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    # find the recipe to delete
    db_recipe = db.query(RecipeModel).filter(RecipeModel.id == recipe_id).first()
    if not db_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    if db_recipe.user_id !=current_user.id:
        raise HTTPException(status_code=403, detail="Operation forbidden")

    db.delete(db_recipe)
    db.commit()
    return {"message": f"Recipe {recipe_id} deleted successfully"}