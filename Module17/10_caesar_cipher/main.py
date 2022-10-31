# TODO здесь писать код

text = input('Введите сообщение: ')
key = int(input('Введите сдвиг: '))
dictionary = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
res = []

for i in range(len(text)):
    if text[i] in dictionary:
        for j in range(len(dictionary)):
            if 0 <= j + key < len(dictionary) and text[i] == dictionary[j]:
                res.append(dictionary[j + key])
            elif j + key >= len(dictionary) and text[i] == dictionary[j]:
                res.append(dictionary[(1 - j - key) % (len(dictionary) - 1)])
            elif j + key < 0 and text[i] == dictionary[j]:
                res.append(dictionary[(j + key) % len(dictionary)])

print('Зашифрованное сообщение: ', ''.join(res))

# Никита - подскажите, как в зашифрованном сообщении поставить пробел? Сломался на этом моменте ((
