# TODO здесь писать код
import functools
from typing import Callable

def counter(func : Callable) -> Callable:
    # @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Функция подсчета количества вызовов
        """
        func()
        wrapper.count +=1
        result = func(*args, **kwargs)
        print(f'Программа {func.__name__} вызвана: {wrapper.count} раз')
        return result
    wrapper.count = 0
    return wrapper

@counter
def test():
    txt = 'Тест счетчика 1'
    print(txt)

@counter
def test2():
    txt = 'Тест счетчика 2'
    print(txt)

test()
test2()
test()
test()
test()
test2()
test2()

'''
Задача 4. Счётчик
Что нужно сделать
Реализуйте декоратор counter, считающий и выводящий количество вызовов декорируемой функции.

Для решения задачи нельзя использовать операторы global и nonlocal (об этом мы ещё расскажем).
'''