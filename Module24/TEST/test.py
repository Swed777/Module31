from colorama import init, Fore
init(autoreset=True)
class Board:
    def __init__(self):
        self.board = [Cell(index) for index in range(1, 10)]                 # Пусть класс хранит информацию о состоянии поля (это может быть список из девяти элементов).
        self.battle = True
    def board_field(self):  # определяем общее состояние поля из 9 ячеек
        print(Fore.GREEN + '- ' * 7)
        for i_cell in range(3):
            print((Fore.GREEN + '|'), (Fore.LIGHTYELLOW_EX + str(self.board[0 + i_cell * 3])),
                   Fore.GREEN + '|',  (Fore.LIGHTYELLOW_EX + str(self.board[1 + i_cell * 3])),
                   Fore.GREEN + '|',  (Fore.LIGHTYELLOW_EX + str(self.board[2 + i_cell * 3])), Fore.GREEN + '|')
            print(Fore.GREEN + '- ' * 7)
    def count_free_cell(self):      #  «Изменить состояние клетки». Метод получает номер клетки и, если клетка не занята,
        count = 0                   #  меняет её состояние. Если состояние удалось изменить, метод возвращает True, иначе возвращается False.
        for cell in self.board:
            if cell.state == 0:
                count += 1
            else:
                print('Клетка уже занята')
                return False
        return count

    def check_win(self):         # Проверяем наборы выигрышных комбинаций
        victory_line = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
        for cell in victory_line:
            sum_row = self.board[cell[0]].state + self.board[cell[1]].state + self.board[cell[2]].state
            if sum_row > 0:
                if self.board[cell[0]].state == self.board[cell[1]].state == self.board[cell[2]].state:
                    self.battle = False
                    return True
        return False

    def finish_game_status(self, player, cell):   #  «Проверить окончание игры». Метод не получает входящих данных, но возвращает True/False.
        self.board[cell].set_status(player.figure)             # True — если один из игроков победил, False — если победителя нет.
        if self.check_win():
            print(f'{player.name}, ходивший фигурой "{Cell.states[player.figure]}" победил.')
            self.board_field()
        if self.count_free_cell() == 0:
           self.board_field()
           self.battle = False
           print('\nБольше нет свободных ячеек.\nВ этот раз ничья.')
    def __str__(self):
        return f'Набор ячеек в таблице выглядит вот так: \n {self.board}'
class Cell:
    states = {0: ' ', 1: 'X', 2: 'O'}
    def __init__(self, index: int):
        self.index = index
        self.state = 0
    def __str__(self):
        if self.state == 0:
            result = f'{self.index}'
        else:
            result = f'{Cell.states[self.state]}'
        return result
    def set_status(self, state: states):
        if self.state == 0:
            self.state = state
        self.print_state()
    def is_free(self):
        if self.state == 0:
            return True
        print('Данная ячейка занята.')
        return False
    def print_state(self):
        print(f'Ячейка {self.index} сейчас {Cell.states[self.state]}.')
class Player:
    def __init__(self, name):
        self.name = name
        self.figure: Cell.states = 0
        self.my_turn = False
    def set_symbol(self, symbol):
        if symbol == 'X':
            self.figure = 1
        else:
            self.figure = 2
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
    def new_game(self):
        self.p = self.clear_place
        self.end_info = 0

    # Основной метод запуска игр. В цикле запускает игры, запрашивая после каждой игры,
    # хотят ли игроки продолжать играть. После каждой игры выводится текущий счёт игроков.
    def main(self):
        while True:
            pass



#  Отладка:
test = Board()
print(test)
test.board_field()

# print('\n1 игрок ходит X, второй - O (буква О англ)'


