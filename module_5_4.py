class Example:
    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        return object.__new__(cls)

    def __init__(self, first, second, third):
        print(first)
        print(second)
        print(third)


ex = Example("data", second=25, third=3.14)


class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        house = super().__new__(cls)
        cls.houses_history.append(args[0])
        return house

    def __del__(self):
        self.houses_history.remove(self.name)
        print(f"{self.name} снесено, но он останется в истории")

    def __init__(self, name, number_of_flours):  # определил метод/конструктор __init__
        self.name = name
        self.number_of_flours = number_of_flours

    def __len__(self):
        return self.number_of_flours

    def go_to(self, new_flour:int): #
        if new_flour < 1 or new_flour > self.number_of_flours:
            print("Такого этажа не существует")
            return
        for i in range(1, new_flour + 1):
            print(i)

    def __add__(self, other):
        other_value = self.__verify_data(other)
        self.number_of_flours += other_value
        return self

    def __radd__(self, other):
        other_value = self.__verify_data(other)
        return self + other_value

    def __iadd__(self, other):
        other_value = self.__verify_data(other)
        self.number_of_flours += other
        return self

    def __eq__(self, other):
        other_value = self.__verify_data(other)
        return self.number_of_flours == other_value

    def __lt__(self, other):
        other_value = self.__verify_data(other)
        return self.number_of_flours < other_value

    def __le__(self, other):
        other_value = self.__verify_data(other)
        return self.number_of_flours <= other_value

    def __gt__(self, other):
        other_value = self.__verify_data(other)
        return self.number_of_flours > other_value

    def __ge__(self, other):
        other_value = self.__verify_data(other)
        return self.number_of_flours >= other_value

    def __ne__(self, other):
        other_value = self.__verify_data(other)
        return self.number_of_flours != other_value

    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_flours}"

    @classmethod # хотел сократить код, но что-то пошло не так
    def __verify_data(cls, other):
        if not isinstance(other, (int, House)):
            raise ArithmeticError("Значение должно быть типа int или объектом House")
        return other if isinstance(other, int) else other.number_of_flours


h1 = House("ЖК Эльбрус", 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
# Удаление объектов
del h2
del h3
print(House.houses_history)
