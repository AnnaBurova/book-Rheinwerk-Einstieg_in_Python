# Set
s1 = set([8, 15, "x"])
print("Original s1:", s1)

# Kopie
s2 = s1.copy()
print("Kopie    s2:", s2)

# Element hinzu
s1.add("abc")
print("Element hinzu s1:", s1)
print("Element hinzu s2:", s2)

# Element entnehmen
s1.discard("x")
print("Element entnommen s1:", s1)
print("Element entnommen s2:", s2)

# Leeren
s1.clear()
print("geleert s1:", s1)
print("geleert s2:", s2)
