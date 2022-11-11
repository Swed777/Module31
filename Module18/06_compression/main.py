# TODO здесь писать код

text = input('Введите строку: ')
final = []
result, temp = [], []
last_elem = text[0]

for elem in text:  # Находим список повторяющиеся элементы в строке
    if elem == last_elem:
        temp.append(elem)
    else:
        result.append(temp)  # Формируем список из списков повторяющихся элементов
        temp = [elem]
        last_elem = elem
result.append(temp)

for i in range(len(result)):
    final.append(result[i][0])
    final.append(str(len(result[i])))

print('Закодированная строка:', ''.join(final))

# [temp.append(elem) if elem == last_elem for elem in text]

# зачтено
