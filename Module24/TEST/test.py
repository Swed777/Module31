from colorama import init, Fore
init(autoreset=True)
class Board:
    board = list(range(1,10))    #  Пусть класс хранит информацию о состоянии поля (это может быть список из девяти элементов).
    def board_field(self):  # определяем общее состояние поля из 9 ячеек
        print(Fore.GREEN + '- ' * 7)
        for i_cell in range(3):
            print((Fore.GREEN + '|'), (Fore.LIGHTYELLOW_EX + str(self.board[0 + i_cell * 3])),
                   Fore.GREEN + '|',  (Fore.LIGHTYELLOW_EX + str(self.board[1 + i_cell * 3])),
                   Fore.GREEN + '|',  (Fore.LIGHTYELLOW_EX + str(self.board[2 + i_cell * 3])), Fore.GREEN + '|')
            print(Fore.GREEN + '- ' * 7)

    def change_cell(self, num_cell_player):   #  «Изменить состояние клетки». Метод получает номер клетки и, если клетка не занята,
                                              #  меняет её состояние. Если состояние удалось изменить, метод возвращает True, иначе возвращается False.
        if num_cell_player in range(1, 10):
            if str(Board.board(num_cell_player)) not in 'XO':
                Board.board(num_cell_player) = self.symbol
                return True
        else:
            print('Ошибка в номере ячейки')
            return False



    def finish_game_status(self):  #  «Проверить окончание игры». Метод не получает входящих данных, но возвращает True/False.
                                    # True — если один из игроков победил, False — если победителя нет.
        pass
    def __str__(self):
        return f'Таблица сейчас выглядит вот так: \n {self.board}'
class Cell:
    free_cell_status = True   #  занята она или нет;
    number_cell = int()    #  номер клетки;
    symbol_cell = {0: ' ', 1: 'X', 2: 'O'}      #  символ, который клетка хранит (пустая, крестик, нолик).

class Player:
    name = ''  # имя,
    count_victory = 0  # количество побед.
    def __init__(self,symbol):
        self.symbol = symbol

    def make_move(self):       #   «Сделать ход». Метод ничего не принимает и возвращает ход игрока (номер клетки).
                               #   Введённый номер нужно обязательно проверить.
    pass
class Game:
    class Game:
        game_status =            # состояние игры,
        player = [p1, p2]       # игроки,
        field_status =           # поле.

    # Метод запуска одного хода игры. Получает одного из игроков, запрашивает у игрока номер клетки,
    # изменяет поле, проверяет, выиграл ли игрок. Если игрок победил, возвращает True, иначе False.

    # Метод запуска одной игры. Очищает поле, запускает цикл с игрой, который завершается победой
    # одного из игроков или ничьей. Если игра завершена, метод возвращает True, иначе False.

    # Основной метод запуска игр. В цикле запускает игры, запрашивая после каждой игры,
    # хотят ли игроки продолжать играть. После каждой игры выводится текущий счёт игроков.



#  Отладка:
test = Board()
print(test)
test.board_field()


