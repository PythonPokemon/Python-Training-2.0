# Wiedeirholung Liste

meine_liste = []
print(type(meine_liste))

# Index         1      2    3     4
meine_liste = [1, "zwei", True, 2,34]

# Index
print(meine_liste[1])
print(meine_liste[2])
print(meine_liste[3])
print(meine_liste[4])

tiere = ["hund", "katze", "maus", "vogel"]

# Aufzählunsvariante der Liste
for index, tiere in enumerate(tiere): 
    print(index, tiere)

# Liste Anfügen
tiere.append("Hai")
print(tiere)
