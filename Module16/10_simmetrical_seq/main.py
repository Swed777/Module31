# TODO здесь писать код

numbers = int(input('Введите количество чисел: '))
number_list = []

for i in range(numbers):
   i = int(input('Число: '))
   number_list.append(i)

count = 0
while number_list != number_list[::-1]:
    number_list.insert(numbers, number_list[count])
    count += 1

print('Нужно приписать чисел:', count)
print('Сами числа:', number_list[:count][::-1])