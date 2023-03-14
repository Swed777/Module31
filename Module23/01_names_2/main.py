# TODO здесь писать код
def check_len(line, number_line):
    try:
        if len(line) < 3:
            raise Exception  # Вызываем исключение
    except Exception:
        print(f'Ошибка: Менее трёх символов в строке: -> {number_line}')
        with open('errors.log', 'a') as error_file:
            error_file.write(i_line + '\n')
    return True


count_line_symb = 0
sum = 0
with open('people.txt', 'r') as people_file:
    people_file_read = people_file.read().splitlines()
    for i_line in people_file_read:
        count_line_symb += 1
        len_i_line = len(i_line)
        sum = sum + len_i_line
        check_len(i_line, count_line_symb)  # Проверяем количество символов не менее 3

print(f'Общее количество символов в файле: -> {sum}')

# зачтено
