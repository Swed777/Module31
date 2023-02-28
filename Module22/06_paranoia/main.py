# TODO здесь писать код

import string

# Шифр цезаря
with open('text.txt', 'r', encoding='utf8') as text:
    for delta, text_translate in enumerate(text.readlines(), 1):
        lower = (string.ascii_lowercase[delta:] + string.ascii_lowercase[:delta])
        translate = {ord(a): d for (a, d) in zip(string.ascii_letters, (lower + lower.upper()))}
        result = str.translate(text_translate, translate)

        print(result)







'''
Задача 6. Паранойя
Что нужно сделать

Артуру постоянно кажется, что за ним следят и все хотят своровать «крайне важную информацию» с его компьютера, включая переписку с людьми. Поэтому он эти переписки шифрует. И делает это с помощью шифра Цезаря (чем веселит агента службы безопасности).
Напишите программу, которая шифрует содержимое текстового файла text.txt шифром Цезаря, при этом символы первой строки файла должны циклически сдвигаться на один, второй строки — на два, третьей строки — на три и так далее. Результат выведите в файл cipher_text.txt.
Пример:

Содержимое файла text.txt:
Hello
Hello
Hello
Hello

Содержимое файла cipher_text.txt:
Ifmmp
Jgnnq
Khoor
Lipps'''