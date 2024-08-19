import this # Встроенная область видимости
# def square(x):
#     a = x ** 2 # Локальная область видимости
#     print(locals())
#     return a
# def square(x):
#     a = x ** 2
#     print(globals())
#     return a
import math


def square(x): # Объемлюющая функция для even
    d = x ** 2
    def even(x):
        # nonlocal - если я хочу взять значение из объемлющей области, то пишу nonlocal d (имя переменной)
        d = x * 2
        if d % 2 == 0:
            print("Chet")
        else:
            print("non-Chet")
    even(x)
    return d


a = 5 # Глобальная область видимости
b = square(4)
print(a)
print(b)

# Локальная обл ==> Всеобъемлюющая ==> Глобальная ==> Встроенная
# print(math.sqrt(a))
# print(globals()) # возвращает список глобальных переменных/имен в виде словарика
# Если я напишу from math import * (импортирую все элементы из библиотеки, то все они станут "глобальными")
# Тогда я смогу обращаться без math - print(square(a).



