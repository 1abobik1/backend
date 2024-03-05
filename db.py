from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

# Создаем подключение к базе данных SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./example.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создаем базовый класс для определения моделей данных
Base = declarative_base()


# Определяем модели данных (таблицы)
class User(Base):
    __tablename__ = 'users'
    id_user = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    create_data_account = Column(DateTime, default=datetime.now)
    posts = relationship("Post", back_populates="author")


class Post(Base):
    __tablename__ = 'posts'
    id_post = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    date_of_publication = Column(DateTime, default=datetime.now)
    author_id = Column(Integer, ForeignKey('users.id_user'))
    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")


class Comment(Base):
    __tablename__ = 'comments'
    id_comments = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    date_of_publication = Column(DateTime, default=datetime.now)
    post_id = Column(Integer, ForeignKey('posts.id_post'))
    post = relationship("Post", back_populates="comments")


# Создаем таблицы в базе данных
Base.metadata.create_all(bind=engine)


# Создаем сессию для взаимодействия с базой данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
