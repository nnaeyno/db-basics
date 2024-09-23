class IDatabaseManager:
    def _create_tables(self):
        pass

    def close(self):
        pass


class IAuthorRepository:

    def add_author(self, author):
        pass

    def get_author_by_id(self, author_id):
        pass

    def get_all_authors(self):
        pass

    def get_youngest_author(self):
        pass

    def no_books(self):
        pass

    def author_with_num_books(self, num_books, num_authors):
        pass


class IBookRepository:

    def add_book(self, book):
        pass

    def get_books_by_author(self, author_id):
        pass

    def get_all_books(self):
        pass

    def find_most_pages(self):
        pass

    def average_pages(self):
        pass
