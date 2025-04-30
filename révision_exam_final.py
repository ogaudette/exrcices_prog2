# Q1
from math import sqrt

from gestion_dossiers_fichiers import nom_fichier

positions = [(1, 0), (2, 2), (0, 1), (2, 2)]


def analyse_positions(positions):

    distance = [sqrt(x**2 + y**2) for x, y in positions]

    moyenne = sum(distance) / len(distance)

    position_max = max(positions, key=lambda position: sqrt(position[0]**2 + position[0]**2))

    decroissant = sorted([position for position in positions if position[0] > position[1]],
                         key=lambda position: sqrt(position[0]**2 + position[0]**2), reverse=True)

    x_unique = {x for x, i in positions}

    return (f"résultats = ("
            f"moyenne_distance: {moyenne:.3f},"
            f"plus_éloignée: {position_max},"
            f"x_sup_y: {decroissant},"
            f"x_unique: {x_unique}.")


# resultat = analyse_positions(positions)
# print(resultat)

# Q2
mouvements = [(1, 0), (0, 1), (1, 1), (1, 0)]

def grouper_mouvements(mouvements):
    dictionnaire = {}
    for dx, dy in mouvements:
        distances = sqrt(dx**2 + dy**2)
        if distances not in dictionnaire:
            dictionnaire[distances] = set()
        dictionnaire[distances].add((dx, dy))
    return dictionnaire

# resultats = grouper_mouvements(mouvements)
# print(resultats)

# Q3
from abc import ABC, abstractmethod

class Entite(ABC):
    def __init__(self, nom, annee_arrivee):
        self.nom = nom
        self.annee_arrivee = annee_arrivee

    @abstractmethod
    def description(self):
        pass

    def __str__(self):
        return f"{self.nom} ({self.annee_arrivee})"

class Animal(Entite):
    def __init__(self, nom, annee_arrivee, espece):
        super().__init__(nom, annee_arrivee)
        self.espece = espece

    def description(self):
        return f"Animal : {self.espece}"

    def __lt__(self, other):
        if self.annee_arrivee != other.annee_arrivee:
            return self.annee_arrivee < other.annee_arrivee
        return self.nom < other.nom

class Enclos(Entite):
    def __init__(self, nom, annee_arrivee, capacite):
        super().__init__(nom, annee_arrivee)
        self.capacite = capacite

    def description(self):
        return f"Enclos avec capacité {self.capacite}"

class ParcAnimalier:
    def __init__(self, entites):
        self.entites = []

    def ajouter_entite(self, *entites):
        for entite in entites:
            self.entites.extend(entite)

    def entites_par_annee(self, min_annee):
        return sorted([entite for entite in self.entites if entite.annee_arrivee >= min_annee],
                      key=lambda entite: entite.annee_arrivee)

        # resultat = []
        #     for e in self.entites:
        #         if e.annee_arrivee >= min_annee:
        #             resultat.append(e)
        #     resultat.sort(key=lambda e: e.annee_arrivee)
        #     return resultat

# parc = ParcAnimalier
# parc.ajouter_entite(Animal("Simba", 2019, "Lion"), Enclos("Savane",
# 2021, 10))
# entites = parc.entites_par_annee(2020)
## entites = [Enclos("Savane", 2021, 10)]
# print([str(e) for e in entites]) # ["Savane (2021)"]

# a1 = Animal("Simba", 2019, "Lion")
# a2 = Animal("Nala", 2019, "Lion")
# a3 = Animal("Dumbo", 2017, "Éléphant")
# print(a1 < a2) # True (car "Simba" < "Nala" alphabétiquement)
# print(a1 < a3) # False (car 2019 > 2017)

# Q5
import csv


def sauvegarder_parc(parc, fichier):

        with open(fichier, "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["csv"])
            writer.writerow(["type","nom","annee_arrivee","espece","capacite"])
            for entite in parc.entites:
                entite_type = entite.__class__.__name__
                nom = entite.nom
                annee_arrivee = entite.annee_arrivee
                espece = entite.espece if entite.__class__.__name__ == "Animal" else None
                capacite = entite.capacite if entite.__class__.__name__ == "Enclos" else None

                writer.writerow([entite_type, nom, annee_arrivee, espece, capacite])

def charger_parc(fichier, parc):
    try:
        with open(fichier, "r", newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for ligne in reader:
                nom = ligne["nom"]
                annee_arrivee = ligne["annee_arrivee"]
                if ligne["type"] == "Animal":
                    espece = ligne["espece"]
                    parc.ajouter_entite(Animal(nom, annee_arrivee, espece))
                elif ligne["type"] == "Enclos":
                    capacite = ligne["capacite"]
                    parc.ajouter_entite(Enclos(nom, annee_arrivee, capacite))
        return parc
    except FileNotFoundError as e:
        print(f"fichier pas trouvé: {e}")
    except Exception as e:
        print(f"Erreur inattendue: {e}")

parc = ParcAnimalier
parc.ajouter_entite(Animal("Simba", 2019, "Lion"), Enclos("Savane",
2021, 10))
sauvegarder_parc(parc, "parc.csv")
nouveau_parc = charger_parc("parc.csv")
print([str(e) for e in nouveau_parc.entites]) # ["Simba (2019)","Savane (2021)"]


# Q6
import os
def lister_fichiers_animaux(dossier):
    resultats = []
    for dossier_racine, _, fichiers in os.walk(dossier):
        for fichier in fichiers:
            if fichier.startwith("animal_") and fichier.endswith('.txt') in fichier:
                chemin = os.path.join(dossier_racine, fichier)
                resultats.append(chemin)
    return resultats

# Q7
def trouver_chemin(grille, debut, fin, obstacles):
    ligne = len(grille)
    colonne = len(grille[0])

    def est_valide(x, y):
        return (0 <= x < ligne) and (0 <= y < colonne) and grille[x][y] == "sol" and (x, y) not in obstacles

    def backtrack(x, y):
        if not est_valide(x, y):
            return False
        position = x,y

        if position == fin:
            return True
        # directions : haut, bas, gauche, droite
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if backtrack(x + dx, y + dy):
                return True

#    if backtrack(debut[0], debut[1]):
#        return position
#    else:
#        return []
# Ne marche pas
