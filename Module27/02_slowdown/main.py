# TODO здесь писать код
from typing import Callable
import time
import functools

def slow_func(func : Callable) -> int:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(5)
        result = func(*args, **kwargs)
        return result
    return wrapper()



'''
Задача 2. Замедление кода
Что нужно сделать
В программировании иногда возникает ситуация, когда работу функции нужно замедлить.
 Типичный пример — функция, которая постоянно проверяет, изменились ли данные на веб-странице или её код.

Реализуйте декоратор, который перед выполнением декорируемой функции ждёт несколько секунд.
'''