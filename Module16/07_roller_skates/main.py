# TODO здесь писать код
skates = int(input('\nКол-во коньков: '))
skates_list = []
for i in range(skates):
    skates_size = int(input(f'Размер {i + 1}-й пары: '))
    skates_list.append(skates_size)

people = int(input('\nКол-во людей: '))
people_list = []
for i in range(people):
    leg_size = int(input(f'Размер ноги {i + 1}-го человека: '))
    people_list.append(leg_size)

print(skates_list, people_list)

people_quantity = 0
print('\nНаибольшее кол-во людей, которые могут взять ролики: ', people_quantity)