# tests/lib.py

from fastapi.testclient import TestClient
from models.tea import TeaModel
from models.user import UserModel
from models.comment import CommentModel
from data.tea_data import teas_list, comments_list
from data.user_data import user_list

def seed_db(db):
    db.commit()

    db.add_all(user_list)
    db.commit()

    db.add_all(teas_list)
    db.commit()

    db.add_all(comments_list)
    db.commit()


def login(test_app: TestClient, username: str):
    response = test_app.post("/api/login", json={"username": username})
    token = response.json()['token']
    headers = {"Authorization": f"Bearer {token}"}
    return headers