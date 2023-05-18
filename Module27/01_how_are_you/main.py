# TODO здесь писать код
import functools
from typing import Callable


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

# зачтено
