# TODO здесь писать код
def check_len(line, number_line):
    try:
        if len(line) < 3:
            raise Exception    #Вызываем исключение
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
        check_len(i_line, count_line_symb) # Проверяем количество символов не менее 3

print(f'Общее количество символов в файле: -> {sum}')


'''
Задача 1. Имена 2
Что нужно сделать
Есть файл people.txt, в котором построчно хранится N имён пользователей. 
Напишите программу, которая берёт количество символов в каждой строке файла и в качестве ответа выводит общую сумму. Если в какой-либо строке меньше трёх символов (не считая литерала \n), то вызывается ошибка и сообщение, в какой именно строке ошибка возника. Программа при этом не завершается и обрабатывает все имена файла.
Также при желании можно вывести все ошибки в отдельный файл errors.log.
Пример работы программы

Содержимое файла people.txt:
Василий
Николай
Надежда
Никита
Ян
Ольга
Евгения
Кристина


Ответ в консоли:
Ошибка: менее трёх символов в строке 5.
Общее количество символов: 49.
'''