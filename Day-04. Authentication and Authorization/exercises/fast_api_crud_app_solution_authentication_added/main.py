from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from config.environment import db_URI
from controllers.teas import router as TeasRouter
from controllers.users import router as UsersRouter  # Import users router
from database import get_db

app = FastAPI()

app.include_router(TeasRouter, prefix="/api")
app.include_router(UsersRouter, prefix="/api")  # Include users router

@app.get('/')
def home():
    return 'Hello World!'
