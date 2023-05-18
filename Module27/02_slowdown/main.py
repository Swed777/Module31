# TODO здесь писать код
import time
import requests
import functools

def slow_func(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(5)          # Перед выполнением функции сделаем задержку на 5 секунд
        result = func(*args, **kwargs)
        return result
    return wrapper

@slow_func
def requests_site(site : str) -> str:
    """
    Функция запроса информации на сайте
    """
    response = requests.get(site)
    print('Данные получены')
    result = response.text
    response.close()
    return result

site = str('http://alexgyver.ru')
test = requests_site(site)
print(test)

print(requests_site.__doc__)     # Проверка работы  @functools.wraps



'''
Задача 2. Замедление кода
Что нужно сделать
В программировании иногда возникает ситуация, когда работу функции нужно замедлить.
 Типичный пример — функция, которая постоянно проверяет, изменились ли данные на веб-странице или её код.

Реализуйте декоратор, который перед выполнением декорируемой функции ждёт несколько секунд.
'''