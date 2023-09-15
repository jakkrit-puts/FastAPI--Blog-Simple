from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from passlib.hash import pbkdf2_sha256

from schemas import *
from models import *
from sqlalchemy.orm import *
from jwt_auth import create_token

def login(request: OAuth2PasswordRequestForm, db: Session):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found!")

    if not pbkdf2_sha256.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="password invalid.")

    access_token = create_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "Bearer"}