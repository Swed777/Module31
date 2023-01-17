# TODO здесь писать код

score_nick_lst = list()

number = int(input('Сколько записей вносится в протокол? \n'))
print('Записи (результат и имя):')
for i in range(number):  # формируем список из кортежей, в каждом из которых нулевой элемент - целое число
    score_nick = input(f'{i + 1}-я запись:').split()
    score_nick[0] = int(score_nick[0])
    score_nick_lst.append(tuple(score_nick))

print('Результаты соревнований: \n-----------------------')

score_nick_lst = sorted(score_nick_lst, reverse=True)  # Сортируем по убыванию список
for i in range(3):
    print(f'{i + 1}-e место. {score_nick_lst[i][1]} ({score_nick_lst[i][0]})')

# зачтено
