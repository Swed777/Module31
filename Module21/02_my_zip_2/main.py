# TODO здесь писать код

def my_zip_2(*args):
    min_len = min(map(len, args))
    tpl = (tuple(elem[i] for elem in args) for i in range(min_len))
    return tpl


x = ['aa', 'b', {'c': 777}, 'd']
y = (1, [2], 'three', 4)

final_zip_2 = my_zip_2(x, y)
print(list(final_zip_2))

# зачтено
