# TODO здесь писать код

max_number = int(input('Введите максимальное число: '))
full_set = set(i for i in range(1, max_number + 1))         # Формируем множество всего диапазона чисел

while True:
    need_number = input('Нужное число есть среди вот этих чисел: ')
    if need_number == 'Помогите!':
        break
    need_number_int = []
    for x in need_number.split():                        # Формируем  список целых чисел
      need_number_int.append(int(x))

    many = set(need_number_int)                   # Формируем множество, которое будем вычитать из всего диапазона

    artem = input('Ответ Артема: ')
    if artem == 'Да':
        full_set &= many
    else:
        full_set -= many

print('Артём мог загадать следующие числа: ', *full_set)        #  * - оператор раскрытия (в данном контексте), т. е. если мы передаём в функцию список без звёздочки, то ей передаётся список целиком, как один аргумент, а со звёздочкой каждый элемент будет отдельно.

