# Erzeugung
alter = {"Peter": 31, "Julia": 28, "Werner": 35}
print("Print Dictionary:", alter)
print("Typ Dictionary:", type(alter))

print()

# Werte
w = alter.values()
print("Print Werte:", w)
print("Typ Werte:", type(w))
print("Anzahl Werte:", len(w))

print()

for x in w:
    print(x)

if 31 in w:
    print("31 ist enthalten")

alter["Peter"] = 41

if 31 not in w:
    print("31 ist nicht enthalten")

print()

# Keys
k = alter.keys()
print("Print Keys:", k)
print("Typ Keys:", type(k))
print("Anzahl Keys:", len(k))

for x in k:
    print(x)

if "Werner" in k:
    print("Werner ist enthalten")

del alter["Werner"]

if "Werner" not in k:
    print("Werner ist nicht enthalten")

print()

# Items
i = alter.items()
alter["Franz"] = 35
print("Print Items:", i)
print("Typ Items:", type(i))
print("Anzahl Items:", len(i))

for x in i:
    print(x)

if ("Julia", 28) in i:
    print("Julia, 28 ist enthalten")
