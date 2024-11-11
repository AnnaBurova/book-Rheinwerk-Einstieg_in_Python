# Set
s = set([8, 15, "x", 8])
print("Set:", s)
print("Typ Set:", type(s))

# Frozenset
fs = frozenset([8, 15, "x", 8])
print("Frozenset:", fs)
print("Typ Frozenset:", type(fs))

for x in fs:
    print(x)

try:
    fs.discard("x")
except AttributeError:
    # AttributeError: 'frozenset' object has no attribute 'discard'
    print("Fehler")
