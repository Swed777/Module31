# TODO здесь писать код

import random
class Warrior:
    def __init__(self, name, health = 100, power= 20):
        self.name = name
        self.health = health
        self.power = power


    def __str__(self):
        return f'Игрок: {self.name} | Здоровье: {self.health}'

    def attack(self, other: 'Warrior'):
        print(f'{self.name} атаковал {other.name}!')
        return other.damage(self.power)

    def damage(self, power: int = 20):
        self.health -= power
        is_dead = self.health <= 0

        if not is_dead:
            print(f'У {self.name} осталось {self.health} здоровья!')
        else:
            print(f'{self.name} умер!!!')

        return is_dead


war1 = Warrior(name='Воин 1')
war2 = Warrior(name='Воин 2')

while war1.health > 0 and war2.health > 0:
    turn = random.randint(0, 101)
    if turn < 50:
        war1.attack(war2)
    else:
        war2.attack(war1)


'''
Задача 1. Драка
Что нужно сделать
Вы работаете в команде разработчиков мобильной игры, и вам досталась часть от ТЗ заказчика.

Есть два юнита, каждый называется «Воин». Каждому устанавливается здоровье в 100 очков. 
Они бьют друг друга в случайном порядке. Тот, кто бьёт, здоровье не теряет. 
У того, кого бьют, оно уменьшается на 20 очков от одного удара. После каждого удара надо выводить сообщение, 
какой юнит атаковал и сколько у противника осталось здоровья. 
Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.
Реализуйте такую программу.

Что оценивается
Результат вычислений корректен.
Модели реализованы в стиле ООП, основной функционал описан в методах классов и отдельных функциях.
Сообщения о процессе получения результата осмысленны и понятны для пользователя.
Переменные, функции и собственные методы классов имеют значащие имена, не a, b, c, d.'''