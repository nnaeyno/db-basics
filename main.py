from database import DatabaseManager, AuthorRepository, BookRepository
from library_statistics import LibraryService
from random_db import Generate_DB

NUM_BOOKS = 1000
NUM_AUTHORS = 500
INITIALIZE = True


def run_library_application():
    db_manager = DatabaseManager()
    author_repo = AuthorRepository(db_manager)
    book_repo = BookRepository(db_manager)
    library_service = LibraryService(book_repo, author_repo)
    db_generator = Generate_DB(library_service)
    if INITIALIZE:
        db_generator.generate_and_store_data(num_books=NUM_BOOKS, num_authors=NUM_AUTHORS)
    try:
        print(library_service.get_youngest_author())
        print(library_service.author_with_no_books())
        print(library_service.get_average_pages())
        print(library_service.get_most_pages())
        print(library_service.author_with_num_books(3, 5))

    finally:
        db_manager.close()


if __name__ == '__main__':
    run_library_application()
