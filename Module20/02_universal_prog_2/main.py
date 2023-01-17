# TODO здесь писать код
def crypto(iterable):
    return [v for i, v in enumerate(iterable) if
            is_prime(i)]  # ФОрмируем список из элементов, если их индекс является простм числом
    pass


def is_prime(number):  # фуркция для проверки простого числа
    k = 0
    for i in range(1, number + 1):
        if number % i == 0:
            k += 1
    return k == 2


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))

# зачтено
