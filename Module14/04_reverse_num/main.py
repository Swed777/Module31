def rotate(x):  # переворот числа наоборот
    rotate_num = 0
    while x != 0:
        num = x % 10
        rotate_num = (rotate_num * 10) + num
        x = x // 10
    print(rotate_num)
    return (rotate_num)
def integer(x):
    intgr = int(x)
    rotate(intgr)
    return(intgr)

def decimal(x):  # Находим дробную часть
    dec = int((x % 1) * 100)
    rotate(dec)
    return()


n = float(input('Введите первое вещественное число: '))
k = float(input('Введите второе вещественное число: '))

print('\nПервое число наоборот: ', integer(n), decimal(n))
print('\nВторое число наоборот: ', decimal(k), decimal(k))
