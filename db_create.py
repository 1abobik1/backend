from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, relationship

engine = create_async_engine("sqlite+aiosqlite:///database.db", echo=True)
new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class UsersTable(Model):
    __tablename__ = "UsersTable"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    create_data_account = Column(String)

class PostsTable(Model):
    __tablename__ = "PostsTable"

    id_post = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    date_of_publication = Column(Integer)
    author_id = Column(Integer, ForeignKey('UsersTable.id'))
    author = relationship("UsersTable", back_populates="posts")

class CommentsTable(Model):
    __tablename__ = "CommentsTable"

    id_comments = Column(Integer, primary_key=True)
    content = Column(String)
    author_id = Column(Integer, ForeignKey('UsersTable.id'))
    author = relationship("UsersTable")
    date_of_publication = Column(Integer)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)