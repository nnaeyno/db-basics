import sqlite3

from objects import Book, Author


class DatabaseManager:
    def __init__(self, db_name: str = 'library.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS authors (
            author_id TEXT PRIMARY KEY,
            name TEXT,
            last_name TEXT,
            birth_year INT,
            birth_place TEXT)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
            book_id TEXT PRIMARY KEY,
            title TEXT,
            author_id TEXT,
            year INT,
            num_pages INT,
            genre TEXT,
            FOREIGN KEY(author_id) REFERENCES authors(author_id))''')
        self.connection.commit()

    def close(self):
        self.connection.close()


class BookRepository:
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager

    def add_book(self, book: Book):
        query = '''INSERT INTO books (book_id, title, author_id, year, num_pages, genre)
                   VALUES (?, ?, ?, ?, ?, ?)'''
        self.db_manager.cursor.execute(query,
            (book.book_id, book.title, book.author_id, book.year, book.num_pages, book.genre))
        self.db_manager.connection.commit()

    def get_books_by_author(self, author_id: str):
        query = '''SELECT * FROM books WHERE author_id = ?'''
        self.db_manager.cursor.execute(query, (author_id,))
        return self.db_manager.cursor.fetchall()

    def get_book_by_id(self, book_id: str):
        query = '''SELECT * FROM books WHERE book_id = ?'''
        self.db_manager.cursor.execute(query, (book_id,))
        return self.db_manager.cursor.fetchone()

    def get_all_books(self):
        query = '''SELECT * FROM books'''
        self.db_manager.cursor.execute(query)
        return self.db_manager.cursor.fetchall()


class AuthorRepository:
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager

    def add_author(self, author: Author):
        query = '''INSERT INTO authors (author_id, name, last_name, birth_year, birth_place)
                   VALUES (?, ?, ?, ?, ?)'''
        self.db_manager.cursor.execute(query,
            (author.author_id, author.name, author.last_name, author.birth_year, author.birth_place))
        self.db_manager.connection.commit()

    def get_author_by_id(self, author_id: str):
        query = '''SELECT * FROM authors WHERE author_id = ?'''
        self.db_manager.cursor.execute(query, (author_id,))
        return self.db_manager.cursor.fetchone()

    def get_all_authors(self):
        query = '''SELECT * FROM authors'''
        self.db_manager.cursor.execute(query)
        return self.db_manager.cursor.fetchall()
