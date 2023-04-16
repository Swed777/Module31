# TODO здесь писать код
import random
class Buddhist:
    def __init__(self, karma=0):
        self.karma = karma
    def get_karma(self):
        return self.karma
    def set_karma(self, more_carma):
        self.karma += more_carma
class KillError(Exception):
    def __str__(self):
        return 'Убийство'
class DrunkError(Exception):
    def __str__(self):
        return 'Напился'
class CarCrashError(Exception):
    def __str__(self):
        return 'Разбил машину'
class GluttonyError(Exception):
    def __str__(self):
        return 'Лопнул от переедания'
class DepressionError(Exception):
    def __str__(self):
        return 'От депрессии прыгнул со скалы'

def one_day(day_number):
    if random.randint(1, 10) == 7:
        with open('karma.log', 'a', encoding='utf-8') as karma_log:
            misconduct = random.choice([KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()])
            karma_log.write(f'На {day_number} день совершен проступок: -> {misconduct}\n')
            raise misconduct
    else:
        return random.randint(1, 7)

buddhist = Buddhist()
day = 0
while buddhist.get_karma() < 500:
    day += 1
    if one_day(day):
        pass
    else:
        buddhist.set_karma(one_day(day))
print(('Просветлен!!!'))

'''
Задача 2. Карма
Что нужно сделать
Один буддист-программист решил создать свой симулятор жизни, в котором нужно набрать 500 очков кармы (это константа), 
чтобы достичь просветления.
Каждый день вызывается специальная функция one_day(), которая возвращает количество кармы от 1 до 7 и может
с вероятностью 1 к 10 выкинуть одно из исключений:
KillError,
DrunkError,
CarCrashError,
GluttonyError,
DepressionError.
(Исключения нужно создать самостоятельно, при помощи наследования от Exception.)
Напишите такую программу. Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
кармы до уровня константы. 
Исключения обработайте и запишите в отдельный лог karma.log.
По итогу у вас может быть примерно такая структура программы:
открываем файл
цикл по набору кармы
   try
      карма += one_day()
   except(ы) с указанием классов исключений, которые нужно поймать
      добавляем запись в файл
закрываем файл
'''