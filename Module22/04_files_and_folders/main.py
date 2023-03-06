# TODO здесь писать код
import os


def dir_file(path):
    result_dir = 0
    result_file = 0
    file_size = 0
    for i_elem in os.listdir(path):
        path_in = os.path.join(path, i_elem)
        if os.path.isdir(path_in):
            result_dir += 1
        elif os.path.isfile(path_in):
            result_file += 1
            file_size += os.path.getsize(path_in)

    print(
        f'Количество подкаталогов:  {result_dir} \nКоличество файлов:   {result_file} \nРазмер директории: {file_size}')


path = input('Введите путь до каталога: ')  # path = '/Users/ei/desktop/linux/python_basic/module22/module14'
dir_file(path)

# зачтено
