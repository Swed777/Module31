# TODO здесь писать код

stroke = input('Введите строку: ').lower()
dict_stroke = {}
case_letter = "abcdefghijklmnopqrstuvwxyzабвгдежзийклмнопрстуфхцчшщэюя"

for letter in stroke:  # Формируем словарь с количеством букв в нашей строке
    if letter in dict_stroke.keys():
        dict_stroke[letter] += 1
    elif letter in case_letter:
        dict_stroke[letter] = 1

# print(dict_stroke)
condition = True  # Переменная для вывода на печать
odd_count = 0
for letter in dict_stroke:
    if dict_stroke[letter] % 2 == 1:
        odd_count += 1
        if odd_count > 1:
            condition = False

if condition == True:
    condition = 'Можно'
else:
    condition = 'Нельзя'

print(f'{condition} сделать палиндромом')

# зачтено
