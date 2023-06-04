# TODO здесь писать код
import requests
import json
from typing import List, Dict

need_list_shp : List = ['name', 'max_atmosphering_speed', 'starship_class', 'pilots']  # Список значений, которые нужно внести в итоговый словарь
need_list_plts: List = ['name', 'height', 'mass', 'homeworld', 'homeworld_url']
# final_dict = {}

#____________ Не нужно для программы
# api = requests.get('https://swapi.dev/api/').headers
# api_root = requests.get('https://swapi.dev/api/').json()
# _____________________________________
# api_shp = requests.get('https://swapi.dev/api/starships/').json()
# api_ppl = requests.get('https://swapi.dev/api/people/').json()

#_________________________________________
api_ships = requests.get('https://swapi.dev/api/starships/?search=Millennium').json()       # вариант get запроса через поисковый запрос
x = api_ships['results'][0]
final_shpMil_dict = ( { k:v for i in need_list_shp for (k,v) in x.items() if k == i } )
print(final_shpMil_dict)






# # Вывод в файлы
# with open('result_ppl.json', 'w') as result_file_ppl:               # Записываем в файл списки пилотов
#     json.dump(api_ppl, result_file_ppl, indent=4)
#
with open('result_shp.json', 'w') as result_file_shp:               # Записываем в файл данные корабля
     json.dump(final_shpMil_dict, result_file_shp, indent=4)
#
# with open('result_api_root.json', 'w') as api_root_f:               # Записываем в файл корневой API
#     json.dump(api_root, api_root_f, indent=4)










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

