# TODO здесь писать код

number = int(input('Введите количество пар слов: '))
synonim = {}

for i in range(1, number + 1):  # Формируем словарь из заданного количества пар
    duble = input(f'{i}-я пара: ').lower().split('-')
    synonim[duble[0].strip()] = duble[1].strip()

while True:  # Проверяем вхождение заданного слова в словарь
    word = input('Введите слово: ').lower().strip()
    for key, value in synonim.items():
        if word == key:
            print('Синоним: ', value)
            break
        elif word == value:
            print('Синоним: ', key)
            break
    else:
        print('Такого слова в словаре нет')

# зачтено
