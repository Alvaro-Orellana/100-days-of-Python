Zuvor haben wir gesehen, dass Funktionen es uns ermöglichen, Code in einem benannten Block zu verpacken, der später wiederholt verwendet werden kann.

### PAUSE 1 - Überprüfung
- Erstellen Sie eine Funktion namens `greet()`.
- Schreiben Sie 3 `print`-Anweisungen innerhalb der Funktion.
- Rufen Sie die Funktion `greet()` auf und führen Sie Ihren Code aus.

### Eingaben
Indem wir beim Erstellen (Definieren) einer neuen Funktion einen Variablennamen in die Klammern setzen, ermöglichen wir dieser Funktion, Eingaben zu erhalten, wenn sie aufgerufen wird. 

Das bedeutet, dass wir das Verhalten der Funktion jedes Mal ändern können, indem wir ihr unterschiedliche Eingaben übergeben.

```
# Die Funktion erstellen
def myFunction(input):
    print(f"Hey! {input}")
```
```
# Die Funktion verwenden
myFunction("Tommy") 
# Gibt "Hey! Tommy" aus
```

### Eingaben sind Variablen
Wenn Sie eine Funktion mit Eingaben erstellen, definieren Sie einen Variablennamen, der den übergebenen Daten zugewiesen wird.

Der Name der Eingabevariablen, z. B. `name` in diesem Code: `def greet(name):`, wird als Parameter bezeichnet.

Der Wert der Eingabevariablen, z. B. `Angela`, wenn Sie die vorherige `greet`-Funktion aufrufen: `greet("Angela")`, wird als Argument bezeichnet.