# TODO здесь писать код
from typing import Iterable


# Класс итератор:
class Square_num:
    def __init__(self, num: int) -> None:
        self.__num = num
        self.__startNumber = 0
        self.__count = 0

    def __iter__(self):
        self.__startNumber = 0
        self.__count = 0
        return self

    def __next__(self) -> int:
        self.__count += 1
        if self.__num <= 0:
            raise StopIteration
        elif self.__num >= 1:
            if self.__count > self.__num:
                raise StopIteration
        self.__startNumber += 1
        return self.__startNumber * self.__startNumber


# Функция- генератор
def gen_func(number: int) -> Iterable[int]:
    for i in range(1, number + 1):
        i = i ** 2
        yield i


number = int(input('Введите число: '))

print('-----------------------')
print('Класс-генератор:')
square_number = Square_num(num=number)
for i in square_number:
    print(i, end=' ')

print('\n-----------------------')
print('Функция-генератор:')
for i in gen_func(number):
    print(i, end=' ')

print('\n-----------------------')
print('Генераторное выражение:')
gen_v = (i ** 2 for i in range(1, number + 1))
for i in gen_v:
    print(i, end=' ')

# зачтено
