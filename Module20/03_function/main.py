# TODO здесь писать код
def slicer(tup, num):
    # ---Определяем первый и последний одинаковый элемент в кортеже
    start, stop = 0, 0      # Начало и конец будущего кортежа
    count = 0               # Признак наличия элемента в кортеже
    flag = False
    new_tuple = tuple()
    for index, value in enumerate(tup):
        if value == (num):
            if flag == False:
                flag = True
                count += 1
                start = index
            else:
                stop = index + 1
                count += 1
                break

# Выводим ответ в нужном виде
    if count == 0:
        new_tuple = ()
    elif count == 1:
        new_tuple = tup[start:]
    elif count == 2:
        new_tuple = tup[start:(stop)]

    return new_tuple

print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))


'''
Задача 3. Функция
Что нужно сделать

Напишите функцию, которая на вход принимает кортеж и какой-то случайный элемент (его можно вводить с клавиатуры). Функция должна возвращать новый кортеж, начинающийся с первого появления элемента в нём и заканчивающийся вторым его появлением включительно.
Если элемента нет вовсе — вернуть пустой кортеж.
Если элемент встречается только один раз — вернуть кортеж, который начинается с этого элемента и идёт до конца исходного.
Основной код оставьте пустым или закомментированным (используйте его только для тестирования).

Пример вызова функции:

print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
Ответ в консоли: (2, 3, 4, 5, 6, 7, 8, 2)
'''