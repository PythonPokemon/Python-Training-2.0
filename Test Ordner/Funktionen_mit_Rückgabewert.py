# Auskommentieren alles markieren Strg + A dann ( Strg + K + C)
# Entkommentieren alles markieren Strg + A dann (Strg + K + U)

# # Was sind Funktionen?
# # Das sind wie Unterprogramme,
# # die einzelnen Funktionalitäten in unterschiedliche Funktionen auslagern!

# Reihenfolge oben und unten müssen eingehalten werden!
#           1  2
def maximum(a, b):
    if a < b: # : müssen meistens zum abschluss stehen, es gibt ausnahmen!
        return b
    else:
        return a
#                  1  2
ergebnis = maximum(4, 7) 
print(ergebnis)

# wenn also a kleiner b ist entspricht 4 < 7
# soll das maximum als ergebnis ausgegeben werden, aslo = 7