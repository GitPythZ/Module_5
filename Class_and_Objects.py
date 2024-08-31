# class Human:
#     def __init__(self, name):
#         self.name = name
#
#
# max = Human("Биба")
# den = Human("Боба")
# print(type(den))
# print(max == den)
# print(max is den)
# print(id(max), id(den))
# print(max.name)
# print(den.name)

class Human:

    head = True
    def __init__(self, name, age): # __init__ - это инициализатор, конструктор
        self.name = name # атрибуты
        self.age = age
        self.say_info()

    def say_info(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age}")

    def birthday(self):
        self.age += 1
        print(f"У {self.name} день рождения, ему теперь {self.age}")

    def __len__(self):
        return self.age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __bool__(self):
        return bool(self.name)

    def __str__(self):
        return f"{self.name}"

    def __del__(self):
        print(f"{self.name} ушел")


max = Human("Биба", 22)
den = Human("Боба", 33)
print(den.name, den.age)
# den.say_info()
max.birthday()
# print(len(den))
# print(den < max)
# print(den > max)
# print(den == max)
# print(den)
print(Human.head)