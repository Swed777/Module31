# TODO здесь писать код

ip_address = input('Введите IP: ')

error_count = 0
for i in ip_address.split('.'):
    if i.isdigit() == False:
        print(i, '- это не целое число')
        error_count += 1
    elif int(i) > 255:
        print(i, '- превышает 255')
        error_count += 1
    if ',' in ip_address:
        print('Адрес должен быть разделен точками.')
        error_count += 1
if len(ip_address.split('.')) != 4:
    print('Адрес должен состоять из 4 чисел')
    error_count += 1
if error_count == 0:
    print('IP адрес корректен')

# Никита - я разделил проверку на наличие 4 чисел и наличие запятой по отдельности. Если это излишне - поправьте пож

# Все верно сделали, но сделали это не оптимально.
# Надо было сделать так:
ip_address = input('Введите IP: ')
split_address = ip_address.split('.')
if len(split_address) == 4:
    for i in split_address:
        # Лучше использовать отрицание not, а не равенство значению False
        if not i.isdigit():
            print(i, '- это не целое число')
            # Вместо увеличения счетчика останавливаем цикл
            break
        elif int(i) > 255:
            print(i, '- превышает 255')
            # Вместо увеличения счетчика останавливаем цикл
            break
    # Добавляем блок else к циклу, который выполнится только тогда,
    # когда цикл пройдет полностью без прерываний, т.е. когда не будет ни одной ошибки
    else:
        print('IP адрес корректен')
else:
    print('Адрес должен состоять из 4 чисел')
# И при таком подходе не нужно даже проверять наличие запятой, для чего бы вы это не делали
