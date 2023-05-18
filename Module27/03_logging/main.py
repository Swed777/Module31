# TODO здесь писать код
from datetime import datetime

def logging(func):
    def wrapper():
        try:
            print(f'{func.__name__} - {func.__doc__}')
            func()
        except Exception as e:
            e = f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")} - {func.__name__} - {e}\n'   # время срабатывания и название функуии с ошибкой в
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



pass
'''
Задача 3. Логирование
Что нужно сделать
Реализуйте декоратор logging, который будет отвечать за логирование функций. На экран выводится название функции 
и её документация. Если во время выполнения декорируемой функции возникла ошибка, 
то в файл function_errors.log записываются название функции и ошибки. 

Также постарайтесь сделать так, чтобы программа не завершалась после обнаружения первой же ошибки, 
а обрабатывала все декорируемые функции и сразу записывала все ошибки в файл.

Дополнительно: запишите дату и время возникновения ошибки, используя модуль datetime.
'''