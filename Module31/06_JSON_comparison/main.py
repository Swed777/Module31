# TODO здесь писать код
from typing import List, Dict, Any
import json

diff_list: List[str] = ['services', 'staff', 'datetime']  # Список параметров для отслеживания
class Find:
    """Формирование словаря из файла по входению в список параметров"""
    def __init__(self, json_f : Dict, result : Dict):
        self.__json_f = json_f
        self.result = result

    def find_param(self, file: Dict, dif_list: List) -> Any:
        for i_key, value in list(file.items()):
            for param in dif_list:
                if param == i_key:
                    self.result[i_key] = value
                elif isinstance(value, dict):
                    self.find_param(value, dif_list)
        return self.result

    def __str__(self):
        return f'Класс, формирующий словарь по вхождению в список параметров (diff_list)'

with open('json_old.json', 'r') as old_file:    # из json файла формируем словарь
    o_file = json.load(old_file)
with open('json_new.json', 'r') as new_file:
    n_file = json.load(new_file)

res1 = Find(o_file, result={})                  # формируем объект класса Find
res2 = Find(n_file, result={})

old = res1.find_param(o_file, diff_list)
new = res2.find_param(n_file, diff_list)

finish_different = ( { k:v for (k,v) in old.items() if old[k] != new[k] } )
print(finish_different)

with open('result.json', 'w') as result_file:               # Записываем в файл отличающиеся параметры
    json.dump(finish_different, result_file, indent=4)




print(res2.__str__())
print(res2.__doc__)

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
