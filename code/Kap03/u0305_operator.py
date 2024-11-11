# Eingabe
print("Geben Sie Ihr Bruttogehalt in Euro ein:")
bruttobetrag = float(input(">>> "))

print("Geben Sie Ihren Familienstand ein:")
print(" 1=ledig")
print(" 2=verheiratet")
familienstand = int(input(">>> "))

# Verzweigung
if bruttobetrag > 4000 and familienstand == 1:
    steuersatz = 26
elif bruttobetrag <= 4000 and familienstand == 2:
    steuersatz = 18
else:
    steuersatz = 22

# Umrechnung
steuerbetrag = bruttobetrag / 100 * steuersatz

# Ausgabe
print("Es ergibt sich ein Steuerbetrag von",
      steuerbetrag, "Euro (" + str(steuersatz) + "%)")
