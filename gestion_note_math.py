import os
from datetime import datetime
from pathlib import Path
import shutil


class GestionNoteMathematique:
    """Cette classe sera utilisée pour gérer un système
        de notes mathématiques organisées par catégories
        """

    def __init__(self, dossier_racine=None):
        """Initialisation de la classe GestionNoteMathematique"""
        if dossier_racine is None:
            self.dossier_racine = Path.home() / 'MathNotes'
        else:
            self.dossier_racine = Path(dossier_racine)
        self.categories = ["algebre", "analyse", "geometrie", "probabilites", "archives"]

    def creer_structure_dossiers(self):
        """Ici la structure des dossiers pour
        les notes de mathématiques doit être créé"""
        self.dossier_racine.mkdir(exist_ok=True)

        # Création des sous dossiers
        for categorie in self.categories:
            dossier_categorie = self.dossier_racine / categorie
            dossier_categorie.mkdir(exist_ok=True)

        print(f"La structure de dossiers a été créée dans {self.dossier_racine}")

    def creer_note(self,categorie,titre,contenu):
        """Cette méthode va créer une nouvelle note mathématique dans la catégorie spécifiée"""
        categories_valides = self.categories[:-1]
        if categorie not in categories_valides:
            print(f"Erreur: la categorie {categorie} est invalide. La liste des catégories disponible est"
                  f" {(categories_valides)}")
            return None
        date_actuelle = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        nom_fichier = f"{date_actuelle}_{titre.replace(' ','_')}.txt"
        chemin_fichier = self.dossier_racine/categorie/nom_fichier  # Chemin complet du fichier

        contenu_complet = f"Titre:{titre}\nDate:{date_actuelle}Contenu:{contenu}"

        chemin_fichier.write_text(contenu_complet, encoding="utf-8")
        print(f"Note créée:{chemin_fichier}")
        return chemin_fichier

    def rechercher_note_par_titre(self,titre):
        """Rechercher la note par titre"""
        resultats=[]
        titre_lower = titre.lower()
        categories_valides = self.categories[:-1]
        for categorie in categories_valides:
            dossier_categorie = self.dossier_racine / categorie
            if not dossier_categorie.exists():
                continue
            for fichier in dossier_categorie.iterdir():
                # ici on vérifie si c'est un fichier et si le titre est dans le nom
                if fichier.is_file() and titre_lower in fichier.name.lower():
                    resultats.append(fichier)

        return resultats

    def rechercher_note_par_contenu(self, texte):

        resultats = []
        texte_lower = texte.lower()
        categories_valides = self.categories[:-1]
        for categorie in categories_valides:
            dossier_categorie = self.dossier_racine / categorie
            if not dossier_categorie.exists():
                continue
            for fichier in dossier_categorie.iterdir():
                # Ici on vérifie si c'est un fichier et si le titre est dans le nom
                if fichier.is_file() and fichier.suffix == '.txt':
                    try:
                        contenu = fichier.read_text(encoding="utf-8")
                        if texte_lower in contenu.lower():
                            resultats.append(fichier)
                    except Exception as e:
                        print(f"Erreur lors de la lecture de {fichier}: {e}")

        return resultats

    def archiver_notes_anciennes(self, jours):
        """
        Déplace les notes plus anciennes que le nombre de jours spécifié vers le dossier archives.

        """
        # Calculer la date limite
        date_limite = datetime.now() - datetime.time(days=jours)
        dossier_archives = self.dossier_racine / "archives"

        # S'assurer que le dossier archives existe
        dossier_archives.mkdir(exist_ok=True)

        notes_archivees = 0

        # Parcourir tous les dossiers de catégories (sauf archives)
        for categorie in self.categories[:-1]:  # Toutes sauf "archives"
            dossier_categorie = self.dossier_racine / categorie

            # Vérifier si le dossier existe
            if not dossier_categorie.exists():
                continue

            # Parcourir tous les fichiers de la catégorie
            for fichier in dossier_categorie.iterdir():
                # Vérifier si c'est un fichier
                if fichier.is_file():
                    # Obtenir la date de modification du fichier
                    temps_modification = fichier.stat().st_mtime
                    date_modification = datetime.datetime.fromtimestamp(temps_modification)

                    # Vérifier si le fichier est plus ancien que la date limite
                    if date_modification < date_limite:
                        # Chemin de destination dans les archives
                        chemin_destination = dossier_archives / fichier.name

                        # Déplacer le fichier
                        fichier.rename(chemin_destination)
                        notes_archivees += 1

        print(f"{notes_archivees} note(s) archivée(s)")
        return notes_archivees

    def afficher_resultats(self, resultats):
        """
        Affiche les résultats d'une recherche.
        """
        if not resultats:
            print("Aucun résultat trouvé.")
        else:
            print(f"{len(resultats)} note(s) trouvée(s):")
            for i, chemin in enumerate(resultats, 1):
                print(f"{i}. {chemin}")


monchemin2 = "C:\\Users\\6331477\\Documents\\ProjetGestionNotesMaths"
G1 = GestionNoteMathematique(monchemin2)
G1.creer_structure_dossiers()

G1.creer_note("algebre", "Equations du second degré",
                            "Formule: x = (-b ± √(b² - 4ac)) / 2a\n\nExemple: Pour 2x² + 3x - 5 = 0\na=2, b=3, c=-5")

# G1.creer_note("analyse", "Formule de Taylor",
#                             "f(x) = f(a) + f'(a)(x-a) + f''(a)(x-a)²/2! + ...\n\nExemple: ex ≈ 1 + x + x²/2 + x³/6 + ...")

G1.creer_note("geometrie", "Théorème de Pythagore",
                            "a² + b² = c²\n\nDans un triangle rectangle, le carré de l'hypoténuse est égal à la somme des carrés des deux autres côtés.")

# print(" Recherche par titre pour le titre 'equation'")
# resultats_titre=G1.rechercher_note_par_titre("triangle")
# print(resultats_titre)

print(" Recherche par contenu pour le texte 'triangle'")
resultats_titre=G1.rechercher_note_par_contenu("triangle")
print(resultats_titre)
