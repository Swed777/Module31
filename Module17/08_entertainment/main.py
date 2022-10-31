# TODO здесь писать код
sticks = int(input('Кол-во палок: '))
throws = int(input('Кол-во бросков: '))

row = ['l'] * sticks

for i in range(throws):
    query = 'Бросок ' + str(i + 1) + '. Сбиты палки с номера '
    while True:
        start = int(input(query)) - 1
        if (start >= 0) and (start <= sticks):
            break
    while True:
        end = int(input('по номер ')) - 1
        if (end >= start) and (end <= sticks):
            break
    for j in range(start, end + 1):
        row[j] = '.'

print('Результат: ', *row, sep='')

# зачтено
