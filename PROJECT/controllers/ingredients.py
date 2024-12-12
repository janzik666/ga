# controllers/ingredients.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.ingredient import IngredientModel
from models.recipe import RecipeModel
from serializers.ingredient import IngredientSchema
from models.user import UserModel # import user model
from typing import List
from models.database import get_db
from dependencies.get_current_user import get_current_user

router = APIRouter()

@router.get("/ingredients", response_model=List[IngredientSchema])
def get_ingredients(db: Session = Depends(get_db)):
    ingredients = db.query(IngredientModel).all()  
    return ingredients

@router.get("/ingredients/{ingredient_id}", response_model=IngredientSchema)
def get_single_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    ingredient = db.query(IngredientModel).filter(IngredientModel.id == ingredient_id).first()
    if not ingredient:
         raise HTTPException(status_code=404, detail="Ingredient not found")
    return ingredient

@router.post("/ingredients", response_model=IngredientSchema)
def create_ingredient(ingredient: IngredientSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    db_recipe = db.query(RecipeModel).filter(RecipeModel.id == ingredient.recipe_id).first()
    
    #This checks who created the recipe and only allows recipe creatore to perform action
    if db_recipe.user_id !=current_user.id:
        raise HTTPException(status_code=403, detail="Operation forbidden")
        

    new_ingredient = IngredientModel(**ingredient.dict())
    db.add(new_ingredient)
    db.commit()
    db.refresh(new_ingredient)
    return new_ingredient

@router.put("/ingredients/{ingredient_id}", response_model=IngredientSchema)
def update_ingredient(ingredient_id: int, ingredient: IngredientSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    # find the ingredient to update
    db_ingredient = db.query(IngredientModel).filter(IngredientModel.id == ingredient_id).first()
    db_recipe = db.query(RecipeModel).filter(RecipeModel.id == db_ingredient.recipe_id).first()

    if not db_ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    #This checks who created the recipe and only allows recipe creatore to perform action
    if db_recipe.user_id !=current_user.id:
        raise HTTPException(status_code=403, detail="Operation forbidden")
        
    # update the ingredient
    ingredient_data = ingredient.dict(exclude_unset=True)
    for key, value in ingredient_data.items():
        try:
            setattr(db_ingredient, key, value)
        except:
            pass
    db.commit()
    db.refresh(db_ingredient)
    return db_ingredient    

@router.delete("/ingredients/{ingredient_id}")
def delete_ingredient(ingredient_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    # find the ingredient to delete
    db_ingredient = db.query(IngredientModel).filter(IngredientModel.id == ingredient_id).first()
    db_recipe = db.query(RecipeModel).filter(RecipeModel.id == db_ingredient.recipe_id).first()
    if not db_ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    #This checks who created the recipe and only allows recipe creatore to perform action
    if db_recipe.user_id !=current_user.id:
        raise HTTPException(status_code=403, detail="Operation forbidden")  

    db.delete(db_ingredient)
    db.commit()
    return {"message": f"Ingredient {ingredient_id} deleted successfully"}