# TODO здесь писать код
from colorama import init, Fore
init(autoreset=True)
class Board:
    board = list(range(9))   # определяем общее состояние поля из 9 ячеек
    def border(self):       # и выводим его на печать
        print(Fore.GREEN + '- ' * 7)
        for i_cell in range(3):
            print((Fore.GREEN + '|'),self.board[0 + i_cell * 3], Fore.GREEN + '|', self.board[1 + i_cell * 3], Fore.GREEN + '|', self.board[2 + i_cell * 3], Fore.GREEN + '|')
            print(Fore.GREEN + '- ' * 7)

    # def change_cell(self):
    #
    # def status_game(self):

#
# class Cell:
# class Player:
# class Game:

contur = Board()
contur.border()




pass

'''
Задача 6. Крестики-нолики
Что нужно сделать
Создайте программу, которая реализует игру «Крестики-нолики».

Для этого напишите:
1. Класс, который будет описывать поле игры.
class Board:
    #  Класс поля, который создаёт у себя экземпляры клетки.
    #  Пусть класс хранит информацию о состоянии поля (это может быть список из девяти элементов).
    #  Помимо этого, класс должен содержать методы:
    #  «Изменить состояние клетки». Метод получает номер клетки и, если клетка не занята, меняет её состояние. Если состояние удалось изменить, метод возвращает True, иначе возвращается False.
    #  «Проверить окончание игры». Метод не получает входящих данных, но возвращает True/False. True — если один из игроков победил, False — если победителя нет.
2. Класс, который будет описывать одну клетку поля:
class Cell:
    #  Клетка, у которой есть значения:
    #  занята она или нет;
    #  номер клетки;
    #  символ, который клетка хранит (пустая, крестик, нолик).
3. Класс, который описывает поведение игрока:
class Player:
    #  У игрока может быть:
    #  имя,
    #  количество побед.
    #  Класс должен содержать метод:
    #   «Сделать ход». Метод ничего не принимает и возвращает ход игрока (номер клетки). Введённый номер нужно обязательно проверить.
4. Класс, который управляет ходом игры:
class Game:    
    # класс «Игры» содержит атрибуты:
    # состояние игры,
    # игроки,
    # поле.
    # А также методы:
    # Метод запуска одного хода игры. Получает одного из игроков, запрашивает у игрока номер клетки, изменяет поле, проверяет, выиграл ли игрок. Если игрок победил, возвращает True, иначе False.
    # Метод запуска одной игры. Очищает поле, запускает цикл с игрой, который завершается победой одного из игроков или ничьей. Если игра завершена, метод возвращает True, иначе False.
    # Основной метод запуска игр. В цикле запускает игры, запрашивая после каждой игры, хотят ли игроки продолжать играть. После каждой игры выводится текущий счёт игроков.
'''