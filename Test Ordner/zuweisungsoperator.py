# Der Zuweisungsoperator rechnet von rechts und weist es dann dem linken wert zu

beispiel1 = 22
beispiel2 = 22 + 3
beispiel3 = (22 - 2) * 3

# variante 1 berechnung
beispiel1 = beispiel1 +10
print(beispiel1)

# variante 2 berechnung, kurzschreibweise
beispiel2 += 10
print(beispiel2)

# der obere wert [(22 - 2) * 3 = 60] geteilt durch 2 laut diesem wert = 30
beispiel3 /= 2
print(beispiel3)