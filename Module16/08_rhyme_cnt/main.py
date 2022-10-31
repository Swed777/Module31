# TODO здесь писать код

numbers = int(input("Кол-во человек: "))
key = int(input("Какое число в считалке? "))
print(f'Значит, выбывает каждый {key} человек')
people_list = list(range(1, numbers + 1))
out_people = 0

for i in range(1, numbers):
    print('\nТекущий круг людей', people_list)
    start_count = out_people % len(people_list)
    print('Начало счёта с номера', people_list[start_count])
    out_people = (start_count + key - 1) % len(people_list)
    print('Выбывает человек под номером', people_list[out_people])
    people_list.remove(people_list[out_people])
print()
print('Остался человек под номером', people_list[0])