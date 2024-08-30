class House:
    def __init__(self, name, number_of_flours):  # определил метод/конструктор __init__
        self.name = name
        self.number_of_flours = number_of_flours

    def __len__(self):
        return self.number_of_flours

    def __eq__(self, other):
        if not isinstance(other, (int, House)):
            raise ArithmeticError("Содержит тип int или House")

        return self.number_of_flours == other.number_of_flours

    def __lt__(self, other):
        if not isinstance(other, (bool, House)):
            raise ArithmeticError("Содержит тип int или House")

        return self.number_of_flours < other.number_of_flours

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

    def __add__(self, value):
        if not isinstance(value, (int, House)):
            raise ArithmeticError("Значение этажей должно иметь тип int или объектом House")
        self.number_of_flours = self.number_of_flours + value
        return f"Название: {self.name}, количество этажей: {self.number_of_flours}"

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        if not isinstance(other, (int, House)):
            raise ArithmeticError("Содержит тип int или House")

        flour = other if isinstance(other, int) else other.number_of_flours
        self.number_of_flours += flour
        return self


h1 = House("ЖК Эльбрус", 10)
h2 = House("ЖК Акация", 20)
print(h1)
print(h2)
print(h1 == h2)
print(h1.__add__(10))
print(h1 == h2)
h1 += 10
print(h1)
h2 = 10 + h2
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
