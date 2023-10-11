print("Willkommen in der Lotterie, 3 - Gewinnt")

nummer_1 = int(input("Erste Zahl, Bitte wähle eine zahl zwischen 1 und 30: "))
nummer_2 = int(input("Zweite Zahl, Bitte wähle eine zahl zwischen 1 und 30: "))
nummer_3 = int(input("Dritte Zahl, Bitte wähle eine zahl zwischen 1 und 30: "))

# Gewinnzahl 1: 3
# Gewinnzahl 1: 7
# Gewinnzahl 1: 21

#-Variante-1
# jede IF-Else verzweigung muss auf der selben höhe verschachtelt werden!
if nummer_1 == 3:
    if nummer_2 == 7:
        if nummer_3 == 21:
            print("Juhhuuu, Du hast den Jackpot :-)")
        else:
            print("Du hast leider verloren, kannt für das Trinkgeld XD")
    else:
        print("Du hast leider verloren, kannt für das Trinkgeld XD")
else:
    print("Du hast leider verloren, kannt für das Trinkgeld XD")

#-Variante-2
# smarte lösung und, oder, nicht Operation verwenden!
if nummer_1 == 3 and nummer_2 == 7 and nummer_3 == 21:
    print("Herzlichen Glückwunsch, du hast die Lotterie gewonnen!")
else:
    print("Du hast erneut rein gepayt XD")