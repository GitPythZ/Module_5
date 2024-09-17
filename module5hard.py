# Задание "Свой YouTube"
import time


class User:
    def __init__(self, nickname, password, age):
        """
        Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
        :param nickname: str
        :param password: в хешированном виде
        :param age: int
        """
        self.nickname = str(nickname)
        self.password = password
        password = hash(password)
        self.age = int(age)

    def __str__(self):
        return f"Логин: {self.nickname} \nПароль: {self.password} \nВозраст: {self.age}"

    def __eq__(self, other):
        return self.nickname == other.nickname


class UrTube:
    from time import sleep

    def __init__(self, users=None, videos=None, current_user=User):
        """
        Атрибуты:
        :param users: cписок объектов User
        :param videos: список объектов Video
        :param current_user: текущий пользователь, User
        """
        self.users = users
        if self.users is None:
            self.users = []
        self.videos = videos
        if self.videos is None:
            self.videos = []
        self.current_user = current_user

    def __str__(self):
        return f""

    def log_in(self, nickname, password):
        """
        Метод log_in, принимает на вход аргументы: nickname, password и пытается найти пользователя в users
        с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного.
        Помните, что password передаётся в виде строки, а сравнивается по хэшу.
        """
        check_user = User(nickname, hash(password), age=0)
        if check_user in self.users:
            print(f"Добро пожаловать {nickname}, вы успешно вошли в ваш аккаунт")
        else:
            print(f"Пользователь с логином {nickname} не найден")

    def register(self, nickname, password, age):
        """
        Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список,
        если пользователя не существует (с таким же nickname).
        Если существует, выводит на экран: "Пользователь {nickname} уже существует".
        После регистрации, вход выполняется автоматически.
        """
        new_user = User(nickname, password, age=0)
        if new_user not in self.users:
            self.users.append(new_user)
        else:
            print(f"Пользователь с логином {nickname} уже существует")

    def log_out(self):
        """
        Метод log_out для сброса текущего пользователя на None.
        """
        self.current_user = None

    def add(self, *args):
        """
        Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
        если с таким же названием видео ещё не существует.
        В противном случае ничего не происходит.
        """
        for i in args:
            self.videos.append(i)

    def get_videos(self, check_word):
        """
        Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео,
        содержащих поисковое слово.
        Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
        """
        get_videos_list = []
        for i in self.videos:
            if check_word.lower() in i.title.lower():
                get_videos_list.append(i.title)
        print(get_videos_list)

    def watch_video(self, key_word):
        """
        Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
        то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
        После текущее время просмотра данного видео сбрасывается.
        Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
        Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
        В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
        Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре,
        т.к. есть ограничения 18+.
        Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
        После воспроизведения нужно выводить: "Конец видео".
        """
        if self.current_user is not None:
            for i in self.videos:
                if key_word in i.title:
                    for j in self.users:
                        if self.current_user == j.nickname:
                            check = User(self.current_user, j.password, j.age)
                            if check.age < 18 and i.adult_mode == True:
                                print('Вам нет 18 лет, пожалуйста покиньте страницу')
                            else:
                                print(f'Воспроизводится: "{i.title}", текущая секунда просмотра:')
                                for c in range(i.duration):
                                    print(f'\r{c:3}', end='')
                                    time.sleep(0.05)
                                print(f'\nКонец видео')
                                i.time_now = 0
                    break
                elif key_word not in i.title:
                    print(f'Видео по запросу: "{key_word}" не найдено')
                    break
        elif self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')


class Video:
    adult_mode = False

    def __str__(self):
        return (f"Название: {self.title} \nПродолжительность: {self.duration} \nСекунда остановки: {self.time_now} "
                f"\nПодходит для детей {self.ad_mode}")

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        """
        :param title: заголовок, строка
        :param duration: продолжительность, секунды
        :param time_now: секунда остановки (изначально 0
        :param adult_mode: ограничение по возрасту, bool (False по умолчанию)
        """
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = time_now
        self.adult_mode = bool(adult_mode)
        if not self.adult_mode:
            self.ad_mode = "Нет"
        else:
            self.ad_mode = "Да"


# Код для проверки
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')