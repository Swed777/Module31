goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# TODO здесь писать код

for key in goods:
    quantity, summa = 0, 0
    for subject in store[goods[key]]:
        quantity += subject['quantity']
        summa += subject['price'] * subject['quantity']
    print(f'{key} - {quantity} штук, стоимость {summa} рублей')


'''
КОд уже работает. Нужно привести к красивому виду

for key in goods:
    # print(key, goods.get(key))
    # print(key, goods[key])
    # print(key, store[goods.get(key)])
    print(key)
    # print(store[goods[key]])
    quantity, summa = 0, 0
    for subject in store[goods[key]]:
        quantity += subject['quantity']
        summa += subject['price'] * subject['quantity']
    print(quantity, summa)
'''