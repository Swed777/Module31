# TODO здесь писать код
def my_lst(data):
    if not data:
        return []
    return my_lst(data[:-1]) + ([data[-1]] if not isinstance(data[-1], list) else my_lst(data[-1]))


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

print('Ответ:', my_lst(nice_list))

# зачтено
