from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
import oauth2

from models import *
from schemas import *
from database import get_db
from repositories import blog

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

@router.post("/blog", status_code=status.HTTP_201_CREATED)
def create_blog(request: BlogRequest, db:Session = Depends(get_db), current_user: UserBase = Depends(oauth2.get_user)):
    return blog.create(request, db, current_user=current_user)

@router.get("/blog", response_model=list[BlogResponse])
def get_blogs(db:Session = Depends(get_db), current_user: UserBase = Depends(oauth2.get_user)):
    return blog.get_all(db)

@router.get("/blog/{id}", response_model=BlogResponse)
def get_blog_by_param(id:int, db:Session = Depends(get_db), current_user: UserBase = Depends(oauth2.get_user)):
    return blog.get_by_id(id, db)

@router.put("/blog/{id}")
def update_blog(id:int, request: BlogRequestUpdate, db:Session = Depends(get_db), current_user: UserBase = Depends(oauth2.get_user)):
    return blog.update(id, request, db)

@router.delete("/blog/{id}")
def remove_blog(id:int, db:Session = Depends(get_db), current_user: UserBase = Depends(oauth2.get_user)):
    return blog.remove(id, db)