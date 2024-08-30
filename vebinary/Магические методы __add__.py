class Clock:
    _DAY = 86400 # число секунд в сутках

    def __init__(self, seconds :int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self._DAY

    def get_time(self):
        s = self.seconds % 60 # секунды
        m = (self.seconds // 60) % 60 # минуты
        h = (self.seconds // 3600) % 24 # часы
        return f"{self._get_formatted(h)}:{self._get_formatted(m)}:{self._get_formatted(s)}"

    def _get_formatted(cls, x):
        return str(x).rjust(2, "0")

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть типом int или объектом Clock")

        sc = other if isinstance(other, int) else other.seconds
        return Clock(self.seconds + sc)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        print("__iadd__")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть типом int или объектом Clock")

        sc = other if isinstance(other, int) else other.seconds
        self.seconds += sc

        return self

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc

    def __gt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds > sc

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Операнд справа должен иметь тип int или Clock")
        return other if isinstance(other, int) else other.seconds


c1 = Clock(1000)
print(c1.get_time())
c1 = c1 + 100
print(c1.get_time())
c2 = Clock(2000)
c3 = c1 + c2
c4 = c1 + c2 + c3
print(c4.get_time())
c1 = 100 + c1
print(c1.get_time())
c1 += 100
print(c1.get_time())
print(c1 == c2)
print(c1 != c2)
print(c1 < c2)
