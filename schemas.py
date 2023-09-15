from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    display_name:str
    email:str
    password:str

class UserRequest(UserBase):
    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    email:str
    class Config:
        orm_mode = True

class UserLoginRequest(BaseModel):
    email:str
    password:str
    class Config:
        orm_mode = True

# =================================================

class BlogBase(BaseModel):
    id:int
    user_id: int
    title:str
    body:str

class BlogRequest(BaseModel):
    title:str
    body:str
    class Config:
        orm_mode = True

class BlogRequestUpdate(BaseModel):
    title:str
    body:str
    class Config:
        orm_mode = True

class BlogResponse(BlogBase): # custom use BaseModel
    title:str
    body:str
    author: UserResponse
    class Config:
        orm_mode = True

# ==================================================

class Token(BaseModel):
    access_token:str
    expires_in: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None