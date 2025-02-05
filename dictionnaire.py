#1
informations = {'nom':'Gaudette','âge':17,'ville_naissance':'Saint-ean'}

#2
print(informations['ville_naissance'])
print(informations['nom'])

#3
informations['profession'] = 'ingénieur'
print(informations['profession'])

#5
del informations['ville_naissance']
print(informations)

#6
étudiant = {"nom": "Gates", "prénom": "Bill", "age": 18, "notes": {"maths": 16, "français": 13, "chimie": 10}}

# a
print(f"Voici la note de chimie: {étudiant["notes"].get("chimie")}")

# b
étudiant["notes"]["anglais"]=13
print(étudiant)

# c
for key in étudiant["notes"].keys():
    print(f"{key}")

for matière, note in étudiant["notes"].items():
    print(f"{matière}")

# Exemple 2
notes = {
    "Alice": {"math": 18, "physique": 16, "information": 17},
    "Bob": {"math": 15, "physique": 14, "information": 16},
    "Charlotte": {"math": 14, "physique": 18, "information": 15},
}

# 1 Calcul moyenne
moyenne = {étudiant: sum(matière.values())/len(matière) for étudiant, matière in notes.items()}
print(moyenne)

# 2 Meilleur note math
max_note = max(notes, key = lambda x: notes[x].get("math"))
print(max_note)

# 3 Ajouter matière chimie
for étudiant in notes:
    notes[étudiant]["chimie"]= 17
print(notes)

# 4 moyenne physique
moyenne_physique = sum(étudiant["physique"] for étudiant in notes.values())/len(notes)
print(moyenne_physique)

print(("*")* 20)
# Exemple 3
formules = {
    "perimetre": lambda r:2*3.14159*r,
    "aire_rectangle": lambda long, larg: long* larg,
}

r=5
longeur = 10
largeur = 6
print(formules["perimetre"](r))
print(formules["aire_rectangle"](longeur, largeur))

print(("*")*20)
# Exemple 4
#1
mots = ['bonjour', 'programmation', 'python', 'dictionnaire', 'structure']
dict_mot_long = {mot: len(mot) for mot in mots}
print(dict_mot_long)
#2
prix_ht =  {'produit1': 100, 'produit2': 200, 'produit3': 300}
prix_rabais = {produit: prix*0.95 for produit, prix in prix_ht.items()}
print(prix_rabais)
#3
original = {"a": 1, "b": 2, "c": 3}
inverse = {valeur : clé for clé, valeur in original.items()}
print(inverse)
