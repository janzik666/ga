"""teas.py"""
from fastapi import APIRouter
from models.tea_data import teas_db

router = APIRouter()


@router.get("/teas")
def get_teas():
    """ Get all teas """
    return teas_db


@router.get("/teas/{tea_id}")
def get_single_tea(tea_id: int):
    """ Get tea by ID """
    return teas_db['teas'][tea_id - 1]  # -1 because list indexes start at 0


@router.post("/teas")
def create_tea(tea: dict):
    """ Create tea """
    teas_db["teas"].append(tea)
    return tea
