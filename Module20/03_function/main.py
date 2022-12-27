# TODO здесь писать код
def slicer(tup, num):
    new_tuple = tup[tup.index(tup[1]):]
    return new_tuple


print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))

print('________________')
tuple_1 = ((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2)

# ---Определяем первый и последний одинаковый элемент в кортеже
start, stop = 0, 0
count = 0               # Признак наличия элемента в кортеже
flag = False
new_tuple_1 = tuple()
for index, value in enumerate(tuple_1[0]):
    if value == (tuple_1[1]):
        if flag == False:
            flag = True
            count += 1
            start = index
        else:
            stop = index + 1
            count += 1
            break
print(start, stop)    # Убрать после отладки

if count == 0:
    new_tuple_1 = ()
elif count == 1:
    new_tuple_1 = tuple_1[0][start:]
elif count == 2:
    new_tuple_1 = tuple_1[0][start:(stop)]

print(new_tuple_1)


"""def slicer(tup, num):
    new_tuple = tup[tup.index(tup[1]):]
    return new_tuple"""