a = 27

print("Dezimal:", a)
'''
Dezimal: 27
'''

print("Hexadezimal:", hex(a))
'''
Hexadezimal: 0x1b
             0x - Hex System
               1 =  1 x (16 ^ 1) = 16
                b = 11 x (16 ^ 0) = 11
'''

print("Oktal:", oct(a))
'''
Oktal: 0o33
       0o - Oktal System
         3 = 3 x (8 ^ 1) = 24
          3 = 3 x (8 ^ 0) =  3
'''

print("Dual:", bin(a))
'''
Dual: 0b11011
      0b - Dual System
        1 = 1 x (2 ^ 4) = 16
         1 = 1 x (2 ^ 3) =  8
          0 = 0 x (2 ^ 2) =  0
           1 = 1 x (2 ^ 1) =  2
            1 = 1 x (2 ^ 0) =  1
'''

b = 0x1a + 12 + 0b101 + 0o67
'''
      26 + 12 +     5 +   55
'''

print("Summe:", b)
'''
Summe: 98
'''
