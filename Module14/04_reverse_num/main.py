def rotate(x):  # переворот части числа наоборот
    rotate_num = 0
    while x != 0:
        num = x % 10
        rotate_num = (rotate_num * 10) + num
        x = x // 10
    return (rotate_num)

n = float(input('Введите первое вещественное число: '))
rotate_n_int = rotate(int(n))                    # Переворачиваем целую часть числа
rotate_n_dec = rotate(int((n % 1) * 100))        # Переворачиваем дробную часть
k = float(input('Введите второе вещественное число: '))
rotate_k_int = rotate(int(k))                    # Переворачиваем целую часть числа
rotate_k_dec = rotate(int((k % 1) * 100))        # Переворачиваем дробную часть

print('\nПервое число наоборот: ', (rotate_n_int + rotate_n_dec/100))
print('Второе число наоборот: ', (rotate_k_int + rotate_k_dec/100))
print('Сумма:                 ', (rotate_n_int + rotate_n_dec/100) + (rotate_k_int + rotate_k_dec/100))
