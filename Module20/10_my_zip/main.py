# TODO здесь писать код

stroke = 'abcd'
tuple_numbers = (10, 20, 30, 40)

generator = ((stroke[i], tuple_numbers[i]) for i in range(
    min(len(stroke), len(tuple_numbers))))  # проходим одновременно по строке и кортежу (по наименьшей длине)

print(generator)
print(*generator, sep='\n')  # * - извелекаем из генератора Все значения

# зачтено
