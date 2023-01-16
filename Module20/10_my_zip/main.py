# TODO здесь писать код

stroke = 'abcd'
tuple_numbers = (10, 20, 30, 40)

generator = ((stroke[i], tuple_numbers[i]) for i in range(min(len(stroke), len(tuple_numbers))))  #проходим одновременно по строке и кортежу (по наименьшей длине)

print(generator)
print(*generator, sep='\n')		# * - извелекаем из генератора Все значения



'''
Задача 10. Своя функция zip
Что нужно сделать
В самом конце собеседования вас неожиданно спросили: «Расскажите, что делает функция zip?». Чтобы произвести впечатление, вы решили не только рассказать про неё, но и написать её аналог.
Даны строка и кортеж из чисел. Напишите программу, которая создаёт генератор из пар кортежей «символ — число». Затем выведите на экран сам генератор и кортежи.

Пример:
Строка: abcd
Кортеж чисел: (10, 20, 30, 40)

Результат:
<generator object <genexpr> at 0x00000204A4234048>

('a', 10)
('b', 20)
('c', 30)
('d', 40)

Дополнительно: создайте полный аналог функции zip — сделайте так, чтобы программа работала с любыми итерируемыми типами данных.
'''