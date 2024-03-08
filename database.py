from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

URL_DATABASE = "sqlite:///database.db"

engine = create_engine(URL_DATABASE, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# async def create_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Model.metadata.create_all)
#
#
# async def delete_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Model.metadata.drop_all)
