# Wozu wird die OOP - Objekt-Orientierte-Programmierung benbötigt?
# Eigene Daten können mithilfe von OOP kreiert werden :-)
# Darstellung von Daten:
# z.B. Zahlen, Strings, Listen
# Basis-Datentyp (int, float, str, list)
# Klassen und Objekte

# __init__ Methode == Funktion die Innerhalb der Klasse/Class bezeichnet wird
class Auto:
    def __init__(self):
        self.auto_marke = None
        self.ps_stärke = None
        self.farbe = None

bmw_m3 =Auto()
print(bmw_m3.auto_marke)