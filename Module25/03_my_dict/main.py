# TODO здесь писать код
class MyDict(dict):
    def get_dict(self, key):
        return super().get(key, 0)


test = {1: 'Автомобиль', 2: 'Катер', 3: 'Яхта', 4: 'Мотоцикл'}
my_dict = MyDict(test)

print(my_dict.get_dict(3))
print(my_dict.get_dict(5))

# зачтено
