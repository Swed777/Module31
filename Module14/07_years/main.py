# TODO здесь писать код

def year(year_min, year_max):
    for x in range(year_min, year_max + 1):
        similar_num(x)
'''def similar_num(x):
    one = x // 1000
    two = x % 1000 // 100
    three = x % 100 // 10
    four = x % 10
    if one == two
'''
def similar_num(x):
    count = 0
    x = str(x)
    for i in x:
        for j in (x):
            if i == j:
                count += 1
                if count >= 3:
                    print(x)

year_min = int(input('Введите первый год: '))
year_max = int(input('Введите второй год: '))

print(f'Годы от {year_min} до {year_max} с тремя одинаковыми цифрами:')
year(year_min, year_max)