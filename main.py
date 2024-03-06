from fastapi import FastAPI
from pydantic import BaseModel
from db_create import create_tables, delete_tables

app = FastAPI()

# Функция для создания таблиц при запуске приложения
async def on_startup():
    await create_tables()
    print("База данных готова к работе")

# Функция для удаления таблиц при остановке приложения
async def on_shutdown():
    await delete_tables()
    print("База данных очищена")

# Добавление обработчиков событий жизненного цикла
app.add_event_handler("startup", on_startup)
app.add_event_handler("shutdown", on_shutdown)

@app.get("/home")
def get_home():
    return "Привет"

# Модели данных
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

# Остальной код вашего FastAPI приложения...