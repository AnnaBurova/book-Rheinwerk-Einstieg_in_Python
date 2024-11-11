# Import des Moduls
import fractions
import math

# Bruch
z = 12
n = 28
print("Bruch:", z, "/", n)

# als Fraction
b1 = fractions.Fraction(z, n)
print("Fraction:", b1)
print("Numerator:", b1.numerator)
print("Denominator:", b1.denominator)

wert = b1.numerator / b1.denominator
print("Wert:", wert)

print()

# Umrechnen
x = 2.375
print("Zahl:", x)

b2 = fractions.Fraction(x)
print("Fraction:", b2)

print()

# ggT: größter gemeinsamer Teiler
print("Bruch:", z, "/", n)
print("ggT:", math.gcd(z, n))
