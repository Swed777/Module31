class Clock:
    __DAY = 86400  # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
            s = self.seconds % 60  # секунды
            m = (self.seconds // 60) % 60  # минуты
            h = (self.seconds // 3600) % 24  # часы
            return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
            return str(x).rjust(2, "0")

    def __add__(self, other):
        if not isinstance(other, int):
            raise ArithmeticError("Правый операнд должен быть типом int")

        return Clock(self.seconds + other)

c1 = Clock(1000)
c2 = Clock(2000)
c3 = c1 + c2
print(c3.get_time())