# TODO здесь писать код
class Property:
    """
    Property: базовый класс, описывает имущество налогоплательщиков. Использует стоимость имущества и метод начисления налога
    attr: worth: стоимость имущества
    """
    def __init__(self, worth):
        self.__worth = worth
    def get_worth(self):
        return self.__worth
    def tax(self, quoter):
        """
        Property: Величина налога. Для разных видов имущества задается отдельно
        """
        return self.__worth / quoter
class Apartment():
    def __init__(self, worth):
        self.__worth = worth
        self.__quoter = 1000

class Car():
    def __init__(self, worth):
        self.__worth = worth
    def tax(self, quoter):
        return self.__worth / quoter
class CountryHouse():
    def __init__(self, worth):
        self.__worth = worth
    def tax(self, quoter):
        return self.__worth / quoter

kv = Property(5000000)
print(kv.tax(1000))
kv1 = Property(33333)
print(kv1.tax(1000))

apart = Apartment(888888)
print(apart)

'''
Задача 1. Налоги
Что нужно сделать
Реализуйте иерархию классов, описывающих имущество налогоплательщиков. Она должна состоять из базового класса Property
и производных от него классов Apartment, Car и CountryHouse.

Базовый класс должен иметь атрибут worth (стоимость), который передаётся в конструктор, и метод расчёта налога, 
переопределённый в каждом из производных классов. 
Налог на квартиру вычисляется как 1/1000 её стоимости, на машину — 1/200, на дачу — 1/500. 

Каждый дочерний класс должен иметь конструктор с одним параметром, передающий свой параметр конструктору базового класса.
Разработайте интерфейс программы. Пусть она запрашивает у пользователя количество его денег и стоимость имущества, 
а затем выдаёт налог на соответствующее имущество и показывает, сколько денег ему не хватает (если это так).

********** Базовый старт
class Property:
    def __init__(self, worth):
        self.__worth = worth

    def get_worth(self):
        return self.__worth

    def set_worth(self):
        return self.__worth

    def tax(self, quoter):
        return self.__worth / quoter

kv = Property(5000000)
print(kv.tax(1000))


'''