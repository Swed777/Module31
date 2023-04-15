class Property:
    def __init__(self, worth):
        self.__worth = worth

    def get_worth(self):
        return self.__worth

    def set_worth(self):
        return self.__worth

    def tax(self, quoter):
        return self.__worth / quoter

class Apartment():


kv = Property(5000000)
print(kv.tax(1000))