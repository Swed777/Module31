# TODO здесь писать код
from functools import wraps
from typing import Callable, Any, Optional


def decorator_with_args_for_any_decorator(enhance_func: Callable) -> Callable:
    def maker(*args, **kwargs) -> Callable:
        def wrapper(func: Callable) -> Callable:
            return enhance_func(func, *args, **kwargs)

        return wrapper

    return maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:  # отсюда уже сами!
    @wraps(func)
    def wrapper(func_args: Optional[Any], func_kwargs: Optional[Any]) -> Callable:
        print(f'Переданные арги и кварги в декоратор: {args}, {kwargs}')
        result = func(func_args, func_kwargs)
        return result

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)

# зачтено
