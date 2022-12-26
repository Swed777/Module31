# TODO здесь писать код
def slicer(tup, num):
    # new_tuple = (tup.index(tup[1]))
    new_tuple = tup[tup.index(tup[1]):]
    return new_tuple


print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))

print('________________')
# tuple_1 = ((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2)
# print(tuple_1[1])
# print([i for i, value in enumerate(tuple_1[0])])
