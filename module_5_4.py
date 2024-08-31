# class Example:
#     def __new__(cls, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         return object.__new__(cls)
#
#     def __init__(self, first, second, third):
#         print(first)
#         print(second)
#         print(third)
#
#
# ex = Example("data", second=25, third=3.14)


class House:
    houses_history = []

    def __new__(cls, houses_history=None, *args, **kwargs):
        print(args)
        print(kwargs)
        houses_history.append(args)
        return cls.houses_history

    def __init__(self, name, number_of_flours):  # определил метод/конструктор __init__
        self.name = name
        self.number_of_flours = number_of_flours

    def __len__(self):
        return self.number_of_flours

    def __add__(self, other):
        if not isinstance(other, (int, House)):
            raise ArithmeticError("Значение этажей должно иметь тип int или объектом House")
        self.number_of_flours = self.number_of_flours + other
        return self

    def __radd__(self, other):
        if not isinstance(other, (int, House)):
            raise TypeError("Правый операнд должен быть типом int или объектом House")
        return self + other

    def __iadd__(self, other):
        if not isinstance(other, (int, House)):
            raise TypeError("Правый операнд должен быть типом int или объектом House")
        self.number_of_flours += other
        return self

    def __eq__(self, other):
        if not isinstance(other, (int, House)):
            raise TypeError("Правый операнд должен быть типом int или объектом House")
        fl = other if isinstance(other, int) else other.number_of_flours
        return self.number_of_flours == fl

    def __le__(self, other):
        if not isinstance(other, (bool, House)):
            raise ArithmeticError("Содержит тип int или House")
        return self.number_of_flours <= other.number_of_flours

    def __gt__(self, other):
        if not isinstance(other, (bool, House)):
            raise ArithmeticError("Содержит тип int или House")
        return self.number_of_flours > other.number_of_flours

    def __ge__(self, other):
        if not isinstance(other, (bool, House)):
            raise ArithmeticError("Содержит тип int или House")
        return self.number_of_flours >= other.number_of_flours

    def __ne__(self, other):
        if not isinstance(other, (bool, House)):
            raise ArithmeticError("Содержит тип int или House")
        return self.number_of_flours != other.number_of_flours

    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_flours}"

    def __del__(self):
        print(f"{self.name} снесен, но останется в истории")


h1 = House("ЖК Эльбрус", 10)
print(House.houses_history)