from models.groupe_forme import Forme
import math


class Triangle(Forme):
    def __init__(self, couleur="vert", rempli=False, cote1=1.0, cote2=1.0, cote3=1.0):
        super().__init__(couleur, rempli)
        self.cote1 = cote1
        self.cote2 = cote2
        self.cote3 = cote3

    def aire(self):
        p = (self.cote1 + self.cote2 + self.cote3)/2
        return math.sqrt(p * (p-self.cote1)*(p-self.cote2)*(p-self.cote3))

    def perimetre(self):
        return self.cote1 + self.cote2 + self.cote3

    def __eq__(self, autre):
        return self.cote1 == autre.cote1 and self.cote2 == autre.cote2 and self.cote3 == autre.cote3
