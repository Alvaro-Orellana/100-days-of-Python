### TypeError
Diese Fehler treten auf, wenn Sie den falschen Datentyp verwenden.  
z. B. `len(12345)`

Da Sie die Funktion `len()` nur mit Strings verwenden können, wird sie verweigern zu arbeiten und einen TypeError ausgeben, wenn Sie ihr eine Zahl (Integer) übergeben.

#### PAUSE 1. Korrigieren Sie die Funktion `len()`, damit sie keine Warnungen oder Fehler mehr ausgibt.

### Typprüfung
Sie können den Datentyp jedes Wertes oder jeder Variablen in Python mithilfe der Funktion `type()` überprüfen.

`print(type("abc")) # gibt <class 'str'> zurück`

#### PAUSE 2. Schreiben Sie 4 Prüfungen für Datentypen
Verwenden Sie die Funktionen `type()` und `print()`, um 4 Zeilen im Ausgabebereich auszugeben, sodass wir die gesamte Sammlung der Datentypen erhalten, die wir gelernt haben. `<class 'str'> <class 'int'> <class 'float'> und <class 'bool'>`

### Typkonvertierung
Sie können Daten in unterschiedliche Datentypen mit speziellen Funktionen umwandeln.  
z. B.

`float()`  

`int()`  

`str()`  

#### PAUSE 3. Lassen Sie diese Codezeile fehlerfrei laufen  
`print("Anzahl der Buchstaben in Ihrem Namen: " + len(input("Geben Sie Ihren Namen ein")))`