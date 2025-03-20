### Abrunden einer Zahl
Sie können eine Zahl abrunden oder alle Dezimalstellen entfernen, indem Sie die Funktion `int()` verwenden, die eine Fließkommazahl (mit Dezimalstellen) in eine ganze Zahl (Ganzzahl) umwandelt.

`int(3.738492) # Wird zu 3`

### Runden einer Zahl
Wenn Sie jedoch eine Dezimalzahl auf die nächstgelegene ganze Zahl runden möchten, basierend auf der traditionellen mathematischen Methode, bei der alles über .5 nach oben und alles darunter nach unten gerundet wird, können Sie die Python-Funktion `round()` verwenden.

`round(3.738492) # Wird zu 4`

`round(3.14159) # Wird zu 3`

`round(3.14159, 2) # Wird zu 3.14`

### Zuweisungsoperatoren
Zuweisungsoperatoren wie der Additionszuweisungsoperator `+=` addieren die Zahl rechts zur ursprünglichen Wert der Variablen links und weisen der Variablen den neuen Wert zu.

`+=`

`-=`

`*=`

`/=`  

### f-Strings
In Python können wir f-Strings verwenden, um eine Variable oder einen Ausdruck in einen String einzufügen.

`age = 12`

`print(f"Ich bin {age} Jahre alt")`

`# Gibt aus: Ich bin 12 Jahre alt.`