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





'''
Задача 8. Угадай число
Что нужно сделать

Артём и Борис играют в игру. Артём загадал натуральное число от 1 до N. Борис пытается угадать это число, для этого он называет несколько чисел подряд. Артём говорит Борису «да», если среди названных Борисом чисел есть задуманное. В противном случае Артём говорит «нет». После нескольких заданных вопросов Борис сдался и попросил вас помочь ему определить, какие числа мог задумать Артём.
Напишите программу, которая имитирует диалог Артёма и Бориса. В начале на вход подаётся число N — это максимальное число, которое мог загадать Артём. Затем Борис предполагает, что среди некоторых чисел есть то, которое загадал Артём (несколько чисел через пробел), а Артём отвечает. Так продолжается до тех пор, пока Борис не попросит помощи (пока не введётся строка «Помогите!»). В конце программы необходимо вывести, какие числа мог загадать Артём.

Пример реализации:

Введите максимальное число: 10

Нужное число есть среди вот этих чисел: 1 2 3 4 5
Ответ Артёма: Да

Нужное число есть среди вот этих чисел: 2 4 6 8 10
Ответ Артёма: Нет

Нужное число есть среди вот этих чисел: Помогите!
Артём мог загадать следующие числа: 1 3 5
'''