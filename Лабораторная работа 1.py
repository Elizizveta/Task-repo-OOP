import random
import doctest

class Xmas_tree:
    def __init__(self, tree_type: str, balls_count: int, height: float, garland: bool):
        """
        Создание и подготовка к работе класса Новогодее Дерево

        tree_type: тип дерева (Ель, сосна, пихта, берёза, стул)
        balls_count: подсчёт количества шаров на дереве
        height: высота дерева
        garland: наличие гирлянды
        """
        self.tree_type = tree_type
        self.balls_count = balls_count
        self.height = height
        self.garland = garland
        if not isinstance(tree_type, str):
            raise TypeError("Тип дерева должен быть типа str")
        if not isinstance(balls_count, int):
            raise TypeError("Количество шаров должно быть целым числом")
        if not isinstance(height, (int,float)):
            raise TypeError("Высота дерева должна быть типа int или float")
        if not isinstance(garland, bool):
            raise TypeError("Наличие гирлянды должно быть типа bool")
        if balls_count < 0:
            raise ValueError("Количество шаров не может быть отрицательным")
        if height < 0:
            raise ValueError("Высота не может быть отрицательна")

    def add_balls(self, num: int) -> None:
        #Добавление шаров на дерево
        #Вводится количество добавляемых шаров
        if not isinstance(num, int):
            raise TypeError("Добавляемое количество шаров должно быть типа int")
        if num < 0:
            raise ValueError("Добавляемое количество шаров не может быть отрицательным")
        self.balls_count += num

    def remove_balls(self, num: int) -> None:
        #Снятие шаров с дерева
        #Вводится количество снимаемых шаров
        if not isinstance(num, int):
            raise TypeError("Снимаемое количество шаров должно быть типа int")
        if num < 0:
            raise ValueError("Снимаемое количество шаров не может быть отрицательным")
        self.balls_count -= num
        if self.balls_count < 0:
            raise ValueError("Количество шаров не может быть отрицательным")

    def grow(self) -> None:
        #Рост дерева
        #Дерево вырасатет на случайную величину в пределах от нуля до своей высоты
        self.height += random.random()*self.height
            

    if __name__ == "__main__":
        doctest.testmod()

class Hair:
    def __init__(self, color: str, length: float, is_curly: bool):
        """
        Создание и подготовка к работе класса Волосы

        color: цвет волос
        length: длина волос
        is_curly: кудрявые или нет
        """
        self.color = color
        self.length = length
        self.is_curly = is_curly
        
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")
        if not isinstance(length, (int, float)):
            raise TypeError("Длина должна быть типа float")
        if not isinstance(is_curly, bool):
            raise TypeError("Кудрявость должна быть типа bool")
        if length < 0:
            raise ValueError("Длина волос не может быть отрицательной")

    def cut(self, cut_len: float) -> None:
        #Функция укораичвания волос
        #На вход получает срезаемую длинну
        if not isinstance(cut_len, (int, float)):
            raise TypeError("Длина должна быть типа float")
        if cut_len < 0:
            raise ValueError("Невозможно отрезать отрицательную длинну")
        self.length -= cut_len
        if self.length < 0:
            raise ValueError("Длина волос не может быть отрицательной")

    def straighten(self) -> None:
        #Метод выпрямляющий кудрявые волосы
        if self.is_curly == True:
            self.is_curly = False
        else:
            raise ValueError("Невозможно выпрямить прямые волосы")

    def curl(self) -> None:
        #Метод завивающий прямые волосы
        if self.is_curly == False:
            self.is_curly = True
        else:
            raise ValueError("Невозможно завить кудрявые волосы")

class Notebook:
    def __init__(self, pages: int, content: str, size: str):
        """
        Создание и подготовка к работе класса Тетрадь

        pages: количество страниц
        content: содержимое тетради 
        size: формат тетради
        """
        self.pages = pages
        self.content = content
        self.size = size

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")\
        if not isinstance(content, str):
            raise TypeError("Содержимое должно быть типа str")
        if not isinstance(size, str):
            raise TypeError("Формат должен быть типа str")
        if pages < 0:
            raise ValueError("Количество страниц не может быть отрицательным")

    def pull_pages(self, num: int) -> None:
        #Метод вырывания страниц из тетради
        #Уменьшает количество страниц тетради на величину равную аргументу num
        if not isinstance(num, int):
            raise TypeError("Количество вырываемых страниц должно быть целым числом")
        if num < 0:
            raise ValueError("Количество вырываемых страниц должно быть положительно")
        self.pages -= num
        if self.pages < 0:
            raise ValueError("Колчиество страниц не может быть отрицательным")

    def write(self, text: str) -> None:
        #Метод записи текста в тетрадь
        #Добавляет в содержимое тетради содержимое переменной text

        if not isinstance(text, str):
            raise TypeError("Текст должен быть строкой")
        self.content += text

    def read_some(self, num: int) -> None:
        #Функция чтения из тетради введённого количества символов
        if not isinstance(num, int):
            raise TypeError("Количество символов должно быть типа int")
        if num <= 0:
            raise ValueError("Невозможно прочитать неположительное количество символов")
        if len(self.content) < num:
            raise ValueError("В тетради меньше символов")

        print(self.content[:num-1])

    def read_all(self) -> None:
        #Метод, печатающий содержимое тетради
        print(self.content)
