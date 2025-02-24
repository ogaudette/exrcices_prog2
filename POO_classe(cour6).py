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
        if age <=0 or age > 150:
            age = 18
        self.__age = age

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nouveau_nom):
        if nouveau_nom == "":
            nouveau_nom = "Toto"
        self.__nom = nouveau_nom

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 <= age <= 150:
            age = 18
            self.__age = age

    # @property
    # def nom(self):
    #    """ici c'est un accesseur"""
    #    return self.__nom

    #@property
    #def modifier_nom(self, nom):
    #    """ici c'est un mutateur'"""
    #    self.__nom = nom

Alice = personne("Alice", "Toto", -20)
print(Alice.nom)
print(Alice.age)

class Etudiant(personne):
    def __init__(self, nom, prenom, annee):
        super().__init__(self, nom, prenom, annee)
        self.__annee = annee

    def afficher_age(self):
        print(f"Étudiant a {2025 - self.__annee} ans.")