# TODO здесь писать код

quantity = int(input('Количество стран: '))
country_city = {}

# Формируем словать, при этом страна является ключем, а города - значением. По каждой стране - 3 пары
for i in range(quantity):
    country = input(f'Название {i + 1} страны и 3 городов: ').split()
    for city in country[1:]:
        country_city[city] = country[0]

for i in range(3):
    city = input('Введите город: ')
    if city not in country_city:
        print(f'По городу {city} данных нет')
    else:
        print(f'Город {city} расположен в стране : {country_city[city]} ')

# зачтено
