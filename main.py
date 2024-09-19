from database import DatabaseManager, AuthorRepository, BookRepository
from library_statistics import LibraryService
from random_db import generate_and_store_data


def run_library_application():
    db_manager = DatabaseManager()
    author_repo = AuthorRepository(db_manager)
    book_repo = BookRepository(db_manager)
    library_service = LibraryService(book_repo, author_repo)
    generate_and_store_data(db_manager, library_service)

    try:

        all_books = library_service.get_all_books()
        for book in all_books:
            print(book)

        all_authors = library_service.get_all_authors()
        for author in all_authors:
            print(author)

    finally:
        db_manager.close()


if __name__ == '__main__':
    run_library_application()
