# Liste
li = [8, 2, 5, 5, 5]
print("Liste:", li)
print("Typ Liste:", type(li))
print("Anzahl:", len(li))

print()

# Set
s1 = set([8, 2, 5, 5, 5])
print("Set:", s1)
print("Typ Set:", type(s1))
print("Anzahl:", len(s1))

print()

# Elemente
for x in s1:
    print("Element:", x)

if 5 in s1:
    print("5 ist enthalten")
