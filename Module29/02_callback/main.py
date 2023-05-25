# TODO здесь писать код
from functools import wraps
from typing import Callable, Any

app = dict()


def callback(route: str) -> Callable:
    """
    Это функция, которая вызывается при срабатывании определённого события: переходе на страницу,
    получении сообщения или окончании обработки процессором
    """

    def decorator_callback(func: Callable) -> Callable:
        app[route] = func

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            return func(*args, **kwargs)

        return wrapper

    return decorator_callback


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

# зачтено
