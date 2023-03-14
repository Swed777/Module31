# TODO здесь писать код

def validata(i_line, count_string):
    result = True
    symbol = ('@', '.')
    try:
        client = i_line.split()  # разбиваем строку по признаку "Пробел"
        name, post, age = client[0], client[1], client[2]  # Множественное присваивание элементам строки
        try:
            if not name.lower().isalpha():
                result = False
                raise NameError(bad_logfile.write(f'\n{i_line.strip()}   Поле «Имя» содержит НЕ только буквы'))
            for i_symbol in symbol:
                if i_symbol not in post:
                    raise SyntaxError(bad_logfile.write(f'\n{i_line.strip()}   Поле «email» НЕ содержит @ и .'))
            if int(age) not in range(10, 99):
                result = False
                raise ValueError(
                    bad_logfile.write(f'\n{i_line.strip()}   Поле «Возраст» НЕ представляет число от 10 до 99'))
        except (IndexError, NameError, SyntaxError, ValueError):
            return result
    except:
        result = False
        bad_logfile.write(f'\nВ строке нр {count_string}: --> {i_line.strip()} <-- отсутствует одновременно ТРИ поля')
    return result


count_string = 0  # счетчик всех строк в файле

# Открываем исходный файл и два файла с логами
with open('registrations.txt', 'r', encoding='utf8') as open_file:
    fin = open_file.readlines()
good_logfile = open('registrations_good.log', 'a', encoding='utf8')
bad_logfile = open('registrations_bad.log', 'a', encoding='utf8')

for i_line in fin:
    count_string += 1
    if validata(i_line, count_string):
        good_logfile.write(f'{i_line}')
    else:
        pass

# Закрываем все файлы
open_file.close()
good_logfile.close()
bad_logfile.close()

# зачтено
