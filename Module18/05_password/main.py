# TODO здесь писать код

count_dig = 0
count_upper = 0

while True:
    password = input('Придумайте пароль: ')
    if len([count_dig + 1 for i in password if
            i in '0123456789']) < 3:  # Проходим по паролю, определяем количество цифр
        print('Пароль ненадежный. Попробуйте еще раз. ')
    elif password.islower() == True:
        print('Пароль ненадежный. Попробуйте еще раз. ')
    else:
        print('Это надёжный пароль!')
        break

# зачтено
