# Zählerschleife
# zum Testen einer variante, alle anderen auskommentieren!

# Variante A
#---------------------!
for zahlen in range (10): # vertikale ausgabe von o - 9, weil 10 steht
    print(zahlen)


# Variante B: mit startpunkt, bsp: 5 
#-----------------------!
for startzahl in range (5, 10): # ab der zahl 5 wird vertikal bis 10 gezählt
    print(startzahl)

# Variante C: mit Schrittweite
# ----------------------------------!
for schrittweite in range (0, 100, 10): # bedeutet startpunkt: 0  bis 100. in 10er schritten
    print(schrittweite)
