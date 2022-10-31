# TODO здесь писать код

list_1 = []
list_2 = []

for number in range(3):
    number = input(f'Введите {number + 1} число для первого списка: ')
    list_1.append(number)

for number in range(7):
    number = input(f'Введите {number + 1} число для второго списка: ')
    list_2.append(number)

print('Первый список: ', list_1)
print('Второй список: ', list_2)

list_1.extend(list_2)           # объединяем два списка в один

for i in list_1:                # убираем дублирующие элементы
    while list_1.count(i) > 1:
        list_1.remove(i)

print('Новый первый список с уникальными элементами: ', '[' , ', '.join(list_1), ']')   # выводим в формате, указанном в задании
