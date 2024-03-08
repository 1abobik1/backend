from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Identity


class UsersTable(Base):
    __tablename__ = "UsersTable"

    id = Column(Integer, primary_key=True)
    # username = Column(String)
    email = Column(String)
    password = Column(String)
    # posts = relationship("PostsTable", back_populates="author")


class PostsTable(Base):
    __tablename__ = "PostsTable"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    picture = Column(String)
    # content = Column(String)
    # date_of_publication = Column(Integer)
    # author_id = Column(Integer, ForeignKey('UsersTable.id'))
    # author = relationship("UsersTable", back_populates="posts")


# class CommentsTable(Base):
#     __tablename__ = "CommentsTable"
#
#     id_comments = Column(Integer, primary_key=True)
#     content = Column(String)
#     author_id = Column(Integer, ForeignKey('UsersTable.id'))
#     author = relationship("UsersTable")
#     date_of_publication = Column(Integer)
#
