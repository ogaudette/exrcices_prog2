# 1a
import string

notes = [85.5, 92.0, 55.5, 85.5, 78.0]
def analyse_notes(notes):
    if not notes:
        return {
            "note moyenne": 0,
            "note plus elevee": None,
            "plus petite note": None,
            "liste note sup à 60": [],
            "ensemble notes uniques": set()
        }

    # note moyenne
    moyenne_notes = sum(notes)/len(notes)

    # note plus élevée
    note_max = max(notes)

    # note minimum
    note_min = min(notes)

    # sup_60
    note_sup_60 = set(filter(lambda note: note > 60, notes))
    note_sup_60_decroissant = sorted(note_sup_60, key = lambda note: notes, reverse = True)

    # uniques
    note_uniques = {note for note in notes}

    return {
        "note moyenne": moyenne_notes,
        "note plus elevee": note_max,
        "plus petite note": note_min,
        "liste note sup à 60": note_sup_60_decroissant,
        "ensemble notes uniques": note_uniques}

resultat = analyse_notes(notes)
# print(resultat)

mots = ["chat", "chien", "rat", "souris"]
# 1b
def grouper_par_longueur(mots):
    resultats = {}
    liste_tuple = []

    for mot in mots:
        liste_tuple.append(len(mot))
        if mot not in resultats:
            resultats[mot] = set()
        resultats[mot].add(mot)
    return resultats

resultats = grouper_par_longueur(mots)
# print(resultats)

# 2a
from abc import ABC, abstractmethod
class Produit(ABC):
    def __init__(self, titre: str, prix: float):
        super().__init__()
        self.titre = titre
        self.prix = prix

    @abstractmethod
    def description(self) -> str:
        pass

    def __str__(self):
        return f"Titre: {self.titre}, Prix: {self.prix}"

class JeuVideo(Produit):
    def __init__(self, titre: str, prix: float, plateforme: str):
        super().__init__(titre, prix)
        self.plateforme = plateforme

    def description(self) -> str:
        return f"Jeu pour {self.plateforme}"

    def __gt__(self, other) -> bool:
        if self.prix != other.prix:
            return self.prix > other.prix
        return self.titre > other.titre

class Accessoire(Produit):
    def __init__(self, titre: str, prix: float, type_accessoire: str):
        super().__init__(titre, prix)
        self.type_accessoire = type_accessoire

    def description(self) -> str:
        return f"Accesoire: {self.type_accessoire}"

class Magasin:
    def __init__(self):
        self.produits = []

    def ajouter_produit(self, *produits):
        self.produits.extend(produits)

    def produits_par_prix(self, max_prix):
        return sorted([p for p in self.produits if p.prix <= max_prix], key=lambda p: p.prix)

magasin = Magasin()
magasin.ajouter_produit(JeuVideo("FIFA 23", 59.99, "PS5"),
Accessoire("Manette Pro", 69.99, "manette"))
# print(magasin.produits_par_prix(60.00))

# 2c
import json

def sauvegarder_magasin(magasin, fichier):

    with open(fichier, "w", newline="", encoding='utf-8') as f:
        json.dump(magasin, f, indent=4)

        for produit in magasin.produits.values():
            produit_type = produit.__class__.__name__
            titre = produit.titre
            prix = produit.prix
            plateforme = produit.plateforme
            type_accessoire = produit.type_accessoire
        if isinstance(produit, Accessoire):
                return f"type: {produit_type}, titre: {titre}, prix: {prix}, type_accessoire: {type_accessoire}"
        else:
            return f"type: {produit_type}, titre: {titre}, prix: {prix}, plateforme: {plateforme},"

def charger_magasin(fichier):
    magasin = Magasin()
    with open(fichier, "r", newline="", encoding='utf-8') as f:
        magasin = json.load(f)

# 2d
import os
def lister_images(dossier):
    resultats = []
    for dossier_racine, _, fichiers in os.walk(dossier):
        for fichier in fichiers:
            if fichier.endswith('.png' or '.jpg' or '.jpeg') in fichier:
                chemin = os.path.join(dossier_racine, fichier)
                resultats.append(chemin)
    return resultats

# 3a
def compter_chemins(m, n):
    debut = (0,0)
    fin = m - 1, n - 1
    def est_valide(x, y):
        return (0 =< x < m) and (0 =< y < n)

    def backtrack(current, chemin):
        x, y = current

        if current == fin:
            return chemin

        mouvements = [(0, 1), (1, 0)]
        for dx, dy in mouvements:
            next_x, next_y = x + dx, y + dy
            if est_valide(next_x, next_y) and (next_x, next_y) not in chemin:
                nouveau_chemin = backtrack((next_x, next_y), chemin + [(next_x, next_y)])
                if nouveau_chemin:
                    return nouveau_chemin
        return []

        if chemin == fin:
            return chemin + nouveau_chemin  #  je sais que ça ne marche pas, mais pas eu le temps de changer

    if not est_valide(*debut) or not est_valide(*fin):
        return []

    return [(debut)] + backtrack(debut, [debut])

# 3b
import string
import random
def generer_mots_caracteres(longueur, caracteres):
    caracteres = string.ascii_lowercase
    def commencer(longueur, caracteres):
        mot_passe = ''.join(random.sample(caracteres) for _ in range(longueur))
        return mot_passe     # manque de temps peut pas finir






