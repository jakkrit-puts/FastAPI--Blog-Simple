from datetime import timedelta, datetime
from jose import jwt,JWTError

from models import User
from schemas import *
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os
load_dotenv()

JWT_SECRET_KEY =  os.getenv("JWT_SECRET_KEY")
JWT_EXPRIE_MINUTES = int(os.getenv("JWT_EXPRIE_MINUTES"))
ALG = os.getenv("ALG")

def get_user(email:str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    return user

def create_token(data: dict):
    data_encode = data.copy()
    expire_date = datetime.now()+timedelta(minutes=JWT_EXPRIE_MINUTES)
    data_encode.update({"exp":expire_date})
    jwt_token = jwt.encode(data_encode, JWT_SECRET_KEY,algorithm=ALG)

    return jwt_token

def verify_token(token:str, credentails_exception):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY,algorithms=ALG)
        email = payload.get("sub")
        if email is None:
            raise credentails_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentails_exception

    return token_data