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
        self.auto_farbe = None

auto1 =Auto()
auto1.auto_marke = 'BMW M3'
auto1.ps_stärke = 250
auto1.auto_farbe = 'Perl Weiss'

print(auto1.auto_marke)
print(auto1.ps_stärke)
print(auto1.auto_farbe)