class Book:
    def __init__(self, id_:int, name: str, pages: int):

        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц не может быть отрицательным")
        if not isinstance(id_, int):
            raise TypeError("Идентификатор должен быть целым числом")
        if id_ <= 0:
            raise ValueError("Идентификатор не может быть отрицательным")
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f"Книга {self.name}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id_={self.id_}, name=\"{self.name}\", pages={self.pages}"

class Library:
    def __init__(self, books: dict = {}):
        if not isinstance(books, dict):
            raise TypeError("Список книг должен быть словарём")
        self.books = books

    def get_next_book_id(self) -> int:
        if len(self.books) == 0:
            return 1
        else:
            return list(self.books.items())[-1][0]+1

    def get_index_by_book_id(self, id_:int) -> int:
        if not isinstance(id_, int):
            raise TypeError("Идентификатор должен быть целым числом")
        if id_ <= 0:
            raise ValueError("Идентификатор не может быть отрицательным")
        return self.books[id_]

