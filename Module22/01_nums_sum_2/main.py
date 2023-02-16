# TODO здесь писать код

file = open('numbers.txt', 'r')
sum = 0
array = tuple()

for i_line in file:
    num_line = tuple(i_line.split())
    array += num_line
print(array)

for i in array:
    sum += int(i)

file.close()

file_2 = open('answer.txt', 'w')
file_2.write(str(sum))
file_2.close()

#  Печатаем для проверки
print('Сумма чисел в файле = ', sum)

'''
Задача 1. Сумма чисел 2
Что нужно сделать
Во входном файле numbers.txt записано N целых чисел, которые могут быть разделены пробелами и концами строк. Напишите программу, которая выводит сумму чисел в выходной файл answer.txt.
Пример:
Содержимое файла numbers.txt
     2
2
  2
        2

Содержимое файла answer.txt
8
'''