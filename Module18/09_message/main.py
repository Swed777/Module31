# TODO здесь писать код

text = input('Сообщение: ').split()
punktuation = ',.!?:;'
result = []

print('Новое сообщение: ', end='')

for word in text:
    new_word = ''
    new_word_all = ''
    new_text_all = ''
    for letter in word:
        if not letter in punktuation:
            new_word += letter
        else:
            new_word_all += new_word[::-1] + letter
            new_word = ''
    new_word_all += new_word[::-1]
    new_text_all += new_word_all
    result.append(new_text_all)

print(' '.join(result))

# зачтено
