Eine Funktion in ihrer einfachsten Form ist einfach ein Bezeichner für einen Block von Code. Sie geben ihr einen Namen, und wenn Sie die Funktion mit diesem Namen aufrufen, wird der gesamte Code im Funktionsblock ausgeführt. Dies kann uns helfen, Zeit zu sparen und wiederholten Code zu reduzieren.

### Eine neue Funktion definieren
```
def <funktionsname>():
    print("Hallo")
    # Etwas anderes machen
    # Etwas anderes machen ...
```

### Eine Funktion aufrufen
Eine Funktion aufzurufen bedeutet einfach, die Funktion auszuführen. Wir können eine Funktion an beliebiger Stelle in unserem Code in Python aufrufen. 

```
<funktionsname>()
```

Alles zusammengeführt, z. B.
```
# Die Funktion erstellen
def get_user_name():
    name = input("Wie heißt du? ")
    print("Hallo, " + name)
    # Innerhalb der Funktion

# Außerhalb der Funktion
print("Hallo")
get_user_name() # Die Funktion aufrufen
```

Dieser Code führt zur folgenden Sequenz an Ausgaben:
```
Hallo
Wie heißt du? #Ich tippe Angela ein
Hallo
Angela