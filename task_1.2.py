from random import random


class Table:
    """
    Класс, представляющий стол.
    """

    def __init__(self, square: float, height: float) -> None:
        """
        Инициализация стола.

        :param square: Площадь поверхности стола (должна быть > 0).
        :param height: Высота стола (должна быть >= 0).
        :raises ValueError: Если параметры не удовлетворяют ограничениям.
        """
        if not isinstance(square, (int, float)) or square <= 0:
            raise ValueError("Площадь стола должна быть положительным числом.")
        if not isinstance(height, (int, float)) or height < 0:
            raise ValueError("Высота стола должна быть неотрицательным числом.")

        self.square = square
        self.height = height

    def sit_down_at_the_table(self) -> None:
        """
        Сесть за стол.

        >>> table = Table(10, 1)
        >>> table.sit_down_at_the_table()
        You sat down at the table
        """
        print("You sat down at the table")

    def get_up_from_the_table(self) -> None:
        """
        Встать из-за стола.

        >>> table = Table(10, 1)
        >>> table.get_up_from_the_table()
        You got up from the table
        """
        print("You got up from the table")


class Tree:
    """
    Класс, представляющий дерево.
    """

    def __init__(self, diameter: float, height: float) -> None:
        """
        Инициализация дерева.

        :param diameter: Диаметр ствола дерева (должен быть > 0).
        :param height: Высота дерева (должна быть >= 0).
        :raises ValueError: Если параметры не удовлетворяют ограничениям.
        """
        if not isinstance(diameter, (int, float)) or diameter <= 0:
            raise ValueError("Диаметр дерева должен быть положительным числом.")
        if not isinstance(height, (int, float)) or height < 0:
            raise ValueError("Высота дерева должна быть неотрицательным числом.")

        self.diameter = diameter
        self.height = height

    def water_the_tree(self) -> None:
        """
        Полить дерево.

        >>> tree = Tree(0.5, 5)
        >>> tree.water_the_tree()
        You watered the tree
        """
        print("You watered the tree")

    def look_for_an_apple(self) -> str:
        """
        Искать яблоко на дереве.

        >>> tree = Tree(0.5, 5)
        >>> result = tree.look_for_an_apple()
        >>> result in ["You didn't find the apple", "You found the apple"]
        True
        """
        return "You found the apple" if random() >= 0.5 else "You didn't find the apple"


class Car:
    """
    Класс, представляющий машину.
    """

    def __init__(self, make: str, max_speed: float) -> None:
        """
        Инициализация машины.

        :param make: Марка машины (не должна быть пустой).
        :param max_speed: Максимальная скорость (должна быть >= 0).
        :raises ValueError: Если параметры не удовлетворяют ограничениям.
        """
        if not isinstance(make, str) or not make:
            raise ValueError("Марка машины должна быть непустой строкой.")
        if not isinstance(max_speed, (int, float)) or max_speed < 0:
            raise ValueError("Максимальная скорость должна быть неотрицательным числом.")

        self.make = make
        self.max_speed = max_speed

    def start(self) -> None:
        """
        Начать движение.

        >>> car = Car("Toyota", 200)
        >>> car.start()
        The car started moving
        """
        print("The car started moving")

    def stop(self) -> None:
        """
        Остановиться.

        >>> car = Car("Toyota", 200)
        >>> car.stop()
        The car stopped
        """
        print("The car stopped")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
