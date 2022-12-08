# TODO здесь писать код

number = int(input('Введите количество заказов: '))
order_list = {}

for i in range(number):  # Формируем список из каждого заказа
    order = input(f'{i + 1}-й заказ: ').split()
    fio, pizza, number = order
    number = int(number)

    if fio not in order_list:  # Преобразуем список в словарь. ключ- это фамилия, значение - словарь из названия пиццы и ее количества
        order_list[fio] = {pizza: number}
    else:
        if pizza not in order_list[fio]:
            order_list[fio][pizza] = number
        else:
            order_list[fio][pizza] += number

for key, volue in sorted(order_list.items()):
    print(key, ':')
    print('     ', volue)

# зачтено
