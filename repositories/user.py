from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models import *
from schemas import *

from passlib.hash import pbkdf2_sha256

def create(request: UserRequest, db: Session):
    hash_password = pbkdf2_sha256.hash(request.password )
    user = User(email = request.email, password= hash_password, display_name = request.display_name)
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_by_id(id:int, db:Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="data not found!")

    return user