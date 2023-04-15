class Property:
    def __init__(self, worth):
        self.__worth = worth

    def get_worth(self):
        return self.__worth

    def tax(self, quoter):
        return self.__worth / quoter

class Apartment():
    def __init__(self, worth):
        self.__worth = worth
    def tax(self, quoter):
        return self.__worth / quoter

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
print(apart.tax(200))