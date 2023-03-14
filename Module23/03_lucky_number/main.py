# TODO здесь писать код
import random


def random_13():  # функция с вероятностью 1/13 . ПРи срабатываении вызывает исключение
    itog = True
    chance = random.randint(1, 13)
    try:
        if chance == 13:
            itog = False
            raise Exception
    except Exception as ex:
        print('Вас постигла неудача! ')
        open_file.close()
    return itog


border_number = 777
sum_number = 0
out_file = 'out_file.txt'

while True:
    number = int(input('Введите число: '))
    if random_13():
        with open(out_file, 'a', encoding='utf8') as open_file:
            open_file.write(str(number) + '\n')

    sum_number += number
    if sum_number >= border_number:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
        open_file.close()
        break

# зачтено
