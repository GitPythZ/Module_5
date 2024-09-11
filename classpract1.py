class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль.
    Требования к паролю: минимум 8 символов, наличие хотя бы 1 заглавной буквы, наличие хотя бы 1 спец. символа,
    наличие хотя бы 1 цифры;
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

    # проверка пароля
    # def has_uppercase(self, password):
    #     for i in password:
    #         if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
    #             return True
    #     return False
    # def has_lowercase(self, password):
    #     for i in password:
    #         if i in "abcdefghijklmnopqrstuvwxyzабвгдежзийклмнопрстуфхцчшщъыьэюя":
    #             return True
    #     return False
    # def has_digit(self, password):
    #     for i in password:
    #         if i in "1234567890":
    #             return True
    #     return False
    # def has_special_symbol(self, password):
    #     for i in password:
    #         if i in "@_$!%*#?&":
    #             return True
    #     return False
    # def verify_password(self, password):
    #     # Длина пароля содержит от 8 символов
    #     if len(password) < 8:
    #         return False
    #     # Содержит хотя бы один знак в верхнем регистре
    #     if not self.has_uppercase(password):
    #         return False
    #     # Содержит хотя бы один знак в нижнем регистре
    #     if not self.has_lowercase(password):
    #         return False
    #     # Содержит хотя бы одну цифру
    #     if not self.has_digit(password):
    #         return False
    #     # Содержит хотя бы один спец.символ
    #     if not self.has_special_symbol(password):
    #         return False
    #     # Если пароль соответствует требованиям надежности, то функция verify_password вернет True
    #     return True


if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input("Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n"))
        if choice == 1:
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f"Вход выполнен {login}")
                    break
                else:
                    print("Вы ввели неверный пароль")
            else:
                print("Пользователь не найден")
        if choice == 2:
            user = User(input("Введите логин: "), password := input("Введите пароль: "),
                        password2 := input("Повторите пароль: "))
            if password != password2:
                print("Пароли не совпадают, попробуйте ещё раз")
                continue
            database.add_user(user.username, user.password)
        print(database.data)



    # while True:
    #     choice = input("Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n")
    #     if choice == 1:
    #         login = input("Введите логин: ")
    #         password = input("Введите пароль: ")
    #         if login in database.data:
    #             if password == database.data[login]:
    #                 print(f"Вход выполнен, {login}")
    #         else:
    #             print("Нет пользователя с таким именем")
    #     if choice == 2:
    #         user = User(input("Введите логин: "), password := input("Введите пароль: "),
    #                     password2 := input("Повторите пароль: "))
    #         if password != password2:
    #             exit()
    #         database.add_user(user.username, user.password)
    #     print(database.data)

