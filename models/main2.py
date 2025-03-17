


def creer_rectangle():
    """définir fonction pour créer rectangle"""

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

    return Rectangle(largeur, longueur)
def