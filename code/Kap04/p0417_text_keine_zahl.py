# Fehler abfangen
x = "15.3p"

try:
    x = float(x)
    print(x * 2)
except ValueError:
    print("Zeichenkette konnte nicht umgewandelt werden")
