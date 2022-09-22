# TODO здесь писать код
def summ_unit(number):
    sum = 0
    while (number != 0):
        sum += number % 10
        number //= 10
    print("Сумма цифр числа равна: ", sum)
    return(sum)
def quantity(number):
    sum = 0
    while number > 0:
        i = number % 10
        number //= 10
        sum += 1  # количество это +1
    print('Количество цифр в числе: ', sum)
    return (sum)

number = int(input("Введите целое число: "))
print('Разность суммы и количества цифр:', summ_unit(number) - quantity(number))

print('----------------------------------')