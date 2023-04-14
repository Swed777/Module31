# TODO здесь писать код
import random


class House:
    food_icebox = 50
    money_box = 0


class People:
    def __init__(self, name, satiety=50):
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
Katya = People('Катя')
info_A = ''
info_K = ''

for i_day in range(1, 366):
    if Artem.satiety < 0:
        print(f'К сожалению, {Artem.name} не дожил до конца эксперимента )')
        break
    if Katya.satiety < 0:
        print(f'К сожалению, {Katya.name} не дожила до конца эксперимента )')
        break
    cub = random.randint(1, 6)
    if Artem.satiety < 20 or Katya.satiety < 20:
        info_A = Artem.eat()
        info_K = Katya.eat()
    elif House.food_icebox < 10:
        info_A = Artem.market()
    elif House.money_box < 50:
        info_K = Katya.work()
    elif cub == 1:
        info_K = Katya.work()
    elif cub == 2:
        info_A = Artem.eat()
    else:
        info_A = Artem.play()
        info_K = Katya.play()

    print(f'День {i_day}: \n{Artem.name} {info_A} \n{Katya.name} {info_K} \nкубик ={cub}')
    print(f'состояние дел: еда {House.food_icebox}, деньги {House.money_box}')
print('**** Ура, выжили! **** ')

# зачтено
