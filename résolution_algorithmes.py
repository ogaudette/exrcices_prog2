import itertools
import string


def force_brute_mot_de_passe(mot_passe_cible, longueur_max=3):
    caracteres = string.ascii_lowercase
    for longueur in range(1, longueur_max + 1):
        for combinaison in itertools.product(caracteres, repeat=longueur):
            essai = ''.join(combinaison)
            if essai == mot_passe_cible:
                return essai
    return None


print(force_brute_mot_de_passe("abc"))


def sous_ensemble_somme(liste, cible):
    n = len(liste)
    for i in range(1 << n):  # 2^n combinaisons
        sous_ensemble = []
        for j in range(n):
            if (i >> j) & 1:  # Vérifier si l'élément est inclus
                sous_ensemble.append(liste[j])
        if sum(sous_ensemble) == cible:
            return sous_ensemble
    return None


# Test
print(sous_ensemble_somme([3, 4, 12, 5, 2, 9], 7))  # Output: [4, 5]
