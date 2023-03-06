# TODO здесь писать код
import string, zipfile


alpha = string.ascii_letters
dict_text = {}
v_i_m = zipfile.ZipFile('voyna-i-mir.zip')
vim = v_i_m.open('voyna-i-mir.txt', 'r').readlines()

for i_word in vim:
        for i_letter in i_word.decode():      # decode() преобразует байты в строку Python.
            if i_letter in alpha:
                x = dict_text.get(i_letter, 0)
                dict_text[i_letter] = x + 1
dict_text_sorted = sorted(dict_text.items(), key=lambda x: (x[1]))

for i in dict_text_sorted:
    dict_text_sort = (f'{i[0]} {i[1]}')
    with open('itog.txt', 'a') as fin:
        fin.write(str(dict_text_sort) + '\n')
fin.close()



pass
'''
Задача 9. Война и мир (необязательная)
Что нужно сделать
Мало кто не знает про знаменитый роман Л. Н. Толстого «Война и мир». Это довольно объёмное произведение лежит в архиве 
voina-i-mir.zip. Напишите программу, которая подсчитает статистику по буквам (не только русского алфавита) в этом романе
и выведет результат на экран (или в файл). Результат должен быть отсортирован по частоте встречаемости букв 
(по возрастанию или убыванию). Регистр символов имеет значение.
Постарайтесь написать программу так, чтобы для её работы не требовалась распаковка архива «вручную».
'''