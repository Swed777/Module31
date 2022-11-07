# TODO здесь писать код

text = input('Сообщение: ')
print('Новое сообщение: ')

for word in text.split():
    new_text = word[::-1]
    print(new_text, end=' ')