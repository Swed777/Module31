# TODO здесь писать код
from typing import List, Dict
import json

diff_list : List[str] = ['services', 'staff', 'datetime']   # Список параметров для отслеживания
result = dict                                               # вывод в консоль - Словарь {параметр: новое_значение, ….}


with open('json_old.json', 'r') as old_file:
    o_file : Dict = json.load(old_file)
    print(o_file)
with open('json_new.json', 'r') as new_file:
    n_file = json.load(new_file)
    # print(n_file)

if o_file == n_file:
    print('Файлы идентичны')
else:
    print('Файлы разные, Ищем разницу в значениях:')

for key, o_items in o_file.items():
    print('Ключ:', key)
    # print('Значение:', o_items)
    for key, n_items in n_file.items():
        if o_items != n_items:
            print('Значение в старом файле', o_items)
            print('Значение в новом файле',  n_items)

key_diff = 'services'
if key_diff in o_file:
    print(key_diff)
else:
    print('Не нашел')

if (o_file['data']['services']) != (n_file['data']['services']):
    print('Вот искомое расхождение: ', n_file['data']['services'])

# with open('result.json', 'w') as result_file:
#     json.dump(o_file, result_file, indent=4)

'''
Задача 6. Поиск разницы между двумя JSON-файлами (пример из реального тестового задания на должность Python-разработчика уровня Junior)
Что нужно сделать
Найдите различия между двумя JSON-файлами. Если различающиеся параметры входят в diff_list, выведите различие. Иными словами, вам нужно отловить изменение определённых параметров и вывести значение: что изменилось и на что. Набор ключей в обоих файлах идентичный, различаются лишь значения.

Напишите программу, которая:

загружает данные из двух предложенных JSON-файлов (находятся в репозитории);
выполняет сравнение параметров, указанных в diff_list;
формирует результат в виде словаря;
записывает словарь в JSON-файл с названием result.json.
Исходные данные

Файлы:

json_old.json,
json_new.json.
Список параметров для отслеживания (можно сформировать инпутом или ввести вручную):

diff_list = [‘services’, ‘staff’, ‘datetime’]

Формат итогового словаря с результатом:

Словарь {параметр: новое_значение, ….}
'''