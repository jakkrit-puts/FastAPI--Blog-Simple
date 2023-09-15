from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models import *
from schemas import *

def create(request: BlogRequest, db: Session, current_user):
    user_email = current_user.email
    user = db.query(Blog).filter(User.email == user_email).first()

    blog = Blog(user_id= user.id, title=request.title, body = request.body)
    db.add(blog)
    db.commit()
    db.refresh(blog)

    return blog

def get_all(db: Session):
    return db.query(Blog).all()

def get_by_id(id:int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="data not found!")

    return blog

def update(id:int, request: BlogRequestUpdate, db: Session):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="id not found!")

    blog.update(request.dict())
    db.commit()

    return blog.first()

def remove(id:int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="id not found!")

    blog.delete(synchronize_session=False)
    db.commit()

    return "done"