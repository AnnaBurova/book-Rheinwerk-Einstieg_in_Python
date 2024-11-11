# Eingabe
print("Geben Sie Ihr Bruttogehalt in Euro ein:")
bruttobetrag = float(input(">>> "))

# Verzweigung
if bruttobetrag > 2500:
    steuersatz = 22
else:
    steuersatz = 18

# Umrechnung
steuerbetrag = bruttobetrag / 100 * steuersatz

# Ausgabe
print("Es ergibt sich ein Steuerbetrag von",
      steuerbetrag, "Euro (" + str(steuersatz) + "%)")
