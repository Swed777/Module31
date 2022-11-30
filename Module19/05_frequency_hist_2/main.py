# TODO здесь писать код

# Задача 3. Гистограмма частоты

# Лингвистам нужно собрать данные о частоте букв в тексте, исходя из этих данных будет строиться гистограмма частоты букв.
# Напишите программу, которая получает сам текст и считает, сколько раз в строке встречается каждый символ.
# На экран нужно вывести содержимое в виде таблицы, отсортированное по алфавиту, а также максимальное значение частоты.

# Пример:
# Введите текст: Здесь что-то написано
#
#   : 2
# - : 1
# З : 1
# а : 2
# д : 1
# е : 1
# и : 1
# н : 2
# о : 3
# п : 1
# с : 2
# т : 2
# ч : 1
# ь : 1
# Максимальная частота: 3

text = input("Введите текст: ")
# def forvard(text):
print('Оригинальный словарь частот: ')
frequency = {}
for symbol in text:
        if symbol in frequency:
            frequency[symbol] += 1
        else:
            frequency[symbol] = 1

for letter, freq in frequency.items():
        print(letter, ':', freq)

print("Максимальная частота: ", max(frequency.values()))
    # print("Максимальная частота: ", max(frequency.values()))

# def invert(frequency):
print('Инвертированный словарь частот: ')
inverse = dict()
for key in frequency:
        val = frequency[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
        print(inverse)
    # return inverse

# text = input("Введите текст: ")
# frequency = forvard(text)
# invert(frequency)