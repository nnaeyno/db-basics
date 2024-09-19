from database import DatabaseManager, AuthorRepository, BookRepository
from library_statistics import LibraryService


def run_library_application():
    # Dependency Injection
    db_manager = DatabaseManager()
    author_repo = AuthorRepository(db_manager)
    book_repo = BookRepository(db_manager)
    library_service = LibraryService(book_repo, author_repo)

    try:
        # Add authors
        library_service.add_author("George", "Orwell", 1903, "India", "1")
        # library_service.add_author("Aldous", "Huxley", 1894, "England", "2")
        #
        # # Add books
        library_service.add_book("1984", "1", 1949, 328, "Dystopian", "101")
        # library_service.add_book("Brave New World", "2", 1932, 288, "Dystopian", "102")

        # Fetch and display data
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
