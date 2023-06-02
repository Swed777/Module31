# TODO здесь писать код
import requests
import json
import re

'Тестирую'

# war_api = requests.get('http://swapi.dev/api/planets/1/')
# param = {'ship_name':'Millennium Falcon'}
# war_api = requests.get('https://swapi.dev/api/people/')

# war_api = requests.get("https://api.thedogapi.com/v1/breeds/1")
# print(war_api.text)
# print(war_api.content)
# # print(war_api.headers)
# war_api.headers.get('Content-Type')
# print(war_api.json())
# print(war_api.json())
# for k,v in war_api.items():
#     print('-->', v, end='\n')

api_key = "IxvocnRc69rLkVZUOrPg47UzMlTjghXdvSoHqzzi"
query_params = {"api_key": api_key, "earth_date": "2020-07-01"}
# nasa_api = requests.get('https://api.nasa.gov/')
nasa_foto = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos", params=query_params)
print(nasa_foto.json())
foto = nasa_foto.json()['photos'][5]['img_src']
print(foto)

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