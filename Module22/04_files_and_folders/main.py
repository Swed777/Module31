# TODO здесь писать код
import os

def dir_file(path):
    result_dir = 0
    result_file = 0
    file_size = 0
    for i_elem in os.listdir(path):
        path_in = os.path.join(path, i_elem)
        if os.path.isdir(path_in):
            result_dir +=1
        elif os.path.isfile(path_in):
            result_file += 1
            file_size += os.path.getsize(path_in)

    print(f'Количество подкаталогов:  {result_dir} \nКоличество файлов:   {result_file} \nРазмер директории: {file_size}')

path = input('Введите путь до каталога: ')   # path = '/Users/ei/desktop/linux/python_basic/module22/module14'
dir_file(path)



'''
Задача 4. Файлы и папки
Что нужно сделать
Напишите программу, которая получает на вход путь до каталога (это может быть и просто корень диска) и выводит общее количество файлов и подкаталогов в нём. Также выведите на экран размер каталога в килобайтах (1 килобайт = 1024 байт).
Важный момент: чтобы посчитать, сколько весит каталог, нужно найти сумму размеров всех вложенных в него файлов. 
Результат работы программы на примере python_basic\Module14:

/Users/ei/desktop/linux/python_basic/module22/module14


E:\PycharmProjects\python_basic\Module14
Размер каталога (в Кб): 8.373046875
Количество подкаталогов: 7
Количество файлов: 15
'''