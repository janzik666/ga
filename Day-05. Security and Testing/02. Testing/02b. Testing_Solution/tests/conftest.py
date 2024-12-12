import pytest
from starlette.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app
from database import get_db
from models.base import BaseModel
from tests.lib import seed_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

BaseModel.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client

@pytest.fixture(scope="module")
def test_db() -> Session:
    # drop all tables in the database
    BaseModel.metadata.drop_all(bind=engine)
    # create all tables in the database
    BaseModel.metadata.create_all(bind=engine)
    # initiate a new session
    db = TestingSessionLocal()
    seed_db(db)
    yield db
    db.close()

@pytest.fixture(scope="module")
def override_get_db(test_db):
    def _get_db_override():
        return test_db
    app.dependency_overrides[get_db] = _get_db_override
    yield
    app.dependency_overrides = {}