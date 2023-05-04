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
        t = self.tax(1000)
        return t


class Car(Property):
    name = 'Автомобиль'

    def tax_is(self):
        t = self.tax(200)
        return t


class CountryHouse(Property):
    name = 'Дача'

    def tax_is(self):
        t = self.tax(500)
        return t


money = float(input('Сколько у Вас денег на уплату налогов?'))
price_a = float(input('Цена апартаментов:'))
price_c = float(input('Цена машины:'))
price_h = float(input('Цена дачи:'))

tax_list = [Apartment(price_a), Car(price_c), CountryHouse(price_h)]

sum_tax = 0
for i in tax_list:
    print(i.name, i.tax_is())
    sum_tax += i.tax_is()
print('\nОбщая сумма налога равна : ', sum_tax)

if sum_tax > money:
    print(f'\n*****   Вам не хватит --> {abs(sum_tax - money)} <-- денег на налоги. Идите работать! *****')

# зачтено
