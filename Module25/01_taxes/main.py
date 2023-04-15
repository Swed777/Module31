# TODO здесь писать код
class Property:
    """
    Property: базовый класс, описывает имущество налогоплательщиков. Использует стоимость имущества и метод начисления налога
    attr: worth: стоимость имущества
    """
    def __init__(self, worth):
        # self.__worth = self.set_worth(worth)
        self.__worth = worth
    def tax(self):
        return self.get_worth() * self.get_quoter()

    def set_worth(self):
        return self.__worth
    def get_worth(self):
        return self.__worth


class Apartment(Property):
    def __init__(self, worth):
        Property.__init__(worth)
    def tax(self):
        self.quoter = 1000
        return self.quoter

class Car(Property):
    pass
class CountryHouse(Property):
    pass

kvartira = Apartment(33)
# print('Налог на квартиру: {}'.format(kvartira.tax))
print(kvartira.tax())

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