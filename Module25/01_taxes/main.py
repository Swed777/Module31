# TODO здесь писать код
class Property:
    """
    Property: базовый класс, описывает имущество налогоплательщиков. Использует стоимость имущества и метод начисления налога
    attr: worth: стоимость имущества
    """
    def __init__(self, worth):
        self.worth = worth
    def get_worth(self):
        return self.worth
    def tax(self, quoter):
        self.quoter = quoter
        """ Property: Алгоритм расчета налога. Для разных видов имущества задается отдельно в дочернем классе """
        return self.worth / self.quoter
class Apartment(Property):
    name = 'Апартаменты'
    def tax_is(self):
        t =  self.tax(1000)
        return t
class Car(Property):
    name = 'Автомобиль'
    def tax_is(self):
        t =  self.tax(200)
        return t
class CountryHouse(Property):
    name = 'Дача'
    def tax_is(self):
        t = self.tax(500)
        return t

money   = float(input('Сколько у Вас денег на уплату налогов?'))
price_a = float(input('Цена апартаментов:'))
price_c = float(input('Цена машины:'))
price_h = float(input('Цена дачи:'))

tax_list = [Apartment(price_a), Car(price_c), CountryHouse(price_h)]

sum_tax = 0
for i in tax_list:
    print(i.name, i.tax_is())
    sum_tax += i.tax_is()
print('Общая сумма налога равна : ', sum_tax)

if sum_tax > money:
    print('*****   Вам не хватит денег на налоги. Идите работать! *****')




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