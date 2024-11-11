# Eingabe
print("Geben Sie Ihr Bruttogehalt in Euro ein:")
bruttobetrag = float(input(">>> "))

# Verzweigung
if bruttobetrag > 4000:
    steuersatz = 26
elif bruttobetrag < 2500:
    steuersatz = 18
else:
    steuersatz = 22

# Umrechnung
steuerbetrag = bruttobetrag / 100 * steuersatz

# Ausgabe
print("Es ergibt sich ein Steuerbetrag von",
      steuerbetrag, "Euro (" + str(steuersatz) + "%)")
