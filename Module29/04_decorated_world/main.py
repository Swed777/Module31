# TODO здесь писать код

from functools import wraps
from typing import Callable, Any

def decorator_with_args_for_any_decorator():



@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):... # отсюда уже сами!

@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)

decorated_function("Юзер", 101)


'''
Задача 4. Весь мир — декоратор…
Что нужно сделать
Реализуйте декоратор для декораторов: он должен декорировать другую функцию, которая должна быть декоратором,
и даёт возможность любому декоратору принимать произвольные аргументы.

Пример использования:
@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):... # отсюда уже сами!

@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)

decorated_function("Юзер", 101)

Результат:
Переданные арги и кварги в декоратор: (100, 'рублей', 200, 'друзей') {}
Привет, Юзер 101
'''