from faker import Faker
import random

from database import DatabaseManager
from library_statistics import LibraryService
from objects import Author, Book

fake = Faker()


def generate_authors(num_authors: int):
    authors = []
    for _ in range(num_authors):
        author_id = fake.uuid4()
        name = fake.first_name()
        last_name = fake.last_name()
        birth_year = random.randint(1850, 1990)
        birth_place = fake.city()
        authors.append(Author(name, last_name, birth_year, birth_place, author_id))
    return authors


def generate_books(authors: list, num_books: int):
    genres = ["Science Fiction", "Fantasy", "Dystopian", "Mystery", "Romance", "Non-fiction", "Thriller", "Historical"]
    books = []
    for _ in range(num_books):
        title = fake.sentence(nb_words=3)
        author = random.choice(authors)
        year = random.randint(1900, 2023)
        num_pages = random.randint(100, 1500)
        genre = random.choice(genres)
        book_id = fake.uuid4()
        books.append(Book(title, author.author_id, year, num_pages, genre, book_id))
    return books


def store_authors_books(library_service, authors, books):
    for author in authors:
        library_service.add_author(author.name, author.last_name, author.birth_year, author.birth_place,
                                   author.author_id)

    for book in books:
        library_service.add_book(book.title, book.author_id, book.year, book.num_pages, book.genre, book.book_id)


def generate_and_store_data(db_manager: DatabaseManager, library_service: LibraryService):
    # Generate 500 authors and 1000 books
    authors = generate_authors(500)
    books = generate_books(authors, 1000)

    # Store authors and books in the database
    store_authors_books(library_service, authors, books)
    print(f"Stored {len(authors)} authors and {len(books)} books in the database.")

