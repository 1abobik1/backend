import sqlite3
import datetime


def get_timestamp(y, m, d):
    return datetime.datetime.timestamp(datetime.datetime(y, m, d))


def create_tables():
    # Открываем соединение с базой данных
    with sqlite3.connect("C:/Users/dima1/PycharmProjects/backend/database.db") as db:
        # Создаем курсор для выполнения SQL-запросов
        cursor = db.cursor()

        # Создаем таблицу пользователей (User)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id_user INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL,
                create_data_account INTEGER NOT NULL  -- Изменили тип данных на INTEGER
            )
        """)

        # Создаем таблицу постов (Post)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id_post INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                date_of_publication INTEGER NOT NULL,  -- Изменили тип данных на INTEGER
                author_id INTEGER,
                FOREIGN KEY (author_id) REFERENCES users(id_user)
            )
        """)

        # Создаем таблицу комментариев (Comment)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS comments (
                id_comments INTEGER PRIMARY KEY,
                content TEXT NOT NULL,
                date_of_publication INTEGER NOT NULL,  -- Изменили тип данных на INTEGER
                author_id INTEGER,
                post_id INTEGER,
                FOREIGN KEY (author_id) REFERENCES users(id_user),
                FOREIGN KEY (post_id) REFERENCES posts(id_post)
            )
        """)

        # Подтверждаем изменения в базе данных
        db.commit()


create_tables()
