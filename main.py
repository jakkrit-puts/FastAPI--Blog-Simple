from fastapi import FastAPI
from routers import blog, user, auth

from models import *
from schemas import *
from database import engine

Base.metadata.create_all(bind=engine)

description = """
## Blogs
## Users
"""

app = FastAPI(
    title="Blogs APIs App Simple",
    description=description,
    summary="Blogs APIs App",
    version="0.0.1",
    # terms_of_service="http://example.com/terms/",
    # contact={
    #     "name": "",
    #     "url": "",
    #     "email": "",
    # },
    # license_info={
    #     "name": "Apache 2.0",
    #     "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    # },
)

@app.get("/", tags=["Index"])
def index():
    return {"data": "fastapi-simple basic"}

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(blog.router)