# TODO здесь писать код

text = input("Введите строку: ")
max_len = 0
max_word = ''

for word in text.split():
      if len(word) > max_len:
            max_len = len(word)
            max_word = word

print('Самое длинное слово: {0} \nДлина этого слова: {1}'.format(max_word, max_len))
