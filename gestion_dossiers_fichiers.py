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
print(fichier_existe)   # ça marche

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
