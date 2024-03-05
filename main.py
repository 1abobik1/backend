from datetime import datetime
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List

from sqlalchemy.orm import Session

app = FastAPI()


# Модели данных
class User(BaseModel):
    id_user: int
    username: str
    email: str
    password: str
    create_data_account: str



class Post(BaseModel):
    id_post: int
    title: str
    content: str
    date_of_publication: datetime
    author: User
    comments: List[str] = []


class Comment(BaseModel):
    id_comments: int
    content: str
    author: User
    date_of_publication: datetime


# Фейковые данные (для примера)
fake_users_db = {
    1: {"id_user": 1, "username": "user1", "email": "user1@example.com", "password": "password1",
        "create_data_account": "2024-03-03", "id_posts": []},
    2: {"id_user": 2, "username": "user2", "email": "user2@example.com", "password": "password2",
        "create_data_account": "2024-03-03", "id_posts": []},
}

fake_posts_db = {
    1: {"id_post": 1, "title": "First Post", "content": "Content of the first post",
        "date_of_publication": datetime.now(), "author": fake_users_db[1], "comments": []},
    2: {"id_post": 2, "title": "Second Post", "content": "Content of the second post",
        "date_of_publication": datetime.now(), "author": fake_users_db[2], "comments": []},
}


# Роуты
@app.get("/posts/", response_model=List[Post])
async def read_posts():
    return list(fake_posts_db.values())


@app.get("/posts/{post_id}", response_model=Post)
async def read_post(post_id: int):
    if post_id not in fake_posts_db:
        raise HTTPException(status_code=404, detail="Post not found")
    return fake_posts_db[post_id]


@app.post("/posts/", response_model=Post)
async def create_post(post: Post):
    post_id = max(fake_posts_db.keys()) + 1
    post.date_of_publication = datetime.now()
    post.id_post = post_id
    fake_posts_db[post_id] = post
    return post


@app.put("/posts/{post_id}", response_model=Post)
async def update_post(post_id: int, post_update: Post):
    if post_id not in fake_posts_db:
        raise HTTPException(status_code=404, detail="Post not found")
    fake_posts_db[post_id] = post_update
    return post_update


# Проверка работоспособности базы данных
@app.get("/check-db")
async def check_db(db: Session = Depends(get_db)):
    try:
        # Получаем первого пользователя из базы данных
        user = db.query(User).first()
        # Если пользователь найден, возвращаем его информацию
        if user:
            return {"status": "Database is accessible", "user": user}
        else:
            return {"status": "Database is accessible but no user found"}
    except Exception as e:
        # Если произошла ошибка, возвращаем информацию об ошибке
        return {"status": "Error accessing database", "error": str(e)}
