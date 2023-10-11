
aufgabe_1 = ("Aufgabe 1, Altersabfrage:")
print(aufgabe_1)

alter = int(input("Bitte gib dein Alter ein: "))

if alter < 18:# alles kleinr 18
    print("Achtung der Nutzer ist unter 18 Jahre alt!")

elif alter == 18: # 18 gleich 18
    print("Der Nutzer ist exakt 18 Jahre alt")
elif alter == 19: # 19 gleich 19
    print("Der Nutzer ist exakt 19 Jahre alt")

else: # alle ab 20 Jahre fallen hier rein
    print("Der Nutzer ist volljährig")




print("Programmende")