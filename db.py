from sqlalchemy import create_engine, text
import sqlite_db

# Создаем подключение к базе данных SQLite
engine = create_engine("sqlite+pysqlite:///database.db", echo=True, future=True)

with engine.connect() as connection:
    result = connection.execute(text("select 'hi'"))
    print(result)
