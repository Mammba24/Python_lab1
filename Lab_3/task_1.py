class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str) -> None:
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс бумажной книги, наследуется от Book."""

    def __init__(self, name: str, author: str, pages: int) -> None:
        super().__init__(name, author)
        self.pages = pages  # Используем сеттер

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    """Класс аудиокниги, наследуется от Book."""

    def __init__(self, name: str, author: str, duration: float) -> None:
        super().__init__(name, author)
        self.duration = duration  # Используем сеттер

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Длительность аудиокниги должна быть положительным числом")
        self._duration = value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"


# Пример использования:
if __name__ == "__main__":
    paper_book = PaperBook("Война и мир", "Лев Толстой", 1225)
    audio_book = AudioBook("1984", "Джордж Оруэлл", 11.5)

    print(paper_book)  # Проверяем __str__
    print(audio_book)  # Проверяем __str__

    print(repr(paper_book))  # Проверяем __repr__
    print(repr(audio_book))  # Проверяем __repr__
