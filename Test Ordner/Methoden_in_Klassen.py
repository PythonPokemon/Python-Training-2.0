# 'Methode' ist die bezeichnung für eine 'Funktion' innerhalb einer 'Klasse'!

# __init__ Methode == Funktion die Innerhalb der Klasse/Class bezeichnet wird
class Auto: # 'Klasse' Generel und erweiterbar für alle Objekte!
    def __init__(self): # 'Methode 1' mit Attributen, für ein Objekt!
        self.auto_marke = None # der Wert None steht für nichts,
        self.ps_stärke = None # damit die Parameter Spezifisch,
        self.auto_farbe = None # objektbezogen, bsp: auto1 oder auto2,
        self.auto_türen = None # eingegeben werden können!
        self.x_position = 5 # start position x-achse 5
        self.y_position = 5 # start position y-achse 5

    def fahren(self, x, y): # 'Methode 2' zum 'Fahren' Attribut
        self.x_position += x
        self.y_position += y

#-----------------------------------------------
# 'Objekt'-Auto 1
auto1 = Auto() # Eingabe Attribute
auto1.auto_marke = 'BMW M3'
auto1.ps_stärke = 250
auto1.auto_farbe = 'Perl Weiss'
auto1.auto_türen = 3


# Auto 1 = ausgabe der Attribute, über print
print(auto1.auto_marke) 
print(auto1.ps_stärke)
print(auto1.auto_farbe)
print(auto1.auto_türen)

# Fahren Attribute  1  2
auto1.fahren(5, 10)
print(auto1.x_position) # Attribut 1, wird + 5 zu x-achse addiert
print(auto1.y_position) # Attribut 2, wird + 10 zu y-achse adiert