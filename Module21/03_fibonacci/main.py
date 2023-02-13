# TODO здесь писать код

def fbn(num_pos):
    if num_pos == 0:
        return 0
    if num_pos == 1:
        return 1
    else:
        return fbn(num_pos - 1) + fbn(num_pos - 2)


num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
print(f'Число: {fbn(num_pos)}')

# зачтено
