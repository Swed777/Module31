# TODO здесь писать код
import os

#  Мой путь :  --->  Users ei desktop Linux Python_basic Module22 Module22 05_save
stroke = input('Введите строку: ')
path = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел):').replace(' ',
                                                                                                         os.sep)  # replace заменяет все вхождения одной строки (пробелы) на другую  для данной ОС - /
path_all = os.path.join(os.sep, path)  # добавляем разделитель / в начало пути в соответствии с текущей ОС
if not os.path.exists(path_all):  # Проверка на существование директории
    print('Такого пути не существует')
file_name = input('Введите имя файла: ')

true_file = os.path.isfile(os.path.join(path_all, file_name))  # Проверяем наличие файла
if true_file:
    rewrite = input('Вы действительно хотите перезаписать файл? Да/Нет\n').lower()
    if rewrite == 'да':
        file_save = open(file_name, 'w', encoding="utf8")  # открываем файл в режиме записи
        file_save.write(stroke)  # записываем строку в файл
        file_save.close()
        print('Файл успешно перезаписан\n')
    else:
        print('Начинаем сначала :)\n')
else:
    file_save = open(file_name, 'w', encoding="utf8")  # открываем файл в режиме записи
    file_save.write(stroke)  # записываем строку в файл
    file_save.close()
    print('Файл успешно сохранен\n')

file_read = open(file_name, 'r')
print('Содержимое файла: ', file_read.read())

# зачтено
