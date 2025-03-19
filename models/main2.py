from models.rectangle import Rectangle
from models.cercle import Cercle
from models.groupe_forme import GroupeForme


def creer_rectangle():
    """définir fonction pour créer rectangle"""
    couleur, rempli = saisir_couleur_remplissage()
    while True:
        try:
            largeur = float(input("Entrer la largeur: "))
            if largeur < 0:
                print("la largeur doit être positive.")
                continue
            break
        except ValueError:
            print("entrer nombre valide")

    while True:
        try:
            longueur = float(input("Entrer la longueur: "))
            if longueur < 0:
                print("la longueur doit être positive.")
                continue
            break
        except ValueError:
            print("entrer nombre valide")

    return Rectangle(couleur, rempli, largeur, longueur)

def creer_cercle():
    """Définir la fonction pour créer un cercle"""
    print("\n====Création d'un Cercle=====")
    couleur, rempli = saisir_couleur_remplissage()
    while True:
        try:
            rayon = float(input("Entrer la rayon: "))
            if rayon < 0:
                print("le rayon doit être positive.")
                continue
            break
        except ValueError:
            print("entrer nombre valide")
    return Cercle(couleur, rempli, rayon)

def saisir_couleur_remplissage():
    """Fonction pour saisir la couleur et l'état de remplissage"""
    couleur = input("Entrer la couleur de remplissage: ")
    remplir_str = input("La forme est-elle rempli? (o/n) ").lower()
    rempli = remplir_str == "o" or remplir_str == "n"
    return couleur, rempli

def afficher_menu():
    """Fonction pour afficher la menu d'affichage"""
    print("\n==== MENU ====")
    print("1. Ajouter un cercle")
    print("2. Ajouter un rectangle")
    print("3. Ajouter un triangle")
    print("4. Afficher les formes")
    print("5. Calculer l'aire totale")
    print("6. Effectuer les opérations spéciales")
    print("0. Quitter")
    return input("Choississez une option: ")

def main():
    """Programme principal interactif"""
    print("Bienvenue dans le programme de forme géométrique.")

    # Création d'un groupe de forme
    groupe = GroupeForme()

    # création d'un dictionnaire de formes spéciales pour des opérations spéciales
    formes_speciales = {'cercles': [], 'rectangles': [], 'triangles': []}

    while True:
        choix = afficher_menu()
        if choix == "0":
            print("bye")
            break
        elif choix == "1":
            cercle = creer_cercle()
            groupe.ajouter(cercle)
            formes_speciales['cercles'].append(cercle)
            print("Cercle ajouté au groupe.")
        elif choix == "2":
            rectangle = creer_rectangle()
            groupe.ajouter(rectangle)
            formes_speciales['rectangles'].append(rectangle)
            print("Rectangle ajouté au groupe.")
        elif choix == "3":
            pass
        elif choix == "4":
            if len(groupe.formes) == 0:
                print("Aucune form dans le groupe.")
            else:
                print("\n===Formes dans le groupe===")
                for i, forme in enumerate(groupe, 1):
                    if isinstance(forme, Cercle):
                        type_forme = "Cercle"
                        taille = f"rayon={forme.rayon}"
                    elif isinstance(forme, Rectangle):
                        type_forme = "Rectangle"
                        taille = f"largeur={forme.largeur}, longueur={forme.longueur}"
                    else:
                        type_forme = "Forme inconnue"
                        Taille = ""
                    print(f"{i}. {type_forme} {taille}" +
                          f"({'rempli' if forme.rempli else 'nonrempli'}.)" +
                          f"{taille},aire={forme.aire():.2f}, perimètre={forme.perimetre():.2f}")

        elif choix=='5':
            if len(groupe.formes)==0:
                print("Aucune forme dans le groupe.")
            else:
                print(f"\nAire totale de toutes les formes:{groupe.aire_totale():.2f}")

        elif choix == '6':
            if len(groupe.formes) == 0:
                print("Aucune forme dans le groupe.")
            else:
                print(f"\nAire totale de toutes les formes:{groupe.aire_totale():.2f}")
        elif choix == '6':
            print(f"\n===Démonstration des opérations spéciales")

            # Addition de cercles
            if len(formes_speciales['cercles']) > 2:
                c1 = formes_speciales['cercles'][0]
                c2 = formes_speciales['cercles'][1]
                print(f"Addition de deux cercles:{c1 + c2:.2f}")
            else:
                print("il faut au moins 2 cercles pour cet opération")

            # Addition rectangle
            if len(formes_speciales['rectangles'])>2:
                r1=formes_speciales['rectangles'][0]
                r2=formes_speciales['rectangles'][1]
                print(f"Addition de deux rectangles:{r1 + r2:.2f}")
            else:
                print("il faut au moins 2 rectangles pour cet opération")

            # Multiplication d'un rectangle
            if len(formes_speciales['rectangles'])>2:
                r=formes_speciales['rectangles'][0]
                facteur_mul = 2
                r_double = r * facteur_mul
                print(f"Rectangles:{r.couleur} mmultiplié par {facteur_mul}:"+
                      f"largeur = {r_double.largeur}, longueur = {r_double.longueur}"+
                      f"aire = {r_double.aire():.2f}")
            else:
                print("il faut au moins 1 rectangles pour cet opération")

            # Opération d'égalité de triangles
                """À completer"""
                pass

        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
