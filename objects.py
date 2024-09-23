from typing import Any
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class Book(Base):
    """წიგნის უნდა ქონდეს შემდეგი ველები:
        ID (primary key)
        დასახელება
        კატეგორიის დასახელება
        გვერდების რაოდენობა
        გამოცემის თარიღი
        ავტორის აიდი
    """
    __tablename__ = 'books'
    book_id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(String, ForeignKey('authors.author_id'), nullable=False)
    year = Column(Integer, nullable=False)
    num_pages = Column(Integer, nullable=False)
    genre = Column(String, nullable=False)

    # Relationship to Author model (many-to-one)
    author = relationship("Author", back_populates="books")
    def __init__(self, title: str, author_id: str, year: int, num_pages: int, genre: str, book_id: str = None,
                 **kw: Any) -> None:
        super().__init__(**kw)
        self.book_id = book_id
        self.author_id = author_id
        self.title = title
        self.year = year
        self.num_pages = num_pages
        self.genre = genre


class Author(Base):

    """ავტორს უნდა ქონდეს შემდეგი ველები
        ID (primary key)
        სახელი
        გვარი
        დაბადების თარიღი
        დაბადების ადგილი
    """
    __tablename__ = 'authors'
    author_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_year = Column(Integer, nullable=False)
    birth_place = Column(String, nullable=False)

    # Relationship to Book model (one-to-many)
    books = relationship("Book", back_populates="author")

    def __init__(self, name: str, last_name: str, birth_year: int, birth_place: str, author_id: str = None,
                 **kw: Any) -> None:
        super().__init__(**kw)
        self.author_id = author_id
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.birth_place = birth_place


