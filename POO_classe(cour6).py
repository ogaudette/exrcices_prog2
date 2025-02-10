class voiture:   # définie une classe nommée "voiture"
    def __init__(self, marque, modèle, couleur):
        """ La méthode init est une méthode spéciale appelée constructeur
        """
        self.marque = marque
        self.modèle = modèle
        self.couleur = couleur

    def accelerer(self):
        print("cette voiture peut accelerer")

ma_voiture = voiture("Subaru", "WRX", "bleue")
print(ma_voiture.marque)
print(ma_voiture.couleur)
ma_voiture.accelerer()


class personne:
    def __init__(self, nom, prenom, age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age

    @property
    def nom(self):
        """ici c'est un accesseur"""
        return self.__nom

    @property
    def modifier_nom(self, nom):
        """ici c'est un mutateur'"""
        self.__nom = nom

Alice = personne("Alice", "Toto", 20)

