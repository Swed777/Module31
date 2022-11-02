# TODO здесь писать код

text = input('Введите строку: ')

result, temp = [], []
last_elem = text[0]

for elem in text:               # Находим список повторяющиеся элементы в строке
    if elem == last_elem:
        temp.append(elem)
    else:
        result.append(temp)     # Формируем список из списков повторяющихся элементов
        temp = [elem]
        last_elem = elem
result.append(temp)

for i in range(len(result)):
    print(len(result[i]), result[i][0])

print(temp, len(temp), temp[0])

# [temp.append(elem) if elem == last_elem for elem in text]