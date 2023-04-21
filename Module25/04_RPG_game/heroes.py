import random

class Hero:
    # Базовый класс, который не подлежит изменению
    # У каждого наследника будут атрибуты:
    # - Имя
    # - Здоровье
    # - Сила
    # - Жив ли объект
    # Каждый наследник будет уметь:
    # - Атаковать
    # - Получать урон
    # - Выбирать действие для выполнения
    # - Описывать своё состояние

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)

    def get_power(self):
        return self.__power

    def set_power(self, new_power):
        self.__power = new_power

    def is_alive(self):
        return self.__is_alive

    # Все наследники должны будут переопределять каждый метод базового класса (кроме геттеров/сеттеров)
    # Переопределенные методы должны вызывать методы базового класса (при помощи super).
    # Методы attack и __str__ базового класса можно не вызывать (т.к. в них нету кода).
    # Они нужны исключительно для наглядности.
    # Метод make_a_move базового класса могут вызывать только герои, не монстры.
    def attack(self, target):
        # Каждый наследник будет наносить урон согласно правилам своего класса
        raise NotImplementedError("Вы забыли переопределить метод Attack!")

    def take_damage(self, damage):
        # Каждый наследник будет получать урон согласно правилам своего класса
        # При этом у всех наследников есть общая логика, которая определяет жив ли объект.
        print("\t", self.name, "Получил удар с силой равной = ", round(damage), ". Осталось здоровья - ", round(self.get_hp()))
        # Дополнительные принты помогут вам внимательнее следить за боем и изменять стратегию, чтобы улучшить выживаемость героев
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        # С каждым днём герои становятся всё сильнее.
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        # Каждый наследник должен выводить информацию о своём состоянии, чтобы вы могли отслеживать ход сражения
        raise NotImplementedError("Вы забыли переопределить метод __str__!")

class Healer(Hero):
    # Целитель:
    def __init__(self, name):
        super().__init__(name)
    # Атрибуты:
    # - магическая сила - равна значению НАЧАЛЬНОГО показателя силы умноженному на 3 (self.__power * 3)
        self.magic_force = self.get_power() * 3

    # Методы:
    # - атака - может атаковать врага, но атакует только в половину силы self.__power
    def attack(self, target):
        target.take_damage(self.get_power() // 2)
        raise NotImplementedError("Вы забыли переопределить метод Attack!")

    # - получение урона - т.к. защита целителя слаба - он получает на 20% больше урона (1.2 * damage)
    def take_damage(self, damage):
        super().take_damage(damage * 1.2)

    # - исцеление - увеличивает здоровье цели на величину равную своей магической силе
    def heal(self, target):
        target.set_hp(target.get_hp() + self.magic_force)

    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # исцеление) на выбранную им цель
    def make_a_move(self, friends, enemies):
        print(self.name, end=' ')
        target_of_potion = friends[0]
        min_health = target_of_potion.get_hp()
        for friend in friends:
            if friend.get_hp() < min_health:
                target_of_potion = friend
                min_health = target_of_potion.get_hp()
        if min_health < 60:
            print('Провожу исцеление:', target_of_potion.name)
            self.heal(target_of_potion)
        else:
            if not enemies:
                return
            print('Атакую противника:', enemies[0].name)
            self.attack(enemies[0])
        print('\n')
class Tank(Hero):
    # Танк:
    def __init__(self, name):
        super().__init__(name)
    # Атрибуты:
    # - показатель защиты - изначально равен 1, может увеличиваться и уменьшаться
        self.defense = 1
    # - поднят ли щит - танк может поднимать щит, этот атрибут должен показывать поднят ли щит в данный момент
        self.shield_status = False

    # Методы:
    # - атака - атакует, но т.к. доспехи очень тяжелые - наносит половину урона (self.__power)
    def attack(self, target):
        target.take_damage(self.get_power() // 2)

    # - получение урона - весь входящий урон делится на показатель защиты (damage/self.defense) и только потом отнимается от здоровья
    def take_damage(self, damage):
        self.set_hp(self.get_hp() - (damage / self.defense))

    # - поднять щит - если щит не поднят - поднимает щит. Это увеличивает показатель брони в 2 раза, но уменьшает показатель силы в 2 раза.
    def shield_up(self):
        if not self.shield_status:
            self.shield_status = True
            self.defense *= 2
            self.set_power(self.get_power() // 2)
            print(f"{self.name} поднимает щит!")

    # - опустить щит - если щит поднят - опускает щит. Это уменьшает показатель брони в 2 раза, но увеличивает показатель силы в 2 раза
    def shield_down(self):
        if self.shield_status:
            self.shield_status = False
            self.defense = self.defense // 2
            self.set_power(self.get_power() * 2)
            print(f"{self.name} опускает щит!")

    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # поднять щит/опустить щит) на выбранную им цель
    def make_a_move(self, friends, enemies):
        print(self.name, end=' ')
        if not enemies:
            return
        if self.get_hp() > 60:
            self.shield_down()
            print('Атакую: ', enemies[0].name)
            self.attack(enemies[0])
        else:
            self.shield_up()
            print('Атакую: ', enemies[0].name)
            self.attack(enemies[0])
        print('\n')


class Attacker(Hero):
    # Убийца:
    def __init__(self, name):
        super().__init__(name)

    # Атрибуты:
    # - коэффициент усиления урона (входящего и исходящего)
        self.__ampl_coeff = 1

    # Методы:
    # - атака - наносит урон равный показателю силы (self.__power) умноженному на коэффициент усиления урона (self.power_multiply)
    # после нанесения урона - вызывается метод ослабления power_down
    def attack(self, target):
        target.take_damage(self.get_power() * self.__ampl_coeff)
        self.power_down()

    # - получение урона - получает урон равный входящему урона умноженному на половину коэффициента усиления урона - damage * (
    # self.power_multiply / 2)
    def take_damage(self, damage):
        self.set_hp(self.get_hp() - (damage - (self.__ampl_coeff / 2)))

    # - усиление (power_up) - увеличивает коэффициента усиления урона в 2 раза
    def power_up(self):
        self.__ampl_coeff *= 2

    # - ослабление (power_down) - уменьшает коэффициента усиления урона в 2 раза
    def power_down(self):
        self.__ampl_coeff /= 2

    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # усиление, ослабление) на выбранную им цель
        def choose_action(self, allies, enemies):
            if self.__health <= 0:
                return
            target = self.__find_weakest_enemy(enemies)
            if target:
                self.attack(target)
            else:
                target = self.__find_most_damaged_ally(allies)
                if target:
                    self.power_up()
                    self.heal(target)
                    self.power_down()