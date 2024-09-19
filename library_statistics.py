from database import BookRepository, AuthorRepository
from objects import Author, Book


class LibraryService:
    def __init__(self, book_repository: BookRepository, author_repository: AuthorRepository):
        self.book_repository = book_repository
        self.author_repository = author_repository

    def add_author(self, name: str, last_name: str, birth_year: int, birth_place: str, author_id: str):
        author = Author(name, last_name, birth_year, birth_place, author_id)
        self.author_repository.add_author(author)

    def add_book(self, title: str, author_id: str, year: int, num_pages: int, genre: str, book_id: str):
        if self.author_repository.get_author_by_id(author_id) is None:
            raise ValueError(f"Author with id {author_id} does not exist.")

        book = Book(title, author_id, year, num_pages, genre, book_id)
        self.book_repository.add_book(book)

    def get_books_by_author(self, author_id: str):
        return self.book_repository.get_books_by_author(author_id)

    def get_all_books(self):
        return self.book_repository.get_all_books()

    def get_all_authors(self):
        return self.author_repository.get_all_authors()
