# TODO здесь писать код
from typing import List, Dict
import json
diff_list : List[str] = ['services', 'staff', 'datetime']   # Список параметров для отслеживания
def find_param(file : Dict, diff_list : List):
    # for param in diff_list:
    for i_key,value in file.items():
        for param in diff_list:
            if param == i_key:
                # print(f'нашел ключ {param}, добавить его в темп')
                print('Словарь из дифлиста', i_key, value)
            else:
                if not isinstance(value, dict):
                    pass
                else:
                    print('конечный елсе', i_key, value)
                    find_param(value, diff_list)


result = dict()                                               # вывод в консоль - Словарь {параметр: новое_значение, ….}

with open('json_old.json', 'r') as old_file:
    o_file : Dict = json.load(old_file)
    print(o_file)
with open('json_new.json', 'r') as new_file:
    n_file = json.load(new_file)
    # print(n_file)
print('Файлы идентичны' if o_file == n_file else  'Файлы разные, ищем разницу в значениях:')
print('*' * 43, end='\n')


# for key, o_items in o_file.items():
#     print('Ключ:', key)
#     # print('Значение:', o_items)
#     for key, n_items in n_file.items():
#         if o_items != n_items:
#             # print('Значение в старом файле', o_items)
#             # print('Значение в новом файле',  n_items)
#             pass

find_param(o_file, diff_list)







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