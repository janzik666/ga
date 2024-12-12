# controllers/users.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user import UserModel
from serializers.user import UserSchema, UserLogin, UserToken
from typing import List
from models.database import get_db

router = APIRouter()

@router.post("/register", response_model=UserSchema)
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    new_user = UserModel(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login", response_model=UserToken)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.username == user.username).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Incorrect username")

    token = db_user.generate_token()
    return {"token": token, "message": "Welcome back!"}