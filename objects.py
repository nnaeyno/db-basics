class Book:
    """წიგნის უნდა ქონდეს შემდეგი ველები:
        ID (primary key)
        დასახელება
        კატეგორიის დასახელება
        გვერდების რაოდენობა
        გამოცემის თარიღი
        ავტორის აიდი
    """

    def __init__(self, title: str, author_id: str, year: int, num_pages: int, genre: str, book_id: str = None) -> None:
        self.book_id = book_id
        self.author_id = author_id
        self.title = title
        self.year = year
        self.num_pages = num_pages
        self.genre = genre


class Author:

    """ავტორს უნდა ქონდეს შემდეგი ველები
        ID (primary key)
        სახელი
        გვარი
        დაბადების თარიღი
        დაბადების ადგილი
    """

    def __init__(self, name: str, last_name: str, birth_year: int, birth_place: str, author_id: str = None) -> None:
        self.author_id = author_id
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.birth_place = birth_place


