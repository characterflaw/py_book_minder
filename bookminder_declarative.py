# import sqlite3 as lite
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class BookAuthor(Base):
    __tablename__ = "bookauthors"
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('book.id'))
    author_id = Column(Integer, ForeignKey('author.id'))

    book = relationship("Book", foreign_keys=book_id)
    author = relationship("Author", foreign_keys=author_id)

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String(32), nullable=False)
    year = Column(Integer, nullable=False)
    own_flag = Column(Integer, nullable=True)
    read_flag = Column(Integer, nullable=True)
    series_id = Column(Integer, ForeignKey('series.id'), nullable=True)

    series = relationship('Series', foreign_keys=series_id)

class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(32), nullable=False)
    last_name = Column(String(32), nullable=False)

class Series(Base):
    __tablename__ = 'series'
    id = Column(Integer, primary_key=True)
    title = Column(String(32), nullable=False)

engine = create_engine('sqlite:///test.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
