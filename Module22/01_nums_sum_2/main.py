# TODO здесь писать код

file = open('numbers.txt', 'r')
sum = 0
array = tuple()

for i_line in file:
    num_line = tuple(i_line.split())
    array += num_line

for i in array:
    sum += int(i)

file.close()

file_2 = open('answer.txt', 'w')
file_2.write(str(sum))
file_2.close()

#  Печатаем для проверки
print('Сумма чисел в файле = ', sum)

# зачтено
