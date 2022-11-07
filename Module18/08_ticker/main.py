# TODO здесь писать код
str_1 = input('Первая строка: ')
str_2 = input('Вторая строка: ')

if len(str_1) != len(str_2):
    print('Строки не равны по длине')

step = 1
flag = False
for i in range(len(str_1) - 1):
            str_2 = str_2[-1] + str_2[:-1]      # Берем последний символ из второй строки, и перемещаем его на первое место
            if str_1 == str_2:
                print(f'Первая строка получается из второй со сдвигом {step} ')
                flag = True
                break
            else:
                step += 1
if flag == False:
            print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
