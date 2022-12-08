# TODO здесь писать код

number = int(input('Введите количество человек: '))
list_all = {}
level_elem = {}

for i in range(1, number):
    descendant, parent = input(f'{i} пара: ').split()
    list_all[descendant] = parent
    level_elem[descendant] = 0
    level_elem[parent] = 0

for i in list_all:
    people = i
    while people in list_all:
        people = list_all[people]
        level_elem[i] += 1

print('\n“Высота” каждого члена семьи:')
for i in sorted(level_elem):
    print(i, level_elem[i])

# зачтено
