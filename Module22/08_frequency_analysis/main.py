# TODO здесь писать код

import string

# znak = string.punctuation           # punctuation  представляет строку со знаками пунктуации
# symb = string.whitespace            # whitespace содержит непечатакемые символы
alfa = string.ascii_lowercase
dict_text = {}
with open('text.txt', 'r') as open_file:
    text = open_file.readlines()
    for i_word in text:
        for i_letter in i_word:
            print(i_letter)
            if i_letter in alfa:
                x = dict_text.get(i_letter, 0)
                dict_text[i_letter] = x + 1

print(dict_text)



'''
Задача 8. Частотный анализ
Что нужно сделать
Есть файл text.txt, который содержит текст. Напишите программу, которая выполняет частотный анализ, определяя долю каждой буквы английского алфавита в общем количестве английских букв в тексте, и выводит результат в файл analysis.txt. Символы, не являющиеся буквами английского алфавита, учитывать не нужно. 
В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте, с тремя знаками в дробной части. Буквы должны быть отсортированы по убыванию их доли. Буквы с равной долей должны следовать в алфавитном порядке.

Пример:
Содержимое файла text.txt:
Mama myla ramu.

Содержимое файла analysis.txt:
a 0.333
m 0.333
l 0.083
r 0.083
u 0.083
y 0.083
'''