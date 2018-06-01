from Model.GameModel import GameModel


class HorizontalModel(GameModel):
    def __init__(self):
        super().__init__()

    def __check_horizontal(self):
        for row in self.get_board_to_display():
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
        if self.__check_horizontal() is True:
            return True
        else:
            return False





