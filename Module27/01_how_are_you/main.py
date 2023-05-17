# TODO здесь писать код
from typing import Callable
import functools

def how_are_you(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        result = func(*args, **kwargs)
        return result

    return wrapper

@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')


@how_are_you
def degree(x: int, y: int) -> int:
    """
    Эта функция вычисляет степень числа
    :return:   Степень числа
    """
    result = x ** y
    print(f'{x} степени {y} равно {result}')
    return result


test()

print('---------------')
degree(7, 37)

print(degree.__doc__)
print(degree.__name__)


'''
Задача 1. Как дела?
Что нужно сделать
Вася совсем заскучал на работе и решил побаловаться с кодом проекта. Он написал надоедливый декоратор, 
который при вызове декорируемой функции спрашивает у пользователя «Как дела?», вне зависимости от ответа пишет что-то
вроде «А у меня не очень!» и только потом запускает саму функцию. Правда, после такой выходки Васю чуть не уволили с работы.

Реализуйте такой же декоратор и проверьте его работу на нескольких функциях.
Пример кода:

@how_are_you
def test():
    print('<Тут что-то происходит...>')

test()
Результат:
Как дела? Хорошо.
А у меня не очень! Ладно, держи свою функцию.
<Тут что-то происходит...>

'''