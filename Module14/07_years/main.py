# TODO здесь писать код

year_min = int(input('Введите первый год: '))
year_max = int(input('Введите второй год: '))

print('-----------------------------')
print(f'Годы от {year_min} до {year_max} с тремя одинаковыми цифрами:')

for x in range(year_min, year_max):
    one = x // 1000
    two = x % 1000 // 100
    three = x % 100 // 10
    four = x % 10
    if one == two == three or two == three == four or one == three == four or one == two == four:
        print(x)

