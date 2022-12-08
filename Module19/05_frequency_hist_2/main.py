# TODO здесь писать код

def forvard(text):
    print('------------------------')
    print('Оригинальный словарь частот: ')
    frequency = {}
    for symbol in text:
        if symbol in frequency:
            frequency[symbol] += 1
        else:
            frequency[symbol] = 1
    [print(letter, ':', freq) for letter, freq in frequency.items()]
    return frequency


def invert(frequency):
    print('------------------------')
    print('Инвертированный словарь частот: ')
    inverse = {}
    for key in frequency:
        val = frequency[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    [print(i, ':', inverse[i]) for i in inverse]


text = input("Введите текст: ")
frequency = forvard(text)
invert(frequency)

# зачтено
