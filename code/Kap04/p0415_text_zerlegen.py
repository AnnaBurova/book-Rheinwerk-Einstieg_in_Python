# Beispiel
test = "Das ist ein Beispielsatz"
print("Text:", test)

print()

# Beginn
if test.startswith("Das"):
    print("Text beginnt mit Das")

# Ende
if not test.endswith("Das"):
    print("Text endet nicht mit Das")

print()

# Zerlegung
teile = test.partition("ei")
print("Zerlegungs-Teil:", teile[1])
print("vor der 1. Teilung:", teile[0])
print("hinter der 1. Teilung:", teile[2])
print("Typ teile:", type(teile))

print()

teile = test.rpartition("ei")
print("Zerlegungs-Teil:", teile[1])
print("vor der 2. Teilung:", teile[0])
print("hinter der 2. Teilung:", teile[2])
print("Typ teile:", type(teile))

print()

# Zerlegung in Liste
wliste = test.split()
for i in range(0, 3):
    print("Element:", i, wliste[i])
print("Typ wliste:", type(wliste))

print()

wliste = test.split("e")
for i in range(0, 3):
    print("Element:", i, wliste[i])
print("Typ wliste:", type(wliste))
