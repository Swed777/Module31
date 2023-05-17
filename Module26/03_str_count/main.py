import os


def get_file_list(dir: str) -> str:
    # Формирование списка файлов в директории
    for root, direct, files in os.walk(dir):
        for i_file in files:
            if i_file.endswith('.py'):
                yield os.path.join(root, i_file)


def count_line(file_name):
    with open(file_name, 'r') as file:
        local_count = 0
        for line in file:
            line = line.strip()
            if len(line) > 0 and not line.startswith('#'):
                local_count += 1
        print(f'{file_name} - {local_count} строк(и)')


directory = "../../Module14/01_os_info/"
file_list = list(get_file_list(directory))
for i_file in file_list:
    count_line(i_file)
