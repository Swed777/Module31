# TODO здесь писать код
import requests
import json
from typing import List, Dict, Callable

need_list_shp : List = ['name', 'max_atmosphering_speed', 'starship_class', 'pilots']           # Список значений корабля, которые нужно внести в итоговый словарь
need_list_plts: List = ['name', 'height', 'mass', 'homeworld']                 # Список значений пилотов, которые нужно внести в итоговый словарь
'homeworld_url'



#_________________________________________
api_ships : Dict = requests.get('https://swapi.dev/api/starships/?search=Millennium').json()       # вариант get запроса - через поисковый запрос по имени корабля
sh = api_ships['results'][0]                                                                        # Получаем Словарь с описанием ключей и значений корабля Millenium
final_shpMil_dict = ( { k:v for i in need_list_shp for (k,v) in sh.items() if k == i } )            # Словарь, включающий параметры корабля, заданноые в условии

pilots_lst_url = final_shpMil_dict['pilots']      # Список пилотов корабля Millenium

api_planet : Dict = requests.get('https://swapi.dev/api/planets/').json()   # Запрос к планетам для получения домашней планеты пилота
planet_dict = api_planet['results']

print(planet_dict, '\n')


#_______________________________
final_pltMil_dict = {}
pilots = []
temp = {}
for i_plt in pilots_lst_url:
    plt : Dict = requests.get(i_plt).json()
    # print(plt)
    for i in need_list_plts:
        temp[i] = plt[i]
        if i == 'homeworld':
            temp['homeworld_url'] = temp[i] # Переименуем ключ в соответствующий содержанию значения (url)
            for i_planet in planet_dict:
                print(i_planet, i_planet['url'])
                if i_planet['url'] == temp[i]:
                    # print(i, '-->', temp[i])
                    temp['homeworld'] = i_planet['name']
                    print(i_planet, '99999')
    pilots.append(temp)
    temp={}
final_shpMil_dict['pilots'] = pilots        # добавляем описание всех пилотов в описание корабля


# print(json.dumps(final_shpMil_dict, indent=4))        #НЕ удалять, идет в итоговый код

with open('result_shp.json', 'w') as result_file_shp:   # Записываем в файл данные корабля
     json.dump(final_shpMil_dict, result_file_shp, indent=4)


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