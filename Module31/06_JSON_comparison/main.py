# TODO здесь писать код
from typing import List, Dict, Any
import json

diff_list: List[str] = ['services', 'staff', 'datetime']  # Список параметров для отслеживания
class Find:
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

with open('json_old.json', 'r') as old_file:
    o_file = json.load(old_file)
with open('json_new.json', 'r') as new_file:
    n_file = json.load(new_file)

res1 = Find(o_file, result={})
res2 = Find(n_file, result={})
x  = res1.find_param(o_file, diff_list)
y = res2.find_param(n_file, diff_list)
print(x)
print(type(x))
print(y)


# for i in diff_list:
#     print(list_o.get(i))
#     print(list_n.get(i))
#     if list_o.get(i) != list_n.get(i):
#         print(list_n.get(i))

# with open('result.json', 'w') as result_file:
#     json.dump(o_file, result_file, indent=4)



'''
***********  Первоначальный резервный вариант  **************

from typing import List, Dict
import json
result = dict()
diff_list: List[str] = ['services', 'staff', 'datetime']  # Список параметров для отслеживания
def find_param(file : Dict, diff_list : List):
    for i_key, value in file.items():
        for param in diff_list:
            if param == i_key:
                result[i_key] = value
            elif isinstance(value, dict):
                find_param(value, diff_list)
    return result


with open('json_old.json', 'r') as old_file:
    o_file : Dict = json.load(old_file)
    # print(o_file)
with open('json_new.json', 'r') as new_file:
    n_file = json.load(new_file)
    # print(n_file)
print('Файлы идентичны' if o_file == n_file else 'Файлы разные, ищем разницу в значениях:')
print('*' * 43, end='\n')


list_o = find_param(o_file, diff_list)
list_n = find_param(n_file, diff_list)
print(list_o)
print(list_n)
'''



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
