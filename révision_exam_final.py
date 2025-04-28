# Q1
from math import sqrt

positions = [(1, 0), (2, 2), (0, 1), (2, 2)]


def analyse_positions(positions):
    # if x >= 0 and y >= 0:  # vérifie si x et y sont positifs ou nul
    #    return x, y
    # else:
    #    raise ValueError("Le x et le y doit être positif ou nul.")

    distance = [sqrt(x**2 + y**2) for x, y in positions]

    moyenne = sum(distance) / len(distance)

    position_max = max(positions, key=lambda position: sqrt(position[0]**2 + position[0]**2))

    decroissant = sorted([position for position in positions if position[0] > position[1]],
                         key=lambda position: sqrt(position[0]**2 + position[0]**2), reverse=True)

    x_unique = {x for x, i in positions}

    return (f"résultats = ("
            f"moyenne_distance: {moyenne:.3f},"
            f"plus_éloignée: {position_max},"
            f"x_sup_y: {decroissant},"
            f"x_unique: {x_unique}.")


resultat = analyse_positions(positions)
print(resultat)
