# Задача "Developer - не только разработчик":
class House:
    def __init__(self, name, number_of_flours): # определил метод/конструктор __init__
        self.name = name
        self.number_of_flours = number_of_flours

    def go_to(self, new_flour:int): #
        if new_flour < 1 or new_flour > self.number_of_flours:
            print("Такого этажа не существует")
            return
        for i in range(1, new_flour + 1):
            print(i)


h1 = House("ЖК Горький", 18)
h2 = House("Домик в деревне", 2)
h1.go_to(5)
h2.go_to(10)