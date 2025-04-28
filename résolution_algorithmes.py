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


# V.exercice d'application
# 1
def puissance(n, exposant):
    if n == 1 or exposant == 0:
        return 1
    return n * puissance(n, exposant - 1)


print(puissance(5, 2))


# 2
#def inverser_chaine(chaine):
#    if len(chaine) == 1:
#        return chaine
#    else:
#        return chaine[-1] + inverser_chaine(chaine[:-1])

#print(inverser_chaine([1,2,3,4,5]))


# 3
def permutations(liste):
    def permuter(liste, debut, resultat):
        if debut == len(liste):
            resultat.append(liste[:])
        else:
            for i in range(debut, len(liste)):
                liste[debut], liste[i] = liste[i], liste[debut]
                permuter(liste, debut+1, resultat)
                liste[debut], liste[i] = liste[i], liste[debut]   # backtracking

    resultat = []
    permuter(liste, 0, resultat)
    return resultat

print(permutations([2,3,5]))

# 4
def force_brute_triplets(liste):
    n = len(liste)
    resultat = []

    # utilise trois boucles imbriquées pour tester toutes les combinaisons possibles
    for i in range(n):
        for j in range(i + 1, n):  # commence i + 1 pour éviter les doublons
            for k in range(j + 1, n):  # commence j + 1 pour éviter les doublons
                # vérifie si somme est égal à zéro
                if liste[i] + liste[j] + liste[k] == 0:
                    resultat.append([liste[i], liste[j], liste[k]])

    return resultat   # retourne les triplets trouvés

nombres = [-1,0,1,2,-1,-4]
print(force_brute_triplets(nombres))
