from Model.StandardModel import StandardModel
from Model.VerticalModel import VerticalModel
from Model.HorizontalModel import HorizontalModel
from Model.ObliqueModel import ObliqueModel


class ModelFactory:
    def __init__(self):
        self.model = None

    def get_model(self, value):
        if value == "Klasyczna":
            self.model = StandardModel()
        elif value == "Tylko w pionie":
            self.model = VerticalModel()
        elif value == "Tylko w poziomie":
            self.model = HorizontalModel()
        else:
            self.model = ObliqueModel()
        return self.model



