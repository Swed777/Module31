# TODO здесь писать код
from datetime import date

class Date():
    def __init__(self, day : int = 0, month : int = 0, year : int = 0):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'День: {self.day}, месяц: {self.month}, год: {self.year}'

    @classmethod
    def split_date(cls, date : str) -> None:
        lst_date = date.split('-')
        if len(lst_date) != 3:
            print('Неверный формат даты. \nИспользуйте дефис в качестве разделителя')
        return lst_date

    @classmethod
    def is_date_valid(cls, date : str) -> bool:
        date_valid = Date.split_date(date)
        if 1 <= int(date_valid[0]) <= 31 and 1 <= int(date_valid[1]) and int(date_valid[2]) < 9999:
            return True
        else:
            return False

    @classmethod
    def from_string(cls, date : str) -> 'Date':
        return
        pass


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))


# my_date = '30-10-2020'
# my_date_err = '30/10/2020'
# test = Date.split_date(my_date)
# print(test)
# print(Date.is_date_valid('20-20-10000'))


'''
Задача 3. Дата
Что нужно сделать
Реализуйте класс Date, который должен:

проверять числа даты на корректность;
конвертировать строку даты в объект класса Date, состоящий из соответствующих числовых значений дня, месяца и года.
Оба метода должны получать на вход строку вида ‘dd-mm-yyyy’.

При тестировании программы объект класса Date должен инициализироваться исключительно через метод конвертации,
например:

date = Date.from_string('10-12-2077')
Неверный вариант: date = Date(10, 12, 2077)

Пример основного кода:

date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

Результат:
День: 10    Месяц: 12    Год: 2077
True
False
'''