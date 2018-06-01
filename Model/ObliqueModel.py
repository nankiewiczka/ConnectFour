from Model.GameModel import GameModel


class ObliqueModel(GameModel):
    def __init__(self):
        super().__init__()

    def __check_oblique(self):
        temp_board = self.get_board_to_display()
        for i, j in zip([3, 4, 5, 5, 5, 5], [6, 6, 6, 5, 4, 3]):
            row = i
            column = j
            pattern = temp_board[row][column]
            pattern_count = 0
            while row >= 0 and column >= 0:
                if temp_board[row][column] == pattern:
                    pattern_count = pattern_count + 1
                    if pattern is not None and pattern_count > 3:
                        return True
                else:
                    pattern = temp_board[row][column]
                    pattern_count = 1
                row = row - 1
                column = column - 1
        for i, j in zip([3, 4, 5, 5, 5, 5], [0, 0, 0, 1, 2, 3]):
            row = i
            column = j
            pattern = temp_board[row][column]
            pattern_count = 0
            while row >= 0 and column <= 6:
                if temp_board[row][column] == pattern:
                    pattern_count = pattern_count + 1
                    if pattern is not None and pattern_count > 3:
                        return True
                else:
                    pattern = temp_board[row][column]
                    pattern_count = 1
                row = row - 1
                column = column + 1
        return False

    def check_if_game_ends(self):
        if self.__check_oblique() is True:
            return True
        else:
            return False




