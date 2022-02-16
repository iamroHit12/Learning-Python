from turtle import color
from pyparsing import col


class Car:
    def __init__(self,name,color):
        self.__name = name
        self.__color = color

    def set_name(self,name):
        self.__name = name

    def set_color(self,color):
        self.__color = color

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

car1 = Car("honda","blue")
car1.set_color("red")
car1.set_name("hero")
print(car1.get_name())
print(car1.get_color())