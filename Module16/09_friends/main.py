# TODO здесь писать код

N = int(input('Введите количество друзей:           '))
frends_list = [0] * N           # Формируем список из N  друзей с нулевым балансом у каждого
K = int(input('Введите количество долговых распиок: '))
print()

for receipt in range(1, K + 1):
    print(f'\n{receipt}-я расписка: ')
    for_people = int(input('Кому:     '))   # отрицаельно, - тот, кто деньги должен вернуть
    from_people = int(input('От кого:  '))  # положительно, - тот, кто деньги должен получить
    how_march = int(input('Сколько?  '))
    frends_list[for_people - 1] -= how_march    # Вычитаем у должника
    frends_list[from_people - 1] += how_march   # ДОбавляем получателю

print('Баланс друзей: ')
for i in range(len(frends_list)):
    print(i + 1 , ':', frends_list[i])