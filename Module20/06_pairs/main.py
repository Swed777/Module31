# TODO здесь писать код

import random       #randint()	Возвращает случайное число в пределах заданного промежутка

rand_list=[]
for i in range(10):
    rand_list.append(random.randint(0,9))   #randint()	Возвращает случайное число в пределах заданного промежутка
print(rand_list)
list_1 = rand_list[::2]
list_2 = rand_list[1::2]
print(list_1)
print(list_2)

for pair in zip(list_1, list_2):
    print(pair)


'''
Задача 6. По парам
Что нужно сделать
Напишите программу, которая инициализирует список из 10 случайных целых чисел, а затем делит эти числа на пары кортежей внутри списка. Выведите результат на экран.
Дополнительно: решите задачу несколькими способами.

Пример:
Оригинальный список: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Новый список: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
'''