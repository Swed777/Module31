# TODO здесь писать код
import os

#  Мой путь :  --->  Users ei desktop Linux Python_basic Module22 Module22 05_save

stroke = input('Введите строку: ')
path = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел):').replace(' ', os.sep)  #replace заменяет все вхождения одной строки (пробелы) на другую - /
path_all = os.path.join(os.sep, path) # добавляем разделитель / в начало пути в соответствии с текущей ОС

if not os.path.exists(path_all):        # Проверка на существование директории
    print('Такого пути не существует')
print(path)
print(path_all)

file_name = input('Введите имя файла: ')


'''
Задача 5. Сохранение
Что нужно сделать
Мы продолжаем работать над усовершенствованием своего текстового редактора. Конечно же, при работе с редактором пользователь, скорее всего, захочет сохранить то, что он написал, в отдельный файл. Ну или перезаписать тот, в котором он продолжил работать. 
Пользователь вводит строку text. Реализуйте функцию, которая запрашивает у пользователя, куда он хочет сохранить эту строку: вводится последовательность папок и имя файла (расширение .txt). Затем в этот файл сохраняется значение переменной text. Если этот файл уже существует, то нужно спросить у пользователя, действительно ли он хочет перезаписать его.
Обеспечьте контроль ввода: указанный из папок путь должен существовать на диске.

Пример 1
Введите строку: programm test

Куда хотите сохранить документ? Введите последовательность папок (через пробел):
Users Roman PycharmProjects Skillbox Module22

Введите имя файла: my_document
Файл успешно сохранён!

Содержимое файла:
programm test

Пример 2
Введите строку: testiruyem

 Куда хотите сохранить документ? Введите последовательность папок (через пробел):
Users Roman PycharmProjects Skillbox Module22

 Введите имя файла: my_document
Вы действительно хотите перезаписать файл? да
Файл успешно перезаписан!

Содержимое файла:
testiruyem
'''