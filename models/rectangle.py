from models.groupe_forme import Forme


class Rectangle(Forme):
    def __init__(self, couleur="rouge", rempli=False, largeur=1.0, longueur=1.0):
        super().__init__(couleur, rempli)
        self.largeur = largeur
        self.longueur = longueur

    def aire(self):
        return self.largeur * self.longueur

    def perimetre(self):
        return (self.largeur + self.longueur) * 2

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return self.aire() + other.aire()
        else:
            raise TypeError("opération impossible entre 2 rectangles")

    def __mul__(self, nb):
        if isinstance(nb, (int, float)):
            return Rectangle(
                self.couleur,
                self.rempli,
                self.largeur * nb,
                self.longueur * nb)
        else:
            raise TypeError("multiplicateur doit être nombre")

    def afficher_aire(self):
        return "L'aire de ce rectangle est "+str(self.aire())
