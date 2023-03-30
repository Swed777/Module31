# TODO здесь писать код
import random
class House:
    food_icebox = 50
    money_box = 0
class People:
    def __init__(self, name, satiety = 50):
        self.name = name
        self.satiety = satiety

    def eat(self):  # ест
        self.satiety += 1
        House.food_icebox -= 1
        return f'ест, сытость {self.satiety} еда {House.food_icebox}'

    def work(self):  # работает
        self.satiety -= 1
        House.money_box += 1
        return f'работает, сытость {self.satiety} деньги {House.money_box}'

    def play(self):  # играет
        self.satiety -= 1
        return f'игрет, сытость {self.satiety}'

    def market(self):  # ходит в магазин
        House.food_icebox += 1
        House.money_box -= 1
        return f'Магазин, холодильник {House.food_icebox} деньги {House.money_box}'


Artem = People('Артем')
eat = People.eat
market = People.market
work = People.work
info = ''
for i_day in range(1, 366):
    cub = random.randint(1,6)
    if Artem.satiety < 20:
        info = People.eat
    elif House.food_icebox < 10:
        info = People.market
    elif House.money_box < 50:
        info = work
    elif cub == 1:
        info = work
    elif cub == 2:
        info = eat
    else:
        info = People.play()

    print(f'День {i_day}: {info}, кубик ={cub}')
    print(f'состояние дел: еда {House.food_icebox}, деньги {House.money_box}')


'''
Задача 5. Совместное проживание
Что нужно сделать
Чтобы понять, стоит ли ему жить с кем-то или лучше остаться в гордом одиночестве, Артём решил провести необычное исследование. Для этого он реализовал модель человека и модель дома.

Человек может (должны быть такие методы):

есть (+ сытость, − еда);
работать (− сытость, + деньги);
играть (− сытость);
ходить в магазин за едой (+ еда, − деньги);
прожить один день (выбирает одно действие согласно описанному ниже приоритету и выполняет его).
У человека есть (должны быть такие атрибуты):

имя,
степень сытости (изначально 50),
дом.
В доме есть: 

холодильник с едой (изначально 50 еды), 
тумбочка с деньгами (изначально 0 денег).
Если сытость человека становится меньше нуля, человек умирает.

Логика действий человека определяется следующим образом:

Генерируется число кубика от 1 до 6.
Если сытость < 20, то нужно поесть.
Иначе, если еды в доме < 10, то сходить в магазин.
Иначе, если денег в доме < 50, то работать.
Иначе, если кубик равен 1, то работать.
Иначе, если кубик равен 2, то поесть.
Иначе играть.
По такой логике эксперимента человеку надо прожить 365 дней.

Реализуйте такую программу и создайте двух людей, живущих в одном доме. Проверьте работу программы несколько раз. 

Советы и рекомендации
В большинстве случаев классы нужны не для того, чтобы с ними работать напрямую, а чтобы с их помощью создавать объекты,
 которые будут содержать необходимую информацию и смогут вызывать нужные методы. Наш случай не исключение: 
 вам не нужно работать напрямую с классами, работайте с объектами, которые создаются при помощи этих классов.
Глобальные переменные создают зависимости. Чем больше класс обращается к переменным, созданным снаружи класса, 
тем больше в классе появляется неопределённости (для работы с классом вам придётся отслеживать значения всех этих 
переменных). По возможности передавайте нужные данные в объект и записывайте их в атрибуты вместо обращения
 к глобальной переменной.
'''