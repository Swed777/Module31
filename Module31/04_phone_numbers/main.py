# TODO здесь писать код
import re
from typing import List

def test_number(tlf, pattern):
    test = {re.findall(pattern, tlf) for i in tlf_orig}
    if test:
        yield f'всё в порядке {test}'
    else:
        yield f'не подходит {test}'

tlf_orig : List[str] = ['9999999999', '999999-999', '99999x9999']
pattern = r'\b[89]\d{9}'

test =  re.findall(r'\b[89]\d{9}', str(tlf_orig))
print(test)

print(test_number(tlf_orig, pattern))



'''
Задача 4. Телефонные номера
Что нужно сделать
В одной организации перед записью телефонного номера в базу данных его проверяют на соответствие следующим критериям:

Длина номера — ровно десять знаков.
Номер начинается с цифры 8 или 9.
Остальные знаки — только цифры.
На вход в программу подаётся список номеров (можно взять готовый или запросить у пользователя).
Реализуйте код, который проверяет каждый номер из списка на соответствие критериям
и выводит на экран соответствующие сообщения.

Пример списка:
['9999999999', '999999-999', '99999x9999']

Результат:
первый номер: всё в порядке
второй номер: не подходит
третий номер: не подходит
'''