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
