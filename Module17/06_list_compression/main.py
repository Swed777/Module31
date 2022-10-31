# TODO здесь писать код


import random

number = int(input('Количество чисел в списке: '))
original_list = [random.randint(0, 2) for _ in range(number)]
print('Список до сжатия', original_list)
print('Список после сжатия: ', [i for i in original_list if i > 0])

# зачтено
