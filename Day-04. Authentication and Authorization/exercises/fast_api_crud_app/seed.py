# seed.py
from sqlalchemy.orm import sessionmaker
from models.base import Base
from data.tea_data import teas_list, comments_list
from config.environment import db_URI
from sqlalchemy import create_engine

engine = create_engine(db_URI)
SessionLocal = sessionmaker(bind=engine)

# ! This seed file is a separate program that can be used to "seed" our database with some initial data.
try:
  print("Recreating database..")
  Base.metadata.drop_all(bind=engine)
  Base.metadata.create_all(bind=engine)

  print("seeding our database..")
  # ! Seed teas
  db = SessionLocal()
  db.add_all(teas_list)
  db.commit()

  # ! Now seeding comments after teas
  db.add_all(comments_list)
  db.commit()
  db.close()

  print("bye 👋")
except Exception as e:
  print(e)