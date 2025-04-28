# 6
class Animal:
    def __init__(self, nom):
        self.nom = nom
class Lion(Animal):
    def __init__(self, nom, espece):
        super().__init__(nom)
        self.espece = espece

# lion = Lion("Simba", "Lion")
# print(lion.nom)

# 7
class Entite:
    def __str__(self):
        return "Entite"
class Enclos(Entite):
    def __str__(self):
        return "Enclos"

# e = Enclos()
# print(e)

# 4
d = {"a": 1, "b": 2}
d.update({"b": 3, "c": 4})
# print(d)

# 3
coords = [(1, 1), (2, 0), (0, 2)]
resultat = [x + y for x, y in coords if x >= y]
# print(resultat)

# 2
d = {"a": 1, "b": 2}
d["c"] = d.get("c", 0) + 1
# print(d)

# 1
lst = [(1, 2), (2, 1), (1, 2)]
s = set(lst)
print(len(s))  # réponse 2, car deux tuples identiques
