from abc import ABC, abstractmethod

class Forme(ABC):
    def __init__(self, couleur="noir", rempli=False):
        super().__init__()
        self.couleur = couleur
        self.rempli = rempli

    @abstractmethod
    def aire(self):
        """Retourne l'aire de la forme"""
        pass

    @abstractmethod
    def perimetre(self):
        """Calcul le perimetre de la forme"""
        pass


class GroupeForme:
    """cette classe représente un groupe de formes"""

    def __init__(self, formes=None):
        self.formes = []

        if formes is not None:
            for forme in formes:
                self.ajouter(forme)

    def ajouter(self, forme):
        if not isinstance(forme, Forme):
            raise TypeError("Objet doit être instance de la forme")
        self.formes.append(forme)

    def aire_totale(self):
        return sum(formes.aires() for formes in self.formes)

    def __iter__(self):
        """Elle permet d'itérer sur les formes du groupes"""
        return iter(self.formes)
