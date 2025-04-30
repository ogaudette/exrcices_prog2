from math import sqrt

def grouper_mouvements(mouvements):
    """
    Groupe les déplacements (dx, dy) par leur distance euclidienne.
    Retourne un dictionnaire où les clés sont les distances et les valeurs
    sont des ensembles de tuples (dx, dy).
    """
    resultat = {}

    for dx, dy in mouvements:
        distance = sqrt(dx**2 + dy**2)
        if distance not in resultat:
            resultat[distance] = set()
        resultat[distance].add((dx, dy))

    return resultat


Partie
1 – Structures
et
types
de
données(30
pts)
Q1.(10
pts)

Écrivez
une
fonction
compter_proximite(positions, seuil=5)
qui
reçoit
une
liste
de
positions(x, y)
et
retourne
le
nombre
de
points
à
une
distance
inférieure
ou
égale
à
seuil
de
l
'origine.

from math import sqrt


def compter_proximite(positions, seuil=5):
    return sum(1 for x, y in positions if sqrt(x ** 2 + y ** 2) <= seuil)


# Exemple :
positions = [(1, 2), (3, 4), (6, 8), (0, 0)]
print(compter_proximite(positions))  # Résultat : 3

Q2.(10
pts)

Écrivez
une
fonction
grouper_par_angle(mouvements)
qui
regroupe
les
déplacements
par
quart
de
cercle(0 - 90, 90 - 180, etc.)
selon
l
'angle entre l’axe x et le vecteur déplacement (dx, dy).

Indice: utilisez
math.atan2(dy, dx).

from math import atan2, degrees


def grouper_par_angle(mouvements):
    groupes = {0: [], 1: [], 2: [], 3: []}
    for dx, dy in mouvements:
        angle = degrees(atan2(dy, dx)) % 360
        groupe = int(angle // 90)
        groupes[groupe].append((dx, dy))
    return groupes


# Exemple :
print(grouper_par_angle([(1, 1), (-1, 1), (-1, -1), (1, -1)]))
# Résultat : {0: [(1,1)], 1: [(-1,1)], 2: [(-1,-1)], 3: [(1,-1)]}

Q3.(10
pts)

Écrivez
une
fonction
filtrer_uniques(objets)
qui
reçoit
une
liste
d’objets(dictionnaires
avec
une
clé
'id') et
retourne
une
nouvelle
liste
ne
contenant
qu’un
seul
exemplaire
par
'id'.


def filtrer_uniques(objets):
    vus = set()
    uniques = []
    for obj in objets:
        if obj['id'] not in vus:
            uniques.append(obj)
            vus.add(obj['id'])
    return uniques


Partie
2 – Programmation
orientée
objet(30
pts)
Q4.(10
pts)

Implémentez
une
classe
Animal
avec
les
attributs
nom, espece, x, y, et
une
méthode
distance()
qui
retourne
la
distance
à
l’origine.

from math import sqrt


class Animal:
    def __init__(self, nom, espece, x, y):
        self.nom = nom
        self.espece = espece
        self.x = x
        self.y = y

    def distance(self):
        return sqrt(self.x ** 2 + self.y ** 2)


Q5.(10
pts)

Implémentez
la
classe
Veterinaire
qui
hérite
d’Animal, et
ajoute
un
attribut
patients(liste
d
'animaux). Ajoutez une méthode soigner() qui remet à (0,0) tous les patients.


class Veterinaire(Animal):
    def __init__(self, nom, x, y):
        super().__init__(nom, "veterinaire", x, y)
        self.patients = []

    def soigner(self):
        for animal in self.patients:
            animal.x = 0
            animal.y = 0


Q6.(10
pts)

Ajoutez
à
Animal
une
méthode
spéciale
__lt__
permettant
de
trier
une
liste
d
'animaux par distance à l’origine.


def __lt__(self, other):
    return self.distance() < other.distance()


# À ajouter dans la classe Animal

Partie
3 – Fichiers(20
pts)
Q7.(10
pts)

Écrivez
une
fonction
lire_animaux(fichier)
qui
lit
un
fichier
CSV
contenant
les
colonnes
nom, espece, x, y, et
retourne
une
liste
d’objets
Animal.

import csv


def lire_animaux(fichier):
    animaux = []
    with open(fichier, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            a = Animal(row['nom'], row['espece'], float(row['x']), float(row['y']))
            animaux.append(a)
    return animaux


Q8.(10
pts)

Écrivez
une
fonction
compter_fichiers_csv(dossier)
qui
retourne
le
nombre
total
de
fichiers.csv
présents
dans
un
dossier(et
ses
sous - dossiers).

import os


def compter_fichiers_csv(dossier):
    total = 0
    for root, dirs, files in os.walk(dossier):
        total += sum(1 for f in files if f.endswith('.csv'))
    return total


Partie
4 – Backtracking(10
pts)
Q9.(10
pts)

Écrivez
une
fonction
récursive
parcours_grille(grille, x, y, chemin)
qui
explore
tous
les
chemins
possibles
dans
une
grille
2
D
sans
obstacles, à
partir
de(x, y)
vers
une
cellule
cible
marquée
'F'.La
fonction
doit
afficher
les
chemins
valides.


def parcours_grille(grille, x, y, chemin):
    if not (0 <= x < len(grille) and 0 <= y < len(grille[0])):
        return
    if grille[x][y] == '#':
        return
    if grille[x][y] == 'F':
        print(chemin + [(x, y)])
        return

    temp = grille[x][y]
    grille[x][y] = '#'  # Marquer comme visité

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        parcours_grille(grille, x + dx, y + dy, chemin + [(x, y)])

    grille[x][y] = temp  # Dé-marquer


Partie
5 – QCM(10
pts)

Q10.Que
retourne
le
code
suivant ?

d = {"a": 1, "b": 2}
print(list(d))

✅ Réponse: ['a', 'b'](par
défaut, on
itère
sur
les
clés
d’un
dictionnaire)

Q11.Quelle
est
la
différence
entre
un
set
et
une
list ? ✅ Réponse: set
ne
conserve
pas
l’ordre, ne
permet
pas
les
doublons.

Q12.Quelle
est
la
complexité
de in dans
une
liste
de
taille
n ? ✅ Réponse: O(n)(parcours
linéaire)

Q13.Que
fait
cette
instruction ?

with open("fichier.txt") as f:
    contenu = f.read()

✅ Réponse: Ouvre
le
fichier, lit
tout
le
contenu, et
le
ferme
automatiquement.

Q14.Que
retourne
la
fonction
suivante ?

def mystere(n):
    if n == 0:
        return 1
    else:
        return n * mystere(n - 1)


print(mystere(3))

✅ Réponse: 6(fonction
factorielle)
