# III Notions de chemins
import os
from pathlib import Path

# obtenir répertoire de travail actuel
repertoire_actuel = os.getcwd()
print(f"Répertoire: {repertoire_actuel}")

# Chemin absolu vers un fichier
chemin_absolu = os.path.join(repertoire_actuel, "données", "fichier.txt")
print(f"Chemin absolu: {chemin_absolu}")

# chemin relatif
chemin_relatif = os.path.join("données", "fichier.txt")
print(f"Chemin relatif: {chemin_relatif}")

# obtenir le nom du fichier et son extension
nom_base, extension = os.path.splitext("fichier.txt")
print(f"Nom de base: {nom_base}, extension: {extension}")

# joindre des parties de chemin (portable entre système d'exploitation
chemin = os.path.join("dossier", "sous_dossier", "fichier.txt")
print(f"Chemin joint: {chemin}")

# obtenir dossier parent d'un chemin
dossier_parent = os.path.dirname("/home/utilisateur/documents/fichier.txt")
print(f"Dossier parent: {dossier_parent}")

# obtenir nom du fichier à partir du chemin
nom_fichier = os.path.basename("/home/utilisateur/documents/fichier.txt")
print(f"Nom du fichier: {nom_fichier}")

# Obtenir chemin absolu
obtenir_chemin_absolu = os.path.abspath("donnees/fichier.txt")
print(f"Chemin absolu: {obtenir_chemin_absolu}")

# Test si fichier existe
fichier_existe = os.path.exists(r"C:\Users\6331477\Pictures\Screenshots\Capture d’écran 2025-03-24 095514.png")
print(fichier_existe)  # ça marche

# créer objet path
chemin2 = Path("donnees/fichier.txt")
# Obtenir répertoire parent
parent = chemin2.parent
print(f"Répertoire parent: {parent}")
# Obtenir nom du fichier
nom = chemin2.name
print(f"Nom du fichier: {nom}")
# Obtenir l'extension
extension = chemin2.suffix
print(f"Extension: {extension}")
# Vérifier si fichier existe
if chemin2.exists():
    print("Le fichier existe")
# chemin absolu
chemin2_absolu = chemin2.absolute()
print(f"Chemin absolu: {chemin2_absolu}")
# Joindre des chemins
nouveau_chemin = Path("dossier") / "sous_dossier" / "fichier.txt"
print(f"Nouveau chemin : {nouveau_chemin}")
# Répertoire de base (home directory)
home = Path.home()
print(f"Répertoire utilisateur : {home}")

# III. Manipulation des dossiers : Suppression

# Dossier vide
os.rmdir("dossier vide")
Path("dossier vide").rmdir()
# dossier avec contenu
import shutil
shutil.rmtree("dossier_avec_contenu")

# Avec shutil (recommandé)
# import shutil
shutil.move('ancien_nom', 'nouveau_nom')
# avec os
# import os
os.rename('ancien_nom', 'nouveau_nom')
# déplacer un dossier
# import shutil
shutil.move('source', 'destination')
# copier un dossier entier
# import shutil
shutil.move('source', 'destination')

# IV. Exploration des dossiers : lister le contenu
# Avec os, on explore le contenu des dossiers de la manière suivante
contenu = os.listdir(".")  # va retourner une liste contenant les noms des fichiers contenu dans le repertoire
fichiers = [f for f in contenu if os.path.isfile(f)]
dossiers = [d for d in contenu if os.path.isdir(d)]

# Avec pathlib, on explore le contenu des dossiers de la manière suivante
chemin = Path(".")
for item in chemin.iterdir():
    if item.is_file():
        print(f"Fichier: {item.name}")
    elif item.is_dir():
        print(f"Dir: {item.name}")
    else:
        print(f"Élément inconnu: {item.name}")

# IV. Exploration des dossiers : Parcourir recursivement le dossier
# Avec os.walk
for dossier, sous_dossiers, fichiers in os.walk("."):
    print(f"Dossier: {dossier}")
# Avec pathlib
for fichier in Path(".").glob("**/*"):
    print(fichier)

# V. Manipulation des fichiers : ouverture, lecture et écriture
# Méthode recommandée avec gestionnaire de contexte
with open("exemple.txt", "w") as fichier:
    """ouverture et ecriture dans un fichier"""
    fichier.write("Première ligne\n")
    fichier.write("Deuxième ligne\n")
# Lire tout le contenu
with open("exemple.txt", "r") as fichier:
    contenu = fichier.read()
# Lire ligne par ligne
with open("exemple.txt", "r") as fichier:
    for ligne in fichier:
        print(ligne.strip())


# VI. Recherche de fichiers
def rechercher_par_nom(dossier, nom):
    resultats = []
    for dossier_racine, fichiers in os.walk(dossier):
        for fichier in fichiers:
            if nom in fichier:
                chemin = os.path.join(dossier_racine, fichier)
                resultats.append(chemin)
    return resultats


# Avec pathlib
def rechercher_par_extension(dossier, ext):
    if not ext.startswith("."):
        ext = "." + ext
    return list(Path(dossier).glob(f"**/*{ext}"))
