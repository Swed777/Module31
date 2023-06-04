# TODO здесь писать код
import requests
import json
from typing import List, Dict

need_list_shp : List = ['name', 'max_atmosphering_speed', 'starship_class', 'pilots']  # Список значений, которые нужно внести в итоговый словарь
final_dict = {}


#____________ Не нужно для программы
api = requests.get('https://swapi.dev/api/').headers
api_root = requests.get('https://swapi.dev/api/').json()

# _____________________________________
api_shp = requests.get('https://swapi.dev/api/starships/').json()
api_ppl = requests.get('https://swapi.dev/api/people/').json()

api_shp_lst = api_shp['results']
# shp_data : List = [i for i in api_shp_lst if i['name'] == "Millennium Falcon"] # Формируем список всех значений корабля
shp_data : List = [i for i in api_shp['results'] if i['name'] == "Millennium Falcon"] # Формируем список всех значений корабля
shp_data_mil : Dict = shp_data[0]                                              # и берем из него первое значение 'name' в виде словаря


for k,v in shp_data_mil.items():
    for i in need_list_shp:
        if k == i:
            print(k, '->', v)




# shp_data_plts = shp_data('pilots')
# print(shp_data_plts)

if 'pilots' in shp_data:
    print('*************')




# Вывод в файлы
# with open('result_ppl.json', 'w') as result_file_ppl:               # Записываем в файл списки пилотов
#     json.dump(api_ppl, result_file_ppl, indent=4)
#
# with open('result_shp.json', 'w') as result_file_shp:               # Записываем в файл данные корабля
#     json.dump(shp_data, result_file_shp, indent=4)
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

