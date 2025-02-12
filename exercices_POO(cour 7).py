import math
# 1
""" Créez une classe CompteBancaire avec les
spécifications suivantes """
class CompteBancaire:
    def __init__(self, solde_initiale = 0):
        self.__solde = solde_initiale

    def deposer(self, montant_depot):
        """Ici on va deposer une montant au solde"""
        if montant_depot > 0:
            self.__solde += montant_depot
        else:
            print("Le montant déposé doit être positif")

    def retirer(self, montant_retire):
        if 0 <= montant_retire < self.__solde:
            self.__solde -= montant_retire
        elif montant_retire > self.__solde:
            print("Fonds insuffisants. Veuillez vérifier votre solde.")
        else:
            print("Le montant doit être positif. Broke ahh")

    def afficher_solde(self):
        print(f"Solde actuel : {self.__solde}$")

compte1 = CompteBancaire(1200)
compte1.retirer(500)
compte1.deposer(69)
compte1.retirer(349)
compte1.afficher_solde()

# 2
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def coordonnees(self):
        print(f"({self.__x}, {self.__y})")

    def distance_origine(self):
        distance = math.sqrt(math.pow(self.__x, 2) + math.pow(self.__y, 2))
        print(f"{distance:.4f} u")

point1 = Point(1, 2)
point1.distance_origine()
point1.coordonnees()
point2 = Point(3, 4)
point2.distance_origine()

#3
class Rectangle:
    def __init__(self, long, large):
        self.__long = long
        self.__large = large

    @property
    def long(self):
        return self.__long

    @long.setter
    def long(self, long):
        if long > 0:
            self.__long = long
        else:
            print("Veuillez saisir une longueur positive. Dumbass")

    @property
    def large(self):
        return self.__large

    @large.setter
    def large(self, large):
        if large < 0:
            print("Veuillez saisir une largeur positive. Dumbass")

    @property
    def surface(self):
        return self.__long * self.__large

    @property
    def perimetre(self):
        return 2 * self.__long + 2 * self.__large

rectangle1 = Rectangle(100, 100)

