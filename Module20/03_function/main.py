# TODO здесь писать код
def slicer(tup, num):
    # new_tuple = (tup.index(tup[1]))
    new_tuple = tup[tup.index(tup[1]):]
    return new_tuple


print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))

print('________________')
tuple_1 = ((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2)
# print(tuple_1[1])
# print([i for i, value in enumerate(tuple_1[0])] if value = (tuple_1[1]))
count = 0
for index, value in enumerate(tuple_1[0]):
    if value == (tuple_1[1]):
        start = index
        count += 1
        if count == 2:
            stop = index
            break
print(start, stop)



# Сделать цикл по 1 кортежу, определить индексы 1 и второго элемента. ДЛя отсечки
# использовать флаг (до 2 взведений)
