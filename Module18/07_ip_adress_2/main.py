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
