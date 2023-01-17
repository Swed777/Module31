# TODO здесь писать код

def rand_l():
    rand_list = []
    [rand_list.append(random.randint(0, 9)) for i in range(10)]
    print('Оригинальный лист: ', rand_list)
    list_1, list_2 = rand_list[::2], rand_list[1::2]  # ФОрмируем списки из нечетных и четных позиций
    return list_1, list_2


def pair_l(list_1, list_2):
    new_list = []
    [new_list.append(pair) for pair in zip(list_1, list_2)]
    return new_list


import random  # randint()	Возвращает случайное число в пределах заданного промежутка

list_1, list_2 = rand_l()
print('Новый список:      ', pair_l(list_1, list_2))

# зачтено
