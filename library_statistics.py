from sqlite_db import BookRepository, AuthorRepository
from database_interfaces import IAuthorRepository, IBookRepository
from objects import Author, Book

"""
განახორციელეთ შემდეგი მოქმედებები:
    იპოვეთ და დაბეჭდეთ ყველაზე მეტი გვერდების მქონე წიგნის ყველა ველი
    იპოვეთ და დაბეჭდეთ წიგნების საშუალო გვერდების რაოდენობა
    დაბეჭდეთ ყველაზე ახალგაზრდა ავტორი
    დაბეჭდეთ ისეთი ავტორები რომელსაც ჯერ წიგნი არ აქვს
"""


class LibraryService:
    def __init__(self, book_repository: IBookRepository, author_repository: IAuthorRepository):
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

    def get_most_pages(self) -> str:
        book = self.book_repository.find_most_pages()
        return (f"Book with most pages:\n       Book id: {book.book_id}, name: {book.title}, publishing year: {book.year}, "
                f"author_id: {book.author_id}, genre: {book.genre}, number of pages: {book.num_pages}")

    def get_average_pages(self) -> str:
        return f"Average number of pages:\n     {self.book_repository.average_pages()}"

    def get_youngest_author(self) -> str:
        result = self.author_repository.get_youngest_author()
        return f"Youngest Author:\n     {result.name} {result.last_name}"

    def author_with_no_books(self) -> str:
        result = self.author_repository.no_books()
        authors = f"Authors with no books:"
        for author in result:
            authors += f"\n     {author.name} {author.last_name}"
        return authors

    def author_with_num_books(self, num_books: int, num_authors: int) -> str:
        result = self.author_repository.author_with_num_books(num_books, num_authors)
        authors = f"{num_authors} Author(s) with more than {num_books} book(s):"
        for author in result:
            author, num_books = author
            authors += f"\n     {author.name} {author.last_name} with {num_books} book(s)"
        return authors

