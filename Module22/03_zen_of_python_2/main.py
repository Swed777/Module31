# TODO здесь писать код
import os

# Вариант открытия файла по абсолютному пути
# file = open('/Users/ei/Desktop/Linux/Python_basic/Module22/Module22/02_zen_of_python/zen.txt', 'r')

file = open(os.path.join('..', '02_zen_of_python' , 'zen.txt'), 'r') # Открытие файла через относительный путь
text_of_file = file.readlines()
num_of_sumbol = 0
num_of_words = 0
num_of_stroke = 0
letters = {}
alfa_beta = 'abcdefghijklmnopqrstuvwxyz'
min_letter = ''

for i_str in text_of_file:
    num_of_sumbol += (len(i_str) - i_str.count(' ')) # Подсчитываем длину символов в каждой строке и вычитаем пробелы
    num_of_words += len(i_str.split(' '))
    num_of_stroke += 1

    dict_letter = {}             # формируем словарь букв по каждой строчке
    for letter in i_str.lower():
        if letter in alfa_beta:
            dict_letter[letter] = i_str.count(letter)

    for k, v in dict_letter.items():     #добавляем буквы из конкретной строчки в общую копилку
        if k in letters:
            letters[k] += v
        else:
            letters[k] = v


min_nunber_letter = min(letters.values())       #Определяем минимальное значение в общем словаре букв

print('Количество букв в файле:',   num_of_sumbol)
print('Количество слов в файле:',   num_of_words)
print('Количество строк в файле:',  num_of_stroke)
for k, v in letters.items():  # если значение конкретного элемента словаря равно минимальному значению
    if v ==  min_nunber_letter:
        print('Наиболее редкая буква: ',  k)

file.close()


'''
Задача 3. Дзен Пайтона 2
Что нужно сделать
Напишите программу, которая определяет, сколько букв (латинского алфавита), слов и строк в файле zen.txt (который содержит всё тот же Дзен Пайтона). Выведите три найденных числа на экран.
Дополнительно: выведите на экран букву, которая встречается в тексте наименьшее количество раз.
Обратите внимание, что регистр буквы не имеет значение. (А и а - одинаковые буквы).

Формат вывода:

Количество букв в файле: 
Количество слов в файле: 
Количество строк в файле: 
Наиболее редкая буква: 
'''