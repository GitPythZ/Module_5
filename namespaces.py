# import this # Встроенная область видимости
# def square(x):
#     a = x ** 2 # Локальная область видимости
#     print(locals())
#     return a
# def square(x):
#     a = x ** 2
#     print(globals())
#     return a
import math


# def square(x): # Объемлюющая функция для even
#     d = x ** 2
#     def even(x):
#         # nonlocal - если я хочу взять значение из объемлющей области, то пишу nonlocal d (имя переменной)
#         d = x * 2
#         if d % 2 == 0:
#             print("Chet")
#         else:
#             print("non-Chet")
#     even(x)
#     return d
#
#
# a = 5 # Глобальная область видимости
# b = square(4)
# print(a)
# print(b)

# Локальная обл ==> Всеобъемлюющая ==> Глобальная ==> Встроенная
# print(math.sqrt(a))
# print(globals()) # возвращает список глобальных переменных/имен в виде словарика
# Если я напишу from math import * (импортирую все элементы из библиотеки, то все они станут "глобальными")
# Тогда я смогу обращаться без math - print(square(a).


# def s():
#     #local
#     a, b, c = 1, 2, 4
#     w = "HELLO"
#     print(a, b, c, w) # могу обратиться к глобальной переменной.
#
#
# w = "Hello" #global
# s()
# print(w)
# w = "Hello" #global если я вызову пфункцию до определения данной переменной, то я не смогу вывести ее на экран, будет ошибка.
# Так как поиск переменных идет из локальной области в глобальную, то он находит w в самой функции и выводит HELLO
# сама переменная w в глобальном пространстве не изменилась, как бы существует две разные переменные w в глобальной и
# локальной области. Это можно доказать методом id - вернет разные коды переменных.


# def local():
#     a = 11
#     b = 22
#     c = 33
#     print(a, b, c, "local")
#
#
# a = 100
# b = 200
# c = 300
# local()
# print(a, b, c, "global")
#
#
# def local(a, b, c):
#     a = 11
#     print(a, b, c, "local")
#
#
# a = [1, 2, 3, 4, 5, 6]
# b = 200
# c = 300
# local(a, b, c)
# print(a, b, c, "global")
#
#
# def local(a, b, c):
#     a[1] = 100
#     print(a, b, c, "local")
#
#
# a = [1, 2, 3, 4, 5, 6]
# b = 200
# c = 300
# local(a, b, c)
# print(a, b, c, "global")


# def primer_global():
#     global a
#     a = 30
#
#
# a = [1, 2, 3, 4, 5]
# primer_global()
#
# print(a, "global")
#
#
# def q():
#     primer_global()


# def s():
#     #enclosing - объемлющая
#     abs = 200
#     def q():
#         # local
#         abs = "hello"
#         print(abs, "q")
#     q()
#     print(abs, "s")
#
#
# #global
# abs = [1, 2, 3]
# s()

# Local - Локальная
# Enclosing Объемлющая
# Global Глобальная
# Built in Встроенная
# Python ищет переменные по принципу LEGB (Local, Enclosing, Global, Built in)

# Вложенные функции
g = "gray" # global
def colors():
    y = "yellow" # enclosing
    g = "green" # enclosing

    def print_red():
        nonlocal y
        r = "red"
        print(r, y, g)
        y = "was changed"

    def print_blue():
        b = "blue"
        print(b, y, g)

    print_red()
    print_blue()


colors()

g = "gray" # global


def colors(param="r"):
    y = "yellow" # enclosing
    g = "green" # enclosing

    def print_red():
        r = "red"
        print(r)

    def print_blue():
        b = "blue"
        print(b)
    if param == "r":
        print_red()
    elif param == "b":
        print_blue()
    else:
        print("I dont know this colors")


colors("b")