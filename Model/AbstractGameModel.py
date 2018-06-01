from abc import ABC, abstractmethod


class AbstractGameModel(ABC):
    @abstractmethod
    def who_won(self):
        pass

    @abstractmethod
    def change_player(self):
        pass

    @abstractmethod
    def update_gameboard_colors(self, column_index):
        pass

    @abstractmethod
    def check_if_game_ends(self):
        pass

    @abstractmethod
    def check_if_has_next_move(self):
        pass

    @abstractmethod
    def get_board_to_display(self):
        pass




