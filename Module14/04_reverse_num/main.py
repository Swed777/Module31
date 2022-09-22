# TODO здесь писать код

def rotate(x):  # переворот числа наоборот
    rotate_num = 0
    while x != 0:
        num = x % 10
        rotate_num = (rotate_num * 10) + num
        x = x // 10
    #    print(num, end = '')
    return (rotate_num)


def decimal(x):  # Находим дробную часть
    dec = x % 1
    intgr = int(x)
    print(x)
#    return (intgr,dec)
    rotate(intgr)
    rotate(dec)
    print(intgr, dec)


n = float(input('Введите первое вещественное число: '))
k = float(input('Введите второе вещественное число: '))

decimal(n)
print('Первое число наоборот: ', rotate(n))
print('Второе число наоборот: ', rotate(k))
