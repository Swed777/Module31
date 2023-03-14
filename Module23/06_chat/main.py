# TODO здесь писать код
import colorama
from colorama import Fore, Style

while True:
    colorama.init()
    name = input(Fore.LIGHTBLUE_EX + '\nВведите Ваше имя: ')
    print(
        Fore.LIGHTBLUE_EX + f'Привет, {name}! Что ты хочешь? \n1. Посмотреть текущий текст чата  \n2. Отправить сообщение  \n0. Завершить чат\n')
    number = int(input())
    if number == 1:
        with open('chat.txt', 'r', encoding='utf8') as open_chat:
            print(Fore.WHITE)
            for i_message in open_chat:
                print(i_message, end='')
    if number == 2:
        message = input('Введите сообщение: ')
        with open('chat.txt', 'a', encoding='utf8') as open_chat:
            open_chat.write(f'{name}:  {message}\n')
    if number == 0:
        print(Fore.RED + Style.DIM + 'Чат завершен :(')
        break

# зачтено
