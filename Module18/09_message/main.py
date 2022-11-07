# TODO здесь писать код

text = input('Сообщение: ')

for i in text.split():
    new_text = text[::-1]
    print('Новое сообщение: ', new_text)