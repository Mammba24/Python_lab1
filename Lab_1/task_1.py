# TODO Написать 3 класса с документацией и аннотацией типов
from random import random
from tokenize import String


class Table:
    def __init__(self, square, height):
        if not isinstance(square, (int, float)):
            raise TypeError
        if not square > 0:
            raise ValueError
        self.square = square  # площадь поверхности стола

        if not isinstance(height, (int, float)):
            raise TypeError
        if height < 0:
            raise ValueError
        self.height = height # высота стола

    def sit_down_at_the_table (self):
        print("You sat down at the table")

    def get_up_from_the_table (self):
        print("You got up from the table")

class Tree:
    def __init__(self, diameter, height):
        if not isinstance(diameter, (int, float)):
            raise TypeError
        if not diameter > 0:
            raise ValueError
        self.diameter = diameter  # диаметер ствола дерева

        if not isinstance(height, (int, float)):
            raise TypeError
        if height < 0:
            raise ValueError
        self.height = height # высота дерева

    def water_the_tree(self):
        print("You watered the tree")

    def look_for_an_apple(self):
        probability = random()
        if(probability < 0.5):
            print("You didn't find the apple")
        else:
            print("You found the apple")

class Car:
    def __init__(self, make, max_speed):
        if not isinstance(make, str):
            raise TypeError
        if not make == "":
            raise ValueError
        self.make = make  # площадь поверхности стола

        if not isinstance(max_speed, (int, float)):
            raise TypeError
        if max_speed < 0:
            raise ValueError
        self.max_speed = max_speed # высота стола

    def start(self):
        print("The car started moving")

    def stop(self):
        print("The car stopped")

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
    pass
