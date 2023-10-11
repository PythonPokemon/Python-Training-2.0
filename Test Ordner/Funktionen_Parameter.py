# Was sind Funktionen?
# Das sind wie Unterprogramme,
# die einzelnen Funktionalitäten in unterschiedliche Funktionen auslagern!

# Reihenfolge beachten:
#                1         2          3           4         5
def sag_hallo(vorname, nachname, taubenname, geburtstag, präsident):
    print('Hallo ' + vorname + nachname + ' Willkommen zurück')
    print('Wo ist deine Brieftaube ' + taubenname + '? XD')
    print('Hat der nicht am 7. ' + geburtstag + ' Geburtstag?')
    print('Wie ' + präsident + '?')

# Reihenfolge beachten
#           1           2              3       4         5
sag_hallo('Ali', ' Vonderlayen', 'Hassan', 'Oktober', 'Putin') # Funktionsaufruf + integrierte Parameter, String

print('Programm Ende')
