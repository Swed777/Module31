# TODO здесь писать код

while True:
    name = input('Введите Ваше имя: ')
    print(f'Привет, {name}! Что ты хочешь? \n1. Посмотреть текущий текст чата  \n2. Отправить сообщение')
    number = int(input())
    if number == 1:
        print('1')
    if number == 2:
        print('2')

# ДОбвить файл с чатом, добавление в него сообщения и чтение всего файла

'''
Задача 4. Чат
Что нужно сделать
Реализуйте программу — чат, в котором могут участвовать сразу несколько человек, то есть программу, которая может работать одновременно для нескольких пользователей. При запуске запрашивается имя пользователя. После этого он выбирает одно из действий:

Посмотреть текущий текст чата.
Отправить сообщение (затем вводит сообщение).
Действия запрашиваются бесконечно. 

Примечание: для решения задачи вам достаточно текущих знаний, нужно лишь проявить немного фантазии и хитрости. Не углубляйтесь в дебри работы с сетями, создание GUI-приложений и прочее. Однако, если очень хочется, то останавливать вас никто не будет!

Что оценивается
Результат вычислений корректен.
Основной функционал описан в отдельных функциях.
Переменные и функции имеют значащие имена, а не только a, b, c, d (подробнее об этом в видео 2.3).
Входные и выходные файлы названы так, как указано в задании.
Сообщения об ошибках осмысленные и понятные для пользователя.
'''