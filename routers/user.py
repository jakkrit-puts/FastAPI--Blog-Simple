from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm import Session

from models import *
from schemas import *
import database
from repositories import user

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

get_db = database.get_db

@router.post("/user", status_code=status.HTTP_201_CREATED)
def create_user(request: UserRequest, db:Session = Depends(get_db)):
    return user.create(request, db)

@router.get("/user/{id}")
def get_user_by_id(id: int, db:Session = Depends(get_db)):
    return user.get_by_id(id, db)