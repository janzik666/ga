# seed.py
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.recipe import RecipeModel
from models.ingredient import IngredientModel
from models.step import StepModel
from models.user import UserModel
from data.recipe_data import recipes_list, ingredients_list, steps_list
from data.user_data import user_list
from config.environment import db_URI
from sqlalchemy import create_engine

engine = create_engine(db_URI)
SessionLocal = sessionmaker(bind=engine)

# ! This seed file is a separate program that can be used to "seed" our database with some initial data.
try:
    print("Recreating database..")
    # ! Dropping (or deleting) the tables and creating them again is for convenience. Once we start to play around with
    # ! our data, changing our models, this seed program will allow us to rapidly throw out the old data and replace it.
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    divider="*********************************************************************"
    print(divider)
    print("seeding our database..")
    print(divider)
    # ! Seed recipes
    db = SessionLocal()
    db.add_all(user_list)
    db.commit()
    #db.close()

    #db = SessionLocal()
    db.add_all(recipes_list)
    db.commit()
    #db.close()

    #db = SessionLocal()
    db.add_all(ingredients_list)
    db.commit()
    #db.close()

    #db = SessionLocal()
    db.add_all(steps_list)
    db.commit()
    
    db.close()


    print("bye 👋")
except Exception as e:
    print(e)