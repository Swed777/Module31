# TODO здесь писать код
from colorama import init, Fore
init(autoreset=True)
class Board:
    board = list(range(9))   # определяем общее состояние поля из 9 ячеек
    def border_field(self):       # и выводим его на печать
        print(Fore.GREEN + '- ' * 7)
        for i_cell in range(3):
            print((Fore.GREEN + '|'), (Fore.LIGHTYELLOW_EX + str(self.board[0 + i_cell * 3])),
                   Fore.GREEN + '|',  (Fore.LIGHTYELLOW_EX + str(self.board[1 + i_cell * 3])),
                   Fore.GREEN + '|',  (Fore.LIGHTYELLOW_EX + str(self.board[2 + i_cell * 3])), Fore.GREEN + '|')
            print(Fore.GREEN + '- ' * 7)

    def change_cell(self, number_cell):
        if number_cell != 'X'.lower() or number_cell != 'O'.lower():
            number_cell =  777 # Добавить информацию о конкретном элементе Х или О
            return True
        else:return False

    def victory_check(board):
        victory_line = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6))
        for i in victory_line:
            if Board.board[i[0]] == Board.board[i[1]] == Board.board[i[2]]:  # Проверяем наличие одинаковых символов Х или О в выигрышных линиях
                return True
        return False
#
class Cell:
    states = {0: ' ', 1: 'X', 2: 'O'}
    def __init__(self, index):
        self.index = int(index)
        self.state = 0
    def cell_status(self):
        if self.state == 0:
            print(f'Данная ячейка ->{self.index} свободна.')
            return True
        print(f'Данная ячейка ->{self.index} занята.')
        return False
class Player:
 def __init__(self, name: str):
        self.name = name
        self.figure: Cell.states = 0
        self.num_of_victory = 0
        self.my_turn = False
 def set_symbol(self, symbol):
        if symbol == 'X':
            self.figure = 1
        else:
            self.figure = 2
# class Game:



print('*****************')
contur = Board()
contur.border_field()
Board.victory_check(1)


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
'''
from colorama import init, Fore
init(autoreset=True)
class Board:
    def __init__(self):
        self.board = [Cell(index) for index in range(1, 10)]                 # Пусть класс хранит информацию о состоянии поля (это может быть список из девяти элементов).
    def board_field(self):  # определяем общее состояние поля из 9 ячеек
        print(Fore.GREEN + '- ' * 7)
        for i_cell in range(3):
            print((Fore.GREEN + '|'), (Fore.LIGHTYELLOW_EX + str(self.board[0 + i_cell * 3])),
                   Fore.GREEN + '|',  (Fore.LIGHTYELLOW_EX + str(self.board[1 + i_cell * 3])),
                   Fore.GREEN + '|',  (Fore.LIGHTYELLOW_EX + str(self.board[2 + i_cell * 3])), Fore.GREEN + '|')
            print(Fore.GREEN + '- ' * 7)
    def change_cell(self, num_cell_player):   #  «Изменить состояние клетки». Метод получает номер клетки и, если клетка не занята,
        if num_cell_player in range(1, 10):   #  меняет её состояние. Если состояние удалось изменить, метод возвращает True, иначе возвращается False.
            return '***'
            # if str(Board.board[num_cell_player]) not in 'XO':
            #     return True
        else:
            print('Клетка уже занята')
            return False
    def finish_game_status(self):  #  «Проверить окончание игры». Метод не получает входящих данных, но возвращает True/False.
                                    # True — если один из игроков победил, False — если победителя нет.
        self.victory_line = ((1, 2, 3), (4, 5, 6), (7, 8, 9),
                             (1, 4, 7), (2, 5, 8), (3, 6, 9),
                              (1, 5, 9), (3, 5, 7))
        for i in self.victory_line:
            if Board.board[i[0]] == Board.board[i[1]] == Board.board[i[2]]:  # Проверяем наличие одинаковых символов Х или О в выигрышных линиях
                return True
            else:
                return False
    def __str__(self):
        return f'Набор ячеек в таблице выглядит вот так: \n {self.board}'
class Cell:
    def __init__(self, index, free_cell_status = 0):
        self.free_cell_status = free_cell_status         #  свободна (0) она или нет (1);
        self.number_cell = int(index)                    #  номер клетки;
        self.symbol_cell = {0:' ', 1:'X', 2:'O'}          #  символ, который клетка хранит (пустая, крестик, нолик).{0:' ', 1:'X', 2:'O'}
    def __str__(self):
        if self.free_cell_status == 0:
            result = f'{self.number_cell}'
        else:
            result = f'{self.symbol_cell[2]}, не равен'  # !!! нужно подставить номер игрока
        return result


class Player:
    name = ''                                    # имя,
    count_victory = 0                            # количество побед.
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self):             #   «Сделать ход». Метод ничего не принимает и возвращает ход игрока (номер клетки).
        return Board.change_cell()   #   ??? Введённый номер нужно обязательно проверить. ??? Е.И. - По условиям задачи клетку мы уже проверяем в классе Board

class Game:
    def __init__(self):
        self.game_status = True               # состояние игры,
        self.player1 = Player('1 игрок')      # игроки,
        self.player2 = Player('2 игрок')
        self.field_status = 0                 # поле.

    # Метод запуска одного хода игры. Получает одного из игроков, запрашивает у игрока номер клетки,
    # изменяет поле, проверяет, выиграл ли игрок. Если игрок победил, возвращает True, иначе False.
    def one_step(self):
        self.pl = int(input('Кто сейчас ходит:? \n1 - первый игрок \n2 - второй игрок\n'))
        Cell.number_cell = int(input('Введите номер клетки для хода:\n'))
        if self.pl == 1:
            Cell.symbol_cell = 'X'
        else:
            Cell.symbol_cell = 'O'
        Board.change_cell(Cell.number_cell)

    # Метод запуска одной игры. Очищает поле, запускает цикл с игрой, который завершается победой
    # одного из игроков или ничьей. Если игра завершена, метод возвращает True, иначе False.

    # Основной метод запуска игр. В цикле запускает игры, запрашивая после каждой игры,
    # хотят ли игроки продолжать играть. После каждой игры выводится текущий счёт игроков.
    def main(self):
        while True:
            pass

#  Отладка:
test = Board()
print(test)
test.board_field()
# print(test.finish_game_status())
# xxx = Game()
# xxx.one_step()
cell1 = Cell(7, 0)
print(cell1)


print(Cell(3, 1))

# print('\n1 игрок ходит X, второй - O (буква О англ)'



'''