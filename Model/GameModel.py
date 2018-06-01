from Model.AbstractGameModel import AbstractGameModel
from Model.WrongColumnError import WrongColumnError


class GameModel(AbstractGameModel):
    def __init__(self):
        super().__init__()
        self.__game_board = [[None for i in range(0, 7)] for j in range(0, 6)]
        self.__player = 1   # always starting red(1), yellow(0)

    def who_won(self):
        return self.__player

    def change_player(self):
        if self.__player == 1:
            self.__player = 0
        else:
            self.__player = 1

    def update_gameboard_colors(self, column_index):
        i = 5
        can_update = False
        while i >= 0:
            if self.__game_board[i][column_index-1] is None:
                self.__game_board[i][column_index-1] = '#921414' if self.__player == 1 else '#EEC111'
                can_update = True
                break
            i = i-1
        if can_update is False:
            raise WrongColumnError("Choose another column!")

    def get_board_to_display(self):
        return self.__game_board

    def check_if_game_ends(self):
        pass

    def check_if_has_next_move(self):
        for rows in self.__game_board:
            for i in rows:
                if i is None:
                    return True

        return False

    def reset_gameboard(self):
        self.__game_board = [[None for i in range(0, 7)] for j in range(0, 6)]
        self.__player = 1




