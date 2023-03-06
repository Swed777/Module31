# TODO здесь писать код

import string

# Шифр цезаря
with open('text.txt', 'r', encoding='utf8') as text:
    for delta, text_translate in enumerate(text.readlines(), 1):
        lower = (string.ascii_lowercase[delta:] + string.ascii_lowercase[:delta])
        translate = {ord(a): d for (a, d) in zip(string.ascii_letters, (lower + lower.upper()))}
        result = str.translate(text_translate, translate)
        with open('cipher_text.txt', 'a', encoding='utf8') as out_cifer:
            out_cifer.write(result)
            print(result)

# зачтено
