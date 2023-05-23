# TODO здесь писать код
from typing import Callable
from functools import wraps
def check_permission(username : str) -> Callable:
    """
        Декоратор проверки прав пользователя.
        Возвращает ошибку или право доступа к функции
        """
    def check_permission_down(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Callable:
            try:
                if username == 'admin':
                    return func(*args, **kwargs)
                else:
                    raise PermissionError
            except PermissionError:
                print(f'PermissionError: У Вас недостаточно прав, чтобы выполнить функцию --> {func.__name__}. \nОбратитесь к администратору')
        return wrapper
    return check_permission_down

@check_permission('admin')
# @check_permission('user_1')
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1')
# @check_permission('admin')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()


'''
Задача 1. Права доступа
Что нужно сделать
Перед вами стоит задача создать и поддерживать специализированный форум. Вы только приступили и сейчас 
работаете над действиями, которые могут совершать посетители форума. 
Для разных пользователей прописаны разные возможности.

Напишите декоратор check_permission, который проверяет, есть ли у пользователя доступ к вызываемой функции, 
и если нет, то выдаёт исключение PermissionError.

Пример кода:
user_permissions = ['admin']

@check_permission('admin')
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')

delete_site()
add_comment()
Результат:
Удаляем сайт
PermissionError: у пользователя недостаточно прав, чтобы выполнить функцию add_comment
'''