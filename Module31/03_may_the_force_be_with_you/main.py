# TODO здесь писать код
import requests
import json
from typing import List, Dict, Callable

need_list_shp : List = ['name', 'max_atmosphering_speed', 'starship_class', 'pilots']           # Список значений корабля, которые нужно внести в итоговый словарь
need_list_plts: List = ['name', 'height', 'mass', 'homeworld']                                  # Список значений пилотов, которые нужно внести в итоговый словарь
final_pltMil_dict = {}

#_________________________________________
api_ships : Dict = requests.get('https://swapi.dev/api/starships/?search=Millennium').json()       # вариант get запроса - через поисковый запрос по имени корабля
sh = api_ships['results'][0]                                                                        # Получаем Словарь с описанием ключей и значений корабля Millenium
final_shpMil_dict = ( { k:v for i in need_list_shp for (k,v) in sh.items() if k == i } )            # Словарь, включающий параметры корабля, заданноые в условии


pilots_lst_url = final_shpMil_dict['pilots']                                                    # Список пилотов корабля Millenium
#_______________________________
pilots = []
temp = {}
for i_plt in pilots_lst_url:
    plt = requests.get(i_plt).json()
    for i in need_list_plts:
         temp[i] = plt[i]
    pilots.append(temp)
    temp={}
final_shpMil_dict['pilots'] = pilots

print(json.dumps(final_shpMil_dict, indent=4))


# # Вывод в файлы
# with open('result_plts.json', 'w') as result_file_plts:               # Записываем в файл списки пилотов
#     json.dump(pilots, result_file_plts, indent=4)
#
with open('result_shp.json', 'w') as result_file_shp:               # Записываем в файл данные корабля
     json.dump(final_shpMil_dict, result_file_shp, indent=4)
#
# with open('result_api_root.json', 'w') as api_root_f:               # Записываем в файл корневой API
#     json.dump(api_root, api_root_f, indent=4)


#
# print('________Ищем имя конкретной планеты___________')
# # parametr = {"name": "https://swapi.dev/api/planets/30/"}
# homeworld_name = requests.get('https://swapi.dev/api/planets/33/').json()['name']
# print('\n', homeworld_name)






'''
Задача 3. May the force be with you
Что нужно сделать
Фанаты «Звёздных войн» (Star Wars) написали API по своей любимой вселенной. Ссылка на документацию: Documentation.

Внимательно изучите документацию этого API и напишите программу, которая выводит на экран (и в JSON-файл) информацию о пилотах легендарного корабля Millennium Falcon.

Информация о корабле должна содержать следующие пункты:

название,
максимальная скорость,
класс,
список пилотов.
Внутри списка о каждом пилоте должна быть следующая информация:

имя,
рост,
вес,
родная планета,
ссылка на информацию о родной планете.
Пример вывода информации по кораблю X-wing в консоль:'''

