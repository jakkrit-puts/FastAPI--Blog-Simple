from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt_auth

oauth_schemas = OAuth2PasswordBearer(tokenUrl="login")

def get_user(token:str = Depends(oauth_schemas)):
  credentails_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                        detail="Could not validate credentails",
                                        headers={"WWW-Authenticate":"Bearer"}
                                        )
  return jwt_auth.verify_token(token, credentails_exception)