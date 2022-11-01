# TODO здесь писать код

text = input("Введите строку: ")
max_word = max([word for word in text.split()])
max_word_long = max([len(word) for word in text.split()])

print('Самое длинное слово: {0} \nДлина этого слова: {1}'.format(max_word, max_word_long))

# ***********************
'''
text = input('Введите строку: ').split()
max_len = 0
max_word = ''
 
for word in text:
    if len(word) > max_len:
        max_len = len(word)
        max_word = word
 
print('Самое длинное слово:', max_word)
print('Длина этого слова:', max_len)
'''