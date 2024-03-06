from fastapi import FastAPI
from pydantic import BaseModel
from contextlib import asynccontextmanager
from db_create import create_tables, delete_tables

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База данных очищена")
    await create_tables()
    print("База данных готова к работе")
    yield
    print("Выключение")

@app.on_event("startup")
async def startup_event():
    await create_tables()

@app.on_event("shutdown")
async def shutdown_event():
    await delete_tables()

class users(BaseModel):
    id_user: int
    username: str
    email: str
    password: str
    create_data_account: str

class posts(BaseModel):
    id_post: int
    title: str
    content: str
    date_of_publication: str
    author: users

class comments(BaseModel):
    id_comments: int
    content: str
    author: users
    date_of_publication: str
