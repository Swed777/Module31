# TODO здесь писать код


class Date:
    def __init__(self, day: int = 0, month: int = 0, year: int = 0):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'День: {self.day}, месяц: {self.month}, год: {self.year}'

    @classmethod
    def split_date(cls, date: str) -> None:
        lst_date = date.split('-')
        if len(lst_date) != 3:
            print('Неверный формат даты. \nИспользуйте дефис в качестве разделителя')
        cls.day, cls.month, cls.year = map(int, lst_date)

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        cls.split_date(date)
        if 1 <= int(cls.day) <= 31 and 1 <= int(cls.month) and cls.year < 9999:
            return True
        else:
            return False

    @classmethod
    def from_string(cls, date: str) -> 'Date':
        cls.split_date(date)
        finish_date = cls(cls.day, cls.month, cls.year)
        return finish_date


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-202020'))

# зачтено
