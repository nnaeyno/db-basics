from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from database_interfaces import IAuthorRepository, IBookRepository, IDatabaseManager
from objects import Author, Base, Book


class SQLAlchemyDatabaseManager(IDatabaseManager):
    def __init__(self, db_name: str = "library.db"):
        self.engine = create_engine(f"sqlite:///{db_name}")
        self._create_tables()

    def _create_tables(self):
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_connection(self):
        return self.session


class AlchemyBookRepository(IBookRepository):
    def __init__(self, db_manager: IDatabaseManager):
        self.db_manager = db_manager

    def add_book(self, book: Book):
        if isinstance(book, Book):
            try:
                self.db_manager.get_connection().add(book)
                self.db_manager.get_connection().commit()
            except Exception as e:
                self.db_manager.get_connection().rollback()
                print(f"Error occurred while adding the book: {e}")
        else:
            raise ValueError("Input is not a Book instance.")

    def get_books_by_author(self, author_id):
        pass

    def get_all_books(self):
        pass

    def find_most_pages(self):
        book = (
            self.db_manager.get_connection()
            .query(Book)
            .order_by(Book.num_pages.desc())
            .first()
        )
        return book

    def average_pages(self):
        avg_pages = (
            self.db_manager.get_connection()
            .query(Book)
            .with_entities(func.avg(Book.num_pages))
            .scalar()
        )
        return avg_pages


class AlchemyAuthorRepository(IAuthorRepository):

    def __init__(self, db_manager: SQLAlchemyDatabaseManager):
        self.db_manager = db_manager

    def add_author(self, author: Author):
        if isinstance(author, Author):
            try:
                self.db_manager.session.add(author)
                self.db_manager.session.commit()
            except Exception as e:
                self.db_manager.session.rollback()
                print(f"Error occurred while adding the author: {e}")
        else:
            raise ValueError("Input is not an Author instance.")

    def get_author_by_id(self, author_id: str):
        author = (
            self.db_manager.session.query(Author).filter_by(author_id=author_id).first()
        )
        return author

    def get_all_authors(self):
        pass

    def get_youngest_author(self):
        author = (
            self.db_manager.session.query(Author)
            .order_by(Author.birth_year.desc())
            .first()
        )
        return author

    def no_books(self):
        authors = (
            self.db_manager.session.query(Author)
            .outerjoin(Book)
            .filter(Book.book_id.is_(None))
            .all()
        )
        return authors

    def author_with_num_books(self, num_books: int, num_authors: int):
        authors = (
            self.db_manager.session.query(
                Author, func.count(Book.book_id).label("book_count")
            )
            .join(Book, Author.author_id == Book.author_id)
            .group_by(Author.author_id)
            .having(func.count(Book.book_id) > num_books)
            .order_by(func.count(Book.book_id).desc())
            .limit(num_authors)
            .all()
        )
        return authors
