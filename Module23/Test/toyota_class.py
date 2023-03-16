import random

class Toyota:
    color = 'white'
    price = '1000'
    max_speed = 200
    speed = 0

    def print_all(self):
        print('Цвет: {}\n Цена: {}\n макс.скорость: {}\n Текущая скорость: {}'.format(
            self.color, self.price, self.max_speed, self.speed)
        )

    def speed_all(self, speedo):
        # self.speed = int(input('Введите скорость: '))
        self.speed = speedo

Toyota_min = Toyota()
Toyota_middle = Toyota()
Toyota_lux = Toyota()

Toyota_min.speed = random.randint(0, 200)
Toyota_middle.speed = random.randint(0, 200)
Toyota_lux.speed = random.randint(0, 200)

# print(Toyota_min.speed, Toyota_middle.speed, Toyota_lux.speed)
Toyota_min.print_all()

Toyota_lux.speed_all(777)
Toyota_lux.print_all()