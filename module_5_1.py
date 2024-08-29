# Задача "Developer - не только разработчик":
class House:
    def __init__(self, name, number_of_flours): # определил метод/конструктор __init__
        self.name = name
        self.number_of_flours = number_of_flours

    def go_to(new_flour, i=None):
        while i < new_flour:
            print(i)
        if i > new_flour.number_of_flours or i < 1:
            print("Такого этажа не существует")


h1 = House("ЖК Горький", 18)
h2 = House("Домик в деревне", 2)
h1.go_to(5)
h2.go_to(10)