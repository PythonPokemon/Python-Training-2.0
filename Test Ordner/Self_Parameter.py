# Wozu wird die OOP - Objekt-Orientierte-Programmierung benbötigt?
# Dadurch können eigene Daten mithilfe von OOP kreiert werden :-)
# Darstellung von Daten:
# z.B. Zahlen, Strings, Listen
# Basis-Datentyp (int, float, str, list)
# Klassen und Objekte

# __init__ Methode == Funktion die Innerhalb der Klasse/Class bezeichnet wird
# 'Klassen' sind wie Baupläne oder Blaupausen für Objekte:-)
class Auto: # 'Klasse' Generel und erweiterbar für alle Objekte!
    def __init__(self): # definition der Attribute, für das Objekt!
        self.auto_marke = None # der Wert None steht für nichts,
        self.ps_stärke = None # damit die Parameter Spezifisch,
        self.auto_farbe = None # objektbezogen, bsp: auto1 oder auto2,
        self.auto_türen = None # eingegeben werden können!
# 'self' ist ein referenz wert, der temporär gespeichert wird bis zum abruf!
#-----------------------------------------------
# 'Objekt'-Auto 1
auto1 = Auto() # Eingabe Attribute
auto1.auto_marke = 'BMW M3' # hier wird der temporäre 'self' wert abgerufen
auto1.ps_stärke = 250 # und dem Objekt zugeordnet
auto1.auto_farbe = 'Perl Weiss'
auto1.auto_türen = 3

# Auto 1 = ausgabe der Attribute, über print
print(auto1.auto_marke) 
print(auto1.ps_stärke)
print(auto1.auto_farbe)
print(auto1.auto_türen)