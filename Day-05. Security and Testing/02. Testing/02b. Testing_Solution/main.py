""" main.py """
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from config.environment import db_URI
from controllers.teas import router as TeasRouter
from controllers.users import router as UsersRouter

app = FastAPI()

app.include_router(TeasRouter, prefix="/api")
app.include_router(UsersRouter, prefix="/api")

@app.get('/')
def home():
    """ Hello world function """
    return 'Hello world!'
