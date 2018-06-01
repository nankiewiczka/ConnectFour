from Controller import Controller


class ConnectFour:
    def __init__(self):
        self.controller = Controller()
        self.controller.add_controller_to_view()
        self.controller.create_gameboard()

    def run(self):
        self.controller.show_gameboard()
