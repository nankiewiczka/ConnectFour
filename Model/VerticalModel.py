from Model.GameModel import GameModel


class VerticalModel(GameModel):
    def __init__(self):
        super().__init__()

    def __check_vertical(self):
        transposed_gameboard = [list(i) for i in zip(*self.get_board_to_display())]
        for row in transposed_gameboard:
            pattern = row[0]
            pattern_count = 0
            for i in row:
                if i == pattern:
                    pattern_count = pattern_count + 1
                    if pattern is not None and pattern_count > 3:
                        return True
                else:
                    pattern = i
                    pattern_count = 1
        return False

    def check_if_game_ends(self):
        if self.__check_vertical() is True:
            return True
        else:
            return False


