# TODO здесь писать код
def slicer(tup, num):
    # ---Определяем первый и последний одинаковый элемент в кортеже
    start, stop = 0, 0
    count = 0  # Признак наличия элемента в кортеже
    flag = False
    new_tuple = tuple()
    for index, value in enumerate(tup):
        if value == (num):
            if flag == False:
                flag = True
                count += 1
                start = index
            else:
                stop = index + 1
                count += 1
                break

# Выводим ответ в нужном виде
    if count == 0:
        new_tuple = ()
    elif count == 1:
        new_tuple = tup[start:]
    elif count == 2:
        new_tuple = tup[start:(stop)]

    return new_tuple

print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))