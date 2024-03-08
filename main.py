from fastapi import HTTPException, Depends, FastAPI
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models_db
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

app = FastAPI()

origins = {
    'http://localhost:300'
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)


class UsersBase(BaseModel):
    email: str
    password: str


class PostBase(BaseModel):
    title: str
    picture: str


class UserModel(UsersBase):
    id: int

    class Config:
        from_attributes = True


class PostModel(PostBase):
    id: int

    class Config:
        from_attributes = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Depends(get_db)

# создание бд
models_db.Base.metadata.create_all(bind=engine)

# очистка бд
# models_db.Base.metadata.drop_all(bind=engine)


@app.post("/user/", response_model=UserModel)
async def create_user(User: UserModel, db: Session = db_dependency):
    db_user = models_db.UsersTable(**User.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post("/post/", response_model=PostModel)
async def create_post(Post: PostModel, db: Session = db_dependency):
    db_post = models_db.PostsTable(**Post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
