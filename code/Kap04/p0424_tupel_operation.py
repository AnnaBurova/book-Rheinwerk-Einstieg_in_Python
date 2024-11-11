# Tupel mit und ohne Klammer
z = (3, 6, -8, 5.5)
print("Tupel 1:", z)

z = 6, 8, -3
print("Tupel 2:", z)

# mehrdimensionales Tupel, unterschiedliche Objekte
x = (("Paris", "Fr", 3500000), ["Rom", "It", 4200000])
print("mehrdim. Tupel:")
print(x)

# Ersetzen erzeugt fehler
try:
    x[0][0] = "Lyon"
except TypeError:
    # Ersetzen nicht erlaubt, weil Tupel
    print("Fehler")

# Ersetzen erlaubt, weil Liste
x[1][0] = "Pisa"
print("Listenelement ersetzt:", x[1])

# Tupel bei for-Schleife
for i in 4, 5, 12:
    print("i:", i)

# Zuweisung mit Tupel
x, y = 2, 18
print("x:", x, "/ y:", y)
