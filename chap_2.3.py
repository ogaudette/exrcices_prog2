# II. Surcharge d'operateur
class Vecteur:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def __add__ (self, autre):
        "Surcharge de l'opérateur +"
        return Vecteur(self.x + autre.x, self.y + autre.y)

    def __sub__(self, other):
        Surcharge de L'opérateur return Vecteur(self.x autre.x, self.y autre.y)

def (self, scalaire):
Surcharge de l'opérateur return Vecteur(self.x scalaire, self.y scalaire)
def str (self):
return f"Vecteur((self.x). (self.y))"
# Utilisation
vi Vecteur(x1, y2)
v2 Vecteur(3,4)
print(v1 v2)#Va retourner Vecteur(4, 6)
print(v1 v2)#Va retourner Vecteur(-2, -2)
print(v13) Va retourner Vecteur(3, 6)