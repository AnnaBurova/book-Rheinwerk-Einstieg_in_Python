# Funktion
def steuer(bruttobetrag):
    # Umrechnung
    if bruttobetrag > 2500:
        steuersatz = 22
    else:
        steuersatz = 18

    # Umrechnung
    steuerbetrag = bruttobetrag / 100 * steuersatz

    # Ergebnis senden
    return steuerbetrag


# Verschiedene Werte
print("Bruttobetrag: 1800 Euro / Steuerbetrag:", steuer(1800), "Euro")
print("Bruttobetrag: 2200 Euro / Steuerbetrag:", steuer(2200), "Euro")
print("Bruttobetrag: 2500 Euro / Steuerbetrag:", steuer(2500), "Euro")
print("Bruttobetrag: 2900 Euro / Steuerbetrag:", steuer(2900), "Euro")
