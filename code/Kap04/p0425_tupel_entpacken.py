# Mehrfache Zuweisung
x, y, z = 3, 5.2, "hallo"
print("Mehrf. Zuweisung:", x, y, z)

# Auswirkungen erst danach
a = 12
b = 15
c = 22
a, b, c = c, a, a+b
print("Auswirkung:", a, b, c)

# Verpacken eines Tupels
p = 3, 4
print("Verpackt:", p)

# Entpacken eines Tupels
m, n = p
print("Entpackt: m:", m, "n:", n)

# Falsche Zuweisung eines Tupels
try:
    s, t = 3, 4, 12
    print(s, t)
except ValueError:
    print("Fehler bei Zuweisung")

print()

# Rest in Liste = *y
x, *y, z = 3, 5.2, "hallo", 7.3, 2.9
print(x)
print(y)
print(z)

print()

# kein Rest, Liste leer = *y
x, *y, z = 3, 5.2
print(x)
print(y)
print(z)
