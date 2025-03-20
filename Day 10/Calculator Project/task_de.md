Das Ziel ist, ein Rechner-Programm zu erstellen.

### Demo
https://appbrewery.github.io/python-day10-demo/

### Funktionen als Wert einer Variablen speichern
Sie können eine Referenz zu einer Funktion als Wert in einer Variablen speichern.  
z. B.
```
def add(n1, n2):
    return n1 + n2
    
    
my_favourite_calculation = add
my_favourite_calculation(3, 5)  # Gibt 8 zurück
```
Im Startdatei sehen Sie ein Wörterbuch, das auf jede der mathematischen Berechnungen verweist, die mit unserem Rechner durchgeführt werden können. Probieren Sie es aus und sehen Sie, ob Sie es schaffen, Addition, Subtraktion, Multiplikation und Division auszuführen.

### PAUSE 1 
TODO: Schreiben Sie die anderen 3 Funktionen - subtrahieren, multiplizieren und dividieren.

### PAUSE 2
TODO: Fügen Sie diese 4 Funktionen als Werte in ein Wörterbuch ein. Schlüssel = "`+`", "`-`", "`*`", "`/`"

### PAUSE 3
TODO: Verwenden Sie die Wörterbuchoperationen, um die Berechnungen durchzuführen. Multiplizieren Sie 4 * 8 mit dem Wörterbuch.

### Funktionalität
- Das Programm fragt den Benutzer nach der Eingabe der ersten Zahl.
- Das Programm fragt den Benutzer nach einem mathematischen Operator (eine Wahl zwischen "`+`", "`-`", "`*`" oder "`/`").
- Das Programm fragt den Benutzer nach der Eingabe der zweiten Zahl.
- Das Programm berechnet das Ergebnis basierend auf dem gewählten mathematischen Operator.
- Das Programm fragt, ob der Benutzer mit dem vorherigen Ergebnis weiterarbeiten möchte.
- Wenn ja, wiederholt das Programm die Berechnung, indem es das vorherige Ergebnis als erste Zahl verwendet.
- Wenn nein, fragt das Programm den Benutzer erneut nach der ersten Zahl und löscht alle vorherigen Berechnungen.
- Fügen Sie das Logo aus der Datei art.py hinzu.

<div class="hint">
  Versuchen Sie, ein Flussdiagramm zu erstellen, um Ihr Programm zu planen.
</div>

<div class="hint">
    Um die Multiplikation aus dem Wörterbuch der Operationen aufzurufen, würden Sie Ihren Code folgendermaßen schreiben:

<code>result = operations["*"](n1= 5, n2= 3)</code>

result wäre dann gleich 15.
</div>