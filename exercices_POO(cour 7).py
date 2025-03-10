import math
import unittest
from math import pi

# 1
""" Créez une classe CompteBancaire avec les
spécifications suivantes """


class CompteBancaire:
    def __init__(self, solde_initiale=0):
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


class Cercle:
    def __init__(self, rayon):
        self.__rayon = rayon

    @property
    def rayon(self):
        return self.__rayon

    @rayon.setter
    def rayon(self, rayon):
        if rayon <= 0:
            raise ValueError("putain ça doit être positif")
        self.__rayon = rayon

    def changer_rayon(self, nouveau_rayon):
        if nouveau_rayon <= 0:
            raise ValueError("putain POSITIF")
        self.__rayon = nouveau_rayon

    def aire(self):
        return pi * (self.__rayon) ** 2

    def perimetre(self):
        return 2 * pi * (self.__rayon)


class TestCercle(unittest.TestCase):
    def setUp(self):
        """Méthode exécuter avant chaque test"""
        self.cercle = Cercle(3)

    def tearDown(self):
        """méthode exécuter après chaque test"""
        pass

    def test_création_cercle(self):
        """Méthode qui permet de tester si la création du cercle est valide"""
        self.assertEqual(self.cercle.rayon, 3)

    def test_creation_cercle_invalide_rayon(self):
        """méthode qui permet de tester la création d'un cercle de rayon négatif"""
        with self.assertRaises(ValueError):
            Cercle(-3)

    def test_perimetre(self):
        """Test perimetre"""
        perimetre = 2 * pi * 3
        self.assertAlmostEqual(self.cercle.perimetre(), perimetre)

    def test_aire(self):
        """test aire"""
        aire_attendue = pi * 3 ** 2
        self.assertAlmostEqual(self.cercle.aire(), aire_attendue)


class Etudiant:
    def __init__(self, id, nom, prenom):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.cours = []  # Liste des cours suivis par l'Etudiant

    def consulterCours(self):
        return [cours.titre for cours in self.cours]

    def inscrireAuCours(self, cours):
        if cours not in self.cours:
            self.cours.append(cours)
            cours.ajouter_Etudiant(self)


class Cours:
    def __init__(self, code, titre, credits):
        self.titre = titre
        self.credits = credits
        self.code = code
        self.Etudiants = []  # Liste des Étudiants inscrits

    def afficher_details(self):
        return f"Cours:{self.titre}, Code:{self.credits}, Credits:{self.code}."

    def ajouter_etudiant(self, Etudiant):
        if Etudiant not in self.Etudiants:
            self.Etudiants.append(Etudiant)


# Exemple d'utilisation
Etudiant1 = Etudiant(1, "Alice", "Bob")
cours_python = Cours(101, "Structure de données en python", 3)
Etudiant1.inscrireAuCours(cours_python)
print(Etudiant1.consulterCours())
