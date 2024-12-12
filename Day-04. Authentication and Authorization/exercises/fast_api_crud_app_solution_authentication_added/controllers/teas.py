"""teas.py"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.tea import TeaModel
from serializers.tea import TeaSchema
from typing import List
from database import get_db

router = APIRouter()


@router.get("/teas", response_model=List[TeaSchema])
def get_teas(db: Session = Depends(get_db)):
    teas = db.query(TeaModel).all()  
    return teas


@router.get("/teas/{tea_id}", response_model=TeaSchema)
def get_single_tea(tea_id: int, db: Session = Depends(get_db)):
    tea = db.query(TeaModel).filter(TeaModel.id == tea_id).first()
    if not tea:
        raise HTTPException(status_code=404, detail="Tea not found")
    return tea


@router.post("/teas", response_model=TeaSchema)
def create_tea(tea: TeaSchema, db: Session = Depends(get_db)):
    new_tea = TeaModel(**tea.dict())
    db.add(new_tea)
    db.commit()
    db.refresh(new_tea)
    return new_tea


@router.put("/teas/{tea_id}", response_model=TeaSchema)
def update_tea(tea_id: int, tea: TeaSchema, db: Session = Depends(get_db)):
    # find the tea to update
    db_tea = db.query(TeaModel).filter(TeaModel.id == tea_id).first()
    if not db_tea:
        raise HTTPException(status_code=404, detail="Tea not found")

    # update the tea
    tea_data = tea.dict(exclude_unset=True)
    for key, value in tea_data.items():
        setattr(db_tea, key, value)

    db.commit()
    db.refresh(db_tea)
    return db_tea


@router.delete("/teas/{tea_id}")
def delete_tea(tea_id: int, db: Session = Depends(get_db)):
    # find the tea to delete
    db_tea = db.query(TeaModel).filter(TeaModel.id == tea_id).first()
    if not db_tea:
        raise HTTPException(status_code=404, detail="Tea not found")

    db.delete(db_tea)
    db.commit()
    return {"message": f"Tea {tea_id} deleted successfully"}