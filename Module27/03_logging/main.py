# TODO здесь писать код
from datetime import datetime


def logging(func):
    def wrapper(*args, **kwargs):
        try:
            print(f'{func.__name__} - {func.__doc__}')
            return func(*args, **kwargs)
        except Exception as e:
            e = f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")} - {func.__name__} - {e}\n'  # время срабатывания и название функуии с ошибкой в
            with open('function_error.log', 'a+', encoding='utf-8') as fnc:
                fnc.write(e)
            print(e)

    return wrapper


@logging
def zerodiv() -> None:
    """Деление на ноль"""
    x = 1 / 0


@logging
def varname() -> None:
    """Присвоим не существующую переменную"""
    x = y


@logging
def just() -> None:
    """Присваение переменной значения"""
    x = int('Hello World!!!')


zerodiv()
varname()
just()

# зачтено
