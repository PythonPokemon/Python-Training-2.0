def meineAnalFunktion(): # es ist egal wie mna die funktion bennent, sie funlktioniert trotzdem
    global x
    x = "fantastisch"

meineAnalFunktion()

print("Python ist " + x)


# Global hat höhere prio als nromale variable sie bsp.

x = "super" # normale variable

def myfunc():
  global x 
  x = "Sau Geil" # globale variable

myfunc()

print("Python is " + x)
