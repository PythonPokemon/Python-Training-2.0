# Wozu wird die OOP - Objekt-Orientierte-Programmierung benbötigt?
# Dadurch können eigene Daten mithilfe von OOP kreiert werden :-)
# Darstellung von Daten:
# z.B. Zahlen, Strings, Listen
# Basis-Datentyp (int, float, str, list)
# Klassen und Objekte

# __init__ Methode == Funktion die Innerhalb der Klasse/Class bezeichnet wird
class Auto: # Generele und erweiterbare Parameter für alle Autos
    def __init__(self):
        self.auto_marke = None # der Wert None steht für nichts,
        self.ps_stärke = None # damit die Parameter Spezifisch,
        self.auto_farbe = None # objektbezogen, bsp: auto1 oder auto2,
        self.auto_türen = None # eingegeben werden können!
#-----------------------------------------------
# Auto 1
auto1 =Auto() # Eingabe Parameter
auto1.auto_marke = 'BMW M3'
auto1.ps_stärke = 250
auto1.auto_farbe = 'Perl Weiss'
auto1.auto_türen = 3

# Auto 1 = ausgabe der Parameter über print
print(auto1.auto_marke) 
print(auto1.ps_stärke)
print(auto1.auto_farbe)
print(auto1.auto_türen)
#-----------------------------------------------
# Auto 2 Eingabe Parameter
auto2 =Auto()
auto2. auto_marke = 'Audi R8'
auto2.ps_stärke = 300
auto2.auto_farbe = 'Schwarz Carbon'
auto2.auto_türen = 2

# Auto 2 = ausgabe der Parameter über print
print(auto2.auto_marke) 
print(auto2.ps_stärke)
print(auto2.auto_farbe)
print(auto2.auto_türen)
