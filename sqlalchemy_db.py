from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

from database_interfaces import IDatabaseManager, IBookRepository, IAuthorRepository
from objects import Author, Base, Book


class SQLAlchemyDatabaseManager(IDatabaseManager):
    def __init__(self, db_name: str = 'library.db'):
        # Set up the SQLite database
        self.engine = create_engine(f'sqlite:///{db_name}')
        Base.metadata.create_all(self.engine)

        # Create a session
        Session = sessionmaker(bind=self.engine)
        self.session = Session()


class AlchemyBookRepository(IBookRepository):
    def __init__(self, db_manager: SQLAlchemyDatabaseManager):
        self.db_manager = db_manager

    def add_book(self, book):
        if isinstance(book, Book):
            try:
                self.db_manager.session.add(book)
                self.db_manager.session.commit()
            except Exception as e:
                self.db_manager.session.rollback()
                print(f"Error occurred while adding the book: {e}")
        else:
            raise ValueError("Input is not a Book instance.")

    def get_books_by_author(self, author_id):
        pass

    def get_all_books(self):
        pass

    def find_most_pages(self):
        book = self.db_manager.session.query(Book).order_by(Book.num_pages.desc()).first()
        return book

    def average_pages(self):
        avg_pages = self.db_manager.session.query(Book).with_entities(func.avg(Book.num_pages)).scalar()
        return avg_pages


class AlchemyAuthorRepository(IAuthorRepository):

    def __init__(self, db_manager: SQLAlchemyDatabaseManager):
        self.db_manager = db_manager

    def add_author(self, author):
        if isinstance(author, Author):
            try:
                self.db_manager.session.add(author)
                self.db_manager.session.commit()
            except Exception as e:
                self.db_manager.session.rollback()
                print(f"Error occurred while adding the author: {e}")
        else:
            raise ValueError("Input is not an Author instance.")

    def get_author_by_id(self, author_id):
        author = self.db_manager.session.query(Author).filter_by(author_id=author_id).first()
        return author

    def get_all_authors(self):
        pass

    def get_youngest_author(self):
        author = self.db_manager.session.query(Author).order_by(Author.birth_year.desc()).first()
        return author

    def no_books(self):
        authors = self.db_manager.session.query(Author).outerjoin(Book).filter(Book.book_id.is_(None)).all()
        return authors

    def author_with_num_books(self, num_books: int, num_authors: int):
        authors = (
            self.db_manager.session.query(Author, func.count(Book.book_id).label('book_count'))
            .join(Book, Author.author_id == Book.author_id)
            .group_by(Author.author_id)
            .having(func.count(Book.book_id) > num_books)
            .order_by(func.count(Book.book_id).desc())
            .limit(num_authors)
            .all()
        )
        return authors
