tname = "Robinson Crusoe"

try:
    tname[3] = "e"
except TypeError:
    print("Fehler")

try:
    tname[3:5] = "el"
except TypeError:
    print("Fehler")
