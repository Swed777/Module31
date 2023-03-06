# TODO здесь писать код

import string

# Справочно, для знаний:
# znak = string.punctuation           # punctuation  представляет строку со знаками пунктуации
# symb = string.whitespace            # whitespace содержит непечатаемые символы

alfa = string.ascii_lowercase
count_letter = 0
dict_text = {}

with open('text.txt', 'r') as open_file:
    text = open_file.readlines()
    for i_word in text:
        for i_letter in i_word.lower():
            if i_letter in alfa:
                x = dict_text.get(i_letter, 0)
                dict_text[i_letter] = x + 1
                count_letter += 1
dict_text_sorted = sorted(dict_text.items(), key=lambda x: (x[1]), reverse=True)

for i in dict_text_sorted:
    dict_text_sort = (f'{i[0]} {i[1] / count_letter:.3f}')  # округляем до 3 знаков
    with open('analysis.txt', 'a') as open_analis:
        open_analis.write(str(dict_text_sort) + '\n')
open_analis.close()

# зачтено
