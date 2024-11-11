# Modul copy
import copy

# Kopie einer Liste, Methode 1
x = [23, "hallo", -7.5]
y = []

# Elemente einzeln kopieren
for i in x:
    y.append(i)
print("gleiches Objekt:", x is y)
print("gleicher Inhalt:", x == y)

print()

# Kopie einer Liste, Methode 2
x = [23, ["Berlin", "Hamburg"], -7.5, 12, 67]

# Funktion zur Tiefenkopie
y = copy.deepcopy(x)
print("gleiches Objekt:", x is y)
print("gleicher Inhalt:", x == y)
