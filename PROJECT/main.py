from fastapi import FastAPI
from controllers.recipes import router as RecipesRouter
from controllers.ingredients import router as IngredientsRouter
from controllers.steps import router as StepsRouter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from config.environment import db_URI
from controllers.users import router as UsersRouter  # Import users router
from models.database import get_db

app = FastAPI()

@app.get('/')
def home():
    return 'Hello World! Recipe Project'

app.include_router(RecipesRouter, prefix="/api")
app.include_router(IngredientsRouter, prefix="/api")
app.include_router(StepsRouter, prefix="/api")
app.include_router(UsersRouter, prefix="/api")  # Include users router
