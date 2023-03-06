# TODO здесь писать код
import string
import zipfile

alpha = string.ascii_letters
dict_text = {}
v_i_m = zipfile.ZipFile('voyna-i-mir.zip')
vim = v_i_m.open('voyna-i-mir.txt', 'r').readlines()

for i_word in vim:
    for i_letter in i_word.decode():  # decode() преобразует байты в строку Python.
        if i_letter in alpha:
            x = dict_text.get(i_letter, 0)
            dict_text[i_letter] = x + 1
dict_text_sorted = sorted(dict_text.items(), key=lambda x: (x[1]))

for i in dict_text_sorted:
    dict_text_sort = (f'{i[0]} {i[1]}')
    with open('itog.txt', 'a') as fin:
        fin.write(str(dict_text_sort) + '\n')
fin.close()

# зачтено
