from abc import abstractmethod, ABC
from math import pi


class Forme(ABC):
    @abstractmethod
    def aire(self):
        pass

    @abstractmethod
    def perimetre(self):
        pass

    def afficher_forme(self):
        return "ceci est une forme"


class Cercle(Forme):

    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return pi * self.rayon ** 2

    def perimetre(self):
        return 2 * pi * self.rayon

    def afficher_forme(self):
        return "ceci est un cercle"


class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur

    def perimetre(self):
        return 2 * self.longueur + 2 * self.largeur

    def afficher_forme(self):
        return "ceci est un rectangle"


# rectangle = Rectangle(8, 4)
# print(rectangle.aire())
# print(rectangle.perimetre())
# print(rectangle.afficher_forme())

# cercle = Cercle(8)
# print(cercle.aire())
# print(cercle.perimetre())
# print(cercle.afficher_forme())

class Véhicule(ABC):
    @abstractmethod
    def type_véhicule(self):
        pass

    @abstractmethod
    def démarrer(self):
        pass

    @abstractmethod
    def arrêter(self):
        pass

    def afficher_annee(self, annee):
        return f"Ce {self.type_véhicule()} a été fabriqué en {annee}!!!!!!"


class jet(Véhicule):
    @property
    def type_véhicule(self):
        return "jet"

    def démarrer(self):
        return "allume ses énormes propulseur et démarre"

    def arrêter(self):
        return "s'arrête en coupant ses propulseurs"

    def afficher_annee(self, annee):
        return "1945"


j1 = jet()
# print(f"Le {j1.type_véhicule} {j1.démarrer()},puis {j1.arrêter()}")
print(j1.afficher_annee)  # marche pas

# Exercice d'application poo

from abc import ABC, abstractmethod


class GroupeForme:
    """cette classe représente un groupe de formes"""
    def __init__(self, formes=None):
        self.formes = []

        if formes is not None:
            for forme in formes:
                # self

    def ajouter(self, forme):
        if not isinstance(forme, Forme):
            raise TypeError("Objet doit être instance de la forme")

    def aire_totale(self):
        return sum(formes.aires() for formes in self.formes)


class Forme(GroupeForme):
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


class Rectangle(Forme):
    def __init__(self, longueur, largeur, rempli, couleur):
        super().__init__(couleur, rempli)
        self.longueur = longueur
        self.largeur = largeur

    def aire(self) -> float:
        return self.longueur * self.largeur

    def perimetre(self) -> float:
        return self.longueur * 2 + 2 * self.largeur

    def __add__(self, other) -> float:
        pass

    def __mul__(self, nb) -> float:
        pass


class Cercle(Forme):
    def __init__(self, rayon, couleur, rempli):
        super().__init__(couleur, rempli)
        self.rayon = rayon

    def aire(self) -> float:
        return pi * self.rayon ** 2

    def perimetre(self) -> float:
        return 2 * pi * self.rayon

    def __add__(self, other) -> float:
        pass


class Triangle(Forme):
    def __init__(self, cote1, cote2, cote3, couleur, rempli):
        super().__init__(couleur, rempli)
        self.cote1 = cote1
        self.cote2 = cote2
        self.cote3 = cote3

    def aire(self) -> float:
        pass

    def perimetre(self) -> float:
        return self.cote1 + self.cote2 + self.cote3

    def __eq__(self, other) -> bool:
        pass
