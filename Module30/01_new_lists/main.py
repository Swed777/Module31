# TODO здесь писать код
from typing import List

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
#_________________________________________________

my_floats : List[float] = list(map(lambda x : round(x ** 3, 3), floats))
my_names : List[str] = list(filter(lambda letter: len(letter) >=5, names))



print('Задание 1:', my_floats)
print('Задание 2:', my_names)

'''
Задача 1. Новые списки
Что нужно сделать
Даны три списка: 

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
Напишите код, который создаёт три новых списка. Вот их содержимое:

Каждое число из списка floats возводится в третью степень и округляется до трёх знаков после запятой.
Из списка names берутся только имена минимум из пяти букв.
Из списка numbers берётся произведение всех чисел.
'''