# TODO здесь писать код
from functools import wraps
from typing import Callable


def check_permission(username: str) -> Callable:
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
                print(
                    f'PermissionError: У Вас недостаточно прав, чтобы выполнить функцию --> {func.__name__}. \nОбратитесь к администратору')

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

# зачтено
