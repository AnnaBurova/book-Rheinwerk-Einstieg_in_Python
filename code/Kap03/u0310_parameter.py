# Funktion
def steuer(bruttobetrag):
    # Umrechnung
    if bruttobetrag > 2500:
        steuersatz = 22
    else:
        steuersatz = 18

    # Umrechnung
    steuerbetrag = bruttobetrag / 100 * steuersatz

    # Ausgabe
    print("Bruttobetrag:", bruttobetrag, "Euro / "
          "Steuerbetrag:", steuerbetrag, "Euro / "
          "Steuersatz:", steuersatz, "%")


# Verschiedene Werte
steuer(1800)
steuer(2200)
steuer(2500)
steuer(2900)
