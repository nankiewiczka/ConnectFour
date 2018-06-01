from View import View
from Model.ModelFactory import ModelFactory
from Model.WrongColumnError import WrongColumnError


class Controller:
    def __init__(self):
        self.__view = View()
        self.__model = ModelFactory().get_model("Klasyczna")

    def add_controller_to_view(self):
        self.__view.add_controller(self)

    def add_model(self, value):
        self.__model = ModelFactory().get_model(value)
        self.reset()

    def create_gameboard(self):
        self.__view.create_gameboard(self.__model.get_board_to_display())

    def show_gameboard(self):
        self.__view.start_loop()

    def click_button(self, b_value):
        try:
            self.__model.update_gameboard_colors(b_value)
            self.__model.change_player()
            self.__view.update_gameboard(self.__model.get_board_to_display())
            if self.__model.check_if_game_ends() is True:
                self.__view.show_message_window("Game over.\nWon PLAYER 1" if self.__model.who_won() == 0
                                                else "Game over.\nWon PLAYER 2")
                self.reset()

            elif self.__model.check_if_has_next_move() is True:
                self.__view.update_information()
            else:
                self.__view.show_message_window("Game over.\n REMIS")
                self.reset()

        except WrongColumnError as error:
            self.__view.show_warning_window(error.message)

    def reset(self):
        self.__model.reset_gameboard()
        self.__view.reset_view()
        self.__view.update_gameboard(self.__model.get_board_to_display())

    def change_player(self):
        self.__model.change_player()


