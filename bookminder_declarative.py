# import sqlite3 as lite
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String(32), nullable=False)
    year = Column(Integer, nullable=False)
    author1_id = Column(Integer, ForeignKey('author.id'))
    author2_id = Column(Integer, ForeignKey('author.id'))
    own_flag = Column(Integer, nullable=True)
    read_flag = Column(Integer, nullable=True)
    series_id = Column(Integer, ForeignKey('series.id'), nullable=True)

    author1 = relationship("Author", foreign_keys=author1_id)
    author2 = relationship("Author", foreign_keys=author2_id)
    series = relationship('Series', foreign_keys=series_id)

class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(32), nullable=False)
    last_name = Column(String(32), nullable=False)
#    books = relationship(Book)

class Series(Base):
    __tablename__ = 'series'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('author.id'))
    title = Column(String(32), nullable=False)
    author = relationship("Author", foreign_keys=author_id)
#    series = relationship(Book)

engine = create_engine('sqlite:///test.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
