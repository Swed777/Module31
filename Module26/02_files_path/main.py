# TODO здесь писать код
import os

# from os.path import join

'''  ЕИ - это к коду не относится, оставил как конспект
https://docs-python.ru/standart-library/modul-os-python/funktsija-walk-modulja-os/ 
os.walk(top, topdown=True, onerror=None, followlinks=False)
Параметры:
top - строка, вершинa каталога,
topdown=True - bool, направление обхода,
onerror=None - функция, которая сообщает об ошибке,
followlinks=False - bool, переходить ли по символическим ссылкам.
Возвращаемое значение:
тройной кортеж.'''


# TODO:
#  В задании сказано:
#  "Реализуйте функцию `gen_files_path`, которая рекурсивно проходит по всем каталогам указанной директории
#  (по умолчанию — корневой диск), находит указанный пользователем каталог и генерирует пути всех встреченных файлов."
#  То есть должна быть одна функция gen_dir_path, которая принимает два параметра на вход:
#  - dir_name - имя директории, которую надо найти
#  - root_path - путь, с которого надо начать поиск. По умолчанию он равен корню диска.
#  Корень диска можно получить как os.path.abspath(os.sep)
#  Итого будет такая функция:
def gen_dir_path(dir_name: str, root_path: str = os.path.abspath(os.sep)):
    for root, dirs, files in os.walk(root_path):
        # TODO:
        #  - Проверяем, если root кончается на dir_name (с помощью метода .endswith()),
        #  то печатаем root и делаем return
        #  - Делаем yield root
        #  - Идем циклом for по files, переменная цикла - file_name.
        #  В цикле делаем yield полного пути файла os.path.join(root, file_name)

# TODO:
#  И никаких return False тоже быть не должно

for i in gen_dir_path(dir_name="01_scary_code", root_path="../../../Python_Basic"):
    print(i)
