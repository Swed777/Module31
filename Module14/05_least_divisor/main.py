# TODO здесь писать код

number = int(input('Введите натуральное число больше 1: '))

for i in range(number, 1, -1):
    if number % i == 0:
        min_divider = i
print(f'Наименьший делитель числа {number} = {min_divider}')

# зачтено
